from Data import Data

if __name__ == '__main__':
    d = Data()
    schedule = d.calculate_traffic_intensity()
    a, _ = d.calculate_busy_hour(schedule)
    d.create_plot(schedule, a)