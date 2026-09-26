import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. LOAD THE MOVIE DATASET
# ============================================================

movies = pd.read_csv("movies.csv")

print("Movie dataset loaded successfully!")
print("Number of movies:", len(movies))


# ============================================================
# 2. SELECT REQUIRED COLUMNS
# ============================================================

movies = movies[["title", "overview", "genres", "keywords"]].copy()


# ============================================================
# 3. HANDLE MISSING VALUES
# ============================================================

movies["overview"] = movies["overview"].fillna("")
movies["genres"] = movies["genres"].fillna("")
movies["keywords"] = movies["keywords"].fillna("")


# ============================================================
# 4. EXTRACT GENRE AND KEYWORD NAMES
# ============================================================

def extract_names(text):
    """
    Extract names from the JSON-like genre/keyword data.
    Example:
    [{"id": 28, "name": "Action"}]
    becomes:
    "Action"
    """

    try:
        data = ast.literal_eval(text)

        if isinstance(data, list):
            return " ".join(
                item["name"]
                for item in data
                if isinstance(item, dict) and "name" in item
            )

    except (ValueError, SyntaxError, TypeError):
        return ""

    return ""


movies["genres"] = movies["genres"].apply(extract_names)
movies["keywords"] = movies["keywords"].apply(extract_names)


# ============================================================
# 5. CREATE COMBINED FEATURES
# ============================================================

movies["tags"] = (
    movies["overview"] + " " +
    movies["genres"] + " " +
    movies["keywords"]
)


# Convert everything to lowercase
movies["tags"] = movies["tags"].str.lower()


print("\nMovie feature data prepared successfully!")

print("\nSample movie data:")
print(movies[["title", "tags"]].head())


# ============================================================
# 6. TF-IDF VECTORIZATION
# ============================================================

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["tags"])


print("\nTF-IDF vectorization completed!")
print("TF-IDF matrix shape:", tfidf_matrix.shape)


# ============================================================
# 7. CALCULATE COSINE SIMILARITY
# ============================================================

similarity_matrix = cosine_similarity(tfidf_matrix)


print("\nCosine similarity calculation completed!")
print("Similarity matrix shape:", similarity_matrix.shape)


# ============================================================
# 8. RECOMMENDATION FUNCTION
# ============================================================

def recommend_movies(movie_title, num_recommendations=5):

    # Remove extra spaces from user input
    movie_title = movie_title.strip()

    # Find the movie
    movie_matches = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    # If movie is not found
    if movie_matches.empty:
        print("\nMovie not found in the dataset.")
        print("Please check the movie title and try again.")
        return

    # Get the index of the selected movie
    movie_index = movie_matches.index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Sort movies according to similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(
        f"\nMovies similar to "
        f"'{movies.loc[movie_index, 'title']}':"
    )

    print("-" * 50)

    count = 0

    for index, score in similarity_scores:

        # Skip the selected movie itself
        if index == movie_index:
            continue

        print(
            f"{count + 1}. "
            f"{movies.iloc[index]['title']} "
            f"(Similarity: {score:.2f})"
        )

        count += 1

        if count == num_recommendations:
            break

    print("-" * 50)


# ============================================================
# 9. INTERACTIVE USER INPUT
# ============================================================

print("\n" + "=" * 60)
print("        MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nEnter a movie name to get similar movie recommendations.")
print("Type 'exit' to close the program.")


while True:

    movie_title = input("\nEnter movie title: ")

    # Exit the program
    if movie_title.lower().strip() == "exit":
        print("\nThank you for using the Movie Recommendation System!")
        break

    # Generate recommendations
    recommend_movies(movie_title, 5)