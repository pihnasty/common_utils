"""
This module provides the Dimensionless class for transforming dimensional flow data
into dimensionless form using various standardization methods.
"""
import copy
from typing import Dict, Callable

from common_utils.dim_less.dimensionless_type import DimensionlessType
from constants.flow_constants import TIME, FLOW, STD, DIMENSIONLESS_TYPE, \
    CHARACTERISTIC_FLOW_VALUE, CHARACTERISTIC_TIME_VALUE


class Dimensionless:
    """Handles the transformation of dimensional flow data into dimensionless form
    using various standardization methods.
    """

    def __init__(self, dim, config: dict = None):
        config = config or {}
        self.dim = dim
        self.dim_time_min = dim[TIME].min()
        self.dim_time_max = dim[TIME].max()
        self.dim_flow_std = config.get(STD, dim[FLOW].std())
        self.custom_flow_value = config.get(CHARACTERISTIC_FLOW_VALUE)
        self.custom_time_value = config.get(CHARACTERISTIC_TIME_VALUE)
        self._apply_transformation(DimensionlessType[config.get(DIMENSIONLESS_TYPE)])

    def _apply_transformation(self, dim_type) -> None:
        self.dim_less = copy.copy(self.dim)
        transformation_methods: Dict[DimensionlessType, Callable[[float, float], None]] = {
            DimensionlessType.STD_TIME_M1_1: self._transform_dim_to_dim_less_by_sdt,
            DimensionlessType.MEAN_TIME_M1_1: self._transform_dim_to_dim_less_by_mean,
            DimensionlessType.CUSTOM_TIME_CUSTOM: self._transform_dim_to_dim_less_by_custom,
        }
        transform = transformation_methods.get(dim_type)
        if transform is not None:
            return transform()
        raise ValueError(f"Unsupported DimensionlessType: {dim_type}")

    def _transform_dim_to_dim_less_by_sdt(self, min_time=-1.0, max_time=1.0):
        """
        Makes transform the dimension flow to the dimensionless flow using given rules std and time.
        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimensionless flow
        """
        self.dim_less[FLOW] = self.dim[FLOW] / self.dim_flow_std
        self.dim_less[TIME] = self.get_dim_less_time_on_interval(min_time, max_time)

    def _transform_dim_to_dim_less_by_mean(self, min_time=-1.0, max_time=1.0):
        """
        Makes transform the dimension flow to the dimensionless flow using given rules mean and time.
        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimensionless flow
        """
        self.dim_less[FLOW] = self.dim[FLOW] / self.dim[FLOW].mean()
        self.dim_less[TIME] = self.get_dim_less_time_on_interval(min_time, max_time)

    def _transform_dim_to_dim_less_by_custom(self, min_time=0.0, max_time=1.0):
        """
        Makes transform the dimension flow to the dimensionless flow using given rules mean and time.
        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimensionless flow
        """
        self.dim_less[FLOW] = self.dim[FLOW] / self.custom_flow_value
        self.dim_less[TIME] = self.get_dim_less_time_on_interval(min_time, max_time / self.custom_time_value)

    def get_dim_less_time_on_interval(self, min_time, max_time):
        """
        Creates dimension less time for the flow.

        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimension less time for the flow.
        """
        dim_less_time = (self.dim[TIME] - self.dim_time_min) / (self.dim_time_max - self.dim_time_min)
        return dim_less_time * (max_time + 1) + min_time

    def get_centred_dim_less(self) -> dict:
        """
        Returns a centered version of the dimensionless flow.
        :return: Centered dimensionless flow.
        """
        centred_dim_less = copy.deepcopy(self.dim_less)
        centred_dim_less[FLOW] = self.dim_less[FLOW] - self.dim_less[FLOW].mean()
        return centred_dim_less

    def get_dim_less(self) -> dict:
        """
        Returns the dimensionless flow.
        :return: Dimensionless flow.
        """
        return self.dim_less
