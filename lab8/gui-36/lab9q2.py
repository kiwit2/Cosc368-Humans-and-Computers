import itertools

file = open("myfile.txt", "r")
lines = file.readlines()

end = len(lines) - 1

for i in range(0, end):
    col1 = lines[i].split()
    
    line = col1[10]+" "+col1[11]+" "+col1[14]
    print(line)