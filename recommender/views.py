from django.shortcuts import render
from .models import Movie
from .content_based import get_similar_movies

def recommend_view(request):
    movies = Movie.objects.all().order_by('title')[:100]  # for dropdown

    selected_id = request.GET.get('movieId')
    recommendations = None

    if selected_id:
        selected_id = int(selected_id)
        recommendations = get_similar_movies(selected_id, top_n=5)

    return render(request, 'recommender/recommendations.html', {
        'movies': movies,
        'recommendations': recommendations
    })
