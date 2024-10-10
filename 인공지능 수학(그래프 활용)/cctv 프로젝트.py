from google.colab import drive
drive.mount("/gdrive")

path = '/content/drive/MyDrive/EBS/cctv.csv'

import pandas as pd
file_cctv= pd.read_csv(path,encoding='cp949')

import matplotlib as mpl
import matplotlib.pyplot as plt
#해당 폰트가 기본 포트가 되도록 설정
import matplotlib.font_manager as fm

fe = fm.FontEntry(
    fname=r'/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', # path to .ttf
    name='NanumBarunGothic')                        # what you want to name that font
fm.fontManager.ttflist.insert(0, fe)              # add the font to Matplotlib
plt.rcParams.update({'font.size': 9, 'font.family': 'NanumBarunGothic'}) # set the font

# 1번
plt.plot([1,2,3,4,5],[7,8,9,10,15])
plt.show()

# 2번
x = [1,2,3,4,5]
y = [10,4,7,2,-1]
plt.plot(x,y)
plt.show()

#3 번
plt.figure(figsize =(10,5))
plt.title("Graph",fontsize = 20)
plt.xlabel("x data")
plt.ylabel("y label")

x = [1,2,3,4,5]
y = [10,4,7,2,-1]
plt.plot(x,y)
plt.show()

#4번
plt.figure(figsize = (12,4))
plt.title("각 자치구별 CCTV 개수",fontsize = 16)
plt.plot(file_cctv['구분'],file_cctv['총계'])
plt.show()

#5번
plt.bar(x,y)
plt.show()

#6번
plt.figure(figsize = (12,4))
plt.title("각 자치 구별 쓰레기무단투기용 CCTV 개수",fontsize = 16)
plt.bar(file_cctv['구분'],file_cctv['쓰레기\n무단투기'],color = 'green')
plt.show()

#7번
import random
y = []

for a in range(19):
  y.append(random.randint(1,1000))
print(sorted(y))
plt.boxplot(y)
plt.show()

#8번
plt.title("각 기관별 CCTV 총계",fontsize = 16)
plt.boxplot(file_cctv['총계'],labels = ["CCTV"])
plt.show()

#9번
import matplotlib.pyplot as plt
plt.title("각 기관별 CCTV 총계",fontsize =16)
plt.hist(file_cctv["총계"],bins=50)
plt.show()
