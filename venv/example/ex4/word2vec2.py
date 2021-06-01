# # word2vec.py run 후 nvmc.model이 생성되었는지 확인 후 실행 할 것
#
# # 모델 로딩
# from gensim.models import Word2Vec
# print("corpus_total_words : ", model.corpus_total_words)
#
# # '사랑'이란 단어로 생성한 단어 임베딩 벡터
# print('사랑 : ', model.wv['사랑'])
#
# # 단어 유사도 계산
# print("일요일 = 월요일\t", model.wv.similarity(w1='일요일',w2='월요일'))
# print("안성기 = 배우\t", model.wv.similarity(w1='안성기',w2='배우'))
# print("대기업 = 삼성\t", model.wv.similarity(w1='대기업',w2='삼성'))
# print("일요일 != 삼성\t", model.wv.similarity(w1='일요일',w2='삼성'))
# print("히어로 != 월요일\t", model.wv.similarity(w1='히어로',w2='삼성'))
#
# # 가장 유사한 단어 추출
# print(model.wv.most_similar("안성기", topn=5))
# print(model.wv.most_similar("시리즈", topn=5))