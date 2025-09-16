# movie-recommender-system-tmdb-dataset
Developed a Netflix-inspired web application for personalized movie recommendations.
Implemented Machine Learning (content-based filtering) with preprocessed datasets (tmdb_5000_movies.csv, tmdb_5000_credits.csv).
Used pickle models (movie_list.pkl, similarity.pkl) for fast recommendation retrieval.
Integrated TMDB API to fetch real-time movie details (posters, cast, genres, release dates).
Optimized system architecture by separating code into modules (data/, model/, utils/) for faster response.
Designed an interactive, modern UI using Streamlit with custom CSS for a Netflix-style experience.
Focused on reducing latency by minimizing repeated API calls and preloading models.

#🗂️ Folder Structure
movie_recommender_netflix_style/
│── app.py                 # Main Streamlit app
│── preprocessing.py        # Data preprocessing and pickle generation
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│
├── data/                   # Raw dataset files
│     └── tmdb_5000_movies.csv
│     └── tmdb_5000_credits.csv
│
├── model/                  # Saved models after preprocessing
│     └── movie_list.pkl
│     └── similarity.pkl
│
├── utils/                  
│     └── tmdb_api.py       # TMDB API integration functions
│
├── notebooks/              
│     └── eda.ipynb         # Exploratory data analysis notebook
│
├── static/                 
      └── style.css         # Custom CSS for Netflix-like UI

#⚙️ Installation
#Clone the repository or extract the zip file
git clone <repo-link>
cd movie_recommender_netflix_style

#Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate   # for Windows
source .venv/bin/activate  # for Mac/Linux

#Install requirements
pip install -r requirements.txt

#▶️ How to Run
#Run preprocessing first to generate pickle files:
python preprocessing.py

#Start the Streamlit app:
streamlit run app.py

#📊 Dataset
The project uses TMDB 5000 Movie Dataset (tmdb_5000_movies.csv & tmdb_5000_credits.csv).
These datasets are stored inside the data/ folder.

#✨ Features
🎥 Personalized Movie Recommendations using content-based similarity.
🌍 Real-time TMDB API Integration for posters, cast, genres, and release dates.
⚡ Fast retrieval with preprocessed pickle models (movie_list.pkl, similarity.pkl).
🎨 Netflix-style web UI built with Streamlit + custom CSS.
📂 Modular code structure with utils/, data/, and model/ folders.

#🚀 Future Enhancements
Add hybrid recommendation system (content + collaborative filtering).
Deploy on cloud (e.g., Streamlit Cloud / Huawei Cloud / Heroku).
Add user login & history-based personalization.
