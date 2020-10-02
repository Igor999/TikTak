line_one = ["-", "-", "-"]
line_two = ["-", "-", "-"]
line_three = ["-", "-", "-"]

def zone():
    print(line_one)
    print(line_two)
    print(line_three)
    return 0
zone()

figure1 = input("Играете крестиком(Х) или ноликом(О) (буквы русские): ")
figure2 = ""

while figure1 != "Х" and figure1 != "О":
    print("Ошибка выбора фигуры")
    figure1 = input("Играете крестиком(Х) или ноликом(О) (буквы русские): ")

if figure1 == "Х":
    figure2 = "О"
else:
    figure2 = "Х"


while True:
    def victory():
        if all([line_one[0] == "Х",
               line_one[1] == "Х",
               line_one[2] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_two[0] == "Х",
               line_two[1] == "Х",
               line_two[2] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_three[0] == "Х",
               line_three[1] == "Х",
               line_three[2] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_one[0] == "Х",
               line_two[0] == "Х",
               line_three[0] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_one[1] == "Х",
               line_two[1] == "Х",
               line_three[1] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_one[2] == "Х",
               line_two[2] == "Х",
               line_three[2] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_one[0] == "Х",
               line_two[1] == "Х",
               line_three[2] == "Х"]):
           print("Победил Х")
           return 1
        if all([line_one[2] == "Х",
               line_two[1] == "Х",
               line_three[0] == "Х"]):
           print("Победил Х")
           return 1



        if all([line_one[0] == "О",
               line_one[1] == "О",
               line_one[2] == "О"]):
           print("Победил О")
           return 1
        if all([line_two[0] == "О",
               line_two[1] == "О",
               line_two[2] == "О"]):
           print("Победил О")
           return 1
        if all([line_three[0] == "О",
               line_three[1] == "О",
               line_three[2] == "О"]):
           print("Победил О")
           return 1
        if all([line_one[0] == "О",
               line_two[0] == "О",
               line_three[0] == "О"]):
           print("Победил О")
           return 1
        if all([line_one[1] == "О",
               line_two[1] == "О",
               line_three[1] == "О"]):
           print("Победил О")
           return 1
        if all([line_one[2] == "О",
               line_two[2] == "О",
               line_three[2] == "О"]):
           print("Победил О")
           return 1
        if all([line_one[0] == "О",
               line_two[1] == "О",
               line_three[2] == "О"]):
           print("Победил О")
           return 1
        if all([line_one[2] == "О",
               line_two[1] == "О",
               line_three[0] == "О"]):
           print("Победил О")
           return 1

    while True:
        line = int(input("Первый игрок выберите линию (1, 2, 3): "))
        column = int(input("Первый игрок выберите столбец (1, 2, 3): "))
        column -= 1

        if line == 1:
            if line_one[column] != "Х" and line_one[column] != "О":
                line_one[column] = figure1
                break
            else:
                print(f"Здесь уже есть {line_one[column]}")
                continue
        elif line == 2:
            if line_two[column] != "Х" and line_two[column] != "О":
                line_two[column] = figure1
                break
            else:
                print(f"Здесь уже есть {line_two[column]}")
                continue
        else:
            if line_three[column] != "Х" and line_three[column] != "О":
                line_three[column] = figure1
                break
            else:
                print(f"Здесь уже есть {line_three[column]}")
                continue

    zone()

    if victory() == 1:
        break

    while True:
        line = int(input("Второй игрок выберите линию (1, 2, 3): "))
        column = int(input("Второй игрок выберите столбец (1, 2, 3): "))
        column -= 1

        if line == 1:
            if line_one[column] != "Х" and line_one[column] != "О":
                line_one[column] = figure2
                break
            else:
                print(f"Здесь уже есть {line_one[column]}")
                continue
        elif line == 2:
            if line_two[column] != "Х" and line_two[column] != "О":
                line_two[column] = figure2
                break
            else:
                print(f"Здесь уже есть {line_two[column]}")
                continue
        else:
            if line_three[column] != "Х" and line_three[column] != "О":
                line_three[column] = figure2
                break
            else:
                print(f"Здесь уже есть {line_three[column]}")
                continue

    zone()

    if victory() == 1:
        break