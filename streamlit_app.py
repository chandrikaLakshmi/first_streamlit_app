import streamlit

streamlit.title('My Favourites new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothiee')
streamlit.text('🐔 Hard boiled free-range egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a pick list here so the can pick the fruit the want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
