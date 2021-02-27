from tkinter import Tk, Canvas, Frame, BOTH, W


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Текст и Шрифт в Tkinter")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        for i in range(0, 50):
            if i%2 == 0:
                canvas.create_text(
                    20, 30, anchor=W, font="10", fill='red',
                    text="Красное солнце сгорает дотла"
                )
            else:
                canvas.create_text(
                    20, 60, anchor=W, font="10", fill='blue',
                    text="На пылающий город падает тень"
                )

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("420x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
