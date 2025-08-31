# from graph import Main_Graph
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/process"

def main():
    st.set_page_config(
        page_title="AI Text Summarizer",
        page_icon="📝",
        layout="centered"
    )

    st.header("Text Summarization and Keyword Extraction with Confidence Scoring")
    # st.caption("Powered by LangGraph + LLMs")

    article_input = st.text_area("Enter the article text here:", height=200,placeholder="Paste your article text here...")

    # response = Main_Graph.invoke({"input":text, "decision": None})

    if st.button("Generate Summary and Keywords"):

        if not article_input.strip():
            st.error("❌ Please enter some text before generating.")
        else:
            with st.spinner("⏳ Generating summary and keywords..."):
                response = requests.post(BACKEND_URL, json={"input": article_input})
                response.raise_for_status()
                result = response.json()

            st.subheader("Response: \n")
            with st.container():
                st.markdown("### 📖 Summary") 
                st.markdown("**Summary** : " + response.json()["summary"][-1])

            with st.container():
                st.markdown("### 🔑 Keywords")
                st.markdown("**Keywords** : " + response.json()["keyword"][-1][-1])

            with st.container():
                st.markdown("### 📊 Confidence Score")
                st.markdown("**Confidence Score** : " + str(response.json()["confidence_score"][-1]) +  "%")
                st.progress((response.json()["confidence_score"][-1]) / 100)


    st.markdown("---")

   

if __name__ == "__main__":
    main()
