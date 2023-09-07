# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess


def call_command(command, text):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return text in output
    except (subprocess.CalledProcessError, FileExistsError):
        return False

"""
Функция перехватывает вывод входящей функции BASH.
"""
if __name__ == '__main__':
    # command = subprocess.call('/home/user/text1.sh')
    text = "SUCCESS"
    print(call_command('/home/user/text1.sh', text))
