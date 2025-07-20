from django.core.management.base import BaseCommand
import pandas as pd
from recommender.models import Movie, Rating

class Command(BaseCommand):
    help = "Import MovieLens data"

    def handle(self, *args, **kwargs):
        movies = pd.read_csv('data/movies.csv')
        ratings = pd.read_csv('data/ratings.csv')

        Movie.objects.all().delete()
        Rating.objects.all().delete()

        for _, row in movies.iterrows():
            Movie.objects.create(
                movieId=row['movieId'],
                title=row['title'],
                genres=row['genres']
            )

        for _, row in ratings.iterrows():
            try:
                movie = Movie.objects.get(movieId=row['movieId'])
                Rating.objects.create(
                    userId=row['userId'],
                    movie=movie,
                    rating=row['rating']
                )
            except Movie.DoesNotExist:
                continue

        self.stdout.write(self.style.SUCCESS("✅ Data imported successfully"))
