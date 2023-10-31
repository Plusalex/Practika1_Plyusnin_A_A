import os
def create_file(file_name):
    try:
        with open(file_name, 'w'):
            print(f"Файл '{file_name}' создан.")
    except IOError as e:
        print(f"Ошибка при создании файла: {e}")


def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print("Содержимое успешно записано в файл.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("Содержимое файла:")
            print(file_content)
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' удален.")
    except FileNotFoundError as e:
        print(f"Ошибка при удалении файла: {e}")


file_name = "example.txt"

create_file(file_name)

user_input = input("Введите строку для записи в файл: ")
write_to_file(file_name, user_input)

read_file(file_name)

delete_file(file_name)
