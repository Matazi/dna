from sys import argv, exit
import csv

def main():
    if len(argv) != 3:
        exit(1)

    with open(argv[1]) as file:
        data = []
        cvs_reader = csv.DictReader(file)
        for row in cvs_reader:
            print(row)
            data.append(row)
        print(data[1]['name'])
        # print(len(data[1]))

    str_file = open(argv[2], 'r')
    sequence = str_file.read()
    # print(sequence)

    strCount = {}
    countt = 0
    readyToPrint = False
    final = ""
    keys = []
    for i in range(len(data[1])):
        # print(f"i is {i}")
        # print(len(data[1]))
        if i < len(data):
            holA = list(data[i].items())

        if i != 0:
            key = holA[i][0]
            keys.append(key)
            value = holA[i][1]
            # print(key)
            print(value)
            countt = sequence_count(key, sequence)
            strCount[key] = countt
            # print(strCount[key])
            # print(value

        else:
            name = holA[i][1]

    compare(strCount, data, keys)

    if readyToPrint:
        print(final)
    print(strCount)

def compare(str, data, keys):
    total = []
    ready = False
    # for i in range(len(data[1])-1):
    #     key = keys[i]
    #     print(data[i][key])
    for line in data:
        for i in range(len(line)-1):
            key = keys[i]
            if int(line[keys[i]]) == int(str[key]):
                print(line[keys[i]])
                ready = True
                total.append(line['name'])
            else:
                ready = False

    print(total)


def sequence_count(str, sequence):
    print(f"Time for the str {str} ", end="")
    maximum = 0
    count = 0
    started = False
    continued = False
    incr = len(str)
    for i in range(len(sequence)):
        # print(f"i at start is {i}")
        if started == False:
            count = count - count
            if sequence[i:i+incr] == str:
                count += 1
                started = True
                print(started)
                print(f"started at i = {i}")
                i += incr
            else:
                count = 0

        else:
            started = True

            if sequence[i:i+incr] == str:
                count += 1
                print(f"continued on i = {i} ")
                print(started)
                print(f" count = {count}")
                i += incr


            # else:
            #     started = False

        if count > maximum:
            maximum = count
    print(maximum)

    # hola = list(data[1].items())
    # key_value = hola[2][0]
    # print(key_value)
    return maximum

main()