from . import pinecone

courses_from_catalog_retriever = None

plan_of_study_retriever = None

def init():
    global courses_from_catalog_retriever
    courses_from_catalog_retriever = pinecone.get_retriever(
        pinecone.get_courses_from_catalog_index()
    )
    
    global plan_of_study_retriever
    plan_of_study_retriever = pinecone.get_retriever(
        pinecone.get_plan_of_study_index()
    )
