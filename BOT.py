from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import os

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("KEY"))

llm.invoke("how can langsmith help with testing?")