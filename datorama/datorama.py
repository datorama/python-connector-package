import csv

output_buffer = []
datorama_log = []


def add_row(rows):
    output_buffer.append(rows)


def add_rows(rows):
    for row in rows:
        add_row(row)


def save():
    for row in output_buffer:
        print(row)
    print_log()


def save_csv(string):
    reader = csv.reader(string.split('\n'), delimiter=',')
    for row in reader:
        print(row)
    print_log()


def log(log_line):
    datorama_log.append(log_line)


def print_log():
    for line in datorama_log:
        print line
