from tkinter import *

def product_even_numbers(var):
    
    list_even_number = [] # список чётных чисел
    result = 1
    # создаём список всех чисел
    list_number = list(map(int, str(var.get()))) 
    print(list_number)
    for x in list_number: # проход по списку всех чисел
        
        if x!=0 and x % 2 == 0: # условие отбора чётных чисел
            list_even_number.append(x) #добавляем в список чётные числа
    print(list_even_number)
    for f in list_even_number: # проход по списку чётных чисел
        
         result = result * f  # произведение чётных чисел

    # вывод результата в виджет Label
    product_number['text'] = f'Произведение чётных чисел\n {result}'
##    product_number.pack(padx = 50)

# Графический интерфейс
root = Tk()

root.geometry('420x120+100+50')
root.resizable(False, False)

var = IntVar() # переменная (введённое пользователем число)

label_enter_number = Label(root, text = 'Введите целое число и нажмите Enter', font = 'Arial 10')
label_enter_number.pack(padx = 50)
# поле ввода
entry_field = Entry(root, textvariable = var, width = 28)
# вызов ф-ции по нажатию клавиши Enter
entry_field.bind('<Return>', lambda e: product_even_numbers(var))
entry_field.pack()
entry_field.focus() # помещает курсор в поле ввода
# дублирующая надпись введённого числа
label_entered_number = Label(root, textvariable = var, font = 'Arial 12 bold')
label_entered_number.pack(padx = 100)

product_number = Label(root, text = '', font = 'Arial 12 bold')
product_number.pack(padx = 90)

root.mainloop()
