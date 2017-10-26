import view
from model import ToDoList, ToDoItem


def check_action():
    FIRST_ACTION = 0
    LAST_ACTION = 7
    while True:
        action = input("  Choose action:")
        if action.isalpha() or int(action) < FIRST_ACTION or int(action) > LAST_ACTION:
            print("Enter only digits between " + str(FIRST_ACTION) + " and " + str(LAST_ACTION)) 
        else:
            return action


def process_todolist(todo_list_obj):
    items_list = []
    id_name = []
    index = 0
    for item in todo_list_obj.todo_list:
            id_name = [index, item.name]
            items_list.append(id_name)
            index += 1
    return items_list


def main():
    todo_list_obj = ToDoList()
    view.start_view()
    while True:
        action = check_action()
        if action == "1":
            name = input("Please enter name: ")
            description = input("Please enter description: ")
            item = ToDoItem(name, description)
            todo_list_obj.add_item(item)
        elif action == "2":
            pass        
        elif action == "3":
            pass
        elif action == "4":
            pass
        elif action == "5":
            view.display_items_list(process_todolist(todo_list_obj))
            pass
        elif action == "6":
            pass
        elif action == "7":
            exit()

if __name__ == "__main__":
    main()