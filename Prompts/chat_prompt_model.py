from langchain_core.prompts import ChatPromptTemplate


chatTemplate = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain {topic} in simple terms.'),
])

prompt = chatTemplate.invoke({'domain': 'travel guide', 'topic': 'swiss alps'})

print(prompt)