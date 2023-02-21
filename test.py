import operator
import os



os.environ["DJANGO_SETTINGS_MODULE"] = 'movies.settings'

import django
django.setup()

from movies_app.models import Movie, Rating

# new_movie = Movie(movie_name = "aaa", year = 2020, duration_in_min = 124)
# new_movie.save()
#
# new_movie = Movie(movie_name = "bbb", year = 2022, duration_in_min = 125)
# new_movie.save()
#
# new_movie = Movie(movie_name = "ccc", year = 2023, duration_in_min = 154)
# new_movie.save()
#
# new_movie = Movie(movie_name = "ddd", year = 2019, duration_in_min = 114)
# new_movie.save()

# all_movies = Movie.objects.all()
# print(all_movies)

# r = Rating.objects.get(id = 1)
# # print(r.movie_id)
# print(r.movie)

# m1 = Movie.objects.get(id = 1)
# print(m1.rating_set.all())
#
# movies_qs = Movie.objects.all().values_list('movie_name', 'duration_in_min')
# # movies_qs = movies_qs[:2]
# movies_qs = movies_qs.filter(year__gt = 2020)
# movies_qs = movies_qs[:2]
# print(movies_qs)

def reduce(func, items):
    result = items.pop()
    for item in items:
        result = func(result, item)

    return result

n_l = [1,2,3,4]
n_l_2 = [False, False, True]
print(reduce(operator.add,n_l))
# print(reduce(print,n_l))
