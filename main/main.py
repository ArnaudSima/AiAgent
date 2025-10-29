from dotenv import load_dotenv
from transformers import pipeline
import torch
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain
#Is the gpu is not available it will use the cpu
device = 0 if torch.cuda.is_available() else -1
model = pipeline("summarization",model="facebook/bart-large-cnn", device=device)

llm = HuggingFacePipeline(pipeline = model)
prompt = PromptTemplate(
    input_variables=["texte"],
    template ="Resume ce texte {texte}"
)


chain = LLMChain(llm = llm, prompt = prompt)

texte = """
Le langage Python est populaire pour le machine learning et le développement web.
Il est simple, lisible et possède de nombreuses bibliothèques puissantes.
"""

resume = chain.invoke({"texte" : texte})
print(resume)
