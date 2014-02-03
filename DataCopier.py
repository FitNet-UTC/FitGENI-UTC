path = 'C:\\Python33\\'
lineCounter = 0
N = 2 # 100 / N = Compression percentage
with open(path + 'birth_of_venus.txt', 'r') as f1, open(path + 'birth_of_venus2.txt', 'w') as f2:
    lineOfData = f1.readline()
    while lineOfData:
        lineCounter += 1

        if (lineCounter % N == 0) : # Skip every Nth line of data.
            lineOfData = f1.readline()
        else:
            counter = 0
            for byteOfData in lineOfData:
                counter += 1
                if (counter % N == 0 and counter < len(lineOfData)) : # Skip every Nth byte of data.
                    continue
                else:
                    f2.write(byteOfData)

            lineOfData = f1.readline()
        