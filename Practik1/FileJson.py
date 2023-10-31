import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

def create_json_file(filename, data):
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
            print(f"Данные успешно записаны в файл '{filename}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")

def read_json_file(filename):
    try:
        with open(filename, 'r') as json_file:
            loaded_data = json.load(json_file)
            print("Содержимое файла JSON:")
            print(loaded_data)
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")

def delete_file(filename):
    try:
        import os
        os.remove(filename)
        print(f"Файл '{filename}' удален.")
    except FileNotFoundError as e:
        print(f"Ошибка при удалении файла: {e}")


json_file_name = "data.json"
create_json_file(json_file_name, data)
read_json_file(json_file_name)
delete_file(json_file_name)
