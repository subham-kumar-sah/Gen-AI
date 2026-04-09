from langchain_core.prompts import PromptTemplate


# Research paper summarization template
research_summary_template = """
You are an expert research assistant.

Your task is to summarize a research paper based on the provided title.

Title: {title}

Requirements:
- Explanation Style: {style}
- Explanation Length: {length}

STRICT RULES:
- Use general knowledge if the paper is well-known.
- Do NOT hallucinate or invent unknown details.
- If you are not confident about the paper, respond EXACTLY:
  "Data is insufficient to provide a reliable summary."

Guidelines:
- Provide a high-level summary
- Focus on key ideas and purpose
- Avoid making specific claims if unsure

Summary:
"""


# Create PromptTemplate object
research_prompt = PromptTemplate(
    input_variables=["title", "style", "length"],
    template=research_summary_template
)
