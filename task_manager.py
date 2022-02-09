<<<<<<< HEAD
menu = {1: 'display a list of tasks', 2: 'add task ', 3:'change task ',4: 'delete task', 5: 'quit'}
=======
menu = {1: 'display a list of tasks', 2: 'add task ', 3:'change task ',
        4: 'delete task', 5: 'quit'}
>>>>>>> flomaster
todo = {1: 'to wash the dishes', 2: 'go to the cinema',
        3: 'make the bed'}

def menu_display():
    print('           MENU')
    for i, j in menu.items():
        print(i, j)

def display():
    print('      task list')
    for i, j in todo.items():
        print(i, j)
    print("to return to the main menu, press '9'")

def add():
    x1 = input('enter a task ')
    for i in todo:
        s = i
    posl = s + 1
    todo[posl] = x1
    print('      task list')
    for i, j in todo.items():
        print(i, j)
    print("to return to the main menu, press '9'")

def change():
    n = int(input('enter the number of the task you want to change '))
    for i in todo.keys():
        if n == i:
            todo[n] = input('enter a new task ')
    display()

def delite():
    n = int(input('enter the number of the task you want to delete '))
    for i in todo.keys():
        if n == i:
            t = n
    del todo[t]
    count = 1
    for i in todo.keys():
        todo.get(count)
        count += 1
    display()


menu_display()
while True:

    x = int(input())
    if x == 1:
        display()
    elif x == 2:
        add()
    elif x == 5:
        break
    elif x == 9:
        menu_display()
    elif x == 3:
        change()
    elif x == 4:
        delite()