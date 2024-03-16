from langchain.tools.retriever import create_retriever_tool

from Backend.langchain import vector_stores

def create_courses_from_catalog_retriever_tool():
    courses_from_catalog_retriever = vector_stores.courses_from_catalog_retriever

    if courses_from_catalog_retriever is None:
        print('Courses from catalog retriever not initialized')
        return None

    return create_retriever_tool(
        courses_from_catalog_retriever,
        "course_from_catalog",
        "Retrieve courses basic information from catalog by given query text."
    )
