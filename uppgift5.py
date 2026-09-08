# I programmet undersöker vi medelvärdet och standardavvikelsen av årsmedeltemperaturen 
# i Stockholm för varje sekel från 1700-2000-talet, samt hela perioden

import math

# Årsmedeltemperatur i Stockholm 1756-2019
data_17_20 = [4.7,5.8,4.6,6.2,5.1,6.4,5.7,4.9,6.2,5.7,6.4,5.1,5.1,5.3,
5.6,4.7,5.0,7.3,5.2,7.6,6.2,5.3,5.6,7.7,5.6,6.5,4.8,6.8,
4.2,4.4,4.2,5.5,4.4,6.8,6.1,7.4,5.7,6.3,7.6,4.7,6.2,6.8,
6.9,4.1,4.9,5.8,5.5,4.7,4.7,4.0,5.3,5.5,5.3,4.7,5.0,6.6,
3.9,5.7,4.3,5.7,4.8,5.6,6.6,6.9,4.6,5.5,7.5,5.7,6.6,6.2,
7.2,5.8,5.3,3.5,4.9,5.4,5.4,5.7,6.6,5.5,4.9,4.7,3.8,5.2,
5.2,5.6,6.4,5.7,4.0,5.0,6.4,5.4,5.6,5.0,5.3,5.9,6.0,5.5,
6.4,4.8,4.6,6.6,6.9,6.6,4.9,5.5,4.6,6.7,4.5,5.5,5.4,3.2,
6.4,5.6,5.1,3.8,6.9,6.4,5.9,4.2,4.8,4.6,6.0,4.6,5.5,3.9,
6.5,5.7,5.7,4.8,5.8,5.7,3.7,5.5,6.0,5.8,4.7,4.7,6.7,5.4,
6.4,6.0,6.1,5.3,5.3,6.2,3.8,6.0,5.2,6.0,6.4,5.3,5.6,5.0,
6.5,6.7,5.6,6.5,7.1,4.3,5.5,5.1,5.9,5.2,6.6,6.6,4.9,4.8,
5.6,6.0,5.5,5.4,5.1,5.4,7.2,4.8,6.3,6.1,7.8,6.6,6.7,6.9,
7.7,6.8,4.4,4.3,4.1,7.3,6.6,6.5,6.2,5.7,6.5,7.5,6.5,6.4,
5.1,7.2,5.8,5.5,4.5,5.9,5.2,7.1,5.9,6.9,5.0,5.3,6.0,5.0,
5.1,6.4,5.8,5.7,4.8,6.2,6.9,6.6,6.9,7.7,5.5,5.7,5.2,5.2,
5.3,5.3,6.3,6.8,6.6,4.1,5.5,4.2,6.2,7.7,7.6,6.6,7.2,6.3,
6.6,6.4,5.7,7.0,6.2,7.5,7.7,6.8,7.4,7.0,6.9,7.2,7.7,7.4,
7.8,6.9,5.3,7.8,6.5,7.1,8.1,8.0,7.4,7.2,8.1,7.8]

# Delar upp datamängden i sekel
data17 = data_17_20[0:44] # Årsmedeltemperatur i Stockholm 1756-1799
data18 = data_17_20[44:144] # Årsmedeltemperatur i Stockholm 1800-1899
data19 = data_17_20[144:244] # Årsmedeltemperatur i Stockholm 1900-1999
data20 = data_17_20[244:] # Årsmedeltemperatur i Stockholm 2000-2019

# Funktion som beräknar genomsnittet i en datamängd
def mean(data): 
    sum = 0
    for i in data:
        sum += i
    return sum/len(data)

# Funktion som beräknar standardavvikelsen i en datamängd
def sigma(data):
    sum = 0
    m = mean(data)
    for i in data:
        sum += (i-m)**2
    return math.sqrt(sum/len(data))


# Beräknar och skriver ut medelvärde och standardavvikelse för hela perioden
print(f"Medelvärdet för hela perioden 1756-2019 är {round(mean(data_17_20),4)}°C och standardavvikelsen {round(sigma(data_17_20),4)}°C")

# Listar datamängderna per sekel för att kunna gå igenom dem ett och ett i for-loop
data_list = [data17, data18, data19, data20]
century = 0

# Beräknar och skriver ut medelvärde och standardavvikelse för respektive sekel
for data in data_list:
    print(f"Medelvärdet för {century+17}00-talet är {round(mean(data),4)}°C och standardavvikelsen {round(sigma(data),4)}°C")
    century += 1