# Николай – оригинальный человек.
# Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
# Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
# В частности:
# - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет;
# - если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.

class Nikola:
    def __init__(self, name: str, age: int):
        self.age = age
        name = name.title()
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"


if __name__ == "__main__":
    nikol = Nikola("Николай", 18)
    maxim = Nikola("Максим", 23)
    print(f"{nikol.name=}, {maxim.name=}")
