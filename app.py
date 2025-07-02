#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os
from datetime import date

input_firstname = st.text_input('名前を入力してください')
input_lastname = st.text_input('名字を入力してください')
select_year = st.selectbox('年',(range(1900,2026)))
select_month = st.selectbox('月',(range(1,13)))
input_date = st.text_input('日')
result=""
col1, col2 = st.columns(2)
with col1:
    button1 = st.button('記号無で生成')
with col2:
    button2 = st.button('記号有で生成')
    
if input_firstname == '' or input_lastname == '':
    st.write('名前を入力してください')
else:
    if int(input_date) < 0 or int(input_date) > 31 or ((int(select_month) == 4 or int(select_month) == 6 or int(select_month) == 9 or int(select_month) == 11) and int(input_day) > 30) or (((int(select_year) % 4 == 0 and int(select_year) % 100 != 0) or int(select_year) % 400 == 0) and int(select_month) == 2 and int(input_date) > 29) or (not((int(select_year) % 4 == 0 and int(select_year) % 100 != 0) or int(select_year) % 400 == 0) and int(select_month) == 2 and int(input_date) > 28):
        st.write('正しい生年月日を入力してください')
    else:
        if button1:
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は' + str(select_year) + '年'+ str(select_month) + '月' + input_date + '日です'
            st.write(result)
        else:
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は、' + str(select_year) + '年'+ str(select_month) + '月' + input_date + '日です!'
            st.write(result)
