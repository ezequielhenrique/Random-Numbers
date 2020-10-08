import tkinter as tk
from tkinter import ttk, messagebox
from scripts import is_integer, generate_numbers
import os


def resource_path(relative_path):
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


images_dir = resource_path('images')


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title('Random Numbers')
        self.master.geometry('500x400')
        self.master.iconbitmap(images_dir+'/icongenerate.ico')
        self.master.configure(background='#BFBFBF')
        self.master.resizable(False, False)

        self.color_grey = '#BFBFBF'

        self.frame_master = tk.Frame(self.master, bg=self.color_grey)
        self.frame_master.pack()

        label_title = tk.Label(self.frame_master, text='Random Numbers', bg=self.color_grey,
                               font=('Roboto', 16, 'bold'))
        label_title.pack(pady=15)

        frame_line1 = tk.Frame(self.frame_master, bg=self.color_grey)
        frame_line1.pack(anchor='w')

        label_qtd = tk.Label(frame_line1, text='Quantidade:', bg=self.color_grey, font=('Roboto', 12))
        label_qtd.pack(side='left')

        self.entry_qdt = tk.Entry(frame_line1, relief='solid', bd=1, width=4, font=('Roboto', 12))
        self.entry_qdt.pack(side='left')

        frame_line2 = tk.Frame(self.frame_master, bg=self.color_grey)
        frame_line2.pack(pady=10, anchor='w')

        label_num = tk.Label(frame_line2, text='Números entre:', bg=self.color_grey, font=('Roboto', 12))
        label_num.pack(side='left')

        self.entry_num1 = tk.Entry(frame_line2, relief='solid', bd=1, width=4, font=('Roboto', 12))
        self.entry_num1.pack(side='left')

        label_e = tk.Label(frame_line2, text='e', bg=self.color_grey, font=('Roboto', 12))
        label_e.pack(side='left')

        self.entry_num2 = tk.Entry(frame_line2, relief='solid', bd=1, width=4, font=('Roboto', 12))
        self.entry_num2.pack(side='left')

        button_generate = tk.Button(self.frame_master, text='Gerar', relief='solid', bd=1, bg='black',
                                    fg=self.color_grey, font=('Roboto', 12, 'bold'), padx=10, command=self.get_values)
        button_generate.pack(pady=5)

        frame_text = tk.Frame(self.frame_master, bg=self.color_grey)
        frame_text.pack(pady=10)

        self.display_text = tk.Text(self.frame_master, width=50, height=10, font=('Roboto', 12), wrap='word')
        self.display_text.pack(side='left')

        scroll = ttk.Scrollbar(self.frame_master, orient='vertical', command=self.display_text.yview)
        scroll.pack(side='left', fill='y')

        self.display_text.configure(yscrollcommand=scroll.set)

    def get_values(self):
        num_numbers = self.entry_qdt.get()
        from_number = self.entry_num1.get()
        to_number = self.entry_num2.get()

        if is_integer(num_numbers) and is_integer(from_number) and is_integer(to_number):
            num_numbers = int(num_numbers)
            from_number = int(from_number)
            to_number = int(to_number)
            if num_numbers > to_number-from_number:
                messagebox.showerror('Error', 'Intervalo numérico errado')
            else:
                try:
                    numbers = generate_numbers(num_numbers, from_number, to_number)
                    self.display_text.delete(1.0, 'end')

                    text = ''
                    for n in numbers:
                        text += f'{str(n)} - '
                    text += 'Fim'

                    self.display_text.insert(tk.INSERT, text)
                except ValueError:
                    messagebox.showerror('Error', 'ValueError: Intervalo vazio')
        else:
            messagebox.showerror('Error', 'Só são aceitos números inteiros!')
            self.entry_qdt.delete(0, 'end')
            self.entry_num1.delete(0, 'end')
            self.entry_num2.delete(0, 'end')


app = tk.Tk()
Interface(app)
app.mainloop()
