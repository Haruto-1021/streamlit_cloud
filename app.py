#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import os
from datetime import date

st.title('パスワード自動作成プログラム')

l0 = ['', '']                   #名前の文字列
l1 = ["none", "upper"]             # 何もしない、大文字へ
l2 = ["all", "first", "even", "odd"] # 全部、最初だけ、偶数番目だけ、奇数番目だけ

n0 = ['', '', '']               #生年月日の文字列

s0 = ["!", "#", "$", "%", "=", "-", "+", "@"] #記号の文字列

result=""

l0[0] = st.text_input('名前を入力してください')
l0[1] = st.text_input('名字を入力してください')
n0[0] = st.selectbox('生まれた年を選択してください',(range(1900,2026)))
n0[1] = st.selectbox('生まれた月を選択してください',(range(1,13)))
if int(n0[1]) == 4 or int(n0[1]) == 6 or int(n0[1]) == 9 or int(n0[1]) == 11:
    n = 30
elif ((int(n0[0]) % 4 == 0 and int(n0[0]) % 100 != 0) or int(n0[0]) % 400 == 0) and int(n0[1]) == 2:
    n = 29
elif not((int(n0[0]) % 4 == 0 and int(n0[0]) % 100 != 0) or int(n0[0]) % 400 == 0) and int(n0[1]) == 2:
    n = 28
else:
    n=31
n0[2] = st.selectbox('生まれた日を選択してください',(range(1,n+1)))

select_sign = st.selectbox('記号を入れたパスワードを作りますか？',('いいえ', 'はい'))
button = st.button('作成')

if button:
    if select_sign == 'いいえ':
        if l0[0] == '' and l0[1] == '':
            st.write('名前と名字を入力してください')
        elif l0[0] == '' and l0[1] != '':
            st.write('名前を入力してください')
        elif l0[0] != '' and l0[1] == '':
            st.write('名字を入力してください')
        else:    
            result = str(l0[0]) + str(l0[1]) + 'の誕生日は' + str(n0[0]) + '年'+ str(n0[1]) + '月' + str(n0[2]) + '日です'
            st.write(result)
    elif select_sign == 'はい':
        if l0[0] == '' and lo[1] == '':
            st.write('名前と名字を入力してください')
        elif l0[0] == '' and l0[1] != '':
            st.write('名前を入力してください')
        elif l0[0] != '' and l0[1] == '':
            st.write('名字を入力してください')
        else:
            result = str(l0[0]) + str(l0[1]) + 'の誕生日は、' + str(n0[0]) + '年'+ str(n0[1]) + '月' + str(n0[2]) + '日です!'
            st.write(result)
