# Bring in deps
import os 
from apikey import apikey
import pandas as pd
from langchain.agents import create_spark_dataframe_agent
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from pyspark.sql import SparkSession

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜🔗 Pyspark Application with ChatGPT')
prompt = st.text_input('Ask your query here')


with st.sidebar.container():
    st.title("Pyspark Query Being Executed")


sql_query_template = PromptTemplate(
    input_variables = ['query'],
    template='Give me the sql query to generate the {query}'
)


pyspark_query_template = PromptTemplate(
    input_variables = ['query'],
    template='Give me the pyspark code to generate {query}'
)


result_template = PromptTemplate(
    input_variables = ['query'],
    template='Give me the results in {query} in table format'
)
# Llms
llm = OpenAI(temperature=0.9)
spark = SparkSession.builder.getOrCreate()
csv_file_path = "/Users/rohanganesh/Desktop/llm-app/csv/multi_store.csv"
csv_file_path2 = "/Users/rohanganesh/Desktop/llm-app/csv/jewellery.csv"
csv_file_path3 = "/Users/rohanganesh/Desktop/llm-app/csv/electronics.csv"
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
df2 = spark.read.csv(csv_file_path2, header=True, inferSchema=True)
df3 = spark.read.csv(csv_file_path3, header=True, inferSchema=True)
sql_query_chain = LLMChain(llm=llm, prompt=sql_query_template, verbose=True, output_key='Query')
pyspark_query_chain = LLMChain(llm=llm, prompt=pyspark_query_template, verbose=True, output_key='Query')
agent = create_spark_dataframe_agent(llm=OpenAI(temperature=0), df=df, verbose=True)
agent2 = create_spark_dataframe_agent(llm=OpenAI(temperature=0), df=df2, verbose=True)
agent3 = create_spark_dataframe_agent(llm=OpenAI(temperature=0), df=df3, verbose=True)


if prompt:
    sql_query = sql_query_chain.run(prompt)
    pyspark_query = pyspark_query_chain.run(prompt)
    final_prompt = prompt+" Convert the following result to a table"
    final_response ="data not found"
    final_response = agent3.run(final_prompt)
    st.sidebar.write(pyspark_query)
    st.write(final_response)


