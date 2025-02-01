import tkinter as tk #вызываем библиотеку

def procentminus():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1 - (value2 / 100 * value2)
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ


def multiplication():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter=value2*value1
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ


def division():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1 / value2
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ

def summa():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value2 + value1
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ


def minus():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1-value2
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ


def procentsumma():# создаём функцию
    value1 = int(entry1.get())  # Получаем значение из первого Entry
    value2 = int(entry2.get())  # Получаем значение из второго Entry
    ter = value1+(value2/100*value2)
    result_label = tk.Label(window, text=f"       {ter}      ")  # Добавляем пробел перед результатом
    result_label.grid(column=1, row=5)#Ставим где должна находится ответ

window = tk.Tk()# Создаем главное окно
entry1 = tk.Entry(window, width=10)# Создаем два поля ввода
entry1.grid(column=1, row=0)#Ставим где должно находится поля для ввода
entry2 = tk.Entry(window, width=10)# Создаем два поля ввода
entry2.grid(column=1, row=1)#Ставим где должно находится поля для ввода

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