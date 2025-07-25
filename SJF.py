n = int(input("Enter number of processes: "))

at = []    
bt = []    
ct = [0] * n  
tat = [0] * n  
wt = [0] * n   
completed = [0] * n  
pid = []  

for i in range(n):
    pid.append(i + 1)
    print(f"Process {pid[i]}:")
    at.append(int(input("  Enter Arrival Time: ")))
    bt.append(int(input("  Enter Burst Time: ")))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if at[j] > at[j + 1]:
            at[j], at[j + 1] = at[j + 1], at[j]
            bt[j], bt[j + 1] = bt[j + 1], bt[j]
            pid[j], pid[j + 1] = pid[j + 1], pid[j]

time = 0
completed_count = 0
total_tat = 0
total_wt = 0

while completed_count < n:
    min_bt = 9999
    index = -1

    for i in range(n):
        if at[i] <= time and completed[i] == 0 and bt[i] < min_bt:
            min_bt = bt[i]
            index = i

    if index != -1:
        ct[index] = time + bt[index]
        tat[index] = ct[index] - at[index]
        wt[index] = tat[index] - bt[index]
        completed[index] = 1
        completed_count += 1
        time = ct[index]

        total_tat += tat[index]
        total_wt += wt[index]
    else:
        time += 1  

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")

avg_tat = total_tat / n
avg_wt = total_wt / n
print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
print(f"Average Waiting Time    = {avg_wt:.2f}")