def start_view():
    print("1.Add item")
    print("2.Modify item")
    print("3.Delete item")
    print("4.Mark item as done")
    print("5.Display items list")
    print("6.Display specific todo item's details")
    print("7.Exit")


def display_items_list(items_list):
    index = 0
    line = "| "
    for item in items_list:
        for element in item:
            line = line + str(element) + " | "
        print (line)
        line = "| "

test_list = [["1", "2"], ["3", "4"], ["3", "4", "5"]]
display_items_list(test_list)



