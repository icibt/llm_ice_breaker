from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get me a link to their linkedin profile page.
    The answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="It gets the LinkedIn page for a person based on his name",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        llm=llm,
    )

    propmpt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linked_profile_url = agent.run(propmpt_template.format_prompt(name_of_person=name))
    return linked_profile_url
