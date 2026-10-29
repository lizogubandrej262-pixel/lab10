import os

folder = "TEXT"

if not os.path.exists(folder):
    print("Помилка: каталог TEXT не знайдено")
else:
    full_path = os.getcwd() + "\\" + folder
    print("Повний шлях до каталогу:", full_path)

    files = os.listdir(folder)

    doc_list = []
    docx_list = []
    txt_list = []

    for name in files:
        if name.endswith(".docx"):
            docx_list.append(name)
        elif name.endswith(".doc"):
            doc_list.append(name)
        elif name.endswith(".txt"):
            txt_list.append(name)

    f = open("my_files.txt", "w")

    f.write("Файли з розширенням .doc:\n")
    for name in doc_list:
        f.write(name + "\n")

    f.write("\nФайли з розширенням .docx:\n")
    for name in docx_list:
        f.write(name + "\n")

    f.write("\nФайли з розширенням .txt:\n")
    for name in txt_list:
        f.write(name + "\n")

    f.close()
    print("Файл my_files.txt успішно створено")