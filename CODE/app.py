import os
import pandas as pd
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("❌ TMDB_API_KEY not found in .env file")

print("✅ TMDB API Loaded")

# -----------------------------
# LOAD DATA (IMPORTANT FIX HERE)
# -----------------------------
movies_df = pd.read_csv("Processed Data/movies_processed.csv")
ui_df = pd.read_csv("Processed Data/UI_dataset.csv")

# MERGE BOTH DATASETS (THIS FIXES YOUR ISSUE)
df = movies_df.merge(ui_df, on="id", how="left")

df = df.dropna(subset=["tags", "title"]).reset_index(drop=True)

# -----------------------------
# MODEL (NO PKL)
# -----------------------------
tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
vectors = tfidf.fit_transform(df["tags"].astype(str))
similarity = cosine_similarity(vectors)

indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

# -----------------------------
# POSTER FUNCTION
# -----------------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        res = requests.get(url, params={"api_key": API_KEY}, timeout=5)
        data = res.json()

        poster = data.get("poster_path")
        if poster:
            return "https://image.tmdb.org/t/p/w500" + poster
    except:
        pass

    return "/static/no-image.jpg"

# -----------------------------
# RECOMMEND FUNCTION
# -----------------------------
def recommend(movie):
    if movie not in indices:
        return []

    idx = indices[movie]
    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:21]

    results = []

    for i, score in movie_list:
        row = df.iloc[i]

        results.append({
            "title": row["title"],
            "vote_average": row.get("vote_average", "N/A"),
            "release_date": row.get("release_date", "N/A"),
            "poster": fetch_poster(row["id"])
        })

    return results

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    movies = sorted(df["title"].unique())

    results = []
    query = ""

    if request.method == "POST":
        query = request.form.get("movie")

        if query and query in indices:
            results = recommend(query)

    # -----------------------------
    # TRENDING MOVIES (NOW WORKS)
    # -----------------------------
    if "popularity" in df.columns:
        top_movies_df = df.sort_values(by="popularity", ascending=False).head(10)
    else:
        top_movies_df = df.sort_values(by="vote_average", ascending=False).head(10)

    top_movies = []

    for _, row in top_movies_df.iterrows():
        top_movies.append({
            "title": row["title"],
            "vote_average": row.get("vote_average", "N/A"),
            "release_date": row.get("release_date", "N/A"),
            "poster": fetch_poster(row["id"])
        })

    return render_template(
        "index.html",
        movies=movies,
        results=results,
        query=query,
        top_movies=top_movies
    )

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
