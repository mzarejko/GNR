from Reader import Reader
import matplotlib.pyplot as plt
import numpy as np

class Data:

    def __init__(self):
        reader = Reader()
        self.__data_frame_int = reader.read_file_int("int.txt")
        self.__data_frame_time = reader.read_file_time("time.txt")
        self.__average_duration = self.calculate_average_duration(self.__data_frame_time)

    def calculate_average_duration(self, list):
        sum = 0
        for number in list:
            sum = sum + number
        average = sum/len(list)
        return average


    def calculate_traffic_intensity(self):
        #function for creating distribution of traffic intensity
        av_call_time = float(self.calculate_average_duration(self.__data_frame_time))
        distribution_call = []
        for i in self.__data_frame_int:
            distribution_call.append(i[1]*av_call_time)

        return distribution_call


    def create_plot(self, distribution_call, busy_hour=None):

        if busy_hour:
            for i in range(len(self.__data_frame_int[::, 0])):
                if self.__data_frame_int[::, 0][i] == busy_hour:
                    plt.plot(self.__data_frame_int[::, 0][:int(i)], distribution_call[:int(i)], color='blue')
                    plt.plot(self.__data_frame_int[::, 0][int(i+60):], distribution_call[int(i+60):], color='blue')
                    plt.plot(self.__data_frame_int[::, 0][int(i):int(i+60)], distribution_call[int(i):int(i+60)], color='orange')
                    break
        else:
            plt.plot(self.__data_frame_int[::, 0], distribution_call)
        plt.title('plot')
        plt.ylabel('traffic intensity')
        plt.xlabel('time')
        plt.show()


    def calculate_busy_hour(self, schedule_call):
        # for every min function calculate sum of traffic distribution from 1 h

        hour_array = {}

        for i in range(self.__data_frame_int.shape[0]):
            if self.__data_frame_int[i][0]+60>self.__data_frame_int[-1][0]:
                break
            TCBH = 0
            a = i
            while True:
                hour=self.__data_frame_int[a][0]

                if hour>=60+self.__data_frame_int[i][0]:
                    break

                TCBH+=schedule_call[a]
                a+=1

            hour_array[self.__data_frame_int[i][0]] = TCBH

        # max value from hour array is busy hour of TCBH
        busy_hour_traffic = list(list(hour_array.items())[0])[1]
        busy_hour = 0
        for i in hour_array:
            if busy_hour_traffic < hour_array[i]:
                busy_hour_traffic = hour_array[i]
                busy_hour = i


        return busy_hour, busy_hour_traffic




d = Data()
schedule = d.calculate_traffic_intensity()
a, _ = d.calculate_busy_hour(schedule)
d.create_plot(schedule, a)
