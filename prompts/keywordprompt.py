from langchain.prompts import ChatPromptTemplate

keywords_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that extracts keywords from the summary. give only keywords as output."),
    ("human", "Extract 5 relevant keywords from the following text. :\n\n{text}"),
])
