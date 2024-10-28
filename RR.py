from collections import deque
import argparse

class Process:
    def __init__(self, name, runtime, arrival_time, io_freq):
        self.name = name
        self.runtime = runtime
        self.arrival_time = arrival_time
        self.remaining_time = runtime
        self.io_freq = io_freq
        self.time_spent = 0
        self.io_interruptions = 0

def round_robin(processes, quantum=1):
    time = 0
    queue = deque()
    processes = sorted(processes, key=lambda x: x.arrival_time)
    process_idx = 0
    output = []

    while process_idx < len(processes) or queue:
        # Add new processes to the queue
        while process_idx < len(processes) and processes[process_idx].arrival_time <= time:
            queue.append(processes[process_idx])
            process_idx += 1

        if queue:
            current_process = queue.popleft()
            output.append(current_process.name)

            # Execute for the time quantum or remaining time, whichever is smaller
            execution_time = min(quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            current_process.time_spent += execution_time
            time += execution_time

            if current_process.remaining_time > 0:
                # Handle I/O interruptions
                if current_process.time_spent >= current_process.io_freq:
                    output.append(f"!{current_process.name}")
                    current_process.time_spent = 0
                queue.append(current_process)  # Re-queue the unfinished process
        else:
            # No process in queue, jump to next arrival time
            if process_idx < len(processes):
                time = processes[process_idx].arrival_time
            else:
                break  # No remaining processes

    return ' '.join(output)

parser = argparse.ArgumentParser()
parser.add_argument('--data-file', type=str, default='Data/d.txt',
                    help='Process data input into the student and marker file')
args = parser.parse_args()

def main():
    try:
        with open(args.data_file, "r") as file:
            n = int(file.readline().strip())
            processes = []

            for _ in range(n):
                line = file.readline().strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) != 4:
                    print(f"Skipping invalid line: '{line}' (expected 4 values, got {len(parts)})")
                    continue
                
                try:
                    name = parts[0].strip()
                    runtime = int(parts[1].strip())
                    arrival_time = int(parts[2].strip())
                    io_freq = int(parts[3].strip())
                    processes.append(Process(name, runtime, arrival_time, io_freq))
                except ValueError as ve:
                    print(f"Error processing line: '{line}'. {ve}")
                    continue

    except FileNotFoundError:
        return "File not found."

    output = round_robin(processes)

    return output

if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)
