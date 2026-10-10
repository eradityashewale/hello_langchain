from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main() -> None:
    prompt = ChatPromptTemplate.from_template("Say hello to {name} in one sentence.")
    llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0)
    chain = prompt | llm | StrOutputParser()

    print(chain.invoke({"name": "world"}))
