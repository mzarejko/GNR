import os
import numpy as np


class Reader:

    def __init__(self):
        self.__data_frame_int = []
        self.__data_frame_time = []
        self.__max_call_time = 1440

    def read_file_int(self, path):
        self.__data_frame_int = []
        if os.path.isfile(path):
            try:
                with open(path, 'r') as f:
                    text = f.read()
            except Exception as e:
                print(str(e))

            split_data = np.array(text.split())
            self.__data_frame_int = split_data.reshape(-1, 2)

            return self.__data_frame_int

    def read_file_time(self, path):
        self.__data_frame_time = []
        if os.path.isfile(path):
            try:
                with open(path, 'r') as f:
                    text = f.read()
            except Exception as e:
                print(str(e))

                split_data = text.split()

                for i in range(len(split_data)):
                    if int(split_data[i]) < self.__max_call_time:
                        self.__data_frame_time.append(int(split_data[i]))

            self.__data_frame_time = np.array(self.__data_frame_time).reshape(-1, 1)
            return self.__data_frame_time


