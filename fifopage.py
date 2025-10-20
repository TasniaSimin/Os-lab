def fifo_rep(pages, capacity):
    memory = []
    faults = 0

    print("\nPages\tMemory\t\tPage Fault")

    for p in pages:
        if p not in memory:
            faults += 1
            if len(memory) < capacity:
                memory.append(p)
            else:
                memory.pop(0)
                memory.append(p)
            print(f"{p}\t{memory}\t\tYes")
        else:
            print(f"{p}\t{memory}\t\tNo")

    print("\nTotal Page Faults:", faults)


# Input section
pages = list(map(int, input("Enter the page references (space separated): ").split()))
capacity = int(input("Enter number of frames: "))

fifo_rep(pages, capacity)
