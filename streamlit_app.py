import streamlit as st
from st_functions import st_button, load_css
from PIL import Image


load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('hi.png'))

st.header('fer dimentica')

st.markdown("""
<div style="background-color: #d9edf7; padding: 10px; border-radius: 5px; text-align: center; color: #31708f;">
    <strong>bienvenidx a tus playlists favoritas</strong>
</div>
""", unsafe_allow_html=True)
icon_size = 10

st.markdown(st_button('spotify', 'https://open.spotify.com/playlist/5Zm4gmdf1MK1HulF6Qb5Hq?si=x7ZF9g1ESXCQ84nYsYO_GA', 'Escuchar en Spotify', 30), unsafe_allow_html=True)
st.markdown(st_button('applemusic',
    'https://music.apple.com/mx/playlist/pop-disfrut%C3%B3n-para-pasarla-bien/pl.u-yZyVE63tdKVB3ZD',
    'Escuchar en Apple Music',
    30),
    unsafe_allow_html=True
)


st_button('spotify', 'https://open.spotify.com/playlist/5Zm4gmdf1MK1HulF6Qb5Hq?si=x7ZF9g1ESXCQ84nYsYO_GA', 'Link Spotify', icon_size)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
