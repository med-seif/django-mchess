from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.conf import settings
from django.db import connection
from scipy import stats as stat





def stats(request: HttpRequest):
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    Game.objects.filter(time_class='rapid').order_by('game_date', 'game_time')
    with connection.cursor() as cursor:
        cursor.execute("SELECT my_rating FROM game WHERE time_class='rapid' ORDER BY game_date, game_time asc ")
        rows = list(cursor.fetchall())
    my_list = []
    for r in rows:
        my_list.append(r[0])

    x = list(range(0, len(my_list)))
    y = my_list
    slope, intercept, r, p, std_err = stat.linregress(x, y)

    def myfunc(x):
        h = slope
        j = intercept
        return slope * x + intercept

    mymodel = list(map(myfunc, x))
    speed = myfunc(1500)
    speed1 = myfunc(1600)
    speed2 = myfunc(1700)

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.rcParams["figure.figsize"] = (30, 10)
    plt.savefig(settings.PROJECT_PATH + '/static/img/plot3.png')


    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    plt.rcParams["figure.figsize"] = (30, 10)
    plt.savefig(settings.PROJECT_PATH + '/static/img/plot4.png')
    return render(request, 'client/games/stats.html', {

    })
