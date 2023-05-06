from datetime import datetime

# Function which contains all user inputs requests
def ask_inputs():
    txt = input('Enter the .txt filename (without .txt):\n')
    txt_filename_ = txt + '.txt'

    init_datetime_str = input('Enter Initial Datetime (dd/mm/yyyy HH:MM:SS):\n')
    init_datetime_ = datetime.strptime(init_datetime_str, "%d/%m/%Y %H:%M:%S")

    end_datetime_str = input('Enter End Datetime (dd/mm/yyyy HH:MM:SS):\n')
    end_datetime_ = datetime.strptime(end_datetime_str, "%d/%m/%Y %H:%M:%S")

    hostname_ = input('Enter the name of the host you want to watch connections:\n')

    return txt_filename_, init_datetime_, end_datetime_, hostname_

# Function to read the .txt and store the data on a dict
def read_txt(txt_filename):

    logs_array_ = []

    with open(txt_filename) as input:
        for line in input:
            # We read line by line and convert str date to date
            record = line.split()
            timestamp_ = datetime.fromtimestamp(int(record[0]) // 1000)  # Convert to seconds
            host1 = record[1]
            host2 = record[2]

            # Storing the data of the log
            log = {
                'timestamp': timestamp_,
                'host1': host1,
                'host2': host2
            }
            # Append to the logs array
            logs_array_.append(log)

    return logs_array_

# Function to complete code challenge question 1
def match_logs(logs_array, init_datetime, end_datetime, hostname):
    # Initial result info texts
    print('\n------------ ' + hostname + ' LOG ------------')
    print('Connections made in the time range you have selected:\n')
    for log in logs_array:
        # We look for the searched host and only take it if time is ok
        if log['host1'] == hostname or log['host2'] == hostname:
            if(init_datetime<=log['timestamp']<=end_datetime):
                log['timestamp'] = log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                # Return the log, presented well formatted
                print(str(log['timestamp']) + ' ' + str(log['host1']) + ' - ' + str(log['host2']))

def main():
    # Code challenge main variables
    txt_filename, init_datetime, end_datetime, hostname = ask_inputs()

    # Using the logs txt, obained logs python array
    logs_array = read_txt(txt_filename)

    # Code challenge question 1 answer
    match_logs(logs_array, init_datetime, end_datetime, hostname)

if __name__ == "__main__":
    main()