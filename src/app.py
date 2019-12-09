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
        Current, average, min, and max.
        """
        def _get_difference(hi, lo):
            dif = list()
            for i in range(len(self.data)):
                dif.append(hi[i] - lo[i])
            return dif

        def _get_average(data):
            return round(sum(data) / len(data))

        _, systolic, diastolic, pulse = self.data
        pulse_pres = _get_difference(systolic, diastolic)

        stat_dict = dict()
        key = ["Systolic", "Diastolic", "Pulse", "Pulse Pressure"]
        for k, v in enumerate([systolic, diastolic, pulse, pulse_pres]):
            avg = _get_average(v)
            stat_dict[key[k]] = (v[-1], avg, min(v), max(v))
        return stat_dict

    def start(self):
        """Load app with saved data, start GUI mainloop.
        """
        self.build_chart()
        self.build_stats()

        self.view.root.mainloop()
