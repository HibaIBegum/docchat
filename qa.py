import os 
from groq import Groq, RateLimitError, APITimeoutError 
from dotenv import load_dotenv
import time 
load_dotenv()   

def ask(collection, question):
    try:
        results = collection.query(query_texts=[question],n_results=3)
        chunks=results["documents"][0]
        distances=results["distances"][0]
        metadatas=results["metadatas"][0]
        if distances[0]> 1.8:
            return "I could not find a relevant answer in this document", None
        combined_context = "\n".join(chunks)
        source = f"Page {metadatas[0]['page']}, Chunk {metadatas[0]['chunk_index']}"

        groq_client =  Groq(api_key= os.getenv("Groq_API_Key"))
        for attempt in range(3):
            try:
                response = groq_client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "system", "content":f"""Answer using ONLY the context below.
                                Do not add anything not in the context.
                                If the anaswer is not in the context, reply with exactly : No_ANSWER 
                                Context: {combined_context}"""},
                    {"role": "user", "content": question}
                ],
                )
                answer = response.choices[0].message.content
                if "<think>" in answer:
                    answer = answer.split("</think>")[-1].strip()
                if "no_answer" in answer.lower() or "no information" in answer.lower():
                    return "I could not find a relevant answer in this document.", None

                return answer, source
            except RateLimitError:
                if attempt <2:
                    time.sleep(5)
                else:
                    return "Too many requests. Please wait a moment and try agaub.", None
            except APITimeoutError:
                if attempt < 2:
                    time.sleep(3)
                else:
                    return "Request timed out. Please try again.",None
    except Exception as e:
        print(f"REAL ERROR: {e}");
        return "Smoething went wrong. Please try again.",None
    
