import numpy as np

from Data import Data

d = Data()
schedule = d.calculate_traffic_intensity()
busy_hour, busy_hour_traffic = d.calculate_busy_hour(schedule)
d.create_plot(schedule, busy_hour)
print("GNR: " + np.format_float_positional(busy_hour) + "min")
print("Średnia wartość natężenia ruchu w GNR: " + np.format_float_positional(busy_hour_traffic, precision=3) + " połączenio-minut")
input()