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
    NumberofProcesses = int(data.strip())
    dataLine = [line.strip().split(',') for line in file]

    Process_Name [] = (row[0] for row in data) # type: ignore
    Process_Runtime [] = (row[1] for row in data)# type: ignore
    Process_ArrivalTime [] # type: ignore
    IO_Frequency [] # type: ignore

    output = "AB AC AB !AD BA CB !BL BX AB" #Example output
    
    """
    End of your algorithm
    """

    return output
    

if __name__ == "__main__":
    scheduler_out = main()
    print(scheduler_out)
