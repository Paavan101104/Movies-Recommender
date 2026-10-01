import streamlit as st
import pickle
import pandas as pd
import joblib
import nltk
import sklearn
similartiy=joblib.load('similarity.joblib')
st.title("Movie Recommender System")
movies=pd.read_pickle('movie.pkl')
name_movies=movies['title'].values
pqt=st.selectbox('Enter the Movie Name',name_movies)

def recomend(name_movie):
    L=[]
    movie_index=movies[movies['title']==name_movie].index[0]
    recomended=similartiy[movie_index]
    movie_list=sorted(enumerate(recomended),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_list:
        L.append(movies.iloc[i[0]].title)
    return L



if st.button('Recommend'):
    r=recomend(pqt)

    st.write("The Recommended Movies are:")
    for i in r:
        st.write(i)