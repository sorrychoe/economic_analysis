import BigKindsParser as bkp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

df = pd.read_excel('./econo_columns_20170510-20220509.xlsx')

st.set_page_config(layout="centered", page_icon="📰", page_title="economic columns")
    
st.title("경제 뉴스 칼럼 키워드 분석")
st.text("문재인 정부 재임 기간(20170510-20220509) 동안 경제 뉴스의 칼럼 키워드를 분석합니다.")


def space(num_lines):
    for _ in range(num_lines):
        st.write("")

def main():

    press = ['전체 언론사 칼럼 빈도', '전체 언론사 키워드', '한국경제', '매일경제', '서울경제', '파이낸셜뉴스', '헤럴드경제']
    symbols = st.selectbox("Choose stocks to visualize",press)

    space(2)
    
    if symbols == '전체 언론사 칼럼 빈도':
        st.image('./press.png')
    
    elif symbols == '전체 언론사 키워드' :
    
        df_keywords = df['키워드']
        keywords = bkp.keywords_list(df_keywords)
        news_key = bkp.keyword_parser(keywords)
        news_key = bkp.duplication_remover(news_key)
        key = bkp.word_counter(news_key)
        news_key = bkp.counter_to_DataFrame(key)
        wc = WordCloud(font_path = '/NanumBarunGothic.ttf',
                        width = 500,
                        height = 500,
                        background_color='white').generate_from_frequencies(news_key.set_index('단어').to_dict()["빈도"])

        cloud = plt.figure(figsize = (10, 10))
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        st.pyplot(cloud)

    else : 
        cloud = plt.figure(figsize = (10, 10))
        wc = bkp.press_keywords_wordcloud(df, symbols)
        st.pyplot(cloud)
            

if __name__ == '__main__':
    main()
