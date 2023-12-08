names_list = []
marks_list = []
run = 1

while (run == 1):
    choice = int(input("Press 1/2/3/4 for Create/Read/Update/Delete: "))
    
    if (choice == 1):
        name = input("Enter your name: ")
        names_list.append(name)

        mark = int(input("Enter your mark: "))
        marks_list.append(mark)

    elif (choice == 2):
        print(names_list)
        print(marks_list)

    elif (choice == 3):
        name = input("Enter name to update the result: ")
        mark = int(input("Enter the mark: "))
        
        i = names_list.index(name)
        marks_list[i] = mark
    else:
        name = input("Enter the name to delete: ")
        i = names_list.index(name)
        names_list.remove(name)
        marks_list.pop(i)

    run = int(input("Press 1 to continue: "))
    print()