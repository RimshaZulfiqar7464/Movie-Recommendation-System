import streamlit as st
import pickle
from utils.tmdb_api import fetch_movies_from_category, fetch_movies_by_genre, fetch_details

st.set_page_config(page_title="🎬 Movie Recommender System", layout="wide")

# ---------------- UI Header ----------------
st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System </h1>", unsafe_allow_html=True)

# ---------------- Load Data ----------------
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# ---------------- Recommendation Logic ----------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_details(movie_id)
        recommended_movies.append(details)
    return recommended_movies

# ---------------- CSS Styling ----------------
# st.markdown(open("static/style.css").read(), unsafe_allow_html=True)

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- Search + Recommend ----------------
movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Search a movie:", movie_list)

if st.button("✨ Show Recommendation"):
    recommended_movies = recommend(selected_movie)
    cols = st.columns(2)
    for i, details in enumerate(recommended_movies):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="movie-card">
                    <img src="{details['poster']}" width="250">
                    <h3>{details['title']}</h3>
                    <p><b>Release Date:</b> {details['release_date']}</p>
                    <p><b>Language:</b> {details['language']}</p>
                    <p><b>Cast:</b> {', '.join(details['cast'])}</p>
                    <p style="text-align: justify;">{details['overview']}</p>
                </div>
                """, unsafe_allow_html=True
            )

# ---------------- Netflix-Style Categories ----------------
st.subheader("🔥 Trending Now")
trending_movies = fetch_movies_from_category("popular")
cols = st.columns(5)
for i, m in enumerate(trending_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("😂 Comedy Movies")
comedy_movies = fetch_movies_by_genre(35)
cols = st.columns(5)
for i, m in enumerate(comedy_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("👻 Horror Movies")
horror_movies = fetch_movies_by_genre(27)
cols = st.columns(5)
for i, m in enumerate(horror_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

st.subheader("🧙 Fantasy Movies")
fantasy_movies = fetch_movies_by_genre(14)
cols = st.columns(5)
for i, m in enumerate(fantasy_movies[:10]):
    with cols[i % 5]:
        st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])

