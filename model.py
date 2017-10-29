class ToDoList():

    def __init__(self):
        self.todo_list = []

    def add_item(self, item):
        if isinstance(item, ToDoItem):
            self.todo_list.append(item)
        else:
            raise ValueError("Incorrect item type")

    def delete_item(self, id):
        self.todo_list.remove(self.todo_list[id])


class ToDoItem():

    def __init__(self, name, description, is_done=False):
        
        NAME_LENGTH = 20
        DESCRIPTION_LENGTH = 150

        if ToDoItem.check_value(name, NAME_LENGTH):
            self.name = name
        if ToDoItem.check_value(description, DESCRIPTION_LENGTH):
            self.description = description
        self.is_done = is_done

    def modify_name(self, name):
        NAME_LENGTH = 20
        if ToDoItem.check_value(name, NAME_LENGTH):
            self.name = name
        return name

    def modify_description(self, description):
        DESCRIPTION_LENGTH = 150
        if ToDoItem.check_value(description, DESCRIPTION_LENGTH):
            self.description = description
        return description

    def mark_item_as_done(self):
        self.is_done = True

    @classmethod    
    def check_value(cls, value, length):
        if len(value) <= length:
            return True
        else:
            raise ValueError("Too long value")

