from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app

import phi
import os
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")
web_serach_agent = Agent(name="Web Search Agent",
                         role="Search the web for the information",
                         model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
                         tools=[DuckDuckGo()],
                         instructions=["Always include sources"],
                         show_tool_calls=True,
                         markdown=True)

finance_agent = Agent(name="Finance AI Agent",
                    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
                    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
                    instructions=["Use tables to display the data"],
                    show_tool_calls=True,
                    markdown=True)

# mulit_ai_agent = Agent(
#     team=[web_serach_agent,finance_agent],
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     instructions=["Always inclue sources","Use table to display the data"],
#     show_tool_calls=True,
#     markdown=True
# )

app = Playground(agents=[finance_agent,web_serach_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)