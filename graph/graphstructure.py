from langgraph.graph import START, END, StateGraph
from state import SummaryState
from nodes import summarize_generator, keywords_generator, reevaluate_keywords, choose
graph = StateGraph(SummaryState)


graph.add_node(summarize_generator, "summarize_generator")
graph.add_node(keywords_generator, "keywords_generator")
graph.add_node(reevaluate_keywords, "reevaluate_keywords")
# graph.add_node("choose", lambda state:state) # passthrough function
# graph.add_node("choose", choose)

graph.add_edge(START, "summarize_generator")
graph.add_edge("summarize_generator", "keywords_generator")
graph.add_edge("keywords_generator", "reevaluate_keywords")
# graph.add_edge("reevaluate_keywords","choose")

graph.add_conditional_edges("reevaluate_keywords",choose,{
    "no" : "summarize_generator",
    "yes" : END
})


Main_Graph = graph.compile()
