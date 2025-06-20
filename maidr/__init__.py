__version__ = "1.2.1"

from .api import close, render, save_html, show, stacked
from .core import Maidr
from .core.enum import PlotType
from .patch import (
    barplot,
    boxplot,
    candlestick,
    clear,
    heatmap,
    highlight,
    histogram,
    lineplot,
    scatterplot,
    regplot,
    kdeplot,
)

__all__ = [
    "close",
    "render",
    "save_html",
    "show",
    "stacked",
]
