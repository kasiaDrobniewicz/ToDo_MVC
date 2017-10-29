import view
from model import ToDoList, ToDoItem


def process_todolist(todo_list_obj, add_is_done=False):
    items_list = []
    id_name = []
    index = 0
    for item in todo_list_obj.todo_list:
        id_name = [index, item.name]
        if add_is_done:
            id_name.append(item.is_done)
        items_list.append(id_name)
        index += 1
    return items_list


def process_todo(todo_list_obj, id):
    attributes_list = [[]]
    attributes_list[0].append(str(id))
    attributes_list[0].append(todo_list_obj.todo_list[id].name)
    attributes_list[0].append(todo_list_obj.todo_list[id].description)

    return attributes_list


def get_valid_id(text, todo_list_obj):
    while True:
        try:
            id = int(input(text))
            check = todo_list_obj.todo_list[id]
            break     
        except ValueError:
            print("That was not a valid number. Try again...")
        except IndexError:
            print("There is no such a task in the list. Try again...")
            
    return id


def get_valid_option():
    while True:
        try:
            modify_option = int(input())
            if modify_option == 1 or modify_option == 2:
                break 
            else:
                print("That was not a valid number. Try again...")    
        except ValueError:
            print("That was not a valid number. Try again...")
        
    return modify_option


def main():
    todo_list_obj = ToDoList()
    view.start_view()
    while True:
        action = input("  Choose action:")
        if action == "1":
            name = input("Please enter name: ")
            description = input("Please enter description: ")
            item = ToDoItem(name, description)
            todo_list_obj.add_item(item)
        elif action == "2":
            view.display_items_list(process_todolist(todo_list_obj))
            id = get_valid_id("Enter the task number which you want to modify: ", todo_list_obj) 
            view.display_modify_options()
            modify_option = get_valid_option()
            if modify_option == 1:
                name = input("Please enter new name: ")
                todo_list_obj.todo_list[id].modify_name(name)
            elif modify_option == 2:
                description = input("Please enter new description: ")
                todo_list_obj.todo_list[id].modify_description(description)
        elif action == "3":
            view.display_items_list(process_todolist(todo_list_obj))
            id = get_valid_id("Enter the task number which you want to remove: ", todo_list_obj) 
            todo_list_obj.delete_item(id)
        elif action == "4":
            view.display_items_list(process_todolist(todo_list_obj, True))
            id = get_valid_id("Enter the task number which you want to marks as done: ", todo_list_obj) 
            todo_list_obj.todo_list[id].mark_item_as_done()
        elif action == "5":
            view.display_items_list(process_todolist(todo_list_obj))
        elif action == "6":
            id = get_valid_id("Enter the task number: ", todo_list_obj) 
            view.display_items_list(process_todo(todo_list_obj, id))
        elif action == "7":
            exit()

if __name__ == "__main__":
    main()