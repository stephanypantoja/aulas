class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = 0
        self.set_temperatura(temperatura)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print("Temperatura inválida.")
            
    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Crítico"

s1 = Sensor(230)
print(s1.get_temperatura(), s1.status())
s2 = Sensor(222)
print(s2.get_temperatura(), s2.status())
s3 = Sensor(130)
print(s3.get_temperatura(), s3.status())
s4 = Sensor(-2333)
print(s4.get_temperatura(), s4.status())