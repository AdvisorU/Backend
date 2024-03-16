from . import pinecone

courses_from_catalog_retriever = None

def init():
    pinecone.pinecone_client = pinecone.init_pinecone_client()

    global courses_from_catalog_retriever
    courses_from_catalog_retriever = pinecone.get_retriever(
        pinecone.get_courses_from_catalog_index()
    )
