from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from search_engine import fetch_market_data
from langchain_core.output_parsers import StrOutputParser

def get_chain():
    llm = ChatGroq(
        model='llama-3.3-70b-versatile',
        max_tokens=1024,
        temperature=0
    )

    template = """
    You are an expert Market Research Analyst.
    Use the following context to answer the user's query.

    Context: {context}
    Topic: {query}

    Structure:
    1. Executive Summary
    2. Key Findings & Trends
    3. Potential Risks/Opportunities
    4. References (URLs)
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {
            "context": RunnableLambda(lambda x: fetch_market_data(x["query"])),
            "query": lambda x: x["query"]
        }
        | prompt 
        | llm 
        | StrOutputParser()
    )
    return chain