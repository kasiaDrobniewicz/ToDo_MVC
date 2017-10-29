def start_view():
    print("1.Add item")
    print("2.Modify item")
    print("3.Delete item")
    print("4.Mark item as done")
    print("5.Display items list")
    print("6.Display specific todo item's details")
    print("7.Exit")


def display_modify_options():
    print("Do you want to modify:")
    print("  1. name")
    print("  2. description")


def display_items_list(items_list):
    line = "| "
    for item in items_list:
        for element in item:
            line = line + str(element) + " | "
        print (line)
        line = "| "
