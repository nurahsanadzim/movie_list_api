from core.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    original_title = serializers.CharField(max_length=100, default='-')
    overview = serializers.CharField(max_length=10000, default='-')
    genres = serializers.CharField(max_length=10000, default='-')
    release_date = serializers.CharField(max_length=10, default='-')
    runtime = serializers.CharField(max_length=4, default='-')
    original_language = serializers.CharField(max_length=10000, default='-')
    spoken_language = serializers.CharField(max_length=10000, default='-')
    production_companies = serializers.CharField(max_length=10000, default='-')
    production_countries = serializers.CharField(max_length=10000, default='-')
    popularity = serializers.CharField(max_length=10, default='-')
    tagline = serializers.CharField(max_length=500, default='-')
    status = serializers.CharField(max_length=20, default='-')
    homepage = serializers.CharField(max_length=100, default='-')

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.original_title = validated_data.get('original_title', instance.original_title)
        instance.overview = validated_data.get('overview', instance.overview)
        instance.genres = validated_data.get('genres', instance.genres)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.runtime = validated_data.get('runtime', instance.runtime)
        instance.original_language = validated_data.get('original_language', instance.original_language)
        instance.spoken_language = validated_data.get('spoken_language', instance.spoken_language)
        instance.production_companies = validated_data.get('production_companies', instance.production_companies)
        instance.production_countries = validated_data.get('production_countries', instance.production_countries)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.status = validated_data.get('status', instance.status)
        instance.homepage = validated_data.get('homepage', instance.homepage)
        instance.save()
        return instance