# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def convert_to_cm(system,unit,number):
    if system == 'american':
        if unit == 'inch':
            result=round(number*2.54,2)
        if unit == 'foot':
            result=round(number*30.48,2)
        if unit == 'mi':
            result=round(number*160934.4,2)
    if system == 'oldrussian':
        if unit=='Elbow':
            result = round(number * 59.37777777777941, 2)
        if unit=='span':
            result = round(number * 17.78, 2)
        if unit=='fathom':
            result = round(number * 213.36, 2)
    return result

def convert_from_cm(system, unit, number):
    if system == 'american':
        if unit == 'hand':
            result = round(number / 10.16, 2)
        elif unit == 'yard':
            result = round(number / 91.44, 2)
        elif unit == 'rod':
            result = round(number / 502.92, 2)
    
    if system == 'oldrussian':
        if unit == 'verst':
            result = round(number / 106680, 2)
        elif unit == 'arshin':
            result = round(number / 71.12, 2)
        elif unit == 'vershok':
            result = round(number / 4.445, 2)


    return result

while True:
    print("-----------------Меню-----------------")
    print("[1] - Преобразовать из американского в старорусский")
    print("[2] - Преобразовать из американского в сантиметр")
    print("[3] - Преобразовать из старорусского в американский")
    print("[4] - Преобразовать из старорусского в сантиметр")

    choose = int(input("Введите ваш выбор: "))
    print("--------------------------------------\n")\
        
    if choose == 1:
        print("Выбрать исходную систему: ")
        print("\t[1] - Inch")
        print("\t[2] - Foot")
        print("\t[3] - Mi")
        source_system = int(input("Ваш выбор: "))
        if source_system == 1:
            source_system = "inch"
        elif source_system == 2:
            source_system = "foot"
        elif source_system == 3:
            source_system = "mi"
        print("Выбрать целевую систему: ")
        print("\t[1] - Verst")
        print("\t[2] - Arshin")
        print("\t[3] - Vershok")
        target_system = int(input("Ваш выбор: "))
        if target_system == 1:
            target_system = 'verst'
        elif target_system == 2:
            target_system = 'arshin'
        elif target_system == 3:
            target_system = 'vershok'
        
        num = int(input("Введите число, которое вы хотите преобразовать: "))
        print("Результат: " + str(convert_from_cm('oldrussian', target_system, convert_to_cm('american', source_system, num))))

    elif choose == 2:
        print("Выбрать исходную систему: ")
        print("\t[1] - Inch")
        print("\t[2] - Foot")
        print("\t[3] - Mi")
        source_system = int(input("Ваш выбор: "))
        if source_system == 1:
            source_system = "inch"
        elif source_system == 2:
            source_system = "foot"
        elif source_system == 3:
            source_system = "mi"
        num = int(input("Введите число, которое вы хотите преобразовать: "))
        print("Результат: " + str(convert_to_cm('american', source_system, num)))

    elif choose == 3:
        print("Выбрать исходную систему: ")
        print("\t[1] - Локоть")
        print("\t[2] - Пядь")
        print("\t[3] - Вникать")
        source_system = int(input("Ваш выбор: "))
        if source_system == 1:
            source_system = "Elbow"
        elif source_system == 2:
            source_system = "span"
        elif source_system == 3:
            source_system = "fathom"
        print("Выбрать целевую систему: ")
        print("\t[1] - Hand")
        print("\t[2] - Yard")
        print("\t[3] - Rod")
        target_system = int(input("Ваш выбор: "))
        if target_system == 1:
            target_system = 'hand'
        elif target_system == 2:
            target_system = 'yard'
        elif target_system == 3:
            target_system = 'rod'
        
        num = int(input("Введите число, которое вы хотите преобразовать: "))
        print("Результат: " + str(convert_from_cm('american', target_system, convert_to_cm('oldrussian', source_system, num))))
    elif choose == 4:
        print("Выбрать исходную систему: ")
        print("\t[1] - Локоть")
        print("\t[2] - Пядь")
        print("\t[3] - Вникать")
        source_system = int(input("Ваш выбор: "))
        num = int(input("Введите число, которое вы хотите преобразовать: "))
        print("Результат: " + str(convert_to_cm('oldrussian', source_system, num)))