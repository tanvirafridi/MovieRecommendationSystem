"""Similarity"""

# Using cosine similarity to get similarity score
similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# Getting the movie name from the user
movie_name = input('Enter your movie name :')

#Creating list with all the movie names in the existing dataset
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

#Finding the closest match for the input given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

Close_match = find_close_match[0]
print(Close_match)

#Finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == Close_match]['index'].values[0]
print(index_of_the_movie)

#Getting a list of similar movies

similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

# sorting the movies based on their similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

# print the name of similar movies based on index
print('Movies you might also like : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<21):
    print(i, '.',title_from_index)
    i+=1