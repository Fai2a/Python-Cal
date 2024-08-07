import streamlit as st

# Calculator function
def calculator():
    st.title("Simple Calculator")

    # User input
    num1 = st.number_input("Enter the first number:", format="%f")
    num2 = st.number_input("Enter the second number:", format="%f")
    operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform calculation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    # Display result
    st.write(f"The result is: {result}")

if __name__ == "__main__":
    calculator()
