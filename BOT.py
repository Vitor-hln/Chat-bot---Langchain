from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import os

llm = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("KEY"),
    )

llm.invoke("how can langsmith help with testing?")