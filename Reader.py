import os
import numpy as np


class Reader:

    def __init__(self):
        self.data_frame_int = []
        self.data_frame_time = []
        self.max_call_time = 1440

    def read_file_int(self, path):
        self.data_frame_int = []
        if os.path.isfile(path):
            try:
                with open(path, 'r') as f:
                    text = f.read()
            except Exception as e:
                print(str(e))

            split_data = np.array(text.split())

            for i in range(len(split_data)):
                if split_data[i].find(',') is not -1:
                    a = split_data[i].replace(',', '.')
                    self.data_frame_int.append(float(a))
                else:
                    self.data_frame_int.append(float(split_data[i]))

            self.data_frame_int = np.array(self.data_frame_int).reshape(-1, 2)

            return self.data_frame_int

    def read_file_time(self, path):
        self.data_frame_time = []
        if os.path.isfile(path):
            try:
                with open(path, 'r') as f:
                    text = f.read()
            except Exception as e:
                print(str(e))

            split_data = text.split()


            for i in range(len(split_data)):
                if int(split_data[i]) < self.max_call_time:
                    self.data_frame_time.append(int(split_data[i]))




            self.data_frame_time = np.array(self.data_frame_time).reshape(-1, 1)
            return self.data_frame_time

r = Reader()
p = r.read_file_int('int.txt')
x = r.read_file_time('time.txt')
print(p)
print(x)