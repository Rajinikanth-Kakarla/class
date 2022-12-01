import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import streamlit as st
from PIL import Image

class Home:
    def Home():
        st.markdown("# Home ")# side channel
        st.sidebar.markdown("# Home ")
        st.sidebar.markdown("<h4 style='text-align: center; color: red;'>New!</h4><h4 style='text-align: center; color: blue;'>Python Basic Programming #BeAnEngineer20 Series </h4><br> <h4 style='text-align: center; color: blue;'>Fallow us: https://www.youtube.com/channel/UC4BtV-PBKllIqIp4rQp_m7w</h4>", unsafe_allow_html=True)
        
        img1 = Image.open('download.jpg')
        image = img1.resize((800, 450))
        st.image(image)

        st.title("Courses")

        col1, col2, col3 = st.columns(3)

        with col1:
            img2 = Image.open('py.jpg')
            image = img2.resize((250, 250))
            st.image(image)

        with col2:
            img3 = Image.open('java.jpg')
            image = img3.resize((250, 250))
            st.image(image)

        with col3:
            img4 = Image.open('c.jpg')
            image = img4.resize((250, 250))
            st.image(image)

class Dashboard:
    def Dashboard():
        st.markdown("# Dashboard ")
        st.sidebar.markdown("# Dashboard ")
        st.sidebar.image("quote.jpg")
        col1, col2, col3 = st.columns(3)

        with col1:
            img5 = Image.open('user.jpg')
            image = img5.resize((200, 200))
            st.image(image)
            st.title('John_24')

        with col2:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.markdown("<h5 style='text-align: center; color: blue;'>Name : John</h5> <br> <h6 style='text-align: center; color: blue;'>Mail : John@gmail.com</h6> <br> <h6 style='text-align: center; color: blue;'>Address : Hyderabad</h6> <br> ",unsafe_allow_html=True)

        with col3:
            st.subheader('Performance')
            courses = ['JAVA','C','PYTHON']
            completion=[20,10,80]
            colors = ['orange', 'red', 'green', ]
            explode = (0.05,0.05,0.05)
            plt.pie(completion, colors=colors, labels=courses,
            autopct='%1.1f%%', pctdistance=0.75,
            explode=explode)
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)
            plt.show()

            st.pyplot(fig)

class Videolec:
    def Videolec():
        st.markdown("# VideoLectures | Notes")

        st.sidebar.markdown("# VideoLectures | Notes <br> <h4 style='text-align: center; color: blue;'>Python Basic Programming #BeAnEngineer20 Series </h4><br> <h4 style='text-align: center; color: blue;'>Fallow us: https://www.youtube.com/channel/UC4BtV-PBKllIqIp4rQp_m7w</h4>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: blue;'>Lecture : Linear Search</h2>", unsafe_allow_html=True)
        video_file = open('Lecture0.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.image('ls1.jpg')
        st.image('ls2.jpg')

        st.markdown("<h2 style='text-align: center; color: blue;'>Lecture : Binary Search</h2>", unsafe_allow_html=True)
        video_file = open('Lecture.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.image('bs1.jpg')
        st.image('bs2.jpg')


class Recommender:
    def Recommender():
        st.markdown("# Recommender ")
        st.sidebar.markdown("# Recommender ")

    ##################################################################################################

    # <==== Code starts here ====>

        courses_list = pickle.load(open('courses.pkl','rb'))
        similarity = pickle.load(open('similarity.pkl','rb'))

        def recommend(course):
            index = courses_list[courses_list['course_name'] == course].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommended_course_names = []
            for i in distances[1:7]:
                course_name = courses_list.iloc[i[0]].course_name
                recommended_course_names.append(course_name)

            return recommended_course_names

        st.markdown("<h2 style='text-align: center; color: blue;'>Student Performance Analysis System - recommender</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>Web App created by Team-6</h4>", unsafe_allow_html=True)

        course_list = courses_list['course_name'].values
        selected_course = st.selectbox(
            "Type or select a course you like :",
            courses_list
        )

        if st.button('Show Recommended Courses'):
            st.write("Recommended Courses based on your interests are :")
            recommended_course_names = recommend(selected_course)
            st.text(recommended_course_names[0])
            st.text(recommended_course_names[1])
            st.text(recommended_course_names[2])
            st.text(recommended_course_names[3])
            st.text(recommended_course_names[4])
            st.text(recommended_course_names[5])
            st.text(" ")
            
# <==== Code ends here ====>
ch = Home
cd = Dashboard
cr = Recommender
cv = Videolec

page_names_to_funcs = {
    "Home": ch.Home,
    "Dashboard": cd.Dashboard,
    "VideoLectures | Notes": cv.Videolec,
    "Recommender": cr.Recommender,
    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()