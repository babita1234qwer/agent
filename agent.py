from agno.agent import Agent
#from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

from agno.team import Team
load_dotenv()
eng_agent=Agent(name="English Agent",role="You answer questions in English")
chi_agent=Agent(name="Chinese Agent" ,role="You answer questions in Chinese")
hindi_agent=Agent(name="Hindi Agent",role="You answer questions in Hindi")

team_leader=Team(
    name="Answer & Translation Team",
    members=[eng_agent,chi_agent,hindi_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must respond to  answer thequery in their specific language .Do not route to just one agent.
                 Output the response of all agents."""


)

team_leader.print_response("What is the capital of India?")


#def build_agent():
#return Agent(
#model=OpenAIResponses(id="gpt-5-mini"),
#tools=[DuckDuckGoTools()],
        #markdown=True,
        #instructions="You are a helpful and expert travel agent."


   # )

#openai_agent=build_agent()

#openai_agent.print_response("My budget is 1 L INR,should I travel to Goa or Pukhet?")

