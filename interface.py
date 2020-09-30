import tkinter as tk


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title('Random Numbers')
        self.master.geometry('400x300')
        self.master.configure(background='#BFBFBF')
        self.master.resizable(False, False)

        self.color_grey = '#BFBFBF'

        self.frame_master = tk.Frame(self.master, bg=self.color_grey)
        self.frame_master.pack()

        label_title = tk.Label(self.frame_master, text='Random Numbers', bg=self.color_grey,
                               font=('Roboto', 16, 'bold'))
        label_title.pack(pady=10)

        frame_line1 = tk.Frame(self.frame_master, bg=self.color_grey)
        frame_line1.pack(anchor='w')

        label_qtd = tk.Label(frame_line1, text='Quantidade:', bg=self.color_grey, font=('Roboto', 12))
        label_qtd.pack(side='left')

        entry_qdt = tk.Entry(frame_line1, relief='solid', bd=1, width=4, font=('Roboto', 12))
        entry_qdt.pack(side='left')

        frame_line2 = tk.Frame(self.frame_master, bg=self.color_grey)
        frame_line2.pack(pady=10, anchor='w')

        label_num = tk.Label(frame_line2, text='Números entre:', bg=self.color_grey, font=('Roboto', 12))
        label_num.pack(side='left')

        entry_num1 = tk.Entry(frame_line2, relief='solid', bd=1, width=4, font=('Roboto', 12))
        entry_num1.pack(side='left')

        label_e = tk.Label(frame_line2, text='e', bg=self.color_grey, font=('Roboto', 12))
        label_e.pack(side='left')

        entry_num2 = tk.Entry(frame_line2, relief='solid', bd=1, width=4, font=('Roboto', 12))
        entry_num2.pack(side='left')

        message = tk.Message(self.frame_master, width=50, font=('Roboto', 12))
        message.pack()


app = tk.Tk()
Interface(app)
app.mainloop()
