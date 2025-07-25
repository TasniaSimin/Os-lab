n = int(input("Enter number of processes: "))

pid = [i + 1 for i in range(n)]  # Process IDs
at = []  
bt = []  
ct = [0] * n  
tat = [0] * n  
wt = [0] * n  

# Input
for i in range(n):
    print(f"Process {pid[i]}:")
    at.append(int(input("   Enter Arrival Time: ")))
    bt.append(int(input("   Enter Burst Time: ")))

for i in range(n - 1):
    for j in range(n - i - 1):
        if at[j] > at[j + 1]:
            at[j], at[j + 1] = at[j + 1], at[j]
            bt[j], bt[j + 1] = bt[j + 1], bt[j]
            pid[j], pid[j + 1] = pid[j + 1], pid[j]

total_tat = 0
total_wt = 0

for i in range(n):
    if i == 0:
        ct[i] = at[i] + bt[i]
    else:
        if ct[i - 1] < at[i]:
            ct[i] = at[i] + bt[i]
        else:
            ct[i] = ct[i - 1] + bt[i]

    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    total_tat += tat[i]
    total_wt += wt[i]

print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
print("-------\t-------\t-----\t----------\t----------\t-------")
for i in range(n):
    print(f"P{pid[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t\t{tat[i]}\t\t{wt[i]}")

print(f"\nAverage Turnaround Time: {total_tat / n:.2f}")
print(f"Average Waiting Time: {total_wt / n:.2f}")

