# Программа создает симуляцию работы лифтов в разных домах и позволяет манипулировать ими с помощью различных функций.


import random

# Класс House включает: адресс, кол-во этажей, кол-во лифтов
class House:
    def __init__(self, address, floors, elevators):
        self.address = address
        self.floors = floors
        self.elevators = elevators

    # Возвращение информации о доме
    def house_info(self):
        return f"Дом находится по адресу: {self.address}, Кол-во этажей: {self.floors}, Кол-во лифтов: {len(self.elevators)}"


# Класс Elevator включает: вместимость(кол-во человек), текущий этаж, направление движения, этаж назначения, состояние дверей (заблок./разблок.) и отображение информации о состоянии лифта
class Elevator:
    def __init__(self, capacity, current_floor, direction, destination):
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = direction
        self.destination = destination
        self.doors = False

    # Получение информации о лифте и его состоянии
    def elevator_info(elevator):
        if elevator.direction == "не двигается":
            print(
                f"Информация о лифте: вместимость - {elevator.capacity}, текущий этаж - {elevator.current_floor}, направление движения - {elevator.direction}")
            print(f"Двери заблокированы: {elevator.doors}")
            print()
        else:
            print(
                f"Информация о лифте: вместимость - {elevator.capacity}, направление движения - {elevator.direction}, назначенный этаж - {elevator.destination}")
            print(f"Лифт добрался до назначенного этажа {elevator.current_floor}")
            print()
            elevator.direction = "не двигается"

        # Класс Operator включает: функции управления лифтом (отправление на этаж, управление дверьми, экстренная остановка лифта)


class Operator:

    # Отправляем лифт на любой этаж дома (Лифт не сможет ехать с заблокированными дверьми)
    def send_elevator_to_floor(elevator, floor):
        if elevator.doors == True:
            print("Чтобы отправить лифт на другой этаж, разблокируйте двери")
            print()
            return

        if floor > elevator.current_floor:
            elevator.direction = "вверх"
        elif floor < elevator.current_floor:
            elevator.direction = "вниз"
        else:
            elevator.direction = "не двигается"
        elevator.start_floor = elevator.current_floor
        elevator.current_floor = floor
        elevator.destination = floor
        print(f"Отправляем лифт на этаж № {floor}")
        print()

    # Останавливаем лифт (В моей модели лифт будет останавливаться на одном из этажей, которые он проезжает. Этот этаж выбирается случайно)
    def elevator_stop(elevator):
        if elevator.direction == "не двигается":
            print("Лифт и так стоит на месте.")
            print()
        else:
            if elevator.start_floor > elevator.destination:
                elevator.current_floor = random.randint(elevator.destination, elevator.start_floor)
            else:
                elevator.current_floor = random.randint(elevator.start_floor, elevator.destination)
            elevator.direction = "не двигается"
            print(f"Лифт экстренно остановлен на этаже {elevator.current_floor}")
            print()

    # Раблок. дверей
    def unblock_doors(elevator):
        elevator.doors = False
        print(f"Двери лифта разблокированы")
        print()

    # Блок. дверей
    def block_doors(elevator):
        elevator.doors = True
        print(f"Двери лифта заблокированы")
        print()


# Проверка на правильность введенного значения (Используется в Меню оператора)
def Obrabotka():
    while True:
        try:
            X = int(input())
            break
        except ValueError:
            print("Ошибка, введите еще раз.")
    return X


# Создаем 4 лифта
elevator1 = Elevator(10, 1, "не двигается", 1)
elevator2 = Elevator(8, 1, "не двигается", 1)
elevator3 = Elevator(4, 1, "не двигается", 1)
elevator4 = Elevator(6, 1, "не двигается", 1)

# Создаем 3 дома
house1 = House("Мира, 40", 10, [elevator1])
house2 = House("Ленина, 69", 8, [elevator2])
house3 = House("Шейкмана, 33", 12, [elevator3, elevator4])

