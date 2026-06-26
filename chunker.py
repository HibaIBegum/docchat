import fitz

def smart_chunk_size(num_pages):
    if num_pages< 5 :
        return 500
    elif num_pages < 10:
        return 1000
    elif num_pages < 50:
        return 1500
    else:
        return 2000
    
def extract_chunks(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    chunk_size= smart_chunk_size(len(doc))
    overlap= int(chunk_size *0.2)
    #full_text = ""
    chunks =[]
    metadatas=[]
    chunk_index=0
    for page_num, page in enumerate(doc):
        full_text =page.get_text()
        i=0
        while i<len(full_text):
            chunk = full_text[i:i+chunk_size].strip()
            if chunk:
                chunks.append(chunk)
                metadatas.append({ 
                    "page": page_num + 1,
                    "chunk_index": chunk_index
                })
                chunk_index += 1
            i += chunk_size - overlap
    return chunks, metadatas

