import argparse

class Process:
    def __init__(self, name, runtime, arrival_time, io_freq):
        self.name = name
        self.runtime = runtime
        self.arrival_time = arrival_time
        self.io_freq = io_freq
        self.remaining_time = runtime
        self.time_spent = 0  
        self.completed = False  


def fcfs_scheduler(processes):
    time = 0
    execution_order = []
    ready_queue = sorted(processes, key=lambda x: x.arrival_time)  

    while ready_queue:
        current_process = ready_queue.pop(0)

        if time < current_process.arrival_time:
            time = current_process.arrival_time

        while current_process.remaining_time > 0:
            if current_process.io_freq > 0 and current_process.time_spent == current_process.io_freq:
                execution_order.append(f"!{current_process.name}")  
                current_process.time_spent = 0  
                time += 1  
            else:
                execution_order.append(current_process.name)
                current_process.remaining_time -= 1
                current_process.time_spent += 1
                time += 1

        current_process.completed = True

    return " ".join(execution_order)


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-file', type=str, default='Data/easy.txt',
                        help='Process data input into the student and marker file')
    args = parser.parse_args()

    # Open the file for reading
    try:
        with open(args.data_file, "r") as file:
            lines = file.readlines()

        # Parse file data
        n = int(lines[0].strip())  # Number of processes
        processes = []
        for line in lines[1:n+1]:
            name, runtime, arrival_time, io_freq = line.strip().split(',')
            process = Process(
                name=name.strip(),
                runtime=int(runtime.strip()),
                arrival_time=int(arrival_time.strip()),
                io_freq=int(io_freq.strip())
            )
            processes.append(process)

    except FileNotFoundError:
        return 1

    output = fcfs_scheduler(processes)
    return output


if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)
