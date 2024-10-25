import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data-file', type=str, default='Data/easy.txt',
                    help='Process data input into the student and marker file')

args = parser.parse_args()


def main():


    # Open the file for reading
    try:
        with open(args.data_file, "r") as file:
            data = file.read()
            file.close()

    except FileNotFoundError:
        return 1


    """
    TODO Your Algorithm - assign your output to the output variable
    """
# Open the file containing process data

    # Read the first line for the number of processes
    dataNo = file.readline().strip()  # Read the first line and strip whitespace
    NumberofProcesses = int(dataNo)  # Convert the number of processes to an integer

    # Initialize lists to store process information
    Process_Name = []
    Process_Runtime = []
    Process_ArrivalTime = []
    IO_Frequency = []

    # Read the remaining lines and populate the lists
    for line in file:
        row = line.strip().split(',')  # Split each line by commas
        if len(row) == 4:  # Ensure there are exactly four columns
            Process_Name.append(row[0].strip())  # Process Name
            Process_Runtime.append(int(row[1].strip()))  # Process Runtime
            Process_ArrivalTime.append(int(row[2].strip()))  # Arrival Time
            IO_Frequency.append(int(row[3].strip()))  # IO Frequency

# Now you can use the lists Process_Name, Process_Runtime, Process_ArrivalTime, and IO_Frequency
print("Number of Processes: {NumberofProcesses}")
print("Process Names:", Process_Name) # type: ignore
print("Process Runtime:", Process_Runtime) # type: ignore
print("Process Arrival Times:", Process_ArrivalTime) # type: ignore
print("IO Frequencies:", IO_Frequency) # type: ignore

  #  output = "AB AC AB !AD BA CB !BL BX AB" #Example output
 