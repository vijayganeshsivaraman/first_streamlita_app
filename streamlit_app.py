#created the main python file

import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

def get_fruitvice_data(this_fruit_chice):
        streamlit.write('The user entered ', fruit_choice)
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_chice)
        # write your own comment -what does the next line do? 
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
         # write your own comment - what does this do?
        return fruityvice_normalized

streamlit.title('My Moms new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]



streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        back_from_function = get_fruitvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
   streamlit.error()

def get_fruit_load_list():
         with my_cnx.cursor() as mycur:
                        my_cur.execute("select * from fruit_load_list")
                        return my_cur.fetchall()
               
streamlit.header("The fruit load list containe:")
streamlit.button('Get Fruit Load List')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list() 
streamlit.dataframe(my_data_rows)
        

streamlit.stop()

fruit_choice = streamlit.text_input('What fruit would you like to add  about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")



   
