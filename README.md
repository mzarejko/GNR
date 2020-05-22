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

W pliku Main.py mamy zawarty poniższy kod, który wywołuje konstruktor klasy Data, następnie deleguje go do wyliczenia średniej wartości natężenia ruchu dla poszczegulnych minut. Posiadając wyliczony przebieg rozpoczyna się proces liczenia GNR oraz rysowania wykresu.

```python
d = Data()
    schedule = d.calculate_traffic_intensity()
    busy_hour, busy_hour_traffic = d.calculate_busy_hour(schedule)
    plt = d.create_plot(schedule, busy_hour)
    print("GNR:" + np.format_float_positional(busy_hour) + " min")
    print("Średnie natężenie w GNR:" + np.format_float_positional(busy_hour_traffic, 2) + " połączenio-minut")
    plt.show()
```


  
