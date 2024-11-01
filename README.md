# MovieRecommendationSystem
This project implements a movie recommendation system using techniques from Artificial Intelligence. It utilizes TF-IDF vectorization and cosine similarity to recommend similar movies based on a user's input.

**Key Features:**
* Reads movie data from a CSV file.
* Preprocesses data by handling missing values and combining relevant features.
* Converts textual features (genres, keywords, etc.) into numerical vectors using TF-IDF.
* Calculates similarity scores between movies using cosine similarity.
* Recommends similar movies to the user based on their input.

**Getting Started:**
1. Install required libraries (`numpy`, `pandas`, `difflib`, `scikit-learn`).
2. Load the movie data from the CSV file (modify the path accordingly).
3. Run the script to make movie recommendations.

**Dependencies:**
* numpy
* pandas
* difflib
* scikit-learn
