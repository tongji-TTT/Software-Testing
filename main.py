import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import test
import triangle_test
import calender_test
import computer_salesperson_test
import tel_charges_test
import get_percent
import datetime
import numpy as np

st.header("SoftwareTesting")
option = st.selectbox(
    'How would you like ?',
     ('aa', 'triangle_test','calender_test','computer_salesperson_test','tel_charges_test')
)
if option == 'aa':
    st.subheader('aa')
    uploaded_file = st.file_uploader("Choose a file",key = 'aa')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe_resulted = dataframe.copy()
        for index in dataframe.index:
            dataframe_resulted.at[index,'test']=test.test_a(
            dataframe.at[index,'a'],dataframe.at[index,'b'],dataframe.at[index,'c'])
        st.write(dataframe)
        st.write(dataframe_resulted)
        dataframe_resulted.to_csv('bigger_2.csv')

elif option == 'triangle_test':
    st.subheader('triangle_test')
    uploaded_file = st.file_uploader("Choose a file", key='triangle_test')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe_resulted = dataframe.copy()
        for index in dataframe.index:
            dataframe_resulted.at[index,'actual']=triangle_test.triangle_atom\
                (dataframe.at[index,'a'],dataframe.at[index,'b'],dataframe.at[index,'c'])
            if(dataframe_resulted.at[index,'expect']==dataframe_resulted.at[index,'actual']):
                dataframe_resulted.at[index, 'isSame'] = True
            else: dataframe_resulted.at[index, 'isSame'] = False
            dataframe_resulted.at[index, 'testTime']=datetime.datetime.now()
            dataframe_resulted.at[index, 'tester'] = 'drt'
        dataframe_resulted_false = dataframe_resulted[dataframe_resulted['isSame']== False]
        # st.write(dataframe)
        st.subheader('Result')
        st.write(dataframe_resulted)
        dataframe_resulted.to_csv('test/1_debug.csv',index= False)
        st.subheader('Bug_result')
        st.write(dataframe_resulted_false)
        # st.write(get_percent.get_per(dataframe_resulted))
        sizes = [get_percent.get_per(dataframe_resulted),1-get_percent.get_per(dataframe_resulted)]
        fig = plt.figure()
        plt.pie(sizes, labels=['passed','failed'],explode=(0,0.2), autopct='%.2f%%', colors=["#d5695d", "#5d8ca8"])
        st.pyplot(fig)
    with st.form("triangle_form"):
        title_1 = st.number_input('side A')
        title_2 = st.number_input('side B')
        title_3 = st.number_input('side C')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(triangle_test.triangle_atom(title_1,title_2,title_3))

elif option == 'calender_test':
    st.subheader('calender_test')
    uploaded_file = st.file_uploader("Choose a file", key='calender_test')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe_resulted = dataframe.copy()
        for index in dataframe.index:
            dataframe_resulted.at[index, 'actual'] = calender_test.get_calender\
                (dataframe.at[index, 'year'], dataframe.at[index, 'month'], dataframe.at[index, 'day'])
            if (dataframe_resulted.at[index, 'expect'] == dataframe_resulted.at[index, 'actual']):
                dataframe_resulted.at[index, 'isSame'] = True
            else:
                dataframe_resulted.at[index, 'isSame'] = False
            dataframe_resulted.at[index, 'testTime'] = datetime.datetime.now()
            dataframe_resulted.at[index, 'tester'] = 'drt'
        dataframe_resulted_false = dataframe_resulted[dataframe_resulted['isSame'] == False]
        st.subheader('Result')
        st.write(dataframe_resulted)
        dataframe_resulted.to_csv('test/2_debug.csv', index=False)
        st.subheader('Bug_result')
        st.write(dataframe_resulted_false)
        sizes = [get_percent.get_per(dataframe_resulted), 1 - get_percent.get_per(dataframe_resulted)]
        fig = plt.figure()
        plt.pie(sizes, labels=['passed', 'failed'], explode=(0, 0.2), autopct='%.2f%%', colors=["#d5695d", "#5d8ca8"])
        st.pyplot(fig)
    with st.form("calender_form"):
        title_1 = st.number_input('year',format='%g')
        title_2 = st.number_input('month',format='%g')
        title_3 = st.number_input('day',format='%g')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(calender_test.get_calender(int(title_1),int(title_2),int(title_3)))

elif option == 'computer_salesperson_test':
    st.subheader('computer_salesperson_test')
    uploaded_file = st.file_uploader("Choose a file", key='computer_salesperson_test')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe_resulted = dataframe.copy()
        for index in dataframe.index:
            dataframe_resulted.at[index, 'actual'] = computer_salesperson_test.get_total\
                (dataframe.at[index, 'host'], dataframe.at[index, 'screen'], dataframe.at[index, 'equipment'])
            if (dataframe_resulted.at[index, 'expect'] == dataframe_resulted.at[index, 'actual']):
                dataframe_resulted.at[index, 'isSame'] = True
            else:
                dataframe_resulted.at[index, 'isSame'] = False
            dataframe_resulted.at[index, 'testTime'] = datetime.datetime.now()
            dataframe_resulted.at[index, 'tester'] = 'drt'
        dataframe_resulted_false = dataframe_resulted[dataframe_resulted['isSame'] == False]
        st.subheader('Result')
        st.write(dataframe_resulted)
        dataframe_resulted.to_csv('test/4_debug.csv', index=False)
        st.subheader('Bug_result')
        st.write(dataframe_resulted_false)
        sizes = [get_percent.get_per(dataframe_resulted), 1 - get_percent.get_per(dataframe_resulted)]
        fig = plt.figure()
        plt.pie(sizes, labels=['passed', 'failed'], explode=(0, 0.2), autopct='%.2f%%', colors=["#d5695d", "#5d8ca8"])
        st.pyplot(fig)
    with st.form("computer_salesperson_form"):
        title_1 = st.number_input('host number')
        title_2 = st.number_input('screen number')
        title_3 = st.number_input('experiment number')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(computer_salesperson_test.get_total(title_1,title_2,title_3))

elif option == 'tel_charges_test':
    st.subheader('tel_charges_test')
    uploaded_file = st.file_uploader("Choose a file", key='tel_charges_test')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        dataframe_resulted = dataframe.copy()
        for index in dataframe.index:
            dataframe_resulted.at[index, 'actual'] = tel_charges_test.get_total\
                (dataframe.at[index, 'minutes'], dataframe.at[index, 'times'])
            if (dataframe_resulted.at[index, 'expect'] == dataframe_resulted.at[index, 'actual']):
                dataframe_resulted.at[index, 'isSame'] = True
            else:
                dataframe_resulted.at[index, 'isSame'] = False
            dataframe_resulted.at[index, 'testTime'] = datetime.datetime.now()
            dataframe_resulted.at[index, 'tester'] = 'drt'
        dataframe_resulted_false = dataframe_resulted[dataframe_resulted['isSame'] == False]
        st.subheader('Result')
        st.write(dataframe_resulted)
        dataframe_resulted.to_csv('test/7_debug.csv', index=False)
        st.subheader('Bug_result')
        st.write(dataframe_resulted_false)
        sizes = [get_percent.get_per(dataframe_resulted), 1 - get_percent.get_per(dataframe_resulted)]
        fig = plt.figure()
        plt.pie(sizes, labels=['passed', 'failed'], explode=(0, 0.2), autopct='%.2f%%', colors=["#d5695d", "#5d8ca8"])
        st.pyplot(fig)
    with st.form("tel_charges_form"):
        title_1 = st.number_input('minutes')
        title_2 = st.number_input('times')
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(tel_charges_test.get_total(title_1, title_2))