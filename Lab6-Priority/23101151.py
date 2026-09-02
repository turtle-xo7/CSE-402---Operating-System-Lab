process = [
    ["P1", 0, 3, 3],
    ["P2", 1, 2, 4],
    ["P3", 2, 4, 6],
    ["P4", 3, 6, 4],
    ["P5", 5, 10, 2],
]

def non_preemptive_priority(process):
    current_time = 0
    completed = []
    result = {}
    sequence = []
    while len(completed) < len(process):
        available = [
            p for p in process if p[1] <= current_time and p[0] not in completed
        ]
        if not available:
            current_time += 1
            continue
        available.sort(
            key=lambda p: (p[2], p[1])
        )  
        pid, at, pr, bt = available[0]
        if current_time < at:
            current_time = at
        ct = current_time + bt
        tat = ct - at
        wt = tat - bt
        result[pid] = [ct, tat, wt]
        completed.append(pid)
        sequence.append(pid)
        current_time = ct
    return result, sequence


def preemptive_priority(process):
    remaining = {p[0]: p[3] for p in process}
    current_time = 0
    completed = []
    result = {}
    sequence = []
    while len(completed) < len(process):
        available = [
            p for p in process if p[1] <= current_time and p[0] not in completed
        ]
        if not available:
            current_time += 1
            continue
        available.sort(key=lambda p: (p[2], p[1]))
        pid, at, pr, bt = available[0]
        current_time += 1
        remaining[pid] -= 1
        sequence.append(pid)
        if remaining[pid] == 0:
            ct = current_time
            tat = ct - at
            wt = tat - bt
            result[pid] = [ct, tat, wt]
            completed.append(pid)
    return result, sequence


def display(name, result, sequence, process):
    total_tat = total_wt = 0
    print(name)
    print("PID\tAT\tPr\tBT\tCT\tTAT\tWT")
    print("-" * 45)
    for p in process:
        pid, at, pr, bt = p
        ct, tat, wt = result[pid]
        total_tat += tat
        total_wt += wt
        print(f"{pid}\t{at}\t{pr}\t{bt}\t{ct}\t{tat}\t{wt}")
    print("-" * 45)
    print(f"Average TAT: {total_tat/len(process):.2f}")
    print(f"Average WT:  {total_wt/len(process):.2f}")
    print("Sequence:", " -> ".join(sequence))
    return total_tat / len(process), total_wt / len(process)


np_result, np_seq = non_preemptive_priority(process)
p_result, p_seq = preemptive_priority(process)
np_tat, np_wt = display("Non-Preemptive Priority", np_result, np_seq, process)
p_tat, p_wt = display("Preemptive Priority", p_result, p_seq, process)
