from langchain.prompts import ChatPromptTemplate


evaluate_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that evaluate the keywords and summary. based on the original text and provide a confidence score out of 100. give only the score as output."),
    ("human", "Given the summary and keywords, give the confidence score about how good the summary and keywords are based on the original text/article. \n\n Original text/article:  {input} \n\nSummary: {summary}\n\nKeywords: {keywords}"),
])