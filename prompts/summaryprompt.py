from langchain.prompts import ChatPromptTemplate


summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that summarizes text."),
    ("human", "Summarize the following text in a concise manner. :\n\n{text}"),
])
