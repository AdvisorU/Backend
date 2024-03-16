from . import courses_from_catalog_retriever

courses_from_catalog_retriever_tool = None

def init():
    global courses_from_catalog_retriever_tool
    courses_from_catalog_retriever_tool = courses_from_catalog_retriever.create_courses_from_catalog_retriever_tool()