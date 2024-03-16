from tkinter import *
import tkinter.font as font
from tkinter import ttk


class View(Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 800
        self.__height = 200

        self.default_font = font.Font(family='Verdana', size=12)
        self.box_font = font.Font(family='Courier', size=12)

        self.title('Otsija')
        self.center_window(self.__width, self.__height)

        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.btn_open, self.search, self.btn_search, self.lbl_name, self.lbl_nr,
         ) = self.create_frame_widgets()

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='light grey', height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='light grey')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        btn_open = Button(self.top_frame, text='Ava fail', font=self.default_font,
                          command=self.controller.open_file)
        btn_open.grid(row=0, column=0, padx=0, pady=5, sticky='ew')

        lbl_info = Label(self.top_frame, text='                avatud faili nimi:', bg='light grey',
                         font=self.default_font)
        lbl_info.grid(row=0, column=1, padx=5, pady=5)

        lbl_name = Label(self.top_frame, text='', bg='light grey', font=self.default_font)
        lbl_name.grid(row=0, column=2, padx=5, pady=5)

        lbl_search = Label(self.top_frame, text='Otsitav sõna:', bg='light grey', font=self.default_font)
        lbl_search.grid(row=1, column=0, padx=5, pady=5)

        search = Entry(self.top_frame, font=self.default_font, state=DISABLED)
        search.grid(row=1, column=1, padx=5, pady=5)

        btn_search = Button(self.top_frame, text='Otsi', font=self.default_font, state=DISABLED,
                            command=self.controller.search_click)
        btn_search.grid(row=1, column=2, padx=0, pady=5, sticky='ew')

        lbl_row = Label(self.top_frame, text='leitud ridu:', bg='light grey', font=self.default_font)
        lbl_row.grid(row=2, column=0, padx=5, pady=5)

        lbl_nr = Label(self.top_frame, text='', bg='light grey', font=self.default_font)
        lbl_nr.grid(row=2, column=1, padx=5, pady=5)

        return btn_open, search, btn_search, lbl_name, lbl_nr

    def draw_search_result(self, header, data):
        if len(data) > 0:
            for widget in self.bottom_frame.winfo_children():
                widget.destroy()

            table = ttk.Treeview(self.bottom_frame)
            vsb = ttk.Scrollbar(self.bottom_frame, orient=VERTICAL, command=table.yview)
            vsb.pack(side=RIGHT, fill=Y)
            table.configure(yscrollcommand=vsb.set)

            table.heading('#0', text='Nr', anchor=CENTER)
            table.column('#0', anchor=CENTER, width=2)

            column_ids = [h.lower() for h in header]
            table['columns'] = column_ids
            for i, h in enumerate(header):
                table.heading(f'{h.lower()}', text=h, anchor=CENTER)
                table.column(f'{h.lower()}', anchor=CENTER, width=50)

            for i, row in enumerate(data):
                table.insert('', 'end', text=i + 1, values=row)

            table.pack(expand=True, fill=BOTH)
