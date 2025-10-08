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

n0 = ['', '', '']               #生年月日の文字列

c0=["000", "001", "002", "003", "004", 
    "010", "011", "012", "013", "014",
    "020", "021", "022", "023", "024",
    "030", "031", "032", "033", "034",
    "040", "041", "042", "043", "044",
    "100", "101", "102", "103", "104",
    "110", "111", "112", "113", "114",
    "120", "121", "122", "123", "124",
    "130", "131", "132", "133", "134",
    "140", "141", "142", "143", "144",
    "200", "201", "202", "203", "204",
    "210", "211", "212", "213", "214",
    "220", "221", "222", "223", "224",
    "230", "231", "232", "233", "234",
    "240", "241", "242", "243", "244",
    "300", "301", "302", "303", "304",
    "310", "311", "312", "313", "314",
    "320", "321", "322", "323", "324",
    "330", "331", "332", "333", "334",
    "340", "341", "342", "343", "344",
    "400", "401", "402", "403", "404",
    "410", "411", "412", "413", "414",
    "420", "421", "422", "423", "424",
    "430", "431", "432", "433", "434",
    "440", "441", "442", "443", "444"] #　並びパターン

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
                if cc[i] == "0":
                  x=x + x0[0]
                elif cc[i] == "1":
                  x=x + x0[1]
                elif cc[i] == "2":
                  x=x + str(x1[0])
                elif cc[i] == "3":
                  x=x + str(x1[1])
                elif cc[i] == "4":
                  x=x + str(x1[2])
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
                  if '0' in x:
                      st.write(x.replace('0', 'o'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if '1' in x:
                      st.write(x.replace('1', 'i'))
                      st.session_state.count += 1
                  else:
                      continue
                      
                  if '2' in x:
                      st.write(x.replace('2', 'z'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if '5' in x:
                      st.write(x.replace('5', 's'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'o' in x:
                      st.write(x.replace('o', '0'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'i' in x:
                      st.write(x.replace('i', '1'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'z' in x:
                      st.write(x.replace('z', '2'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 's' in x:
                      st.write(x.replace('5', 's'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                st.write(str(st.session_state.count) + '個のパスワードを生成しました')
                
            elif select_sign == "はい":
                st.session_state.count=0
                for v1,v2,w0 in itertools.product(l1,l2,c0):
                  #print(v0,v1,v2)
                  name=[]
                  name.append(change0(l0[0],v1,v2))
                  name.append(change0(l0[1],v1,v2))
                  x=change1(name,n0,w0)
                  st.write(x)
                  if '0' in x:
                      st.write(x.replace('0', 'o'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if '1' in x:
                      st.write(x.replace('1', 'i'))
                      st.session_state.count += 1
                      st.write(x.replace('1', '!'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if '2' in x:
                      st.write(x.replace('2', 'z'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if '5' in x:
                      st.write(x.replace('5', 's'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'o' in x:
                      st.write(x.replace('o', '0'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'i' in x:
                      st.write(x.replace('i', '1'))
                      st.session_state.count += 1
                      st.write(x.replace('i', '!'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'z' in x:
                      st.write(x.replace('z', '2'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 's' in x:
                      st.write(x.replace('s', '5'))
                      st.session_state.count += 1
                      st.write(x.replace('s', '$'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                  if 'a' in x:
                      st.write(x.replace('a', '@'))
                      st.session_state.count += 1
                  else:
                        continue
                      
                st.write(str(st.session_state.count) + '個のパスワードを生成しました')
