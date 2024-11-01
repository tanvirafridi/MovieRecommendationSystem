
"""Movie Recommendations for you"""

movie_name = input('Enter your movie name :')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

Close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == Close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies you might also like : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<21):
    print(i, '.',title_from_index)
    i+=1