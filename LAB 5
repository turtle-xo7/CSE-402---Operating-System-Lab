process = [
    ["P1", 4, 2],
    ["P2", 2, 2],
    ["P3", 1, 3],
    ["P4", 0, 6],
    ["P5", 3, 1],
]

TQ = 2
remaining = {p[0]: p[2] for p in process}

current_time = 0
completed = []
result = {}
execution_sequence = []

while len(completed) < len(process):
    available = []

    for p in process:
        if p[1] <= current_time and p[0] not in completed:
            available.append(p)

    if len(available) == 0:
        current_time += 1
        continue

    available.sort(key=lambda p: (remaining[p[0]], p[1]))
    selected = available[0]

    pid = selected[0]
    at = selected[1]
    bt = selected[2]

    run_time = min(TQ, remaining[pid])
    current_time += run_time
    remaining[pid] -= run_time

    execution_sequence.append(pid)

    if remaining[pid] == 0:
        ct = current_time
        tat = ct - at
        wt = tat - bt

        result[pid] = [ct, tat, wt]
        completed.append(pid)

total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")
print("--------------------------------")

for p in process:
    pid = p[0]
    at = p[1]
    bt = p[2]

    ct = result[pid][0]
    tat = result[pid][1]
    wt = result[pid][2]

    total_tat += tat
    total_wt += wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

avg_tat = total_tat / len(process)
avg_wt = total_wt / len(process)

print("--------------------------------")
print(f"Average TAT: {avg_tat}")
print(f"Average WT: {avg_wt}")
print("Execution sequence:")
print(" -> ".join(execution_sequence))
