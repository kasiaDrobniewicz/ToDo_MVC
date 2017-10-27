import view
from model import ToDoList, ToDoItem


def check_action():
    FIRST_ACTION = 0
    LAST_ACTION = 7
    while True:
        action = input("  Choose action:")
        if action.isalpha() or type(action) is int: #int(action) < FIRST_ACTION or int(action) > LAST_ACTION:
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


def process_todolist_all(todo_list_obj, id):
    items_list_all = []
    id_name_description = []
    index = 0
    for item in todo_list_obj.todo_list:
        id_name_description = [index, item.name, item.description]
        items_list_all.append(id_name_description)
        index += 1
        return items_list_all
    for item in items_list_all:
        id_item = item[index]
        if id_item == id:
            return item


'''def process_todolist_all(todo_list_obj, id):
    items_list_all = []
    id_name_description = []
    index = 0
    for item in todo_list_obj.todo_list:
        id_name_description = [index, item.name, item.description]
        items_list_all.append(id_name_description)
        index += 1
        for item in items_list_all:
            if index == id:
                return id_name_description'''



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
            id = input("Enter the task number: ")
            item = process_todolist_all(todo_list_obj, id)
            print(item)
            #view.display_items_list(process_todolist_all(todo_list_obj, id))
            #view.display_items_list_all(process_todolist_all(todo_list_obj, id))
            pass
        elif action == "7":
            exit()

if __name__ == "__main__":
    main()