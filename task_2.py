from task_1 import Tree, Car, Student # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    tree = Tree(5.0, 10, "oak")
    car = Car("Toyota", 180, 50)
    student = Student("Alice", 14, [85, 90, 78])
    # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        print(tree.read(-5.0)) # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        print(car.drive(-10)) # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        tree.grow(-1) # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')