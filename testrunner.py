from graph import Main_Graph

text = """Just as the internet has drastically lowered the cost of information transmission, AI will lower the cost of cognition. That’s according to Harvard Business School professor Karim Lakhani, who has been studying AI and machine learning in the workplace for years. As the public comes to expect companies that deliver seamless, AI-enhanced experiences and transactions, leaders need to embrace the technology, learn to harness its potential, and develop use cases for their businesses. “The places where you can apply it?” he says. “Well, where do you apply thinking?”"""

# response = Main_Graph.invoke({"input":text, "decision": None})
response = Main_Graph.invoke({"input":text})

print("Original Input : ",response["input"])
print()
print("Summary : ",response["summary"])
print()
print("Keywords : ",response["keyword"])
print()
print("Confidence Score : ",response["confidence_score"])