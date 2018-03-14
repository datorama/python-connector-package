import csv

datorama_out_put_result = []


def add_row(rows):
        datorama_out_put_result.append(rows)


def add_rows(rows):
        for row in rows:
            add_row(row)


def save():
        myFile = open('/tmp/fileName', 'wb')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(datorama_out_put_result)
        myFile = open('/tmp/fileName', 'r')
        with myFile:
            spamreader = csv.reader(myFile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(row)



def save_csv(string):
        myFile = open('/tmp/fileName', 'wb')
        with myFile:
            myFile.write(string)
        myFile = open('/tmp/fileName', 'r')
        with myFile:
            spamreader = csv.reader(myFile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(row)


