from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate, MigrateCommand
import json

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
@app.route('/home')

def index():
    with open('odno-kino/data.json', encoding='UTF-8') as file:
        data1 = json.load(file)

        # сортирую фаил, по ключу имдб от большего к меньшему вывожу X элементов
        data = (sorted(data1, key=lambda user: user['imdb'], reverse=True)[:35000])

    naz = []
    naz1 = []
    naz2 = []
    naz3 = []
    result = []
    ganre = []
    year = 0


    if request.method == "POST":
        if request.form.get('a'):
            ganre.append(request.form.get('a'))

        if request.form.get('b'):
            ganre.append(request.form.get('b'))

        if request.form.get('c'):
            ganre.append(request.form.get('c'))
        if request.form.get('d'):
            ganre.append(request.form.get('d'))

        if request.form.get('e'):
            ganre.append(request.form.get('e'))

        if request.form.get('f'):
            ganre.append(request.form.get('f'))
        if request.form.get('g'):
            ganre.append(request.form.get('g'))

        if request.form.get('h'):
            ganre.append(request.form.get('h'))

        if request.form.get('i'):
            ganre.append(request.form.get('i'))
        if request.form.get('j'):
            ganre.append(request.form.get('j'))

        if request.form.get('k'):
            ganre.append(request.form.get('k'))

        if request.form.get('l'):
            ganre.append(request.form.get('l'))
        if request.form.get('m'):
            ganre.append(request.form.get('m'))

        if request.form.get('n'):
            ganre.append(request.form.get('n'))

        if request.form.get('o'):
            ganre.append(request.form.get('o'))
        if request.form.get('p'):
            ganre.append(request.form.get('p'))

        if request.form.get('q'):
            ganre.append(request.form.get('q'))

        if request.form.get('r'):
            ganre.append(request.form.get('r'))
        if request.form.get('s'):
            ganre.append(request.form.get('s'))

        if request.form.get('t'):
            ganre.append(request.form.get('t'))

        if request.form.get('u'):
            ganre.append(request.form.get('u'))
        if request.form.get('v'):
            ganre.append(request.form.get('v'))

        if request.form.get('w'):
            ganre.append(request.form.get('w'))

        if request.form.get('x'):
            ganre.append(request.form.get('x'))
        if request.form.get('y'):
            ganre.append(request.form.get('y'))
        if request.form.get('z'):
            ganre.append(request.form.get('z'))

        if request.form.get('aa'):
            ganre.append(request.form.get('aa'))
        if request.form.get('bb'):
            ganre.append(request.form.get('bb'))
        if request.form.get('year'):
            year = (request.form.get('year'))

        print(year)
        # ganre.sort()

        if len(ganre) == 1:
            for el in data:
                for i in el['ganre']:
                    if ganre:
                        if i in ganre:
                            if year == False:
                                naz.append(
                                    {
                                    'nazFilm' : (el['nazFilm']),
                                    'href': (el['href']),
                                    'pic_href': (el['pic_href']),
                                    'ganre': (el['ganre']),
                                    'imdb': (el['imdb']),
                                    'prosmotr': (el['prosmotr']),
                                    'year' : (el['year'])
                                }
                                )
                                naz = (sorted(naz, key=lambda user: user['imdb'], reverse=True)[:100])
                                # print(naz)
                            else:
                                if year == (el['year']):
                                    naz1.append(
                                        {
                                            'nazFilm': (el['nazFilm']),
                                            'href': (el['href']),
                                            'pic_href': (el['pic_href']),
                                            'ganre': (el['ganre']),
                                            'imdb': (el['imdb']),
                                            'prosmotr': (el['prosmotr']),
                                            'year': (el['year'])
                                        }
                                    )
        else:
            for el in data:
                el['ganre'].sort()
                # print(ganre)
                # print(el['ganre'])
                if  list(set(ganre).intersection(set(el['ganre']))):
                # if any(i in ganre for i in el['ganre']):
                    lim = len(ganre)
                    if (len(list(set(ganre).intersection(set(el['ganre']))))) == lim:
                # if  set(ganre) & set(el['ganre']):
                # if ganre == el['ganre']:
                        if year == False:
                            naz2.append(
                                {
                                    'nazFilm': (el['nazFilm']),
                                    'href': (el['href']),
                                    'pic_href': (el['pic_href']),
                                    'ganre': (el['ganre']),
                                    'imdb': (el['imdb']),
                                    'prosmotr': (el['prosmotr']),
                                    'year': (el['year'])
                                }
                            )
                            naz2 = (sorted(naz2, key=lambda user: user['imdb'], reverse=True)[:100])
                            # print(naz2)
                        else:
                            if year == (el['year']):
                                naz3.append(
                                {
                                    'nazFilm': (el['nazFilm']),
                                    'href': (el['href']),
                                    'pic_href': (el['pic_href']),
                                    'ganre': (el['ganre']),
                                    'imdb': (el['imdb']),
                                    'prosmotr': (el['prosmotr']),
                                    'year': (el['year'])
                                }
                            )



    ganre = '  '.join(ganre)



    return render_template("index.html", data=data, ganre= ganre, naz1=naz1, naz3=naz3, year= year, naz=naz, naz2=naz2)






if __name__ == "__main__":
    app.run(debug=False)