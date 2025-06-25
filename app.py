#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os

input_firstname = st.text_input('名前を入力してください')
input_lastname = st.text_input('名字を入力してください')
input_year = st.text_input('生まれ年を入力してください')
input_month = st.text_input('生まれた年を入力してください')
input_date = st.text_input('生まれた日を入力してください')
result=""

if st.button('表示'):
    result='「'+input_firstname+'」「'+input_lastname+'」の誕生日は「'+input_year+'」年「'+input_month+'」月「'+input_date+'」日です'
    st.write(result)

