from pprint import pprint
from googletrans import Translator, constants, why

from wordcloud import WordCloud
import pandas as pd
import numpy as np
import streamlit as st
import random
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


st.set_page_config(layout="wide", page_title="ADM_Project",
                   page_icon=":computer:")


with open("english.txt") as f1:
    sentences_en = f1.readlines()
with open("french.txt") as f:
    sentences_fr = f.readlines()
# st.write(sentences_en)2


# st.markdown("<h2 style='text-align: center; color: white;'>Translating Languages with AI: A Natural Language Processing Approach</h2>", unsafe_allow_html=True)


with st.container():
    st.markdown(
        "<h2 style='text-align: center; color: #3366ff; font-weight: bold; background-color: #f2f2f2; padding: 10px; border-radius: 10px;'>Translating Languages with AI: A Natural Language Processing Approach</h2>",
        unsafe_allow_html=True)


# generating random sentences:
# def generate_random_sentenses(length, sentences_en, sentences_fr):
#     random_sentence = st.sidebar.slider(
#         "Select number of random sentences to generate", min_value=1, max_value=100, value=5)
#     random_generator = random.sample(range(length), int(random_sentence))

#     for i in random_generator:
#         st.write(f"English sentence {i+1} = {sentences_en[i]}")
#         st.write(f"French sentence {i+1} = {sentences_fr[i]}")


def generate_random_sentences(length, sentences_en, sentences_fr):
    random_sentence = st.sidebar.slider(
        "Select number of random sentences to generate", min_value=1, max_value=100, value=5)
    random_generator = random.sample(range(length), int(random_sentence))

    with st.container():
        st.header("Randomly Generated Sentences")
        for i in random_generator:
            st.info(
                f"English sentence {i+1} = {sentences_en[i]} \nFrench sentence {i+1} = {sentences_fr[i]}")


# Create sidebar for selecting number of sentences to generate
# st.sidebar.title('Sentence Generator')
length = len(sentences_en)
generate_random_sentences(length, sentences_en, sentences_fr)


# word cloud

words_en = [word for sentence in sentences_en for word in sentence.split(" ")]

words_fr = [word for sentence in sentences_fr for word in sentence.split(" ")]

st.set_option('deprecation.showPyplotGlobalUse', False)


# work cloud generator
def make_wordcloud(words, max_words, background_color):

    words_str = ' '.join(words)
    wordcloud = WordCloud(background_color=background_color,
                          max_words=max_words).generate(words_str)
    plt.imshow(wordcloud)
    plt.axis('off')
    st.pyplot()


st.sidebar.title('Word Cloud Parameters')


max_words = st.sidebar.slider(
    'Maximum number of words', min_value=50, max_value=500, value=200)


background_color = st.sidebar.color_picker('Background color', '#FFFFFF')


st.markdown("<h2 style='text-align: center; color: white;'>Word cloud for English words</h2>",
            unsafe_allow_html=True)
make_wordcloud(words_en, max_words, background_color)


st.markdown("<h2 style='text-align: center; color: white;'>Word cloud for French words</h2>",
            unsafe_allow_html=True)
make_wordcloud(words_fr, max_words, background_color)


# model implementation:


translator = Translator()
st.title("Translator")
sentence = st.text_input("Enter a sentence in English", max_chars=500)
translation = translator.translate(sentence, src="en", dest="fr")
st.success(f"French: {translation.text}")
# st.write(translation.text)

# st.sidebar.markdown("----")
# st.sidebar.markdown("Thank you for using our app!")


st.markdown("----")
st.markdown(
    "<h3 style='text-align: center; color: white; font-weight: bold; padding-bottom: 10px;'>By: Team-3 &rarr; Hruthik, Nandini, Adithya</h3>",
    unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align: center; color: white; font-weight: bold; padding-bottom: 10px;'>Thank you!!🙂</h3>",
    unsafe_allow_html=True)
