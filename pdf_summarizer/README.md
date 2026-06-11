# PDF Summarizer

A Python tool that reads PDF files and generates concise summaries using the Groq API (LLaMA 3.1).

## What it does
- Extracts text from any PDF file
- Summarizes individual PDFs
- Batch processes an entire folder of PDFs automatically

## Why I built this
This is the first module of a larger proposal generation tool I'm building for a robotics and automation company. The goal is to eventually analyze past proposals and assist in drafting new ones.

## Setup
1. Clone the repo
2. Install dependencies: `pip install groq pypdf python-dotenv`
3. Create a `.env` file with your Groq API key: `GROQ_API_KEY=your_key_here`
4. Add PDFs to a folder called `proposals`
5. Run: `python summarizer.py`

## Tech used
- Python
- Groq API (LLaMA 3.1)
- pypdf
- python-dotenv