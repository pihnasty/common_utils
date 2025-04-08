"""
Defines the DimensionlessType enum used for selecting methods of transforming flow data into dimensionless form.
"""
from enum import Enum


class DimensionlessType(Enum):
    """
    DimensionlessType.

    Defines the type of reduction to dimensionless form.
    """
    MEAN_TIME_M1_1 = 1           # TIME_M1_1 -> min = - 1;  max = +1;  MEAN ->  g=x/MEAN.
    STD_TIME_M1_1 = 2            # TIME_M1_1 -> min = - 1;  max = +1;  STD  ->  g=x/STD.
    CUSTOM_TIME_CUSTOM = 3       # CUSTOM_TIME_CUSTOM -> min = custom_min;  max = custom_max;
                                 # VALUE  ->  g=x/custom_value.
