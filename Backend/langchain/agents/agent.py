from Backend.langchain import models
from Backend.langchain import tools
from langchain.agents import AgentExecutor, create_react_agent

def create_agent(memory, prompt):
    agent = create_react_agent(
        tools = [
            tools.courses_from_catalog_retriever_tool,
            tools.plan_of_study_retriever_tool
            ],
        llm = models.chatbot_client,
        prompt = prompt,
    )
    return AgentExecutor.from_agent_and_tools(
        agent = agent, 
        tools = [
            tools.courses_from_catalog_retriever_tool,
            tools.plan_of_study_retriever_tool
            ], 
        verbose = True, 
        memory = memory, 
        handle_parsing_errors = True
    )
