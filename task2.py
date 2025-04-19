import turtle

def koch_curve(t, order, size):
   
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def draw_koch_snowflake(order, size=300):

    screen = turtle.Screen()
    screen.bgcolor("#f0f8ff")
    screen.title("Сніжинка Коха")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

def main():
    print("❄️ Побудова сніжинки Коха ❄️")

    while True:
        try:
            order = int(input("Введіть рівень рекурсії (не менше 0): "))
            if order >= 0:
                break
            print("Рівень має бути 0 або більше.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    while True:
        try:
            size = int(input("Введіть розмір сніжинки (пікселі): "))
            if size > 0:
                break
            print("Розмір має бути більше нуля.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    draw_koch_snowflake(order, size)

if __name__ == "__main__":
    main()
