class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        return self._length * self._width * 25 * 5 / 1000


def main():
    """
    2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см*число см толщины полотна. Проверить работу метода.
    Например: 20м*5000м*25кг*5см = 12500 т
    """
    result = Road(20, 5000)
    print(result.calculate())


if __name__ == '__main__':
    main()
