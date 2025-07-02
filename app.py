#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os
from datetime import date

st.title('パスワード自動作成プログラム')

input_firstname = st.text_input('名前を入力してください')
input_lastname = st.text_input('名字を入力してください')
select_year = st.selectbox('生まれた年を選択してください',(range(1900,2026)))
select_month = st.selectbox('生まれた月を選択してください',(range(1,13)))
if int(select_month) == 4 or int(select_month) == 6 or int(select_month) == 9 or int(select_month) == 11:
    n = 30
elif ((int(select_year) % 4 == 0 and int(select_year) % 100 != 0) or int(select_year) % 400 == 0) and int(select_month) == 2:
    n = 29
elif not((int(select_year) % 4 == 0 and int(select_year) % 100 != 0) or int(select_year) % 400 == 0) and int(select_month) == 2:
    n = 28
else:
    n=31
select_date = st.selectbox('生まれた日を選択してください',(range(1,n+1)))

result=""
select_sign = st.selectbox('記号を入れたパスワードを作りますか？',('はい', 'いいえ'))
button = st.button('作成')

if button:
    if radio1:
        if input_firstname == '' or input_lastname == '':
            st.write('名前を入力してください')
        else:    
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は' + str(select_year) + '年'+ str(select_month) + '月' + str(select_date) + '日です'
            st.write(result)
    elif radio2:
        if input_firstname == '' or input_lastname == '':
            st.write('名前を入力してください')
        else:
            result = str(input_firstname) + str(input_lastname) + 'の誕生日は、' + str(select_year) + '年'+ str(select_month) + '月' + str(select_date) + '日です!'
            st.write(result)
