import numpy as np

from Data import Data

try:
    d = Data()
    schedule = d.calculate_traffic_intensity()
    busy_hour, busy_hour_traffic = d.calculate_busy_hour(schedule)
    plt = d.create_plot(schedule, busy_hour)
    print("GNR:" + np.format_float_positional(busy_hour) + " min")
    print("Średnie natężenie w GNR:" + np.format_float_positional(busy_hour_traffic, 2) + " połączenio-minut")
    plt.show()
except Exception as e:
    print(e)
    input()
