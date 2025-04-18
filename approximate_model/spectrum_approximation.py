"""
This module provides a class for performing harmonic analysis of
dimensionless flow data using Fourier approximation. It supports
splitting the data into intervals, calculating harmonic components,
and reconstructing the signal using either all or mean harmonics.
"""
import math
import numpy as np

import pandas as pd
from numpy import std, mean

from constants.flow_constants import TIME, FLOW, NUMBER_OF_INTERVALS, NUMBER_OF_HARMONICS
from maths import math_util


class SpectrumWithMoreRealizationApproximate:
    """
    Initialize the approximation class with input dimensionless data and configuration.

    :param dim: DataFrame containing dimensionless flow data.
    :param config: Dictionary with configuration values including number of intervals and harmonics.
    """
    def __init__(self, dim, config: dict = None):
        self.dim = dim
        self.number_of_spectrum_split_parts = config.get(NUMBER_OF_INTERVALS)
        self.number_of_harmonics = config.get(NUMBER_OF_HARMONICS)


    def __get_harmonic_values(self, dim_parts):
        """
        Compute cosine and sine harmonic values and their transposed matrices for each partition.

        :param dim_parts: List of DataFrame splits of the dimensionless data.
        :return: Tuple containing cosine values, sine values, and their transposed matrices.
        """
        cos_harmonic_values = [[0] * self.number_of_harmonics] * self.number_of_spectrum_split_parts
        sin_harmonic_values = [[0] * self.number_of_harmonics] * self.number_of_spectrum_split_parts
        for i in range(self.number_of_spectrum_split_parts):
            cos_harmonic_values[i], sin_harmonic_values[i] \
                = math_util.numeric_calculate_fourier_series(dim_parts[i][FLOW], dim_parts[i][TIME],
                                                             self.number_of_harmonics)
        transposed_matrix_cos = [[cos_harmonic_values[k][m] for k in range(len(cos_harmonic_values))]
                             for m in range(len(cos_harmonic_values[0]))]
        transposed_matrix_sin = [[sin_harmonic_values[k][m] for k in range(len(sin_harmonic_values))]
                                 for m in range(len(sin_harmonic_values[0]))]
        return cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin

    def get_param(self):
        """
        Approximate the original dimensionless data using Fourier harmonics and return the result.

        :return: Tuple containing:
                 - Approximate dimensionless DataFrame,
                 - Mean value of the first harmonic (cosine),
                 - Root of summed variance from all harmonics.
        """
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin \
            = self.__get_harmonic_values(dim_parts)
        mean_value = 0.0
        std2 = 0.0
        k_sin = 0
        for row in transposed_matrix_cos:
            std2 = std2 + 0.5 * std(row) ** 2 + 0.5 * std(transposed_matrix_sin[k_sin])**2 # / len(dim_parts)
            k_sin=k_sin+1
        mean_value = mean_value + mean(transposed_matrix_cos[0])

        approximate_dim_parts = math_util.calculate_function(dim_parts, cos_harmonic_values, sin_harmonic_values)
        approximate_array_dim = np.concatenate(approximate_dim_parts)
        approximate_dim = pd.DataFrame(approximate_array_dim, columns=[TIME, FLOW])
        return approximate_dim, mean_value, math.sqrt(std2)

    def get_transposed_matrix(self):
        """
        Retrieve transposed matrices of cosine and sine harmonic values.

        :return: Tuple containing transposed cosine and sine harmonic matrices.
        """
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        _, _, transposed_matrix_cos, transposed_matrix_sin\
            = self.__get_harmonic_values(dim_parts)
        return transposed_matrix_cos, transposed_matrix_sin

    def get_cos_and_sin_harmonic_values(self):
        """
        Retrieve original (non-transposed) cosine and sine harmonic values.

        :return: Tuple containing cosine and sine harmonic values.
        """
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values, _, _ = self.__get_harmonic_values(dim_parts)
        return cos_harmonic_values, sin_harmonic_values

    def get_mean_by_row_of_transposed_matrix(self):
        """
        Calculate mean harmonic values (cos and sin) across all partitions for each harmonic.

        :return: Tuple of arrays containing mean values for each harmonic (cosine, sine).
        """
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        _, _, transposed_matrix_cos, transposed_matrix_sin = self.__get_harmonic_values(dim_parts)
        return np.mean(transposed_matrix_cos, axis=1), np.mean(transposed_matrix_sin, axis=1)

    def get_mean_approximate_dim(self):
        """
        Use mean harmonic values to approximate the dimensionless data.

        :return: DataFrame containing the approximated dimensionless data using mean harmonics.
        """
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values = self.get_mean_by_row_of_transposed_matrix()
        approximate_dim_parts\
            = math_util.calculate_function_by_mean_harmonic_values(dim_parts, cos_harmonic_values, sin_harmonic_values)
        approximate_array_dim = np.concatenate(approximate_dim_parts)
        approximate_dim = pd.DataFrame(approximate_array_dim, columns=[TIME, FLOW])
        return approximate_dim
