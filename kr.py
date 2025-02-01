import tkinter as tk

def procentminus():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1 - (value2 / 100 * value2)
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)


def multiplication():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter=value2*value1
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)


def division():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1 / value2
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)

def summa():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value2 + value1
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)


def minus():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1-value2
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)


def procentsumma():
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1+(value2/100*value2)
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)

window = tk.Tk()# Создаем главное окно
entry1 = tk.Entry(window, width=10)# Создаем два поля ввода
entry1.grid(column=1, row=0)
entry2 = tk.Entry(window, width=10)# Создаем два поля ввода
entry2.grid(column=1, row=1)

btn = tk.Button(window, text="*", command=multiplication)# Создаем кнопку для получения значений
btn.grid(column=1, row=2)# Создаем кнопку для получения значений

btn2 = tk.Button(window, text="/", command=division)# Создаем кнопку для получения значений
btn2.grid(column=1, row=3)# Создаем кнопку для получения значений

btn = tk.Button(window, text="+", command=summa)# Создаем кнопку для получения значений
btn.grid(column=2, row=3)# Создаем кнопку для получения значений

btn = tk.Button(window, text="-", command=minus)# Создаем кнопку для получения значений
btn.grid(column=2, row=2)#Ставим где должна находится кнопка


btn = tk.Button(window, text="%-", command=procentminus)# Создаем кнопку для получения значений
btn.grid(column=1, row=4)#Ставим где должна находится кнопка


btn = tk.Button(window, text="%+", command=procentsumma)# Создаем кнопку для получения значений
btn.grid(column=2, row=4)#Ставим где должна находится кнопка


window.mainloop()# Запускаем главный цикл приложения