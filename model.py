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

    def __str__(self):

        formatted_list = []
        index = 0
        for item in self.todo_list:
            formatted_list.append(str(index) + ". " + item.__str__())
            index += 1
       
        return "".join(formatted_list)


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

    def __str__(self):
        return "Name: " + self.name + " | " + "Description: " + self.description + " | " + "Status: " + str(self.is_done) + "\n"


item1 = ToDoItem("Zrobić zakupy", "Lista zakupów: pomidor, chleb")
item2 = ToDoItem("Posprzątać", "Pokój")
#print(item1)
#print(ToDoItem.modify_name("Pranie", 20))
#print(ToDoItem.check_value("Zrobić zakupy", 20))
#print(ToDoItem.modify_name(item, "Pranie"))
#print(ToDoItem.modify_description(item, "Blalalalalalallalala"))

todo_list = ToDoList()
#print(todo_list)
todo_list.add_item(item1)
todo_list.add_item(item2)
#print(todo_list)

#todo_list.delete_item(0)
#print(todo_list)
#item1.mark_item_as_done()
#print(item1)

#item_list = todo_list.display_items_list() 

#print(item_list)