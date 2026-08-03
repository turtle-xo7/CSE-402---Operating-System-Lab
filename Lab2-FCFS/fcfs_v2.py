process = [
    ["p3", 1, 2],
    ["p2", 2, 2],
    ["p0", 3, 1],
    ["p1", 5, 3],
    ["p4", 6, 3],
]

current_time = 0
total_tat = 0
total_wt = 0
execution_sequence = []

print("PID\tAT\tBT\tCT\tTAT\tWT")
print("------------------------")

for p in process:
    pid = p[0]
    at = p[1]
    bt = p[2]

    if current_time < at:
        current_time = at

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    execution_sequence.append(pid)
    total_tat = total_tat + tat
    total_wt = total_wt + wt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    current_time = ct

print("___________________________")

avg_tat = total_tat / 5
avg_wt = total_wt / 5

print(f"average turn around time: {avg_tat}")
print(f"average waiting time: {avg_wt}")

print("Execution sequence:")
print(" -> ".join(execution_sequence))
