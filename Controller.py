import os
from tkinter import filedialog
import tkinter as tk
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.view.search.bind("<Return>", lambda event: self.search_click())

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            filename = os.path.basename(file_path)
            self.model.read_file(file_path)
            self.view.btn_search['state'] = 'normal'
            self.view.search['state'] = 'normal'
            self.view.lbl_name['text'] = filename
            self.view.search.focus_set()
            self.view.lbl_nr['text'] = ''
        for widget in self.view.bottom_frame.winfo_children():
            widget.destroy()

    def search_click(self):
        result = self.view.search.get()
        results = self.model.search(result)
        header = self.model.header

        if results:
            self.view.draw_search_result(header, results)
            count = len(results)
            self.view.lbl_nr['text'] = count
        else:
            self.view.draw_search_result([], [])
            self.view.lbl_nr['text'] = "0"

        self.view.search.delete(0, tk.END)
