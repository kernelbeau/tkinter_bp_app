"""Tkinter GUI access point.
"""
from matplotlib.backends.backend_tkagg \
    import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.base_gui import BaseGUI, BG


class MainView(BaseGUI):
    """TODO: docstring."""
    def __init__(self):
        super().__init__()

    def create_chart(self, data):
        """Return a Matplotlib Figure().
        Takes a tuple of lists."""
        ts, systolic, diastolic, pulse = data
        fig = Figure(
            dpi=84, facecolor=BG, edgecolor=BG,
            frameon=True, tight_layout=True)
        ax = fig.add_subplot(
            xlabel='Time of Reading',
            ylabel='Pulse (bpm) / Pressure (mgHg)')
        ax.plot(
            ts, systolic, label='Systolic',
            color='blue')
        ax.plot(
            ts, diastolic, label='Diastolic',
            color='black', linestyle='--')
        ax.bar(
            ts, pulse, label='Pulse',
            alpha=0.25, color='red')
        fig.autofmt_xdate()
        fig.legend(
            loc='upper center', ncol=3, framealpha=1)
        return fig

    def display_chart(self, fig):
        """TODO: docstring."""
        chart_frame = self.get_chart_frame()
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill='both', expand=True)

    def fill_stats_frame(self, stats):
        """TODO: docstring."""
        print(stats)

    def __repr__(self):
        return f"<class '{self.__class__.__name__}'"
