import argparse
import heapq
from collections import deque

class Process:
    def __init__(self, name, runtime, arrival_time, io_freq):
        self.name = name
        self.runtime = runtime
        self.arrival_time = arrival_time
        self.remaining_time = runtime
        self.io_freq = io_freq
        self.time_spent = 0
        self.io_interruptions = 0

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time

def preemptive_shortest_to_completion(processes):
    time = 0
    ready_queue = []
    io_queue = deque()
    processes = sorted(processes, key=lambda x: x.arrival_time)
    process_idx = 0
    output = []  

    while process_idx < len(processes) or ready_queue or io_queue:
        while process_idx < len(processes) and processes[process_idx].arrival_time <= time:
            process = processes[process_idx]
            heapq.heappush(ready_queue, process)
            process_idx += 1

        if io_queue:
            io_process = io_queue[0]
            if io_process.arrival_time <= time:
                io_queue.popleft()
                io_process.io_interruptions += 1
                io_process.arrival_time = time + 1  
                heapq.heappush(ready_queue, io_process)

        if ready_queue:
            current_process = heapq.heappop(ready_queue)
            output.append(current_process.name) 

            current_process.remaining_time -= 1
            current_process.time_spent += 1
            time += 1

            if current_process.time_spent == current_process.io_freq and current_process.remaining_time > 0:
                output.append(f"!{current_process.name}") 
                current_process.time_spent = 0  
                io_queue.append(current_process) 
            elif current_process.remaining_time > 0:
                heapq.heappush(ready_queue, current_process)  
        else:
            time += 1

    return ' '.join(output) 

parser = argparse.ArgumentParser()
parser.add_argument('--data-file', type=str, default='Data/extreme.txt',
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

    output = preemptive_shortest_to_completion(processes)

    return output

if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)