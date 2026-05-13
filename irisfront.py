import streamlit as st
import pickle
st.write("enter the detail requires to find which species does a flower belong")
a=st.number_input("enter the sepal length")
b=st.number_input("enter the sepal width")
c=st.number_input("enter the petal length")
d=st.number_input("enter the petal wwidth")
if st.button("predict"):
    with open(r"C:\Users\khade\akira\iris_model.pkl","rb") as file:
        loaded_model=pickle.load(file)
    result=loaded_model.predict([[a,b,c,d]])
    st.write(result)