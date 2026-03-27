from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os

# ✅ Load environment variables FIRST
load_dotenv()


# ✅ Create LLM inside a function (IMPORTANT for Streamlit Cloud)
def get_llm():
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")

    return ChatGroq(
        model_name="llama-3.3-70b-versatile",
        groq_api_key=groq_api_key
    )


# ✅ Main extraction function
def extract(article_text):
    if not article_text or article_text.strip() == "":
        raise ValueError("Input text is empty.")

    llm = get_llm()  # ✅ Initialize here (not globally)

    prompt = """
    From the below news article, extract revenue and eps in JSON format containing the
    following keys: 'revenue_actual', 'revenue_expected', 'eps_actual', 'eps_expected'. 

    Each value should have a unit such as million or billion.

    Only return valid JSON. No preamble.

    Article
    =======
    {article}
    """

    # ✅ Create prompt template
    pt = PromptTemplate.from_template(prompt)

    # ✅ Create chain
    chain = pt | llm

    # ✅ Invoke model
    response = chain.invoke({"article": article_text})

    # ✅ Parse output
    parser = JsonOutputParser()

    try:
        result = parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException(
            "Failed to parse LLM output. Try smaller input."
        )

    # ✅ Ensure all keys exist (safe handling)
    expected_keys = [
        "revenue_actual",
        "revenue_expected",
        "eps_actual",
        "eps_expected"
    ]

    for key in expected_keys:
        if key not in result:
            result[key] = "Not Available"

    return result
