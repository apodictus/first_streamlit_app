import streamlit
import pandas

streamlit.title('my Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set the index for the list
my_fruit_list = my_fruit_list.set_index("Fruit")
#Add a picklist + default picks
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table
streamlit.dataframe(fruits_to_show)

#fruityvice API
streamlit.header('Fruityvice Fruit Advice')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()) #just dumps json to screen
#normalize json output
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it as table
streamlit.dataframe(fruityvice_normalized)
