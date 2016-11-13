import itertools

file = open("4-and-36.txt", "r")
lines = file.readlines()

half = (len(lines)//2 - 1)

newfile = open('myfile.txt', 'w')

for i in range(0, half - 1):
    value = lines[i].split("\t")
    col1 = value[-1]
    value2 = lines[i + half].split("\t")
    col2 = value2[-1]
    
    line = col1 + "\t" + col2
    newfile.write(line)
    print(line)
    
    