#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os
from datetime import date

input_firstname = st.text_input('名前を入力してください')
input_lastname = st.text_input('名字を入力してください')
select_year = st.selectbox('年',(range(1990,2025)))
select_month = st.selectbox('月',(range(1,12)))
input_date = st.text_input('日')
result=""

if st.button('記号有で生成'):
    result=''+input_firstname+''+input_lastname+'の誕生日は'+select_year+'年'+select_month+'月'+input_date+'日です'
    st.write(result)
elif st.button('記号無で生成'):
    result=''+input_firstname+''+input_lastname+'の誕生日は、'+select_year+'年'+select_month+'月'+input_date+'日です!'
