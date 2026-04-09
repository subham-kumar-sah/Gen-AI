from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from prompt_template import research_prompt

load_dotenv()

st.header("Research Tool")
# Dropdown: Title
title = st.selectbox(
    "Select Research Paper Title",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-4 Technical Report",
        "ResNet: Deep Residual Learning",
        "Diffusion Models for Image Generation"
    ]
)

# Dropdown: Explanation Style
style = st.selectbox(
    "Select Explanation Style",
    [
        "Simple (Beginner friendly)",
        "Technical",
        "Bullet Points",
        "Detailed Explanation"
    ]
)

# Dropdown: Explanation Length
length = st.selectbox(
    "Select Explanation Length",
    [
        "Short (3-5 lines)",
        "Medium (1 paragraph)",
        "Detailed (multiple paragraphs)"
    ]
)

model = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=300)

if st.button("Summarize"):
    
    #Filling the prompt template with user selections
    final_prompt = {
        "title": title,
        "style": style,
        "length": length
    }
    # Creating a chain that combines the prompt template and the model
    chain =  research_prompt | model
    with st.spinner("Generating summary..."):
        response = chain.invoke(final_prompt)

    st.subheader("📌 Summary")
    st.write(response.content)    
