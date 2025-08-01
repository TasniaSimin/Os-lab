def get_process_input():
   
    processes_data = []
    num_processes = 0

    while True:
        try:
            num_processes = int(input("Enter the number of processes: "))
            if num_processes > 0:
                break
            else:
                print("Please enter a positive number for processes.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("\nEnter process details:")
    for i in range(num_processes):
        pid = f"P{i + 1}"
        while True:
            try:
                arrival_time = int(input(f"Enter Arrival Time for {pid}: "))
                if arrival_time >= 0:
                    break
                else:
                    print("Arrival Time cannot be negative. Please enter a non-negative integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                burst_time = int(input(f"Enter Burst Time for {pid}: "))
                if burst_time > 0:
                    break
                else:
                    print("Burst Time must be positive. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        processes_data.append({
            "pid": pid,
            "arrival_time": arrival_time,
            "burst_time": burst_time,
        })
    return processes_data

def get_time_quantum_input():
    """
    Takes user input for the time quantum.
    """
    while True:
        try:
            time_quantum = int(input("Enter the Time Quantum: "))
            if time_quantum > 0:
                break
            else:
                print("Time Quantum must be positive. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return time_quantum

def round_robin_scheduler():
    """
    Implements the Round Robin (RR) CPU scheduling algorithm with user input.
    """
    processes_data = get_process_input()
    time_quantum = get_time_quantum_input()

  
    processes = []
    for p_data in processes_data:
        processes.append({
            "pid": p_data["pid"],
            "arrival_time": p_data["arrival_time"],
            "burst_time": p_data["burst_time"],
            "remaining_burst_time": p_data["burst_time"],
            "completion_time": 0,
            "turnaround_time": 0,
            "waiting_time": 0,
            "has_arrived": False 
        })

  
    processes.sort(key=lambda p: p["arrival_time"])

    print(f"\n--- Round Robin Scheduling (Time Quantum = {time_quantum}) ---\n")

   
    current_time = 0
    ready_queue = [] 
    completed_processes_count = 0
    n = len(processes) 

   
    while completed_processes_count < n:
      
        for p in processes:
            if p["arrival_time"] <= current_time and not p["has_arrived"]:
                ready_queue.append(p["pid"])
                p["has_arrived"] = True

      
        if not ready_queue:
            next_arrival_time = float('inf')
            found_next = False
            for p in processes:
                if not p["has_arrived"] and p["arrival_time"] < next_arrival_time:
                    next_arrival_time = p["arrival_time"]
                    found_next = True

            if found_next:
                if next_arrival_time > current_time:
                    print(f"Time {current_time:2d}: CPU idle. Advancing to {next_arrival_time} for next arrival.")
                    current_time = next_arrival_time
                    continue 
            else:
                
                break 

      
        current_pid = ready_queue.pop(0)

       
        current_process = None
        for p in processes:
            if p["pid"] == current_pid:
                current_process = p
                break

        if current_process is None:
            print(f"Error: Process {current_pid} not found. Skipping.")
            continue

      
        run_time = min(time_quantum, current_process["remaining_burst_time"])

        print(f"Time {current_time:2d}: Executing {current_process['pid']} for {run_time} units.")

       
        current_time += run_time
        current_process["remaining_burst_time"] -= run_time

        
        for p in processes:
            if p["arrival_time"] <= current_time and not p["has_arrived"]:
                ready_queue.append(p["pid"])
                p["has_arrived"] = True

        
        if current_process["remaining_burst_time"] == 0:
            current_process["completion_time"] = current_time
            completed_processes_count += 1
            print(f"Time {current_time:2d}: {current_process['pid']} completed.")
        else:
            
            ready_queue.append(current_process["pid"])

   
    print("\n--- Calculating Metrics ---")
    for p in processes:
        p["turnaround_time"] = p["completion_time"] - p["arrival_time"]
        p["waiting_time"] = p["turnaround_time"] - p["burst_time"]

     
    print("\n--- Final Results ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")

    
    total_tat = sum(p["turnaround_time"] for p in processes)
    total_wt = sum(p["waiting_time"] for p in processes)

    print(f"\nAverage Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time: {total_wt / n:.2f}")


if __name__ == "__main__":
    round_robin_scheduler()
