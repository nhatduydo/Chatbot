import streamlit as st
from PyPDF2 import PdfReader # dùng pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter #chia tách văn bản


#upload file PDF
st.header("My chatbot")
with st.sidebar:
      st.title("your Document")
      file = st.file_uploader("upload file PDF", type='pdf')
      
#extract the text
if file is not None:
      pdf_reader = PdfReader(file)
      text = ""
      for page in pdf_reader.pages:
            text+= page.extract_text()

            # st.write(text)
#break it into chunks
      text_splitter = RecursiveCharacterTextSplitter(
            separators="\n",
            chunk_size = 1000,
            chunk_overlap = 150,
            length_function = len
      )
      
      chunks = text_splitter.split_text(text)
      st.write(chunks)