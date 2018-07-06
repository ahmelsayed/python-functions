import logging

import azure.functions as func
import numpy as np
import random
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def main(req: func.HttpRequest) -> func.HttpResponse:
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)

    return func.HttpResponse(output.getvalue(), mimetype="image/png", status_code=200)

