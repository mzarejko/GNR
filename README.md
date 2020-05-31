# Program do liczenia GNR
## Konfiguracja programu
  - python 3.7
  - matplotlib
  - numpy 
  - warnings 
  

## Dokumentacja

### Cel
Zadaniem programu jest policzenie średniej wartości natężenia ruchu korzystając ze wzoru A = D*h, gdzie D jest średnią intensywnością wywołań w każdej minucie, a h średnią arytmetyczną czasu trwania połączeń. Program zakłada, że wartości z wielu dni zostały uśrednione do 1 doby. Tak jak plik int.txt, który zawiera uśrednione wartości intensywności wywołań połączeń na określoną minutę z ciągu 1439 wartości.

### Opis kodu

W pliku Main.py mamy zawarty poniższy kod, który wywołuje konstruktor klasy Data i dokonuje poniższych operacji. 

```python
    d = Data()
    schedule = d.calculate_traffic_intensity()
    busy_hour, busy_hour_traffic = d.calculate_busy_hour(schedule)
    plt = d.create_plot(schedule, busy_hour)
    print("GNR:" + np.format_float_positional(busy_hour) + " min")
    print("Średnie natężenie w GNR:" + np.format_float_positional(busy_hour_traffic, 2) + " połączenio-minut")
    plt.show()
```

Obiekt klasy Data odczytuje za pomocą obiektu klasy Reader 2 pliki tekstowe "int.txt", "time.txt" oraz wylicza średnią arytmetyczą z wartości "time.txt".

```python
 reader = Reader()
        self.__data_frame_int = reader.read_file_int("int.txt")
        self.__data_frame_time = reader.read_file_time("time.txt")
        self.__average_duration = self.calculate_average_duration(self.__data_frame_time)
```

  Następnie deleguje wartosć `d` do wyliczenia średniej wartości natężenia ruchu dla poszczegulnych minut na podstawie przedstawionego wcześniej wzoru. 
  
  ```python
   def calculate_traffic_intensity(self):
        # fukcja do stworzenia przebiegu średniego natężenia ruchu
        av_call_time = float(self.calculate_average_duration(self.__data_frame_time))
        distribution_call = []
        for i in self.__data_frame_int:
            distribution_call.append(i[1] * av_call_time)

        return distribution_call
  ```
Posiadając wyliczony przebieg rozpoczęto liczenie GNR.

```python

  def calculate_busy_hour(self, schedule_call):
        # dla każdej minuty funkcja liczy sumę średnich natężeń ruchu dla 1 godziny
        hour_array = {}
        for i in range(self.__data_frame_int.shape[0]):
            if self.__data_frame_int[i][0] + 60 > self.__data_frame_int[-1][0]:  # kończy pętle aby nie wyszła o godzinę za daleko
                break
            TCBH = 0
            a = i
            while True:  # tworzenie tablicy z sumą natężen średnich w poszczególnych godzinach
                hour = self.__data_frame_int[a][0]

                if hour >= 60 + self.__data_frame_int[i][0]:
                    break

                TCBH += schedule_call[a]
                a += 1

            hour_array[self.__data_frame_int[i][0]] = TCBH

        # maksymalna wartość z busy_hour będzie szukaną wartością TCBH
        busy_hour_traffic = list(list(hour_array.items())[0])[1]
        busy_hour = 0  # 0 czy 1?, bo hour_array.items())[0])[1] dotyczy 1, ale to znów kwestia interpreteacji przedziału
        for i in hour_array:  # przeszukanie tablicy z godzinami w celu znalezienia największej wartości
            if busy_hour_traffic < hour_array[i]:
                busy_hour_traffic = hour_array[i]
                busy_hour = i

        return busy_hour, busy_hour_traffic
```
