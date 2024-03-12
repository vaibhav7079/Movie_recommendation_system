import streamlit
import pandas as pd
from utils import  list_of_movies , recommended

list_of_rec = list_of_movies()

streamlit.header("MOVIE RECOMMENDATION SYSTEM")

selected_movie=streamlit.selectbox("Select a movie",list_of_rec)
count = streamlit.slider("How many movies you want to show ?")

reco = recommended(selected_movie,count)
streamlit.write(reco)


