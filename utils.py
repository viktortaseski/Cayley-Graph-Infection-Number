import csv


def write_table(filename, results):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(results)


def logTable(table):
    for row in table:
        print(f"{str(row[0]):<5} {str(row[1]):<5} {str(row[2]):<25} {str(row[3]):<5}")
