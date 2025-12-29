import streamlit as st
import requests

st.set_page_config(
    page_title="Market Intel AI",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2666/2666505.png", width=100)
    st.title("Market Analyst Bot")
    st.markdown("""
    ### About
    This system uses **Tavily AI** for real-time web search and **Llama-3** to analyze:
    *  Competitor Trends
    * Market Risks
    *  New Opportunities
    """)
    st.divider()
    st.info("Ensure the FastAPI server is running on port 8000")

st.title(" AI Market Intelligence Analyst")
st.write("Get real-time deep research on any company, industry, or market trend.")

query = st.text_input("What market or company do you want to analyze?", 
                     placeholder="e.g. Impact of AI on the European automotive industry...")

if st.button("Generate Market Report"):
    if query:
        with st.spinner(" Searching web and synthesizing data... This may take a few seconds."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask", 
                    json={"query": query},
                    timeout=60 
                )
                
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    
                    st.success(" Analysis Complete!")
                    st.markdown("---")
                    
                    st.markdown(answer)
                    
                    st.download_button(
                        label=" Download Report",
                        data=answer,
                        file_name=f"market_report_{query.replace(' ', '_')}.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Backend Error: {response.status_code}")
                    st.json(response.json()) 
                    
            except requests.exceptions.ConnectionError:
                st.error(" Connection Failed! Please make sure your FastAPI server (uvicorn) is running.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning(" Please enter a topic to research.")