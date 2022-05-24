from django.shortcuts import render, redirect

# Create your views here.
import psycopg2
from ex06.forms import myForm


def create_table(request):
    try:
        conn = psycopg2.connect(database="djangotraining", user="djangouser", password="secret", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE ex06_movies (
            episode_nb int PRIMARY KEY, 
            title varchar(64) unique not null, 
            opening_crawl text, 
            director varchar(32) not null, 
            producer varchar(128) not null, 
            release_date date not null,
            created timestamp default now(),
            updated timestamp default now()
            );
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """
        )
        conn.commit()
        conn.close()
        cur.close()
        context = 'OK'
    except Exception as e:
        context = e
    finally:
        return render(request, 'ex00/index.html', {'context': context})


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
    try:
        conn = psycopg2.connect(database="djangotraining", user="djangouser", password="secret", host="localhost",
                                port="5432")
        cur = conn.cursor()
        for elem in data:
            try:
                cur.execute(
                    f"""INSERT INTO "ex06_movies" (episode_nb, title, director, producer, release_date) 
                    VALUES ({elem['episode_nb']}, '{elem['title']}', '{elem['director']}', '{elem['producer']}', '{elem['release_date']}');"""
                )
                context.append('OK')
                conn.commit()
            except Exception as e:
                conn.rollback()
                context.append(e)
        conn.close()
        cur.close()
    except Exception as e:
        context.append(e)
    finally:
        return render(request, 'ex02/insert.html', {'context': context})


def get_data(request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT * from ex06_movies")
        context = cur.fetchall()
        conn.commit()
        conn.close()
        cur.close()
        return render(request, 'ex06/data.html', {'context': context})
    except Exception:
        return render(request, 'ex06/data.html')


def update_data(request):
    try:
        conn = psycopg2.connect(
            database="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        if request.method == 'POST':
            cur.execute("SELECT title from ex06_movies")
            rows = cur.fetchall()
            data = myForm([(row[0], row[0]) for row in rows], request.POST)
            if data.is_valid():
                cur.execute(f"Update ex06_movies set opening_crawl = '{data.cleaned_data['opening_crawl']}' where title = '{data.cleaned_data['title']}'")
                conn.commit()
            conn.close()
            cur.close()
            return redirect(request.path)
        cur.execute("SELECT title FROM ex06_movies;")
        rows = cur.fetchall()
        context = {'form': myForm([(row[0], row[0]) for row in rows])} if rows else None
        conn.close()
        cur.close()
        return render(request, 'ex06/update.html', context)
    except Exception:
        return render(request, 'ex06/update.html')


