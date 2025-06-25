#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os
from datetime import date

input_firstname = st.text_input('名前を入力してください')
input_lastname = st.text_input('名字を入力してください')
select_year = st.selectbox('年',(range(1990,2026)))
select_month = st.selectbox('月',(range(1,13)))
input_date = st.text_input('日')
result=""
col1, col2 = st.columns(2)
with col1:
    button1 = st.button('記号無で生成')
with col2:
    button2 = st.button('記号有で生成')
    
if input_firstname = '' or input_lastname = '':
    st.write('名前を入力してください')
else:
    if input_date < 0 or ((select_month = 4 or select month = 6 or select_month = 9 or select_month = 11) and int(input_date) > 31):
        st.write('正しい生年月日を入力してください')
    else:
        if button1:
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は' + str(select_year) + '年'+ str(select_month) + '月' + input_date + '日です'
            st.write(result)
        elif button2:
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は、' + str(select_year) + '年'+ str(select_month) + '月' + input_date + '日です!'
            st.write(result)
