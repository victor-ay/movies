from rest_framework import serializers
from rest_framework.serializers import Serializer

from movies_app.models import *


# class MovieSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Movie
#         fields = '__all__'
#         depth = 1

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ['actors', 'description']


class MovieDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ['actors']

class MovieAllRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        depth = 1

# class ActorNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ['name']
#
# class MovieActorSerializer(serializers.ModelSerializer):
#     actor = ActorNameSerializer(many=False)
#     class Meta:
#         model = MovieActor
#         exclude = ['movie']
#         depth = 1

class MovieActorSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(many=False)
    class Meta:
        model = MovieActor
        exclude = ['movie']
        depth = 1




class MyActorSerializer(Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256, min_length=3,
                                 allow_blank=False, trim_whitespace=True)
    birth_year = serializers.IntegerField(max_value=2020, min_value=1900)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

class WriteableMovieActorRelatedField(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
        return Actor.objects.all()

    def to_internal_value(self, data):
        val = super().to_internal_value(data)
        return val.pk

class AddMovieActorSerializer(serializers.Serializer):

    # actor_id = WriteableMovieActorRelatedField(
    #     read_only=False, many=False)
    actor_id = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all().values_list('id', flat=True))
    salary = serializers.IntegerField(min_value=0)
    main_role = serializers.BooleanField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        MovieActor.objects.create(movie_id=self.context['movie_id'],
                                  **validated_data)