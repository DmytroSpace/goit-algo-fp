import turtle
import colorama
from colorama import Fore, Style

colorama.init()

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)                                    # Малюємо основну гілку

    t.left(45)                                                  # Рекурсивно малюємо ліву гілку
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)

    t.right(90)                                                 # Повертаємось до основної лінії
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)

    t.left(45)                                                  # Відновлюємо початкову позицію
    t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)                                                  # Початковий напрямок черепахи (вверх)

    
    try:                                                        # Запит у користувача на введення рівня рекурсії через термінал
        level = int(input("Введіть рівень рекурсії (дійсне число, більше за 0): "))
    except ValueError:
        print(Fore.RED + "Будь ласка, введіть дійсне число." + Style.RESET_ALL)
        turtle.bye()
        return

    if level < 0:
        print(Fore.RED + "Рівень рекурсії не може бути від'ємним." + Style.RESET_ALL)
        turtle.bye()
        return

    branch_length = 80                                          # Довжина початкової гілки

    t.penup()
    t.goto(0, -200)                                             # Переміщуємо початкову позицію до низу екрана
    t.pendown()

    draw_pythagoras_tree(t, branch_length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
