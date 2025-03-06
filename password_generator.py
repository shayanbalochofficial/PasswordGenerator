import streamlit as st
import random
import string


def passwordGen(Lenght, use_digits, use_speacial):
    char = string.ascii_letters 

    if use_digits:
        char += string.digits  #Add numbers (0-9)

    if use_speacial:
        char += string.punctuation #Adds Speacial Characters

    return ''.join(random.choice(char) for _ in range(Lenght))

st.title('Password Generator')
length = st.slider("Select Password Length", min_value=8, max_value=24, value=10)

use_digits = st.checkbox('Use Digits')
use_speacial = st.checkbox('Use Speacial Characters')

if st.button('Generate Password'):
    password = passwordGen(length, use_digits, use_speacial)
    st.write(f'Generated Password: \t `{password}`')

st.write('----------------------------------------------------------------')

st.write('🚀 Made by [Shayan Baloch](www.github.com/shayanbalochofficial)')

