# -*- coding: utf-8 -*-
from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    var = int(input(f"В каком формате записать данные?\n"
                    f"1 вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n"
                    f"2 вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Введен неподдерживаемый вариант! \n Попробуйте еще раз.")
        var = int(input("выберите вариант: "))
        
    if var == 1:
        with open('data_first_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def edit_data():
    # TODO: передать в ф-цию искомый заменяемый параметр
    # и вариант файла для редакирования
    var = int(input(f"В каком файле заменить данные?\n"
                    f"1. файл записи в столбик?\n"
                    f"2. файл записи в строку?\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Введен неподдерживаемый вариант! \n Попробуйте еще раз.")
        var = int(input("выберите вариант: "))
    
    if var == 1:
        with open('data_first_var.csv', 'r', encoding='utf-8') as f:
            lines_1 = f.read()
    elif var == 2:
        with open('data_second_var.csv', 'r', encoding='utf-8') as f:
            lines_2 = f.read()
            
    var_change = int(input(f"Выберите данные для изменения?\n"
                            f"1. фамилия\n"
                            f"2. имя\n"
                            f"Выберите вариант: "))
    if var_change == 1:
        find_surname = input("Введите фамилию которую нужно заменить: ")
        change_surname = input("Введите измененную фамилию: ")
        if var == 1:
            pos = lines_1.find(find_surname)
            lines_1 = lines_1[:pos] + change_surname + lines_1[pos+len(change_surname):]
            with open('data_first_var.csv', 'w', encoding='utf-8') as f:
                f.write(lines_1)
            
        elif var == 2:
            pos = lines_2.find(find_surname)
            lines_2 = lines_2[:pos] + change_surname + ';' + lines_1[pos+len(change_surname):]
            with open('data_second_var.csv', 'w', encoding='utf-8') as f:
                f.write(lines_2)
            with open('data_second_var.csv', 'w', encoding='utf-8') as f:
                f.write(lines_2)
    
    elif var_change == 2:
        find_name = input("Введите имя которое нужно заменить: ")
        change_name = input("Введите измененное имя: ")
        if var == 1:
            pos = lines_1.find(find_name)
            lines_1 = lines_1[:pos] + change_name + lines_1[pos+len(change_name):]
            with open('data_first_var.csv', 'w', encoding='utf-8') as f:
                f.write(lines_1)
        elif var == 2:
            pos = lines_2.find(find_name)
            lines_2 = lines_2[:pos] + change_name + ';' + lines_2[pos+len(change_name):]
            with open('data_second_var.csv', 'w', encoding='utf-8') as f:
                f.write(lines_2)

def output_data():
    print("Вывод данных из первого файла: \n")
    with open('data_first_var.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
        
    print("Вывод данных из второго файла: \n")
    with open('data_second_var.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second) 
        

def remove_data():
    var = int(input(f"В каком файле удалить данные?\n"
                    f"1. файл записи в столбик?\n"
                    f"2. файл записи в строку?\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Введен неподдерживаемый вариант! \n Попробуйте еще раз.")
        var = int(input("выберите вариант: "))
    
    if var == 1:
        with open('data_first_var.csv', 'r', encoding='utf-8') as f:
            del_str_1 = f.read()
    elif var == 2:
        with open('data_second_var.csv', 'r', encoding='utf-8') as f:
            del_str_2 = f.read()
            
    del_name = input(f"Введите имя для удаления: ")
    
    if var == 1:
        pos = del_str_1.find(del_name)
        pos_next = del_str_1[pos:].find('\n\n') 
        del_str_1 = del_str_1[:pos] + del_str_1[pos_next+2:]
        with open('data_first_var.csv', 'w', encoding='utf-8') as f:
            f.write(del_str_1)
            
    elif var == 2:
        pos = del_str_2.find(del_name)
        pos_next = del_str_2[pos:].find(';\n')
        del_str_2 = del_str_2[:pos] + del_str_2[pos_next+2:]
        with open('data_second_var.csv', 'w', encoding='utf-8') as f:
            f.write(del_str_2)