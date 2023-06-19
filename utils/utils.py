import pandas as pd
import os
import json

from plotly import __version__
from plotly.offline import download_plotlyjs, plot, iplot
from plotly import graph_objs as go


def plotDFs(df, limit=-1, title=None, tofile=False, filename='iplot.html', columns=None):
    if isinstance(df, list):
        df=pd.concat(df, axis=1)
    if columns is None:
        columns=df.columns.tolist()
    datalist=[]
    for count,col in enumerate(columns):
        try:
            datalist.append(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
        except:
            print (col)

    layout = dict(title = "bbt")
    fig = dict(data = datalist, layout = layout)
    if not tofile:
        iplot(fig, show_link=False)
    else:
        iplot(fig, show_link=False)
        plot(fig, filename=filename)