"""
This module defines constant keys used throughout the flow processing project.
These constants are primarily used for configuration, DataFrame access, and data transformation steps.
"""

FLOW = "flow"
TIME = "time"

# Approximation
APPROXIMATE = "approximate"
APPROXIMATE_TYPE = "approximate_type"
APPROXIMATE_DIMLESS_FLOW = "approximate_dimless_flow"
APPROXIMATE_ERR_DIMLESS_FLOW = "approximate_err_dimless_flow"
HARMONIC_NUMBER = "harmonic_number"
COS_HARMONIC_VALUES = "cos_harmonic_values"
SIN_HARMONIC_VALUES = "sin_harmonic_values"
NUMBER_OF_INTERVALS = "number_of_intervals"
NUMBER_OF_HARMONICS = "number_of_harmonics"
STD = "std"

# Dimensionless
DIMENSIONLESS = "dimensionless"
DIMENSIONLESS_TYPE = "dimensionless_type"
DIMLESS_FLOW = "dimless_flow"
DIMLESS_FLOW3 = "dimless_flow3"
TAU = "tau"
CHARACTERISTIC_FLOW_VALUE = "characteristic_flow_value"
CHARACTERISTIC_TIME_VALUE = "characteristic_time_value"

# Correlation
# This constant defines which points from flow using for calculate a correlation function.
# By "period" = 1 all points are used (0,1,2,3,4,5.6, ...).
# By "period" = 2 only each second point is used ( 0,2,4,6,8, ...).
# By "period" = 10 only each ten-th point is used ( 0,10,20,30,40, ...).
# This approach allows to reduce the calculation correlation function, where complicity is (n/period)*(n/period).
CORRELATION = "correlation"
PERIOD = "period"
VARTHETA = "vartheta"

# Probability
PROBABILITY = "probability"
# This constant defines number intervals by executing probability or density. It is usual to equal 50.
NUMBER_DENSITY_INTERVALS = "number_density_intervals"
FLOW_PROBABILITY_Y = "flow_probability_y"
FLOW_PROBABILITY_X = "flow_probability_x"
FLOW_DENSITY_Y = "flow_density_y"
CRITICAL_PROB_VALUE = "critical_prob_value"
