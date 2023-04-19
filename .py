import streamlit as st

def largest_of_three_numbers(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

st.title("Find the largest among three numbers")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

if st.button("Find largest number"):
    result = largest_of_three_numbers(a,b,c)
    st.success(f"The largest number is {result}")
