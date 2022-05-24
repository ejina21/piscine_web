import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .parsing import parsing_people, parsing_planet


def create_table(request):
    try:
        conn = psycopg2.connect(
            dbname='djangotraining',
            user='postgres',
            password='password',
            host='localhost',
            port='5432',
        )
        CREATE_TABEL = f"""
                CREATE TABLE ex08_planets(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    climate VARCHAR,
                    diameter INT,
                    orbital_period INT,
                    population BIGINT,
                    rotation_period INT,
                    surface_water REAL,
                    terrain VARCHAR(128)
                    );
                CREATE TABLE ex08_people(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    birth_year VARCHAR(32),
                    gender VARCHAR(32),
                    eye_color VARCHAR(32),
                    hair_color VARCHAR(32),
                    height INT,
                    mass REAL,
                    homeworld VARCHAR(64) REFERENCES ex08_planets(name)
                    );
                """
        with conn.cursor() as curs:
            curs.execute(CREATE_TABEL)
        conn.commit()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("OK")


class Populate(View):
    table_planets = "ex08_planets"
    table_people = "ex08_people"
    planets = []
    people = []
    conn = psycopg2.connect(
        dbname='djangotraining',
        user='postgres',
        password='password',
        host='localhost',
        port='5432',
    )

    def get(self, request):
        try:
            with open('data/planets.csv') as f:
                self.planets = [parsing_planet(line) for line in f.readlines()]
            with open('data/people.csv') as f:
                self.people = [parsing_people(line) for line in f.readlines()]
        except Exception as e:
            return HttpResponse(e)

        result = []
        INSERT_PLANET = f"""
                    INSERT INTO {self.table_planets}
                    (
                        name,
                        climate,
                        diameter,
                        orbital_period,
                        population,
                        rotation_period,
                        surface_water,
                        terrain
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    );
                    """

        INSERT_PEOPLE = f"""
                    INSERT INTO {self.table_people}
                    (
                        name,
                        birth_year,
                        gender,
                        eye_color,
                        hair_color,
                        height,
                        mass,
                        homeworld
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    );
                    """

        curs = self.conn.cursor()
        for planet in self.planets:
            try:
                curs.execute(INSERT_PLANET, [
                    planet['name'],
                    planet['climate'],
                    planet['diameter'],
                    planet['orbital_period'],
                    planet['population'],
                    planet['rotation_period'],
                    planet['surface_water'],
                    planet['terrain'],
                ])
                result.append("OK")
                self.conn.commit()
            except psycopg2.DatabaseError as e:
                self.conn.rollback()
                result.append(e)

        for people in self.people:
            try:
                curs.execute(INSERT_PEOPLE, [
                    people['name'],
                    people['birth_year'],
                    people['gender'],
                    people['eye_color'],
                    people['hair_color'],
                    people['height'],
                    people['mass'],
                    people['homeworld'],
                ])
                result.append("OK")
                self.conn.commit()
            except psycopg2.DatabaseError as e:
                self.conn.rollback()
                result.append(e)

        curs.close()
        return HttpResponse("<br/>".join(str(i) for i in result))


class Display(View):
    template = 'ex08/display.html'
    conn = psycopg2.connect(
        dbname='djangotraining',
        user='postgres',
        password='password',
        host='localhost',
        port='5432',
    )

    def get(self, request):
        SELECT_TABEL = f"""
            SELECT
                ex08_planets.name,
                ex08_people.homeworld,
                ex08_planets.climate
            FROM
                ex08_planets
                RIGHT JOIN ex08_people
                ON
                    ex08_people.homeworld = ex08_planets.name
                where
                    ex08_planets.climate LIKE '%windy%'
                ORDER BY ex08_planets.name;
            """
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                datas = curs.fetchall()
            print("Q")
            return render(request, self.template, {'context': datas})
        except Exception as e:
            return HttpResponse("Нет доступных данных")
