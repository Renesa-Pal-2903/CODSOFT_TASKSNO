# 🎬 Movie Recommendation System

A content-based movie recommendation system developed in Python as part of the **CodSoft Artificial Intelligence Internship**.

The system recommends movies similar to a movie selected by the user. It uses movie overviews, genres, and keywords to calculate similarity between movies.

---

## 📌 Project Overview

The Movie Recommendation System uses a **Content-Based Filtering** approach.

When the user enters a movie title, the system analyzes the movie's features and recommends other movies with similar characteristics.

The project uses:

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

---

## ✨ Features

- Loads movie information from a CSV dataset
- Handles missing data
- Extracts movie genres and keywords
- Combines movie overview, genres, and keywords into features
- Converts text features into numerical vectors using TF-IDF
- Calculates movie similarity using Cosine Similarity
- Provides the top 5 similar movies
- Displays similarity scores
- Supports interactive user input
- Handles invalid movie names
- Allows the user to exit the program

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**

---

## 📂 Project Structure

```text
Task-4-Recommendation-System
│
├── recommendation_system.py
├── movies.csv
└── README.md
```
## ⚙️ How It Works

1. Load Dataset

The system loads the movie dataset from movies.csv.

2. Select Movie Features

The following information is used:

Movie title
Movie overview
Genres
Keywords

3. Data Preprocessing

Missing values are replaced with empty strings.
Genres and keywords are extracted from the dataset and combined with the movie overview.

4. TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) converts the textual movie information into numerical vectors.
This allows the system to mathematically compare the content of different movies.

5. Cosine Similarity

Cosine Similarity is used to calculate how similar two movies are based on their feature vectors.
A higher similarity score indicates greater similarity between the movies.

6. Generate Recommendations

When the user enters a movie title, the system finds the most similar movies and displays the top 5 recommendations.

## ▶️ How to Run

### Step 1: Install Python
Make sure Python is installed on your system.

### Step 2: Install Required Libraries
Open the terminal in the project folder and run:
```bash
python -m pip install pandas scikit-learn
```
### Step 3: Run the Program
```bash
python recommendation_system.py
```
### Step 4: Enter a Movie Name
For example:
```bash
Enter movie title: The Dark Knight Rises
```
The system will display similar movies.

## 🧪 Sample Output
```text
============================================================
        MOVIE RECOMMENDATION SYSTEM
============================================================

Enter a movie name to get similar movie recommendations.
Type 'exit' to close the program.

Enter movie title: The Dark Knight Rises

Movies similar to 'The Dark Knight Rises':
--------------------------------------------------
1. The Dark Knight (Similarity: 0.52)
2. Batman Returns (Similarity: 0.44)
3. Batman (Similarity: 0.43)
4. Batman Forever (Similarity: 0.42)
5. Batman Begins (Similarity: 0.37)
--------------------------------------------------
```

## 📊 Dataset

The project uses the TMDB 5000 Movies Dataset, containing information about 4,803 movies.

The dataset includes information such as:

- Movie titles
- Overviews
- Genres
- Keywords
- Release information
- Ratings
- Popularity

Only the relevant features required for content-based recommendation are used by the program.

## 🧠 Recommendation Technique

This project uses Content-Based Filtering.

The recommendation is based on the similarity between movie features rather than user ratings or user behavior.

### Formula

Cosine Similarity is calculated as:
```text
Cosine Similarity = (A · B) / (||A|| × ||B||)
```
where A and B represent the feature vectors of two movies.

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Work with real-world datasets
* Perform data preprocessing
* Extract useful information from structured data
* Convert text into numerical representations
* Apply TF-IDF vectorization
* Calculate cosine similarity
* Build a content-based recommendation system
* Create an interactive Python application

## 🎓 Internship

**Internship:** CodSoft Artificial Intelligence Internship

**Task:** Task 4 – Recommendation System 

#CodSoft #ArtificialIntelligence #Python #MachineLearning #RecommendationSystem

## 👩‍💻 Author

**Renesa Pal**