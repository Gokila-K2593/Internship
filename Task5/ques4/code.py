with open('logfile.txt', 'r') as log_file:
    log_lines = log_file.readlines()
error_count = 0
for line in log_lines:
    if "ERROR" in line:
        error_count += 1 
print(error_count)