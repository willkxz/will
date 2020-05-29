#!/usr/bin/env python
# coding: utf-8

# In[24]:


#導入套件
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #中文字型
df = pd.read_csv('http://data.taipower.com.tw/opendata/apply/file/d007012/%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E5%85%AC%E5%8F%B8_%E5%90%84%E7%B8%A3%E5%B8%82%E4%BD%8F%E5%AE%85%E3%80%81%E6%9C%8D%E5%8B%99%E6%A5%AD%E5%8F%8A%E6%A9%9F%E9%97%9C%E7%94%A8%E9%9B%BB%E7%B5%B1%E8%A8%88%E8%B3%87%E6%96%99.csv')
df.head(25)


# In[25]:


basic = df[df['日期']=='2020年02月'].sort_values('縣市用電佔比(%)').tail(10)
fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(basic['縣市'], basic['縣市用電佔比(%)'])
cols=[x for i,x in enumerate(df.columns) if df.iat[0,i]=='合計']
df=df.drop(cols,axis=1)


# In[26]:


colors = dict(zip(
    ["新北市", "台北市", "桃園市", "台中市", "台南市", "高雄市", "宜蘭縣","新竹縣","苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","台東縣","花蓮縣","基隆市","新竹市","嘉義市","澎湖縣","金門縣","連江縣","合計"]
    ,["#2E86AB", "#424B54", "#00A6A6", "#F24236", "#9E643C", "#f7bb5f", "#EDE6F2","#E9D985", "#8C4843", "#90d595", "#e48381", "#090446", "#f7bb5f", "#eafb50","#adb0ff","#ffb3ff", "#90d595", "#e48381", "#aafbff",'#746D75',"#4B0082","#00FF00","#003C9D"]
))

fig, ax = plt.subplots(figsize=(16, 9))


def race_barchart(input_year):
    dff = df[df['日期'].eq(input_year)].sort_values(by='縣市用電佔比(%)', ascending=True).tail(22)
    ax.clear()

    ax.barh(dff['縣市'], dff['縣市用電佔比(%)'], color=[colors[x] for x in dff['縣市']],height=0.8)
    dx = dff['縣市用電佔比(%)'].max() / 200
    
    for i, (value, name) in enumerate(zip(dff['縣市用電佔比(%)'], dff['縣市'])):
        ax.text(0, i,name+' ',size=16, weight=600, ha='right', va='center')
        ax.text(value+dx, i,f'{value:,.10f}',  size=16, ha='left',  va='center')
            
    ax.text(0.9, 0.2, input_year[:7].replace('-','/'), transform=ax.transAxes, color='#777777', size=72, ha='right', weight=1000)
    ax.text(0, 1.06, '用電數', transform=ax.transAxes, size=14, color='#777777')
    ax.text(0.59, 0.14, '總用電數:'+str(int(dff['縣市用電佔比(%)'].sum())), transform=ax.transAxes, size=24, color='#000000',ha='left')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.xaxis.set_ticks_position('top')
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(0, 1.15, '各縣市用電佔比',
                transform=ax.transAxes, size=24, weight=600, ha='left', va='top')

    plt.box(False)

   
    
race_barchart('2012年01月')


# In[27]:


#轉成動畫:利用FunAnimation來完成，是利用反覆呼叫我們設定的畫圖函式，來完成一張又一張的圖片，然後再結合起來變成動畫
#就以本次例子來說共有三個參數，fig為初始設置畫布、race_barchart為我們設定的函式，frames則為丟進該函式的值
#整理Frame月資料
from matplotlib.animation import FuncAnimation
month = list(set(df.日期.values))
month.sort()

fig, ax = plt.subplots(figsize=(16, 9))
animator = animation.FuncAnimation(fig, race_barchart, frames=month)
HTML(animator.to_jshtml())







