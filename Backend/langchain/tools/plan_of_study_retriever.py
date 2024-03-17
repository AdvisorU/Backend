from langchain.tools.retriever import create_retriever_tool

from Backend.langchain import vector_stores

def create_plan_of_study_retriever_tool():
    plan_of_study_retriever = vector_stores.plan_of_study_retriever

    if plan_of_study_retriever is None:
        print('Courses from catalog retriever not initialized')
        return None

    return create_retriever_tool(
        plan_of_study_retriever,
        "plan_of_study",
        "Retrieves a plan of study for computer science major that everyone should follow."
    )
