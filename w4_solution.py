import datetime
import operator
import os
from functools import reduce

from django.db.models import Count, Q, Max

os.environ["DJANGO_SETTINGS_MODULE"] = 'movies.settings'

import django
django.setup()

from movies_app.models import *

def get_actors_younger_age(age:int) -> list[Actor]:
    return Actor.objects.filter(birth_year__gt = datetime.date.today().year - age)

def get_actors_age () -> list[Actor]:
    return Actor.objects.annotate(per_age = 63)

if __name__ == '__main__':
    # print(get_actors_younger_age(age=50))
    # print(get_actors_age())

    # # 2. Get movies that last less than 2.5 hours and were released after 2005
    # print(Movie.objects.filter(duration_in_min__lt = 2.5*60, year__gt = 2005))

    # 3. Get all the movies that contain a word “criminal”, “mob” or “cop” in their description
    # n_l = ['cop','mob']
    # print(Movie.objects.filter(reduce(operator.or_, (Q(description__icontains=x) for x in n_l))))

    # 4. Like previous, but get only movies that were released before 2010
    # n_l = ['cop','mob']
    # print(Movie.objects.filter(reduce(operator.or_, (Q(description__icontains=x, year__lt = 2010) for x in n_l))))

    # 5. Get list of actors, and add amount of movies they played in (for each one)
    # all_actors = Actor.objects.all().annotate(movie_num = Count('movie'))
    # for ac in all_actors:
    #     print(ac, ac.movie_num)

    # Get max and min salary for the movie per each actor
    all_actors = Actor.objects.all()
    for ac in all_actors:
        print(ac, ac.max_salary)
