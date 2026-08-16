process = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9],
]

time_quantum = 5


def fcfs(process):
    sorted_process = sorted(process, key=lambda p: p[1])
    current_time = 0
    result = {}
    sequence = []

    for p in sorted_process:
        pid = p[0]
        at = p[1]
        bt = p[2]

        if current_time < at:
            current_time = at

        ct = current_time + bt
        tat = ct - at
        wt = tat - bt

        result[pid] = [ct, tat, wt]
        sequence.append(pid)
        current_time = ct

    return result, sequence


def sjf(process):
    current_time = 0
    completed = []
    result = {}
    sequence = []

    while len(completed) < len(process):
        available = []

        for p in process:
            if p[1] <= current_time and p[0] not in completed:
                available.append(p)

        if len(available) == 0:
            current_time = current_time + 1
            continue

        shortest = available[0]

        for p in available:
            if p[2] < shortest[2]:
                shortest = p

        pid = shortest[0]
        at = shortest[1]
        bt = shortest[2]

        ct = current_time + bt
        tat = ct - at
        wt = tat - bt

        result[pid] = [ct, tat, wt]
        completed.append(pid)
        sequence.append(pid)
        current_time = ct

    return result, sequence


def round_robin(process, time_quantum):
    sorted_process = sorted(process, key=lambda p: p[1])
    remaining_time = {}

    for p in process:
        remaining_time[p[0]] = p[2]

    current_time = 0
    next_process = 0
    completed = 0
    queue = []
    result = {}
    sequence = []

    while completed < len(process):
        while next_process < len(sorted_process):
            if sorted_process[next_process][1] <= current_time:
                queue.append(sorted_process[next_process])
                next_process = next_process + 1
            else:
                break

        if len(queue) == 0:
            current_time = sorted_process[next_process][1]
            continue

        selected = queue.pop(0)

        pid = selected[0]
        at = selected[1]
        bt = selected[2]

        if remaining_time[pid] <= time_quantum:
            running_time = remaining_time[pid]
        else:
            running_time = time_quantum

        current_time = current_time + running_time
        remaining_time[pid] = remaining_time[pid] - running_time
        sequence.append(pid)

        while next_process < len(sorted_process):
            if sorted_process[next_process][1] <= current_time:
                queue.append(sorted_process[next_process])
                next_process = next_process + 1
            else:
                break

        if remaining_time[pid] == 0:
            ct = current_time
            tat = ct - at
            wt = tat - bt

            result[pid] = [ct, tat, wt]
            completed = completed + 1
        else:
            queue.append(selected)

    return result, sequence


def display(name, result, sequence):
    total_tat = 0
    total_wt = 0

    print("\n" + name)
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    print("--------------------------------")

    for p in process:
        pid = p[0]
        at = p[1]
        bt = p[2]

        ct = result[pid][0]
        tat = result[pid][1]
        wt = result[pid][2]

        total_tat = total_tat + tat
        total_wt = total_wt + wt

        print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    average_tat = total_tat / len(process)
    average_wt = total_wt / len(process)

    print("--------------------------------")
    print("Sequence:", " -> ".join(sequence))
    print(f"Average TAT: {average_tat:.2f}")
    print(f"Average WT: {average_wt:.2f}")

    return average_tat, average_wt


fcfs_result, fcfs_sequence = fcfs(process)
sjf_result, sjf_sequence = sjf(process)
rr_result, rr_sequence = round_robin(process, time_quantum)

fcfs_tat, fcfs_wt = display(
    "FCFS", fcfs_result, fcfs_sequence
)

sjf_tat, sjf_wt = display(
    "SJF", sjf_result, sjf_sequence
)

print("\nRound Robin Time Quantum:", time_quantum)

rr_tat, rr_wt = display(
    "ROUND ROBIN", rr_result, rr_sequence
)

print("\nCOMPARISON")
print("Algorithm\tAverage TAT\tAverage WT")
print("------------------------------------------")
print(f"FCFS\t\t{fcfs_tat:.2f}\t\t{fcfs_wt:.2f}")
print(f"SJF\t\t{sjf_tat:.2f}\t\t{sjf_wt:.2f}")
print(f"Round Robin\t{rr_tat:.2f}\t\t{rr_wt:.2f}")

if fcfs_wt < sjf_wt and fcfs_wt < rr_wt:
    print("\nFCFS has the lowest average waiting time.")

elif sjf_wt < fcfs_wt and sjf_wt < rr_wt:
    print("\nSJF has the lowest average waiting time.")

elif rr_wt < fcfs_wt and rr_wt < sjf_wt:
    print("\nRound Robin has the lowest average waiting time.")

else:
    print("\nTwo or more algorithms have the same average waiting time.")
