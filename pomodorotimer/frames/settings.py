import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self['style'] = 'Background.TFrame'

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(self, padding="30 15 30 15", style='Background.TFrame')
        settings_container.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        pomodoro_label = ttk.Label(settings_container, text="Pomodoro", style='LightText.TLabel')
        pomodoro_label.grid(column=0, row=0, sticky='w')
        pomodoro_input = ttk.Spinbox(settings_container, from_=0, to=120, increment=1, justify='center', textvariable=controller.pomodoro, width=10)
        pomodoro_input.grid(column=1, row=0, sticky='ew')
        pomodoro_input.focus()

        short_break_label = ttk.Label(settings_container, text="Short Break", style='LightText.TLabel')
        short_break_label.grid(column=0, row=2, sticky='w')
        short_break_label = ttk.Spinbox(settings_container, from_=0, to=30, increment=1, justify='center', textvariable=controller.short_break, width=10)
        short_break_label.grid(column=1, row=2, sticky='ew')

        long_break_label = ttk.Label(settings_container, text="Long Break", style='LightText.TLabel')
        long_break_label.grid(column=0, row=1, sticky='w')
        long_break_label = ttk.Spinbox(settings_container, from_=0, to=60, increment=1, justify='center', textvariable=controller.long_break, width=10)
        long_break_label.grid(column=1, row=1, sticky='ew')

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style='Background.TFrame')
        button_container.grid(sticky='ew', pady=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(button_container, text='<- Back', command=show_settings, cursor="hand2", style='PomodoroButton.TButton')
        timer_button.grid(row=0, column=0, sticky='ew', padx=2)