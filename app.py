# import pickle
# import streamlit as st
# import requests
#
# # ---------------- Streamlit Config ----------------
# st.set_page_config(page_title="🎬 Movie Recommender System", layout="wide")
#
# # ---------------- API Key ----------------
# API_KEY = st.secrets["TMDB_API_KEY"]
#
# # ---------------- Fetch Movies from TMDB ----------------
# def fetch_movies_from_category(category="popular"):
#     url = f"https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page=1"
#     data = requests.get(url).json()
#     return data.get("results", [])
#
# def fetch_movies_by_genre(genre_id):
#     url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres={genre_id}&page=1"
#     data = requests.get(url).json()
#     return data.get("results", [])
#
# def fetch_details(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url).json()
#
#     poster_path = data.get("poster_path")
#     poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
#     title = data.get("title", "Unknown")
#     overview = data.get("overview", "No description available.")
#     language = data.get("original_language", "N/A")
#     release_date = data.get("release_date", "N/A")
#
#     # Cast
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
#     cast_data = requests.get(cast_url).json()
#     cast = [actor["name"] for actor in cast_data.get("cast", [])[:5]]
#
#     return {
#         "poster": poster_url,
#         "title": title,
#         "overview": overview,
#         "language": language,
#         "release_date": release_date,
#         "cast": cast
#     }
#
# # ---------------- Recommendation Logic ----------------
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movies = []
#     for i in distances[1:7]:
#         movie_id = movies.iloc[i[0]].movie_id
#         details = fetch_details(movie_id)
#         recommended_movies.append(details)
#     return recommended_movies
#
# # ---------------- CSS Styling ----------------
# st.markdown(
#     """
#     <style>
#     body {
#         background: linear-gradient(135deg, #0f0f0f, #1c1c1c, #111);
#         color: white;
#     }
#     .stSelectbox label {
#         font-size: 18px;
#         color: #E50914;
#     }
#     .stButton>button {
#         background-color: #E50914;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-weight: bold;
#         transition: 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #b20710;
#         transform: scale(1.05);
#     }
#     .movie-card {
#         background-color: #1c1c1c;
#         border-radius: 15px;
#         padding: 15px;
#         margin: 10px;
#         text-align: center;
#         box-shadow: 0 4px 15px rgba(0,0,0,0.7);
#     }
#     .movie-card img {
#         border-radius: 10px;
#         margin-bottom: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # ---------------- UI Header ----------------
# st.markdown("<h1 style='text-align: center; color: #E50914;'>🍿 Movie Recommender System </h1>", unsafe_allow_html=True)
#
# # ---------------- Load Data ----------------
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # ---------------- Search + Recommend ----------------
# movie_list = movies['title'].values
# selected_movie = st.selectbox("🎥 Search a movie:", movie_list)
#
# if st.button("✨ Show Recommendation"):
#     recommended_movies = recommend(selected_movie)
#     cols = st.columns(2)
#     for i, details in enumerate(recommended_movies):
#         with cols[i % 2]:
#             st.markdown(
#                 f"""
#                 <div class="movie-card">
#                     <img src="{details['poster']}" width="250">
#                     <h3>{details['title']}</h3>
#                     <p><b>Release Date:</b> {details['release_date']}</p>
#                     <p><b>Language:</b> {details['language']}</p>
#                     <p><b>Cast:</b> {', '.join(details['cast'])}</p>
#                     <p style="text-align: justify;">{details['overview']}</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )
#
# # ---------------- Netflix-Style Categories ----------------
# st.subheader("🔥 Trending Now")
# trending_movies = fetch_movies_from_category("popular")
# cols = st.columns(5)
# for i, m in enumerate(trending_movies[:10]):
#     with cols[i % 5]:
#         st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])
#
# st.subheader("😂 Comedy Movies")
# comedy_movies = fetch_movies_by_genre(35)  # 35 = Comedy
# cols = st.columns(5)
# for i, m in enumerate(comedy_movies[:10]):
#     with cols[i % 5]:
#         st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])
#
# st.subheader("👻 Horror Movies")
# horror_movies = fetch_movies_by_genre(27)  # 27 = Horror
# # cols = st.columns(5)
# for i, m in enumerate(horror_movies[:10]):
#     with cols[i % 5]:
#         st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])
#
# st.subheader("🧙 Fantasy Movies")
# fantasy_movies = fetch_movies_by_genre(14)  # 14 = Fantasy
# cols = st.columns(5)
# for i, m in enumerate(fantasy_movies[:10]):
#     with cols[i % 5]:
#         st.image(f"https://image.tmdb.org/t/p/w200{m['poster_path']}", caption=m['title'])


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
