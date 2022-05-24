from django.shortcuts import render
import psycopg2


# Create your views here.
def create_table(request):
    try:
        conn = psycopg2.connect(database="djangotraining", user="djangouser", password="secret", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE ex00_movies ("
            "episode_nb int PRIMARY KEY, "
            "title varchar(64) unique not null, "
            "opening_crawl text, "
            "director varchar(32) not null , "
            "producer varchar(128) not null, "
            "release_date date not null"
            ");"
        )
        conn.commit()
        conn.close()
        cur.close()
        context = 'OK'
    except Exception as e:
        context = e
    finally:
        return render(request, 'ex00/index.html', {'context': context})