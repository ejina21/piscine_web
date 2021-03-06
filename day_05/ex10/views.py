from django.db.models import Q
from django.shortcuts import render
from .models import Movies, People, Planets


def movies(request):
    results = "Nothing corresponding to your research"

    if request.method == 'POST':
        min_date = request.POST.get('min_date', '')
        max_date = request.POST.get('max_date', '')
        diameter = request.POST.get('diameter', '')
        gender = request.POST.get('gender', '')
        people = People.objects.all()
        lookups = (
            Q(gender=gender) &
            Q(homeworld__diameter__gte=diameter) &
            Q(movies_people__release_date__range=[min_date, max_date])
        )
        results = People.objects.filter(lookups)

    return render(request, 'ex10/movies.html', {'results': results})
