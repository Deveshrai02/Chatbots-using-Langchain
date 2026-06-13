from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatOpenAI(model="gpt-4" , temperature=0.2)
result = model.invoke("What is the capital of France?")
print(result.content)
result2 = model.invoke("where is it located?")
print(result2.content)