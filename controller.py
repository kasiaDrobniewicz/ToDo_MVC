import view
from model import ToDoList, ToDoItem


def check_action():
    while True:
        action = input("  Choose action:")
        if action.isalpha():
            print("Enter only digits") 
        #elif action != 1:
        #    print("There is no task with this number") 
        else:
            return action


def main():
    todo_list = ToDoList()
    view.startView()
    while True:
        #action = input("Choose action:")
        action = check_action()
        #check_action()
        if action == "1":
            name = input("Please enter name: ")
            description = input("Please enter description: ")
            item = ToDoItem(name, description)
            todo_list.add_item(item)
        elif action == "2":
            pass        
        elif action == "3":
            pass
        elif action == "4":
            pass
        elif action == "5":
            pass
        elif action == "6":
            pass
        elif action == "7":
            exit()

if __name__ == "__main__":
    main()