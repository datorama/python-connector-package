import csv

output_buffer = []


def add_row(rows):
        output_buffer.append(rows)


def add_rows(rows):
        for row in rows:
            add_row(row)


def save():
    for row in output_buffer:
      print(row)



def save_csv(string):
        reader = csv.reader(string.split('\n'), delimiter=',')
        for row in reader:
            print(row)




