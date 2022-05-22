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
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())#just writes the data to the screen

#Take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#Output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
