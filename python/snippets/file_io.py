import datetime

time = datetime.datetime.now()

with open('file_io.txt', mode='r') as file:
    file_contents = file.readlines()
    for i in file_contents:
        print(i)

with open('file_io.txt', mode='a') as file:
    output = f"{time} This is a test string that I added via file_io.py\n"
    append = file.write(output)
