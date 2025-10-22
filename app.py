#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import os
from datetime import date
import itertools

st.title('パスワード自動作成プログラム')

l0 = ['', '']                   #名前の文字列
l1 = ["none", "upper"]             # 何もしない、大文字へ
l2 = ["all", "first", "even", "odd"] # 全部、最初だけ、偶数番目だけ、奇数番目だけ

n0 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']               #生年月日の文字列

bef0 = ['0', '1', '2', '5', 'i', 'o', 's', 'z']
aft0 = ['o', 'i', 'z', 's', '1', '0', '5', '2']
bef1 = ['0', '1', '1', '2', '5', 'a', 'i', 'i', 'o', 's', 's', 'z']
aft1 = ['o', 'i', '!', 'z', 's', '@', '1', '!', '0', '5', '$', '2']

c0=["abcdefghijklmnopqrst"] #　並びパターン

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

n0[3] = n0[0] + n0[1] + n0[2]
n0[4] = n0[0] + n0[1]
n0[5] = n0[0] + n0[2]
n0[6] = n0[1] + n0[2]

n0[7] = str(int(n0[0]) + int(n0[1]) + int(n0[2]))
n0[8] = str(int(n0[0]) + int(n0[1]))
n0[9] = str(int(n0[0]) + int(n0[2]))
n0[10] = str(int(n0[1]) + int(n0[2]))

n0[11] = str(int(int(int(n0[0]) / 1000) % 10) + int(int(int(n0[0]) / 100) % 10) + int(int(int(n0[0]) / 10) % 10) + int(int(n0[0]) % 10))
n0[12] = str(int(int(int(n0[1]) / 10) % 10) + int(int(n0[1]) % 10))
n0[13] = str(int(int(int(n0[2]) / 10) % 10) + int(int(n0[2]) % 10))
n0[14] = str(int(int(int(n0[0]) / 1000) % 10) + int(int(int(n0[0]) / 100) % 10) + int(int(int(n0[0]) / 10) % 10) + int(int(n0[0]) % 10) + int(int(int(n0[1]) / 10) % 10) + int(int(n0[1]) % 10) + int(int(int(n0[2]) / 10) % 10) + int(int(n0[2]) % 10))
n0[15] = str(int(int(int(n0[0]) / 1000) % 10) + int(int(int(n0[0]) / 100) % 10) + int(int(int(n0[0]) / 10) % 10) + int(int(n0[0]) % 10) + int(int(int(n0[1]) / 10) % 10) + int(int(n0[1]) % 10))
n0[16] = str(int(int(int(n0[0]) / 1000) % 10) + int(int(int(n0[0]) / 100) % 10) + int(int(int(n0[0]) / 10) % 10) + int(int(n0[0]) % 10) + int(int(int(n0[2]) / 10) % 10) + int(int(n0[2]) % 10))
n0[17] = str(int(int(int(n0[1]) / 10) % 10) + int(int(n0[1]) % 10) + int(int(int(n0[2]) / 10) % 10) + int(int(n0[2]) % 10))

select_sign = st.selectbox('記号を入れたパスワードを作りますか？',('いいえ', 'はい'))

button = st.button('作成')

if button:
        if l0[0] == '' and l0[1] == '':
            st.write('名前と名字を入力してください')
        elif l0[0] == '' and l0[1] != '':
            st.write('名前を入力してください')
        elif l0[0] != '' and l0[1] == '':
            st.write('名字を入力してください')
        else:    
            def change0(x0, x1, x2): # 文字列の置き換え
              if x1 == "none":
                return x0
              elif x1 == "upper":
                if x2 == "all":
                  return x0.upper()
                elif x2 == "first":
                  return x0[0].upper() + x0[1:]
                elif x2 == "even":
                  return "".join([x0[i].upper() if i % 2 == 0 else x0[i] for i in range(len(x0))])
                elif x2 == "odd":
                  return "".join([x0[i].upper() if i % 2 == 1 else x0[i] for i in range(len(x0))])
                else:
                  return x0
              else:
                return x0
            
            def change1(x0, x1, cc): # 文字列の置き換え
              x = ""
              for i in range(len(cc)):
                if cc[i]=="a":
                  x=x+x0[0]
                elif cc[i]=="b":
                  x=x+x0[1]
                elif cc[i]=="c":
                  x=x+x1[0]
                elif cc[i]=="d":
                  x=x+x1[1]
                elif cc[i]=="e":
                  x=x+x1[2]
                elif cc[i] == "f":
                  x=x+x1[3]
                elif cc[i] == "g":
                  x=x+x1[4]
                elif cc[i] == "h":
                  x=x+x1[5]
                elif cc[i] == "i":
                  x=x+x1[6]
                elif cc[i] == "j":
                  x=x+x1[7]
                elif cc[i] == "k":
                  x=x+x1[8]
                elif cc[i] == "l":
                  x=x+x1[9]
                elif cc[i] == "m":
                  x=x+x1[10]
                elif cc[i] == "n":
                  x=x+x1[11]
                elif cc[i] == "o":
                  x=x+x1[12]
                elif cc[i] == "p":
                  x=x+x1[13]
                elif cc[i] == "q":
                  x=x+x1[14]
                elif cc[i] == "r":
                  x=x+x1[15]
                elif cc[i] == "s":
                  x=x+x1[16]
                elif cc[i] == "t":
                  x=x+x1[17]
                else:
                  x = x
              return x
                
            if select_sign == 'いいえ':
                st.session_state.count = 0
                for v1, v2, w0 in itertools.product(l1, l2, c0):
                  #print(v0,v1,v2)
                  name = []
                  name.append(change0(l0[0], v1, v2))
                  name.append(change0(l0[1], v1, v2))
                  x = change1(name, n0, w0)
                  st.write(x)
                  st.session_state.count += 1
                  for a in range(len(bef0)):
                      if bef0[a] in x:
                          st.write(x.replace(bef0[a], aft0[a]))
                          st.session_state.count += 1
                st.write(str(st.session_state.count) + '個のパスワードを生成しました')
                
            if select_sign == 'はい':
                st.session_state.count = 0
                for v1, v2, w0 in itertools.product(l1, l2, c0):
                  #print(v0,v1,v2)
                  name = []
                  name.append(change0(l0[0], v1, v2))
                  name.append(change0(l0[1], v1, v2))
                  x = change1(name, n0, w0)
                  st.write(x)
                  st.session_state.count += 1
                  for b in range(len(bef1)):
                      if bef1[b] in x:
                          st.write(x.replace(bef1[b], aft1[b]))
                          st.session_state.count += 1
                st.write(str(st.session_state.count) + '個のパスワードを生成しました')
