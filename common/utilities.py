def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) -1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()