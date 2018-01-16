# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:28:25 2018

@author: Changdong Oh
"""

# 긴 문자열은 가독성을 위해 다음과 같이 괄호를 활용해서 묶어줄 수 있습니다.
text = ('프로그램 언어를 익히기 위해 책이나 글만 보면서 '
        '따라해서는 중간에 막히는 부분들이 발생합니다. '
        '그리고 막연히 어렵게 느껴지기도 하고요. '
        '또 어떤 경우에는 눈으로만 읽는 분들이 있는데, '
        '눈으로만 봐서는 실제로 프로그램을 작성하기가 어렵습니다. '
        '본 과정은 실습을 중심으로 진행합니다. '
        '그래서, 따라할 수 있는 형태의 강의 자료가 제공됩니다. '
        '온라인에 공개되기 때문에 수업을 듣지 않은 분들도 자료를 '
        '열람할 수 있지만, 실습을 진행하면서 발생하는 Q&A나 개별 1:1 지도, '
        '각 개인의 프로젝트 목표에 대한 피드백 등은 제한된 메일링 '
        '리스트를 사용하여 진행합니다.')

# 쉼표와 마침표 제거하고, split 함수 활용해 어절 단위로 분리
word_list = text.replace(',', '').replace('.', '').split()
# set 데이터로 변환해 unique 단어만 추출
word_unique_set = set(word_list)

# dictionary comprehension 응용해서 unique 단어 set의 단어들을 key로 지정
# 각 key에 대응하는 값은 일단 0
unique_dict = {i: 0 for i in word_unique_set}

# 전체 단어 리스트를 활용해서 for문을 만들고
for word in word_list:
    # 어떤 단어가 등장했을 때 key에 대응하는 값에 1을 추가.
    # += 는 i = i + 1 과 같은 표현을 그대로 축약해주는 방법입니다.
    # 아래의 경우 unique_dict[i] = unique_dict[i] + 1 과 같은 의미.
    unique_dict[word] += 1

print(unique_dict)
