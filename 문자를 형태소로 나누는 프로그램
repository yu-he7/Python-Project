import os
from konlpy.tag import Okt

#java_path 직접 지정
os.environ['java_Home'] = r'C:/Program Files/Java/jdk-20'

okt = Okt()
text = '아버지가 방에 들어갑니다'

morphs = okt.morphs(text) #형태소 단위로 분석
noun = okt.nouns(text) #명사 단위
pos = okt.pos(text) #형태소 별 품사 태깅

print("====morphs====")
print(morphs)

print('====noun====')
print(noun)

print('====pos====')
print(pos)
