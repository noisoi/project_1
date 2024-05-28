import re
from konlpy.tag import Okt


def text_cleaning(text) :
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    print(type(result))
    return result    


def text_filter(titleList):
    # 한글만 추출하기
    titleList = list(map(lambda x:text_cleaning(x), titleList))
    #print(titleList)

    title_corpus = "".join(titleList) # 추출한 각 요소를 띄어쓰기로 join
    nouns_tagger = Okt() # 형태소 초기화
    count = nouns_tagger.nouns(title_corpus) # 명사 추출

    #print(count)
    remove_char_counter = [x for x in count if len(x) > 1]    # 데이터 길이가 1보다 큰 것만 필터링
    #print(remove_char_counter)

    # 불용어 처리 경로 지정
    korean_stopwords_path = "C:/Users/CDL/myproject/myapp/stopwords-ko.txt"

    # stopwords 파일 열기
    with open(korean_stopwords_path, encoding='utf8') as f:
        stopwords = f.readlines()
    stopwords = [x.strip() for x in stopwords]

    # 위에서 필터링한 리스트를 하나씩 for 문 돌려서 stopwords에 해당되지 않는 것만 갯수 세기
    remove_char_counter = [x for x in remove_char_counter if x not in stopwords]
    print(remove_char_counter)

text_filter(text_cleaning("물놀이 축제 추천해줘"))