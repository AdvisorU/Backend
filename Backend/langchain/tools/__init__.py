from . import courses_from_catalog_retriever
from . import plan_of_study_retriever

courses_from_catalog_retriever_tool = None
plan_of_study_retriever_tool = None

def init():
    global courses_from_catalog_retriever_tool
    courses_from_catalog_retriever_tool = courses_from_catalog_retriever.create_courses_from_catalog_retriever_tool()
    
    global plan_of_study_retriever_tool
    plan_of_study_retriever_tool = plan_of_study_retriever.create_plan_of_study_retriever_tool()
    