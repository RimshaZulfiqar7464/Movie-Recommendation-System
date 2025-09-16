# import requests
# import streamlit as st
#
# API_KEY = st.secrets["TMDB_API_KEY"]
#
# @st.cache_data
# def fetch_movies_from_category(category="popular"):
#     url = f"https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page=1"
#     return requests.get(url).json().get("results", [])
#
# @st.cache_data
# def fetch_movies_by_genre(genre_id):
#     url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres={genre_id}&page=1"
#     return requests.get(url).json().get("results", [])
#
# @st.cache_data
# def fetch_details(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url).json()
#
#     poster_path = data.get("poster_path")
#     poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
#
#     cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
#     cast_data = requests.get(cast_url).json()
#     cast = [actor["name"] for actor in cast_data.get("cast", [])[:5]]
#
#     return {
#         "poster": poster_url,
#         "title": data.get("title", "Unknown"),
#         "overview": data.get("overview", "No description available."),
#         "language": data.get("original_language", "N/A"),
#         "release_date": data.get("release_date", "N/A"),
#         "cast": cast
#     }
import streamlit as st
import requests

API_KEY = st.secrets["TMDB_API_KEY"]

# ---------------- Cached API Requests ----------------
@st.cache_data(show_spinner=False)
def fetch_movies_from_category(category="popular"):
    """Fetch movies by category (popular, top_rated, upcoming)."""
    url = f"https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page=1"
    data = requests.get(url).json()
    return data.get("results", [])


@st.cache_data(show_spinner=False)
def fetch_movies_by_genre(genre_id):
    """Fetch movies by genre id (e.g. 35=Comedy, 27=Horror)."""
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&language=en-US&with_genres={genre_id}&page=1"
    data = requests.get(url).json()
    return data.get("results", [])


@st.cache_data(show_spinner=False)
def fetch_details(movie_id):
    """Fetch movie details + cast from TMDB API (cached)."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
    title = data.get("title", "Unknown")
    overview = data.get("overview", "No description available.")
    language = data.get("original_language", "N/A")
    release_date = data.get("release_date", "N/A")

    # Cast
    cast_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
    cast_data = requests.get(cast_url).json()
    cast = [actor["name"] for actor in cast_data.get("cast", [])[:5]]

    return {
        "poster": poster_url,
        "title": title,
        "overview": overview,
        "language": language,
        "release_date": release_date,
        "cast": cast
    }

