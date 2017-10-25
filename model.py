class ToDoList():

    def __init__(self):
        self.todo_list = []

    def add_item(self, item):
        if isinstance(item, ToDoItem):
            self.todo_list.append(item)
        else:
            raise ValueError("Incorrect item type")


class ToDoItem():

    def __init__(self, name, description, is_done=False):

        NAME_LENGTH = 20
        DESTRIPCTION_LENGTH = 150

        if ToDoItem.check_value(name, NAME_LENGTH):
            self.name = name
        if ToDoItem.check_value(description, DESTRIPCTION_LENGTH):
            self.description = description
        self.is_done = is_done

