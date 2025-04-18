"""
This module provides functions to calculate probability density values
for normal and uniform distributions. Useful for probabilistic modeling
and statistical analysis.
"""
import numpy as np
import pandas as pd


def normal_distribution(value, mean, std):
    """
    Calculates the probability density of a normal (Gaussian) distribution.

    Args:
        value (float): The point at which to evaluate the distribution.
        mean (float): The mean (μ) of the distribution.
        std (float): The standard deviation (σ) of the distribution.

    Returns:
        float: The probability density at the given point.
    """
    return 1. / std / np.sqrt(2 * np.pi) * np.exp(-((value - mean) ** 2) / 2. / std ** 2)


def uniform_distribution(value, mean, min_value):
    """
    Calculates the probability density of a uniform distribution centered at `mean`.

    Args:
        value (float): The point at which to evaluate the distribution.
        mean (float): The center of the uniform distribution.
        min_value (float): The minimum value used to define the range.

    Returns:
        float: The probability density at the given point, or 0.0 if out of range.
    """
    delta = mean - min_value
    result = 0.0
    if mean - delta <= value <= mean + delta:
        result = 1.0 / (2.0 * delta)
    return result


def calculate_probability(values, intervals, y_name="y", x_name="x"):
    delta, generated_distribution_density =  calculate_density(values, intervals, y_name, x_name,)
    probability = initialization_function_y_from_x(intervals, y_name, x_name)
    summa = 0.0
    for k in range(intervals):
        summa += generated_distribution_density[y_name][k] * delta
        probability[x_name][k] = generated_distribution_density[x_name][k]
        probability[y_name][k] = summa
    return probability


def calculate_density(values, intervals, y_name, x_name,):
    max_tau = values.max() * 1.001
    min_tau = values.min() * 0.999
    delta = (max_tau - min_tau) / intervals
    line = sorted(values)
    generated_distribution_density = initialization_function_y_from_x(intervals, y_name, x_name)
    tau = min_tau
    for k in range(intervals):
        for i in range(len(line)):
            if tau < line[i] <= tau + delta:
                generated_distribution_density[y_name][k] += 1.0 / (delta * len(line))
        tau = tau + delta
        generated_distribution_density[x_name][k] = tau
    return delta, generated_distribution_density


def initialization_function_y_from_x(intervals, y_name="y", x_name="x"):
    function = pd.DataFrame()
    function[x_name] = [0.0] * intervals
    function[y_name] = [0.0] * intervals
    return function

