from src.toolBox.toolBox import ToolBox
from src.tools import Tools
from dotenv import load_dotenv
from transformers import pipeline
import torch
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

#Is the gpu is not available it will use the cpu
device = 0 if torch.cuda.is_available() else -1
model = pipeline("summarization",
                  model="facebook/bart-large-cnn",
                  device=device,
                  max_length=500,
                  min_length=10
                   )
llm = HuggingFacePipeline(pipeline = model)
prompt = PromptTemplate(
    input_variables=["texte"],
    template ="Resume ce texte en gardant le contexte clair il faut faire comprendre a l'usager ce que le texte veut faire comprendre {texte}"
)


chain = prompt | llm

rawString = ToolBox.convert_pdf_to_string(r"C:\Users\Arnaud\Downloads\CV_Arnaud_Simard-Desmeules.pdf")
convertedString = Tools.prepare_string_for_ai(rawString)

resume = chain.invoke({"texte" : convertedString})
print(resume)
