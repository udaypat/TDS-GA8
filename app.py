import numpy as np
import pandas as pd
import streamlit as st


def div():
  st.title("Division of Two Numbers")
  html_temp = """
  <h2 style="text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  
  if(num1==0 or num2==0):
    result = 0
  else:
    result=num1/num2
  
  st.success(f'The Division is {result}')
  
if __name__ == "__main__":
  div()
