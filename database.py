import chromadb

def build_database(chunks,metadatas):
    client = chromadb.Client()
    try:
        client.delete_collection("dochat")
    except:
        pass
    collection= client.create_collection("dochat")
    collection.add(
        documents= chunks,
        metadatas=metadatas,
        ids=[f"chunks{i}" for i in range(len(chunks))]
    )
    return collection
