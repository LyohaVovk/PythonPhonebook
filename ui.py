# -*- coding: utf-8 -*-
from logger import input_data, edit_data, output_data, remove_data

def interface():
    print("Доброго дня! Вас приветствует бот-справочник от GeekBrains!")
    print("1. - запись данных;\n2. - редактирование данных;\n3. - вывод данных;\n4. - удаление данных;\n5. - выход.")
    command = int(input("Введите команду: "))
    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5:
        print("Введена неподдерживаемая команда! \n Попробуйте еще раз.")
        command = int(input("Введите команду: "))
     
    if command == 1:
        input_data()
    elif command == 2:
        edit_data()
    elif command == 3:
        output_data()
    elif command == 4:
        remove_data()
    elif command == 5:
        pass
        
# interface()