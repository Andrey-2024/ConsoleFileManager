import os
import shutil
import platform

def display_menu():
    print("\nКонсольный файловый менеджер")
    print("1. Создать папку")
    print("2. Удалить (файл/папку)")
    print("3. Копировать (файл/папку)")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Посмотреть только папки")
    print("6. Посмотреть только файлы")
    print("7. Просмотр информации об операционной системе")
    print("8. Создатель программы")
    print("9. Играть в викторину")
    print("10. Мой банковский счет")
    print("11. Смена рабочей директории")
    print("12. Выход")


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' успешно создана.")
    except FileExistsError:
        print("Папка с таким именем уже существует.")
    except Exception as e:
        print(f"Ошибка: {e}")

def delete_file_or_folder(name):
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален.")
    else:
        print("Файл или папка не найдены.")

def copy_file_or_folder(source, destination):
    if os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Папка '{source}' скопирована в '{destination}'.")
    elif os.path.isfile(source):
        shutil.copy(source, destination)
        print(f"Файл '{source}' скопирован в '{destination}'.")
    else:
        print("Файл или папка не найдены.")

def list_directory_contents():
    items = os.listdir()
    for item in items:
        print(item)

def list_only_folders():
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    for folder in folders:
        print(folder)

def list_only_files():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    for file in files:
        print(file)

def display_os_info():
    print("Информация об операционной системе:")
    print(platform.platform())

def display_creator_info():
    print("Создатель программы: Ваше Имя")

# Добавьте функции для игры в викторину и банковского счета из предыдущих дз

while True:
    display_menu()
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        folder_name = input("Введите название папки: ")
        create_folder(folder_name)
    elif choice == '2':
        name = input("Введите название файла или папки для удаления: ")
        delete_file_or_folder(name)
    elif choice == '3':
        source = input("Введите название файла/папки для копирования: ")
        destination = input("Введите новое название файла/папки: ")
        copy_file_or_folder(source, destination)
    elif choice == '4':
        list_directory_contents()
    elif choice == '5':
        list_only_folders()
    elif choice == '6':
        list_only_files()
    elif choice == '7':
        display_os_info()
    elif choice == '8':
        display_creator_info()
    elif choice == '12':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
