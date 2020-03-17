from Reader import Reader


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


data = Data()
