import streamlit as st


def div():
  st.title("Division of Two Numbers")
  html_temp = """
  <div>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  
  if(num1==0 or num2==0):
    result = 0
  else:
    result=num1/num2
  
  st.success(f'The division is {result}')
  
if __name__=='__main__':
  div()
