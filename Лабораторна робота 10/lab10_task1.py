import random
import os

if not os.path.exists("numbers.txt"):
    print("Помилка: файл numbers.txt не знайдено")
else:
    f = open("numbers.txt", "r")
    out = open("full_numbers.txt", "w")

    for line in f:
        line = line.strip()
        if line != "":
            num = random.randint(1000, 9999)
            out.write(line + " " + str(num) + "\n")

    f.close()
    out.close()
    print("Файл full_numbers.txt успішно створено")