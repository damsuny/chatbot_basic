import jpype                    ### jpype가 자동으로 연결이 안되기 때문에 꼭 import 하고 시작해야 한다.ㄷ
from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "지금 어디 있는지. 아프지는 않는지. 가슴 속에 담아 둔 마음 전하고는 싶은데."

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
# 단어 사전 구출 및 단어별 인덱스 부여
dics={}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics)
print(dics)
# 원-핫 인코딩
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)