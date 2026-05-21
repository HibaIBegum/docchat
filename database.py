import chromadb

def build_database(chunks):
    client = chromadb.Client()
    collection= client.create_collection("dochat")
    collection.add(
        documents= chunks,
        ids=[f"chunks{i}" for i in range(len(chunks))]
    )
    return collection
