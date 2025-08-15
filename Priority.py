n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    pid = int(input(f"Enter Process ID for process {i+1}: "))
    prio = int(input(f"Enter Priority for P{pid} (lower number = higher priority): "))
    at = int(input(f"Enter Arrival Time for P{pid}: "))
    bt = int(input(f"Enter Burst Time for P{pid}: "))
    processes.append((pid, prio, at, bt))

completed = []
time = 0
CT_list = []
TAT_list = []
WT_list = []
process_order = []

while len(completed) < n:
    available = [p for p in processes if p[2] <= time and p[0] not in completed]
    if available:
        available.sort(key=lambda x: x[1])
        pid, prio, at, bt = available[0]
        time += bt
        CT_list.append(time)
        TAT_list.append(time - at)
        WT_list.append((time - at) - bt)
        completed.append(pid)
        process_order.append((pid, time, time - at, (time - at) - bt))
    else:
        time = min(p[2] for p in processes if p[0] not in completed)

print("\nPID\tCT\tTAT\tWT")
for pid, ct, tat, wt in process_order:
    print(f"{pid}\t{ct}\t{tat}\t{wt}")

avg_tat = sum(TAT_list) / n
avg_wt = sum(WT_list) / n

print(f"\nAverage TAT = {avg_tat:.2f}")
print(f"Average WT  = {avg_wt:.2f}")
