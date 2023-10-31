import zipfile
import os

def create_zip_archive(zip_file_name):
    try:
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            print(f"ZIP-архив '{zip_file_name}' успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании ZIP-архива: {e}")

def add_file_to_zip(zip_file_name, file_name):
    try:
        with zipfile.ZipFile(zip_file_name, 'a', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_name, os.path.basename(file_name))
            print(f"Файл '{file_name}' успешно добавлен в ZIP-архив '{zip_file_name}'.")
    except Exception as e:
        print(f"Ошибка при добавлении файла в ZIP-архив: {e}")

def get_zip_archive_size(zip_file_name):
    try:
        archive_size = os.path.getsize(zip_file_name)
        print(f"Размер ZIP-архива '{zip_file_name}': {archive_size} байт")
    except Exception as e:
        print(f"Ошибка при определении размера ZIP-архива: {e}")

def extract_file_from_zip(zip_file_name, extracted_file_name):
    try:
        with zipfile.ZipFile(zip_file_name, 'r') as zipf:
            zipf.extract(extracted_file_name)
            with open(extracted_file_name, 'r') as file:
                content = file.read()
                print(f"Разархивированный файл '{extracted_file_name}' содержит следующее:")
                print(content)
    except Exception as e:
        print(f"Ошибка при разархивировании и чтении файла: {e}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' удален.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")


zip_file_name = "example.zip"
file_to_archive = "file_to_archive.txt"

create_zip_archive(zip_file_name)

user_input = input("Введите данные для записи в файл для архивирования: ")
with open(file_to_archive, 'w') as file:
    file.write(user_input)

add_file_to_zip(zip_file_name, file_to_archive)

get_zip_archive_size(zip_file_name)

extracted_file = "extracted_file.txt"
extract_file_from_zip(zip_file_name, extracted_file)

delete_file(file_to_archive)
delete_file(extracted_file)
delete_file(zip_file_name)
