#import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

os.environ["GOOGLE_API_KEY"] = "**write****your***api***key*****************" 
#getpass.getpass("Enter your Google AI API Key : ")

## LLM, Prompt_Templates

from langchain import PromptTemplate
from langchain.chains import LLMChain

#prompt_tempalate-1
prompt_templ = PromptTemplate(input_variables=["name"],template = "Top 10 places to visit in  {name}")

#llm
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.4,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

#LLMchain
chain1=LLMChain(llm=llm,prompt =prompt_templ,verbose=True,output_key='place')

# Simple_Sequncial_Chain

from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

#prompt_tempalate-2

second_prompt_template = PromptTemplate(input_variables = ["place"], template = "What is famous street food at {place}?")
chain2 =LLMChain(llm=llm,prompt=second_prompt_template,verbose =True,output_key ="food")

#parent_hain
#parent_chain = SimpleSequentialChain(chains = [chain1,chain2],verbose = True)
parent_chain = SequentialChain(chains =[chain1,chain2],input_variables=["name"],output_variables =["place","food"],verbose=True)

#streamlit_
st.title("Langchain Demo with GOOGLE GEMINI API : Explore Places to visit and popular foods for any city")
input_text =st.text_input("Enter Name of city : ")

if input_text :
    #st.write(parent_chain.run(input_text))
    st.write(parent_chain({'name':input_text}))



