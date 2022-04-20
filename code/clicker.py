from tkinter import *
from random import randint
from tkinter import messagebox


def clicker_dmitry():
    global counter, count, tt
    counter = 0
    count = 0

    def check(c):
        if c < 15:
            button["text"] = "НАжМи СюдА хыххыы :)"
            button["bg"] = "#f7f7f7"
            button["width"] = 20
            button["height"] = 1
        if 15 <= c < 30:
            button["text"] = "Попади, если сможешь"
            button["bg"] = "#41990b"
            button["width"] = 30
            button["height"] = 12

        if 30 <= c < 50:
            button["text"] = "Ха"
            button["bg"] = "#4543b5"
            button["width"] = 2
            button["height"] = 1

        if 50 <= c < 75:
            button["text"] = "У тебя есть терпение"
            button["bg"] = "#ff2950"
            button["width"] = 20

        if 75 <= c < 100:
            button["text"] = ":("
            button["bg"] = "#4543b5"
            button["width"] = 1
            button["height"] = 1

        if c >= 100:
            button["text"] = "Наслаждайся"
            button["bg"] = "#66ff99"
            button["width"] = 20
            button_clear["text"] = "Нажми, чтобы очистить"
            button_quit["text"] = "Давай выходи"


    def click():
        global counter
        counter += 1
        button.place(x=randint(50, 860), y=randint(10, 600))
        paint_counter["text"] = str(counter)
        paint_counter.pack()

        check(counter)

    def clear():
        global counter
        counter = 0
        paint_counter["text"] = str(counter)

        check(counter)

    def quit():
        window.destroy()

    def troll():
        global counter, count
        counter -= 20
        paint_counter["text"] = str(counter)
        check(counter)
        if count == 0:
            messagebox.showerror("ЫВХФФХВФВФЦХ", "Ты реально хотел 100 очков?????")
        count += 1
        if count == 1:
            button_troll["text"] = "Давай прибавим 200 очков"
        elif count == 2:
            button_troll["text"] = "Давай прибавим 300 очков"
            messagebox.showerror("ХВААХВХВАХВАХАХ", "АХУФЫХАУХФЫАФХУЫАУХХАХЫАХФУЫАФУЫХ")
        elif count == 3:
            button_troll["text"] = "Давай прибавим 400 очков"
            messagebox.showerror("ДА..даа....", "До сих пор веришь мне?")
        elif count == 4:
            button_troll["text"] = "Награда за тест"
            messagebox.showerror("^_^", "Держи подарок")
            counter += 200
        else:
            button_troll.destroy()

    window = Tk()

    window["bg"] = "#f7f7f7"
    window.title("Мой clicker ^_^")
    window.geometry("1000x690+150+5")
    window.resizable(width=False, height=False)

    paint_counter = Label(window, text='Давай начнем', bg="#f7f7f7", font='Calibri 30')
    paint_counter.pack(side=TOP)

    button = Button(window, text="НАжМи СюдА хыххыы :)", width=20, command=click)
    button.place(x=randint(50, 200), y=randint(10, 200))

    button_clear = Button(window, text="Давай очистим", width=25, height=2, command=clear)
    button_clear.place(x=20, y=640)

    button_troll = Button(window, text="Давай прибавим 100 очков", width=25, height=2, command=troll)
    button_troll.place(x=400, y=640)

    button_quit = Button(window, text="Пойдем выйдем", width=25, height=2, command=quit)
    button_quit.place(x=800, y=640)

    window.mainloop()


def main():
    clicker_dmitry()


if __name__ == "__main__":
    main()
