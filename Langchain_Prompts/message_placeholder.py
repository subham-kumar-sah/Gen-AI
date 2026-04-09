from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', "You are a hepful customer support agent"),
    ( MessagesPlaceholder(variable_name="chat_history")),
    ('human', '{query}')
])

chat_history = []
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

print (chat_history)    

prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "What is the status of my refund?"
})

print(prompt)