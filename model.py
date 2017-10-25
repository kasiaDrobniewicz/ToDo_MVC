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

    def modify_name(self, name):
        NAME_LENGTH = 20
        if ToDoItem.check_value(name, NAME_LENGTH):
            self.name = name
        return name

    def modify_description(self, description):
        DESTRIPCTION_LENGTH = 150
        if ToDoItem.check_value(description, DESTRIPCTION_LENGTH):
            self.description = description
        return description

    @classmethod    
    def check_value(cls, value, length):
        if len(value) <= length:
            return True
        else:
            raise ValueError("Too long value")     

    def __str__(self):
        return "Name: " + self.name + "\nDescription: " + self.description + "\nStatus: " + str(self.is_done)

item = ToDoItem("Zrobić zakupy", "Lista zakupów: pomidor, chleb")
print(item)
#print(ToDoItem.modify_name("Pranie", 20))
#print(ToDoItem.check_value("Zrobić zakupy", 20))
#print(ToDoItem.modify_name(item, "Pranie"))
#print(ToDoItem.modify_description(item, "Blalalalalalallalala"))