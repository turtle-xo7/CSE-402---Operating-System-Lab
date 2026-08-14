process = [
    ["P1", 3, 3],
    ["P2", 2, 5],
    ["P3", 5, 4],
    ["P4", 1, 3],
    ["P5", 6, 2],
]

fcfs_process = sorted(process, key=lambda p: p[1])

current_time = 0
fcfs_total_tat = 0
fcfs_total_wt = 0
fcfs_sequence = []

print("FCFS")
print("PID\tAT\tBT\tCT\tTAT\tWT")
print("--------------------------------")

for p in fcfs_process:
    pid = p[0]
    at = p[1]
    bt = p[2]

    if current_time < at:
        current_time = at

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    fcfs_total_tat = fcfs_total_tat + tat
    fcfs_total_wt = fcfs_total_wt + wt
    fcfs_sequence.append(pid)

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    current_time = ct

fcfs_avg_tat = fcfs_total_tat / len(process)
fcfs_avg_wt = fcfs_total_wt / len(process)

print("--------------------------------")
print("Sequence:", " -> ".join(fcfs_sequence))
print("Average TAT:", fcfs_avg_tat)
print("Average WT:", fcfs_avg_wt)


current_time = 0
sjf_total_tat = 0
sjf_total_wt = 0
completed = []
sjf_sequence = []

print("\nSJF")
print("PID\tAT\tBT\tCT\tTAT\tWT")
print("--------------------------------")

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

    sjf_total_tat = sjf_total_tat + tat
    sjf_total_wt = sjf_total_wt + wt
    completed.append(pid)
    sjf_sequence.append(pid)

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    current_time = ct

sjf_avg_tat = sjf_total_tat / len(process)
sjf_avg_wt = sjf_total_wt / len(process)

print("--------------------------------")
print("Sequence:", " -> ".join(sjf_sequence))
print("Average TAT:", sjf_avg_tat)
print("Average WT:", sjf_avg_wt)


print("\nCOMPARISON")
print("Algorithm\tAverage TAT\tAverage WT")
print("------------------------------------------")
print(f"FCFS\t\t{fcfs_avg_tat:.2f}\t\t{fcfs_avg_wt:.2f}")
print(f"SJF\t\t{sjf_avg_tat:.2f}\t\t{sjf_avg_wt:.2f}")

if sjf_avg_wt < fcfs_avg_wt:
    print("\nSJF is better because it has lower average waiting time.")
elif fcfs_avg_wt < sjf_avg_wt:
    print("\nFCFS is better because it has lower average waiting time.")
else:
    print("\nBoth algorithms have the same average waiting time.")
