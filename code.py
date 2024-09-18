import streamlit as st
import requests
st.title('A Dad Joke App')


def create_joke ():
        
    url = "https://icanhazdadjoke.com/"
    parameters = {
        "Accept" : "text/plain",
        "User-Agent": "VSCode",
    }

    response = requests.get(url, headers=parameters)
    return response.text


def addition(firstnum, secondnum):
    return firstnum + secondnum


def checkint(first,second):
    if type(first) == int and type(second) == int:
        return True
    
    # #first number not interger, second is integer
    # elif type(first) != int and type(second) == int:
    #     print ("first number is not integer \n")

    # #second number not interger, first is integer
    # elif type(first) == int and type(second) != int:
    #     print ("second number is not integer \n")

    else: 
        return False

def multiply (first,second):
    isnumber = checkint(first,second)
    if isnumber == True:
        return first * second

    else:
        return False
    



display_joke = st.button("generate joke", type="primary")


if display_joke:
    st.caption(create_joke())





# Function to add two numbers
def add_numbers():
    st.title("Add Two Numbers")

    # Input fields to prompt the user for two numbers
    num1 = st.number_input("Enter the first number", value=0, key=1)
    num2 = st.number_input("Enter the second number", value=0, key=2)

    # Add the two numbers
    sum_result = addition(num1,num2)

    # Display the result when the button is clicked
    if st.button("Add"):
        st.write(f"The sum of {num1} and {num2} is {sum_result}")

# Call the function
if __name__ == "__main__":
    add_numbers()



def multiply_numbers():
    st.title("Multiply Two Numbers")

    # Input fields to prompt the user for two numbers
    num3 = st.number_input("Enter the first number", value=0, key=3)
    num4 = st.number_input("Enter the second number", value=0, key=4)

    # Multiply the two numbers
    product_result = multiply(num3,num4)

     # Display the result when the button is clicked
    if st.button("Multiply"):
        st.write(f"The product of {num3} and {num4} is {product_result}")

# Call the function
if __name__ == "__main__":
    multiply_numbers()
