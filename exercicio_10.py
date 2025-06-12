import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def plot_histograma(vals: list[float], bins: int = 10) -> Figure:
    fig, ax = plt.subplots()
    ax.hist(vals, bins=bins, edgecolor='black')
    ax.set_title('Histograma')
    ax.set_xlabel('Valores')
    ax.set_ylabel('Frequência')
    return fig
