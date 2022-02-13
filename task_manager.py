
menu = {1: 'display a list of tasks', 2: 'add task ', 3:'change task ',
        4: 'delete task',5: 'execute', 6: 'completed', 7: 'unfulfilled',8: 'find', 0: 'quit' }

todo = ['помыть машину', 'сходить в магазин', 'убрать дома', 'посмотреть футбол']

def decor(func):
    def new():
        func()
        x = 'y'
        while x == 'y':
            x = input('do you want to repeat the operation? (y/n)')
            if x =='y':
                func()
            else:
                menu_display()
    return new

def menu_display():
    print('           MENU')
    for i, j in menu.items():
        print(i, j)

def display():
    print('      task list')
    for i in range(len(todo)):
        print(i+1, todo[i])

    print("to return to the main menu, press '9'")

@decor
def add():
    x1 = input('enter a task ')
    todo.append(x1)
    print('      task list')
    for i in range(len(todo)):
        print(i + 1, todo[i])
    print("to return to the main menu, press '9'")

@decor
def change():
    n = int(input('enter the number of the task you want to change '))
    for i in range(len(todo)):
        if n-1 == i:
            todo[n-1] = input('enter a new task ')
    display()

@decor
def delite():
    n = int(input('enter the number of the task you want to delete '))
    for i in range(len(todo)):
        if n-1 == i:
            del todo[n-1]
    display()

@decor
def perform():
    n = list(map(int, input('mark completed tasks').split()))
    for i in n:
        todo[i-1] = '^^^'+todo[i-1]+'^^^'
    display()


def delete_completed():
    x = input('do you want to delete completed tasks? (y/n)')
    if x == 'y':
        todo1 = todo.copy()
        for i in range(len(todo1)):
            if '^' in todo1[i]:
                del todo[i]
                i += 1
    else:
        display()
    display()

def completed ():
    print('      task list')
    for i in range(len(todo)):
        if '^' in todo[i]:
            print(i+1, todo[i])
    delete_completed()

def unfulfilled ():
    print('      task list')
    for i in range(len(todo)):
        if todo[i][0] != '^':
            print(i+1, todo[i])
    display()

@decor
def find():
    x = input('enter the word')
    for i in range(len(todo)):
        if x in todo[i]:
            print(i+1, todo[i])
    print("to return to the main menu, press '9'")

menu_display()
while True:

    x = int(input())
    if x == 1:
        display()
    elif x == 2:
        add()
    elif x == 0:
        break
    elif x == 9:
        menu_display()
    elif x == 3:
        display()
        change()
    elif x == 4:
        display()
        delite()
    elif x == 5:
        perform()
    elif x == 6:
        completed()
    elif x == 7:
        unfulfilled()
    elif x == 8:
        find()