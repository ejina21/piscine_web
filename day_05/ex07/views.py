from django.shortcuts import render, redirect

from ex07.models import Movies
from ex06.forms import myForm


def insert_data(request):
    context = []
    data = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19',
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16',
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19',
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25',
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17',
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25',
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11',
        },
    ]
    for el in data:
        try:
            Movies.objects.create(
                title=el['title'],
                episode_nb=el['episode_nb'],
                director=el['director'],
                producer=el['producer'],
                release_date=el['release_date'],
            )
            context.append('OK')
        except Exception as e:
            context.append(e)
    return render(request, 'ex02/insert.html', {'context': context})


def get_data(request):
    try:
        context = Movies.objects.all()
        data = []
        for el in context:
            data.append(
                [
                    el.episode_nb,
                    el.title,
                    el.opening_crawl,
                    el.director,
                    el.producer,
                    el.release_date,
                    el.created,
                    el.updated
                ]
            )
        return render(request, 'ex06/data.html', {'context': data})
    except Exception:
        return render(request, 'ex06/data.html')


def update_data(request):
    try:
        if request.method == 'POST':
            rows = Movies.objects.all()
            data = myForm([(row.title, row.title) for row in rows], request.POST)
            if data.is_valid():
                mov = Movies.objects.get(title=data.cleaned_data['title'])
                mov.opening_crawl = data.cleaned_data['opening_crawl']
                mov.save()
            return redirect(request.path)
        rows = Movies.objects.all()
        context = {'form': myForm([(row.title, row.title) for row in rows])} if rows else None
        return render(request, 'ex06/update.html', context)
    except Exception:
        return render(request, 'ex06/update.html')
