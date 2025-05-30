import copy

import pandas as pd

from constants.flow_constants import TIME, FLOW, PERIOD, CORRELATION
from io_utils.console.progress import progress


class CorrelationFunction:
    """
    Creating correlation function, that uses for calculated correlation function for dim set.
    """
    def __init__(self, dim, config: dict = None):
        """
        :param dim: stochastic flow.
        :param period: self.experiment["period"].
        """
        self.dim = dim
        self.period = config[PERIOD]

        self.correlation = pd.DataFrame()
        self.size = round(len(dim[TIME]) / self.period / 2.0)
        self.correlation[TIME] = [0.0] * self.size
        self.correlation[CORRELATION] = [0.0] * self.size

        self.interval_tau = (dim[TIME].max() - dim[TIME].min())
        self.delta_tau = dim[TIME][1] - dim[TIME][0]

        self.flow_mean = dim[FLOW].mean()
        self.flow_std = dim[FLOW].std()

        self.correlation = self.execute_correlation()

    def execute_correlation(self):
        """
        Executes correlation function.

        :return: correlation function
        """
        return self.execute_correlation_n_n_mv()

    def execute_correlation_n_n_mv(self):
        """
        Executes correlation function for rule n(n-v). .

        :return: correlation function.
        """
        dim_size = len(self.dim[TIME])
        for n_v in range(self.size):
            value = 0.0
            tau = n_v * self.period * self.delta_tau
            count_2 = round(dim_size - n_v * self.period)
            for n_tau in range(count_2):
                gamma_1 = self.dim[FLOW][n_tau] - self.flow_mean
                gamma_2 = self.dim[FLOW][n_tau + n_v * self.period] - self.flow_mean
                value = value + gamma_1 * gamma_2 * self.delta_tau
            self.correlation[TIME][n_v] = tau
            self.correlation[CORRELATION][n_v] = value / self.interval_tau * dim_size / count_2 / self.flow_std ** 2

            progress(n_v, self.size, "CorrelationFunction.execute_correlation_n_n_mv")
        progress(self.size, self.size, "CorrelationFunction.execute_correlation_n_n_mv\n")
        return self.correlation

    def get_correlation(self):
        return self.correlation;

    @staticmethod
    def cut_by_template(template_dim, dim):
        """
        Equalizes the size of time intervals.

        :return: correlation function with size of template_dim.
        """
        temp_dim = copy.copy(template_dim)
        for i in range(len(template_dim[TIME])):
            temp_dim[CORRELATION][i] = dim[CORRELATION][i]
        return temp_dim
