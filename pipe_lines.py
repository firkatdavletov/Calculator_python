import tkinter as tk
from tkinter import ttk
from main import Application

class PipeLine(tk.Frame, Application):
    def __init__(self):
        self.grid()
        self.add_pipLines()

    def add_pipLines(self):
        self.title2 = tk.Label(self.tab2, text='Отдельные трубопроводы')

