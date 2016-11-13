import math


def summary():
    datalist = []
    data = {}
    
    file = open("experiment_fitts_log.txt", "r")
    lines = file.readlines()
    for line in lines:
        split = line.split()
        amplitude = int(split[1])
        width = int(split[2])
        selectionNum = split[3]
        time = float(split[4])
        ID = math.log2((amplitude/width) + 1)
        key = (amplitude, width, round(ID, 3))
        datalist.append((key, time))
    
    summary = open("summary.csv", "w")
    count = 0
    i = 0
    for item in datalist:
        
        if i >= 7:
            data[item[0]] = count/6
            
            summary.write(str(item[0][2]) + "\t" + str(round(data[item[0]], 3)) + "\n") 
            count = 0
            i = 0
            
        elif i <= 1:
            i += 1
                
        else:
            i += 1
            count += item[1]
            
print(summary())    