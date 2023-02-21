from django.shortcuts import *

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from movies_app.models import *
from movies_app.serializers import *


def get_movies_list(request):
    movies_qs = Movie.objects.all()

    if 'name' in request.query_params:
        movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
    if 'duration_from' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
    if 'duration_to' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
    if 'description' in request.query_params:
        movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

    if not movies_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = MovieSerializer(movies_qs, many =True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def movies_list(request: Request):
    if request.method == 'GET':
        return get_movies_list(request)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def movie_details(request:Request, movie_id: int):
#     try:
#         movie = Movie.objects.get(id = movie_id)
#         serializer = MovieDetailsSerializer(movie, many=False)
#         return Response(serializer.data)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PATCH'])
def movie_details(request:Request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.query_params == 'GET':
        serializer = MovieDetailsSerializer(movie, many=False)
        return Response(serializer.data)

    elif request.query_params == 'PATCH':
        serializer = MovieDetailsSerializer(movie, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response()


@api_view(['GET'])
def movie_ratings(request: Request):
    ratings_qs = Rating.objects.all()

    # print(f"{request.query_params['min_rating']}, {type(request.query_params['min_rating'])}, {int(float(request.query_params['min_rating']))}")

    if 'min_rating' in request.query_params:
        ratings_qs = ratings_qs.filter(rating__gte = int(float(request.query_params['min_rating'])))

    if 'max_rating' in request.query_params:
        ratings_qs = ratings_qs.filter(rating__lte = request.query_params['max_rating'])

    serializer = MovieAllRatingsSerializer(ratings_qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_actors(request: Request, movie_id: int):
    if request.method == 'GET':
        movie_actors = MovieActor.objects.filter(movie_id = movie_id)
        serializer = MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddMovieActorSerializer(data=request.data, many=False, context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response()

def index(request):
    return render(request, 'index.html')