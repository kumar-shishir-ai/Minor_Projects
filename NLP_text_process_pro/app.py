import streamlit as st
from streamlit_lottie import st_lottie
import re
import nltk
import pathlib
import pygame
import json
from pygame import mixer
pygame.init()
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
from nltk.corpus import wordnet
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

st.set_page_config(
    page_title="nlp",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_lottie_file(filepath:str):
    with open(filepath,"r")as f:
        return json.load(f)


st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 45px;
            font-weight: 800;
            background: linear-gradient(to right, white,blue);
            color: transparent;
            -webkit-background-clip: text;
            }
            .result-box {
            text-align: center;
            font-size: 20px;
            font-weight: 700;
            margin-top: 10px;
            border-radius: 12px;
            padding: 5px;
        }
    </style>
""", unsafe_allow_html=True)

def css_file(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

filepath = pathlib.Path("pro.css")
css_file(filepath)


st.markdown('<div class="title">Modern NLP Preprocessing Dashboard🎉</div>', unsafe_allow_html=True)


text = st.text_area("Write Here")
side = st.columns(4)
with side[0]:
    word_button = st.button("Word Tokenize",key="word")
with side[1]:
    sent_button = st.button("Sent Tokenize",key="sent")
with side[2]:
    bi_button = st.button("Bigrams",key="big")
with side[3]:
    tri_button = st.button("Trigrams",key="tri")



with st.sidebar:
    st.title("Remove Garbage")
    st.markdown("---")

    p = st.toggle("**Remove Punctuation**")
    h = st.toggle("**Remove Html Tag**")
    e = st.toggle("**Remove Emoji**")
    s = st.toggle("**Remove Stopword**")
    n = st.toggle("**Remove Number**")


# Remove punctuation from the text ___________
with side[0]:
    if p:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if word_button:
            pun = re.sub(r'[^\w\s]', "", text)
            tokens_w = word_tokenize(pun)
            st.write("Word Tokenize")
            st.write(tokens_w)
with side[1]:
    if p:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if sent_button:
            pun = re.sub(r'[^\w\s]', "", text)
            tokens_s = sent_tokenize(pun)
            st.write("Sentence Tokenize")
            st.write(tokens_s)
with side[2]:
    if p:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if bi_button:
            pun = re.sub(r'[^\w\s]', "", text)
            w_token = word_tokenize(pun)
            bigrams = list(nltk.bigrams(w_token))
            st.write("Bigrams")
            st.write(bigrams)
with side[3]:
    if p:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if tri_button:
            pun = re.sub(r'[^\w\s]', "", text)
            w_token = word_tokenize(pun)
            trigrams = list(nltk.trigrams(w_token))
            st.write("Trigrams")
            st.write(trigrams)


# Remove HTML tags from the text ___________
with side[0]:
    if h:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if word_button:
            pattern1 = re.compile('<.*?>')
            sub1 = pattern1.sub(r'',text)
            tokens_w = word_tokenize(sub1)
            st.write("Word Tokenize")
            st.write(tokens_w)
with side[1]:
    if h:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if sent_button:
            pattern2 = re.compile('<.*?>')
            sub2 = pattern2.sub(r'',text)
            tokens_s = sent_tokenize(sub2)
            st.write("Sentence Tokenize")
            st.write(tokens_s)
with side[2]:
    if h:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if bi_button:
            pattern3 = re.compile('<.*?>')
            sub3 = pattern3.sub(r'',text)
            token = word_tokenize(sub3)
            bigrams = list(nltk.bigrams(token))
            st.write("Bigrams")
            st.write(bigrams)
with side[3]:
    if h:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if tri_button:
            pattern4 = re.compile('<.*?>')
            sub4 = pattern4.sub(r'',text)
            token = word_tokenize(sub4)
            trigrams = list(nltk.trigrams(token))
            st.write("Trigrams")
            st.write(trigrams)


# Remove emojis from the text ___________
with side[0]:
    if e:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if word_button:
            emoji_pattern1 = re.compile("["
                                           u"\U0001F600-\U0001F64F"  # emotions
                                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                           u"\U0001F1E0-\U0001F64F"  # flags (iios)
                                           u"\U00002720-\U000027B0"
                                           u"\U000024C2-\U0001F251"
                                           "]+", flags=re.UNICODE)
            emoji1 = emoji_pattern1.sub(r'',text)
            tokens_w = word_tokenize(emoji1)
            st.write("Word Tokenize")
            st.write(tokens_w)
with side[1]:
    if e:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if sent_button:
            emoji_pattern2 = re.compile("["
                                           u"\U0001F600-\U0001F64F"  # emotions
                                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                           u"\U0001F1E0-\U0001F64F"  # flags (iios)
                                           u"\U00002720-\U000027B0"
                                           u"\U000024C2-\U0001F251"
                                           "]+", flags=re.UNICODE)
            emoji2 = emoji_pattern2.sub(r'',text)
            tokens_s = sent_tokenize(emoji2)
            st.write("Sentence Tokenize")
            st.write(tokens_s)
with side[2]:
    if e:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if bi_button:
            emoji_pattern3 = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emotions
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F64F"  # flags (iios)
                                    u"\U00002720-\U000027B0"
                                    u"\U000024C2-\U0001F251"
                                    "]+", flags=re.UNICODE)
            emoji3 = emoji_pattern3.sub(r'', text)
            word_t = word_tokenize(emoji3)
            bigrams = list(nltk.bigrams(word_t))
            st.write("Bigrams")
            st.write(bigrams)
with side[3]:
    if e:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if tri_button:
            emoji_pattern4 = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emotions
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F64F"  # flags (iios)
                                    u"\U00002720-\U000027B0"
                                    u"\U000024C2-\U0001F251"
                                    "]+", flags=re.UNICODE)
            emoji4 = emoji_pattern4.sub(r'', text)
            token_w = word_tokenize(emoji4)
            trigrams = list(nltk.trigrams(token_w))
            st.write("Trigrams")
            st.write(trigrams)

# Remove stopwords from the text __________
with side[0]:
    if s:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if word_button:
            word1 = text.split()
            eng_stop = stopwords.words('english')
            stop1 = [i for i in word1 if i not in eng_stop]
            fresh1 = " ".join(stop1)
            tokens_w = word_tokenize(fresh1)
            st.write("Word Tokenize")
            st.write(tokens_w)
with side[1]:
    if s:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if sent_button:
            word2 = text.split()
            eng_stop = stopwords.words('english')
            stop2 = [i for i in word2 if i not in eng_stop]
            fresh2 = " ".join(stop2)
            tokens_s = sent_tokenize(fresh2)
            st.write("Sentence Tokenize")
            st.write(tokens_s)
with side[2]:
    if s:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if bi_button:
            word3 = text.split()
            eng_stop = stopwords.words('english')
            stop3 = [i for i in word3 if i not in eng_stop]
            fresh3 = " ".join(stop3)
            word_t = word_tokenize(fresh3)
            bigrams = list(nltk.bigrams(word_t))
            st.write("Bigrams")
            st.write(bigrams)
with side[3]:
    if s:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if tri_button:
            word4 = text.split()
            eng_stop = stopwords.words('english')
            stop4 = [i for i in word4 if i not in eng_stop]
            fresh4 = " ".join(stop4)
            word_t = word_tokenize(fresh4)
            trigrams = list(nltk.trigrams(word_t))
            st.write("Trigrams")
            st.write(trigrams)


# Remove number from the text ___________
with side[0]:
    if n:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if word_button:
            a1 = regexp_tokenize(text, pattern="\d+")
            token = word_tokenize(text)
            tokens_w = [i for i in token if i not in a1]
            st.write("Word Tokenize")
            st.write(tokens_w)
with side[1]:
    if n:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if sent_button:
            a2 = regexp_tokenize(text, pattern="\d+")
            token = word_tokenize(text)
            result = [j for j in token if j not in a2]
            sent = " ".join(result)
            tokens_s = nltk.sent_tokenize(sent)
            st.write("Sentence Tokenize")
            st.write(tokens_s)
with side[2]:
    if n:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if bi_button:
            a3 = regexp_tokenize(text, pattern="\d+")
            token = word_tokenize(text)
            result = [j for j in token if j not in a3]
            bi_no = " ".join(result)
            token = word_tokenize(bi_no)
            bigrams = list(nltk.bigrams(token))
            st.write("Bigrams")
            st.write(bigrams)
with side[3]:
    if n:
        pygame.mixer.music.load("pop_2.wav")
        pygame.mixer.music.play()
        if tri_button:
            a4 = regexp_tokenize(text, pattern="\d+")
            token = word_tokenize(text)
            result = [j for j in token if j not in a4]
            tri_no = " ".join(result)
            token = word_tokenize(tri_no)
            trigrams = list(nltk.trigrams(token))
            st.write("Trigrams")
            st.write(trigrams)


# Converting stemming and lemmatizing of the word ____________
with st.sidebar:
    st.markdown("---")
    obj1 = PorterStemmer()
    word = st.text_input("**Write words**")
    c1, c2 = st.columns(2)
    with c1:
        stemming = st.button("**Stemming**",key="stem")
        if stemming:
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()
            if word:
                stem = obj1.stem(word)
                st.write(stem)
            else:
                pygame.mixer.music.load("please.wav")
                pygame.mixer.music.play()
                st.markdown(
                    '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;">Please Enter the word.</div>',
                    unsafe_allow_html=True)
    obj2 = WordNetLemmatizer()
    with c2:
        lemma = st.button("**Lemmatize**",key="lem")
        if lemma:
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()
            if word:
                lematize = obj2.lemmatize(word)
                st.write(lematize)
            else:
                pygame.mixer.music.load("please.wav")
                pygame.mixer.music.play()
                st.markdown(
                    '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;">Please Enter the word.</div>',
                    unsafe_allow_html=True)
    data_lottie = load_lottie_file("ROBO_hello.json")
    st_lottie(
        data_lottie,
        height=300,
        width=None
    )


# Find name, definition and examples of the word ___________
st.markdown("---")
correct_word = st.text_input("Write a Meaningful Word")
write = st.columns(3)
with write[0]:
    bn = st.button("Name",key="name")
    if bn:
        pygame.mixer.music.load("click.wav")
        pygame.mixer.music.play()
        if correct_word:
            synsets = wordnet.synsets(correct_word)
            if synsets:
                obj = synsets[0]
                s_name = obj.name()
                st.success(s_name)
        else:
            pygame.mixer.music.load("please.wav")
            pygame.mixer.music.play()
            st.markdown(
                '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;">Please Enter the word.</div>',
                unsafe_allow_html=True)
with write[1]:
    bd = st.button("Definition",key="defi")
    if bd:
        pygame.mixer.music.load("click.wav")
        pygame.mixer.music.play()
        if correct_word:
            synsets = wordnet.synsets(correct_word)
            if synsets:
                obj = synsets[0]
                s_defi = obj.definition()
                st.success(s_defi)
        else:
            pygame.mixer.music.load("please.wav")
            pygame.mixer.music.play()
            st.markdown(
                '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;">Please Enter the word.</div>',
                unsafe_allow_html=True)
with write[2]:
    be = st.button("Examples",key="exa")
    if be:
        pygame.mixer.music.load("click.wav")
        pygame.mixer.music.play()
        if correct_word:
            synsets = wordnet.synsets(correct_word)
            if synsets:
                obj = synsets[0]
                s_exa = obj.examples()
                st.success(s_exa)
        else:
            pygame.mixer.music.load("please.wav")
            pygame.mixer.music.play()
            st.markdown(
                '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;">Please Enter the word.</div>',
                unsafe_allow_html=True)


# Draw the text using WordCloud ___________
st.markdown("---")
word = st.text_area("**Text Here To Display The Image**")
image = st.button("Image",key="image")
if image:
    if word:
        pygame.mixer.music.load("cloud.wav")
        pygame.mixer.music.play()
        wc = WordCloud().generate(word)
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
    else:
        pygame.mixer.music.load("clear_cloud.wav")
        pygame.mixer.music.play()
        st.markdown(
            '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;">Please enter some text to generate the Word Cloud.</div>',
            unsafe_allow_html=True)




# use wordcloud______
# 1. Python is easy to learn, and Python is powerful. Python supports machine learning, data science, and web development. Learning Python opens many doors. Python, Python, Python!
# 2. Education is important. Education builds future. Education gives knowledge. Students need good education. Education, education, education!
# 3. Education is important. Education builds future. Education gives knowledge. Students need good education. Education, education, education!

# emoji removal ______
# 1. I love programming 💻❤️ Python is awesome 😎🔥 coding developer 🚀👨‍💻
# 2. That movie was 🔥🔥🔥 totally worth the hype 😮👏🍿 Bollywood
# 3. omg this food is so good i cant stop eating 😋🍕🍔😩
# 4. celebrating diwali with family 🎆🎉 love the lights and sweets diwali2025

# html tags removal ______
# 1. <div class="review"><h3>The movie was great! <i>It had fantastic visuals</i> and a <strong>gripping story</strong>.</h3></div>
# 2. <h2>Top Programming Languages in 2025</h2><p>Python is a versatile language for <em>data science</em> and <strong>AI</strong>.</p>
# 3. <section><h3>Best Actor Nominee</h3><p><b>John Doe</b> for his role in <i>Super Movie</i></p></section>

# punctuation remove ______
# 1. why is this happe*&ning??@!! #%& I cannot deal with this right now!! Why on earth!! why?!!
# 2. okay seriously!!! How could this hap%^$pen @!!&?!! What's going on?! Is this even real?!! I am speechless...!! #@$%!
# 3. omg!!! What in the world is ha#$ppening @^&*() ???!!! I can't even%&!!! This is unbelievable!@^$&!! Do you see it??!

# stopword remove______
# 1. This new algorithm is designed to solve the problem of missing data in large datasets efficiently
# 2. This phone is really good because it has a great camera, fast processing speed, and a long-lasting battery
# 3. The team has been working hard on this project for several months, and we are excited to present the results.

# number remove ______
# 1. The book costs 25 dollars, but the discounted price is only 15 dollars.
# 2. We have 50 items in stock, and each one weighs around 2 kilograms.
# 3. You need 3 cups of flour, 2 tablespoons of sugar, and 1 teaspoon of salt for this recipe.