"""
This module provides functions to calculate probability density values
for normal and uniform distributions. Useful for probabilistic modeling
and statistical analysis.
"""
import numpy as np

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
