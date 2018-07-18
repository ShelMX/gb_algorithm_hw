__author__ = 'Шелест Леонид Викторович'
"""
В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число. 
Если за 10 попыток число не отгадано, то вывести его.
"""

from random import randint as r


def main():
    while True:
        play = input("\nПредлагаю сыграть в угадай число!"
                     "\nЕсли согласен, то введи + ")
        if play == '+':
            print("Загадано число от 1 до 100")
            check = r(1, 100)
            step = 1
            answers = set(())
            for _ in range(10):
                answer = int(input(f"Шаг {step}. Введи число "))
                step += 1
                if answer == check:
                    print(f"Ты потратил {step} попыток и угадал число {check}.")
                    break
                else:
                    message = f"Загаданное число {'меньше' if check < answer else 'больше'} {answer}\n"
                    check_fool = len(answers)
                    answers.add(answer)
                    if check_fool == len(answers):
                        message += "ты что совсем дурак дважды одно число вводить?"
                    print(message)
            else:
                print(f"Ты потратил 10 попыток и не угадал число {check}.")
        else:
            break


if __name__ == '__main__':
    main()