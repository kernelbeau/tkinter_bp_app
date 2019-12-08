"""Control module.
Import model and view. Set data source. Start GUI loop.
"""
import os

from src.model import DataContainer
from src.view import MainView

DEMO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.pardir, 'data/demo.csv')
USER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.pardir, 'data/user.csv')
USER_DATA = os.path.exists(USER)


class AppCtrl:

    def __init__(self):
        self.model = self._initialize_model()
        self.data = self.model.get_plot_data()
        self.view = MainView()

    def _initialize_model(self):
        """Is user data available, if not use demo data.
        """
        if USER_DATA:
            model = DataContainer(USER)
        else:  # use demo data
            model = DataContainer(DEMO)
        return model

    def __repr__(self):
        return "<class '{}({!r}, {!r})'>".format(
            self.__class__.__name__, self.model, self.view)

    def build_chart(self):
        fig = self.view.create_chart(self.data)
        self.view.display_chart(fig)

    def build_stats(self):
        stats = self.calculate_stats()
        self.view.fill_stats_frame(stats)

    def calculate_stats(self):
        """Return a dictionary of tuples.
        Min/Max, average, latest reading for systolic,
        diastolic, pulse, and pulse pressure.
        """
        def _get_difference(hi, lo):
            dif = list()
            for i in range(len(self.data)):
                dif.append(hi[i] - lo[i])
            return dif

        def _get_min_max(data):
            return (min(data), max(data))

        def _get_average(data):
            return round(sum(data) / len(data))

        _, systolic, diastolic, pulse = self.data
        pulse_pres = _get_difference(systolic, diastolic)

        stat = dict()
        key = ["systolic", "diastolic", "pulse", "pulse_pressure"]
        for k, v in enumerate([systolic, diastolic, pulse, pulse_pres]):
            min_max = _get_min_max(v)
            avg = _get_average(v)
            stat[key[k]] = (
                min_max, avg, v[-1],
                )
        return stat

    def start(self):
        """Load app with saved data, start GUI mainloop.
        """
        self.build_chart()
        self.build_stats()

        self.view.root.mainloop()