# Меню оператора
print("Добро пожаловать в программу, моделирующую работу оператора лифтов.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    print("К какому дому обратиться: Мира, 40; Ленина, 69; Шейкмана, 33?")
    print("Введите соответсвенно 1, 2, 3 (либо 4 для выхода из программы): ", end=" ")
    n = Obrabotka()

    # Первый дом
    if n == 1:
        print(f"Информация о доме: {house1.house_info()} ")
        while True:
            print("Информация о лифте - 1")
            print("Отправить лифт на этаж - 2")
            print("Остановка лифта - 3")
            print("Заблокировать/разблокировать двери 4")
            print("Выбрать другой дом - 5")
            x = Obrabotka()
            print()

            if x == 1:
                elevator1.elevator_info()

            elif x == 2:
                while True:
                    try:
                        m = int(input("на какой этаж (1-10) отправить лифт: "))
                        if m not in range(1, 11):
                            raise ValueError
                        break
                    except ValueError:
                        print("Выберите от 1 до 10.")
                Operator.send_elevator_to_floor(elevator1, m)

            elif x == 3:
                Operator.elevator_stop(elevator1)

            elif x == 4:
                if elevator1.doors == True:
                    Operator.unblock_doors(elevator1)
                else:
                    Operator.block_doors(elevator1)

            elif x == 5:
                break

    # Второй дом
    elif n == 2:
        print(f"Информация о доме: {house2.house_info()} ")
        while True:
            print("Информация о лифте - 1")
            print("Отправить лифт на этаж - 2")
            print("Остановка лифта - 3")
            print("Заблокировать/разблокировать двери 4")
            print("Выбрать другой дом - 5")
            x = Obrabotka()
            print()

            if x == 1:
                elevator2.elevator_info()

            elif x == 2:
                while True:
                    try:
                        m = int(input("на какой этаж (1-8) отправить лифт: "))
                        if m not in range(1, 9):
                            raise ValueError
                        break
                    except ValueError:
                        print("Выберите от 1 до 8.")
                Operator.send_elevator_to_floor(elevator2, m)
            elif x == 3:
                Operator.elevator_stop(elevator2)

            elif x == 4:
                if elevator2.doors == True:
                    Operator.unblock_doors(elevator2)
                else:
                    Operator.block_doors(elevator2)

            elif x == 5:
                break

    # Третий дом
    elif n == 3:
        print(f"Информация о доме: {house3.house_info()} ")
        while True:
            print("В этом доме 2 лифта: выберите 1 или 2 (выбрать другой дом - 3)", end=" ")
            lift = Obrabotka()

            if lift == 1:
                while True:
                    print("Информация о лифте - 1")
                    print("Отправить лифт на этаж - 2")
                    print("Остановка лифта - 3")
                    print("Заблокировать/разблокировать двери 4")
                    print("Выбрать другой лифт - 5")
                    x = Obrabotka()
                    print()

                    if x == 1:
                        elevator3.elevator_info()

                    elif x == 2:
                        while True:
                            try:
                                m = int(input("на какой этаж (1-12) отправить лифт: "))
                                if m not in range(1, 13):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Выберите от 1 до 12.")
                        Operator.send_elevator_to_floor(elevator3, m)

                    elif x == 3:
                        Operator.elevator_stop(elevator3)

                    elif x == 4:
                        if elevator3.doors == True:
                            Operator.unblock_doors(elevator3)
                        else:
                            Operator.block_doors(elevator3)

                    elif x == 5:
                        break

            if lift == 2:
                while True:
                    print("Информация о лифте - 1")
                    print("Отправить лифт на этаж - 2")
                    print("Остановка лифта - 3")
                    print("Заблокировать/разблокировать двери 4")
                    print("Выбрать другой лифт - 5")
                    x = Obrabotka()
                    print()

                    if x == 1:
                        elevator4.elevator_info()

                    elif x == 2:
                        while True:
                            try:
                                m = int(input("на какой этаж (1-12) отправить лифт: "))
                                if m not in range(1, 13):
                                    raise ValueError
                                break
                            except ValueError:
                                print("Выберите от 1 до 12.")
                        Operator.send_elevator_to_floor(elevator4, m)

                    elif x == 3:
                        Operator.elevator_stop(elevator4)

                    elif x == 4:
                        if elevator4.doors == True:
                            Operator.unblock_doors(elevator4)
                        else:
                            Operator.block_doors(elevator4)

                    elif x == 5:
                        break

            elif lift == 3:
                break

    elif n == 4:
        break
