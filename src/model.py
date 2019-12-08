"""Access application data.
"""
# import datetime as dt
from collections import namedtuple


class DataContainer:
    """Provide methods to retrieve data.
    """
    def __init__(self, source):
        self.source = source

    def _fetch_reading(self):
        """Generate list of strings for each line of data.
        """
        try:
            with open(self.source) as txtfile:
                for line in txtfile:
                    yield line.strip().split(',')
        except TypeError:
            pass

    def _generate_tuple(self):
        """Generate namedtuple object for each reading.
        """
        reading = self._fetch_reading()  # generator object
        nt = namedtuple('BP', next(reading))
        while reading:
            try:
                yield nt(*next(reading))
            except StopIteration:
                break

    def get_plot_data(self):
        """Return a tuple of lists.
        """
        ts, s, d, p = [], [], [], []  # define lists
        bp_data = self._generate_tuple()  # iterator
        for bp in bp_data:
            ts.append(bp.timestamp)
            # ts.append(dt.datetime.strptime(
            #     bp.timestamp, '%Y%m%d%H%M'))
            s.append(int(bp.systolic))
            d.append(int(bp.diastolic))
            p.append(int(bp.pulse))
        return (ts, s, d, p)

    def __repr__(self):
        return f"<class '{self.__class__.__name__}'"


if __name__ == '__main__':
    import os

    USER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.pardir, 'data/user.csv')
