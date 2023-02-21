import os

from django.db.models import Count

os.environ["DJANGO_SETTINGS_MODULE"] = 'movies.settings'

import django
django.setup()

from movies_app.models import *

# m=Movie.objects.get(id=3)
# new_actor = Actor(name = 'tttt', birth_year = 200)
# new_actor.save()
# ma = MovieActor(movie = m, actor = new_actor, salary = 10000, main_role = False)
# ma.save()

# new_actor = Actor(name = 'Brad Pit', birth_year = 1964)
# new_actor.save()
#
# new_actor = Actor(name = 'Kevin Spacy', birth_year = 1972)
# new_actor.save()
#
# new_actor = Actor(name = 'Eddy Merphy', birth_year = 1968)
# new_actor.save()

# new_rating = Rating(movie = Movie.objects.get(id = 1), rating = 8)
# new_rating.save()

# new_rating = Rating(movie = Movie.objects.get(id = 2), rating = 6.7)
# new_rating.save()
# new_rating = Rating(movie = Movie.objects.get(id = 2), rating = 9.1)
# new_rating.save()
# new_rating = Rating(movie = Movie.objects.get(id = 3), rating = 1.8)
# new_rating.save()
# new_rating = Rating(movie = Movie.objects.get(id = 3), rating = 2.3)
# new_rating.save()
# new_rating = Rating(movie = Movie.objects.get(id = 4), rating = 8.8)
# new_rating.save()

# ma = MovieActor(actor = Actor.objects.get(id = 4),
#                 movie = Movie.objects.get(id = 4),
#                 salary = 128_000,
#                 main_role = False)
# ma.save()
#
# ma = MovieActor(actor = Actor.objects.get(id = 1),
#                 movie = Movie.objects.get(id = 4),
#                 salary = 260_000,
#                 main_role = True)
# ma.save()

# ma = MovieActor(actor = Actor.objects.get(id = 4),
#                 movie = Movie.objects.get(id = 1),
#                 salary = 160000,
#                 main_role = True)
# ma.save()

# m = Movie.objects.get(id=3)
# m.actors.create(name = 'Jesica Parker',
#                 birth_year = 1988,
#                 through_defaults = {'salary': 12000,
#                                     'main_role': True}
#                 )

# m = Movie.objects.get(id =3)
# # m.actors.add(Actor.objects.get(id=5),through_def`aults = {'salary': 10_000,
# #                                     'main_role': True})
#
# print(m.actors.all())
# print(m.movieactor_set.all())


# a = Actor.objects.get(id = 4)
# print(a.movie_set.all())
#
# a.movie_set.add(Movie.objects.get(id =3), through_defaults = {
#     'salary' : 125,
#     'main_role': False
# })

# for m in Movie.objects.all().prefetch_related('actors'):
#     print(m, m.actors.all())

# r_v = Movie.objects.all().annotate(Count('actors'))
# for r in r_v:
#     print(r, r.actors__count, r.movieactor_set)

# r_v = Movie.objects.filter(movieactor__salary__gt = 100)
# print(r_v)

r_v = Movie.objects.values('year').annotate(movies_per_year=Count('id'))
print(r_v)