# Напишите класс ListWorker:
# - принимает в себя неограниченное количество неименованных аргументов и работает с ними как со списком
# - реализуйте методы, которые возвращают:
# - - только числа
# - - только строки
# - - все кроме чисел и строк

class ListWorker(list):
    def __init__(self, *args):
        super().__init__(list(args))

    def __call__(self, *args):
        self = self + list(args)
        return self

    def get_numbers(self) -> filter:
        return filter(lambda el: isinstance(el, int) or isinstance(el, float), self)

    def get_strings(self) -> filter:
        return filter(lambda el: isinstance(el, str), self)

    def get_other(self) -> filter:
        return filter(lambda el: not (isinstance(el, int) or isinstance(el, float) or isinstance(el, str)), self)


if __name__ == "__main__":
    LW = ListWorker(1, 2., "str", None)
    print(f"{LW=}")
    print(f"{[*LW.get_numbers()]=}\n{[*LW.get_strings()]=}\n{[*LW.get_other()]=}")
