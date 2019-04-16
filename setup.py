#!/usr/bin/python3

from sys import argv

# chmod +x main.py
# ./main.py file.jpg

def read_byte():
    try:
        nameFile = argv[1]
    except IndexError:
        print("Error: arguments");
        raise SystemExit

    try:
        with open(nameFile, "rb") as file:
            byte = file.read(1)
            counter = 0
            while byte:
                print(byte)
                byte = file.read(1)
                counter += 1
    except FileNotFoundError:
        print("[x] File: '{name}' is not defined!".format(name=nameFile))
    else:
        print("Number of bytes in the '{name}': {number}".format(name=nameFile, number=counter))


def write_byte():
    try:
        nameFile = argv[1]
        textFile = argv[2:]
    except IndexError:
        print("Error: Arguments!");
        raise SystemExit

    with open(nameFile, 'ab') as file:
        file.write("".join(textFile).encode("utf-8"))
        print("[+] File successfully overwritten!")

# запуск программы осуществляется путем запуска файла setup.py с передачей требуемых параметров
# ./setup.py file.jpg - для считывания
# для записи добавляем 2й аргумент
def main():
    # считываем байты входного изображения
    print('Выберите требуемую операцию: ')
    inp = input("1 - read | !1 - write\n")
    if inp == '1':
        read_byte()
        print('количество байтов исходного изображения: ')
    else:
        # интегрируем в изображение требуемый код
        write_byte()
        # количествво байтов измененного изображения
        print('count byte')
        print('результирующий код изо')

main()