# Напишите класс с описанием параллелепипеда:
# - принимает в себя ширину и длину основания, а также высоту
# - реализуйте методы для расчета его объема, площади основания и площади боковой стороны
# - *добавьте статический метод info, который бы выводил перечень методов (без использования dir, а обычным принтом)

class RectangularParallelepiped:
    __volume: float = None
    __base_area: float = None
    __side_area_a: float = None
    __side_area_b: float = None

    @staticmethod
    def info() -> tuple:
        methods = (("get_volume", "возвращает объём"),
                   ("get_base_area", "возвращает площадь основания"),
                   ("get_side_area_a", "возвращает площадь основания боковой стороны с основанием \"a\""),
                   ("get_side_area_a", "возвращает площадь основания боковой стороны с основанием \"b\""))
        print("Методы:\n" +
              "\n".join([f"- {method[0]} - {method[1]}" for method in methods]))
        return methods

    def __init__(self, a: float, b: float, h: float):
        self.a = a
        self.b = b
        self.h = h

    def get_volume(self) -> float:
        if self.__volume is None:
            self.__volume = self.a * self.b * self.h
        return self.__volume

    def get_base_area(self) -> float:
        if self.__base_area is None:
            self.__base_area = self.a * self.b * self.h
        return self.__base_area

    def get_side_area_a(self) -> float:
        if self.__side_area_a is None:
            self.__side_area_a = self.a * self.h
        return self.__side_area_a

    def get_side_area_b(self) -> float:
        if self.__side_area_b is None:
            self.__side_area_b = self.b * self.h
        return self.__side_area_b


if __name__ == "__main__":
    RP = RectangularParallelepiped(2, 3, 4)
    RP.info()
    print(f"{RP.get_volume()=}")
    print(f"{RP.get_base_area()=}")
    print(f"{RP.get_side_area_a()=}")
    print(f"{RP.get_side_area_b()=}")
