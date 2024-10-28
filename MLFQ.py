import argparse
from collections import deque

class Process:
    def __init__(self, name, runtime, arrival_time, io_frequency):
        self.name = name
        self.remaining_time = runtime
        self.arrival_time = arrival_time
        self.io_frequency = io_frequency
        self.completed = False
        self.io_count = 0  # Keep track of how many times I/O has been requested

class MLFQ:
    def __init__(self, time_slices):
        self.queues = [deque() for _ in range(len(time_slices))]
        self.time_slices = time_slices
        self.current_time = 0
        self.output = []

    def add_process(self, process):
        self.queues[0].append(process)

    def schedule(self):
        while any(queue for queue in self.queues):
            for i, queue in enumerate(self.queues):
                if queue:
                    process = queue.popleft()

                    # Simulate arrival of processes
                    if process.arrival_time > self.current_time:
                        # If the process has not arrived yet, put it back and continue
                        queue.append(process)
                        continue

                    # Determine how much to execute based on the time slice
                    execution_time = min(process.remaining_time, self.time_slices[i])
                    # Process execution
                    for _ in range(execution_time):
                        self.output.append(process.name)  # Append process name for each unit of time
                        self.current_time += 1

                        # Handle I/O (check if io_frequency is greater than 0)
                        if process.io_frequency > 0 and (self.current_time - process.arrival_time) % process.io_frequency == 0 and process.remaining_time > 0:
                            if process.remaining_time > 1:  # Only trigger I/O if more time remains
                                self.output.append(f"!{process.name}")  # Append I/O request
                                process.io_count += 1  # Count I/O request

                    process.remaining_time -= execution_time

                    # Move process to the next queue if it has remaining time
                    if process.remaining_time > 0:
                        next_queue_index = min(i + 1, len(self.queues) - 1)
                        self.queues[next_queue_index].append(process)
                    else:
                        process.completed = True
                    break

    def get_output(self):
        # Join output list to create a single output string
        return ' '.join(self.output)  # Ensure a space between each action

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-file', type=str, default='Data/easy.txt',
                        help='Process data input file')
    args = parser.parse_args()

    # Open the file for reading
    try:
        with open(args.data_file, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        return "File not found."

    # Read the number of processes and process data
    time_slices = [4, 6, 10]  # MLFQ with three queues
    mlfq = MLFQ(time_slices)

    # Parse process data
    n = int(lines[0].strip())  # The first line is the number of processes
    for line in lines[1:n+1]:  # Read the specified number of processes
        name, runtime, arrival_time, io_frequency = line.strip().split(',')
        mlfq.add_process(Process(name, int(runtime), int(arrival_time), int(io_frequency)))

    # Execute the scheduling
    mlfq.schedule()
    output = mlfq.get_output()
    
    return output

if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)
