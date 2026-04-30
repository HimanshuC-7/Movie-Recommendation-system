# 🎬 Movie Recommendation System

A **Flask-based Machine Learning web application** that recommends movies based on content similarity using **TF-IDF and Cosine Similarity**, with real-time movie posters fetched from the **TMDB API**.

---

## 🚀 Project Overview

This project recommends movies by analyzing movie metadata such as **tags, genres, and descriptions**. It builds a similarity model at runtime and returns the most relevant movies based on user selection.

It also includes a **Netflix-style UI**, trending movies section, and dynamic poster fetching using an external API.

---

## ✨ Features

- 🎯 Content-based movie recommendation system  
- 🔍 Search movies from dataset  
- 🎬 Trending movies section (based on popularity / ratings)  
- 🖼️ Real-time movie posters using TMDB API  
- ⚡ TF-IDF + Cosine Similarity model (runtime generation)  
- 💻 Modern Netflix-inspired UI  
- 📱 Fully responsive frontend design  

---

## 🧠 How It Works

1. Load datasets (`movies_processed.csv` + `UI_dataset.csv`)
2. Merge datasets using movie ID
3. Convert movie tags into numerical vectors using **TF-IDF**
4. Compute similarity using **Cosine Similarity**
5. Recommend top 20 similar movies
6. Fetch movie posters from **TMDB API**
7. Display results in Flask web interface

---

# 🌐 Live Demo

The project is live and deployed on Render:

👉 Try it here: **[Click to Open Web Page](https://movie-recommendation-system-tzs1.onrender.com)**

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python
- Flask
- Pandas

### 🔹 Machine Learning
- TF-IDF Vectorizer
- Cosine Similarity
- Content-Based Filtering

### 🔹 Frontend
- HTML5
- CSS3 (Netflix-style UI)

### 🔹 API
- TMDB API (Movie posters)

---

## 📁 Project Structure

```text
MOVIE RECOMMENDATION SYSTEM/
│
├── CODE/
│   ├── app.py                      # Flask backend application
│   ├── .env                        # TMDB API key (not uploaded to GitHub)
│   │
│   ├── static/
│   │   ├── style.css              # UI styling (Netflix-inspired design)
│   │   ├── no-image.jpg           # fallback poster image
│   │
│   ├── templates/
│   │   ├── index.html             # Frontend UI page
│
├── Processed Data/
│   ├── movies_processed.csv       # Cleaned dataset
│   ├── UI_dataset.csv             # Metadata (ratings, popularity)
│
├── Raw Data/
│   ├── tmdb_5000_movies.csv       # Original TMDB dataset
│   ├── tmdb_5000_credits.csv      # Cast & crew dataset
│
└── README.md
```

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```
## 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
## 3️⃣ Install Dependencies
```bash 
pip install flask pandas scikit-learn requests python-dotenv
```
## 4️⃣ Setup .env file
```bash 
TMDB_API_KEY=your_tmdb_api_key_here
```
## 5️⃣ Run the Application
```bash 
cd CODE
python app.py
```


# 🎯 Recommendation System Logic

- Each movie is converted into a TF-IDF vector  
- Cosine similarity measures similarity between movies  
- Top 20 similar movies are recommended  
- Results are dynamically generated per request  

---

# 🎬 Trending Section

Displays top 10 movies based on:

- Popularity (if available)  
- Otherwise vote average  

Fetches posters using TMDB API  

---

# 🔥 Key Highlights

- No pre-trained `.pkl` files used  
- Fully dynamic ML pipeline  
- Lightweight Flask application  
- Real-time API integration  
- Netflix-style modern UI  

---

# 🚀 Future Improvements

- ⚡ Save TF-IDF model as `.pkl` for faster loading  
- 🤖 Add collaborative filtering system  
- ❤️ User login & favorites system  
- 🎥 Add trailer preview (YouTube API)  
- 📊 Improve ranking algorithm  

---

# 👨‍💻 Author

**Himanshu Choudhary**  
📍 Hyderabad, India  

🔗 LinkedIn: https://linkedin.com/in/himanshuchoudhary17  
💻 GitHub: https://github.com/HimanshuC-7  

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository  
- 🍴 Fork it  
- 🚀 Share it with others  
