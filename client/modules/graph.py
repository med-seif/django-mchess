import matplotlib.pyplot as plt
import numpy as np
from django.conf import settings
from datetime import datetime


def get_game_results_graph(gtype, data):
    y = np.array([35, 25, 25, 15])
    my_labels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels=my_labels)
    plt.legend()
    graph_name = 'img/result_' + str(datetime.utcnow().timestamp()) + '.png'
    path = settings.PROJECT_PATH + '/static/' + graph_name
    plt.savefig(path)

    return graph_name
