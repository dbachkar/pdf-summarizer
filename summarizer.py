from dotenv import load_dotenv
import os
from pypdf import PdfReader
from groq import Groq


load_dotenv(r"D:\PYTHON PROJECTS\.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize(text):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": f"Summarize this in one sentence: {text}"}
        ]
    )
    return response.choices[0].message.content



def read_pdf(file_path):
    reader =PdfReader(file_path)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text

def summarize_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            full_path =os.path.join(folder_path,filename)
            text =read_pdf(full_path)
            summary=summarize(text)
            print(f"File: {filename}\nSummary: {summary}\n")


summarize_folder("proposals")