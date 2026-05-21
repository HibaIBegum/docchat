import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()   

def ask(collection, question):

    results = collection.query(query_texts=[question],n_results=2)
    chunks=results["documents"][0]
    distances=results["distances"][0]
    if distances[0]> 1.8:
        return "I could not find a relevant answer in this document"
    combined_context = "\n".join(chunks)

    groq_client =  Groq(api_key= os.getenv("Groq_API_Key"))
    response = groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content":f"""Answer using ONLY the context below.
Do not add anything not in the context.
Context: {combined_context}"""},
            {"role": "user", "content": question}
    ]
)
    return response.choices[0].message.content

