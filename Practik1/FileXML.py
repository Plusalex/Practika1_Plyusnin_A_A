import xml.etree.ElementTree as ET

def create_xml_file(file_name):
    try:
        root = ET.Element("root")
        data = input("Введите данные для записи в XML: ")
        element = ET.SubElement(root, "data")
        element.text = data
        tree = ET.ElementTree(root)
        tree.write(file_name)
        print(f"Данные успешно записаны в файл '{file_name}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")

def read_xml_file(file_name):
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
        for element in root:
            print(f"{element.tag}: {element.text}")
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")

def delete_file(file_name):
    try:
        import os
        os.remove(file_name)
        print(f"Файл '{file_name}' удален.")
    except FileNotFoundError as e:
        print(f"Ошибка при удалении файла: {e}")


xml_file_name = "data.xml"
create_xml_file(xml_file_name)
read_xml_file(xml_file_name)
delete_file(xml_file_name)
