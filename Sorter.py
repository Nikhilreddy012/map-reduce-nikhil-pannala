input = open("01.txt","r")  # open file, read-only
sortoutput = open("sortdata.txt", "w") # open file, write
lines = input.readlines()
lines.sort()

for line in lines:
 sortoutput.write(line)

input.close()
sortoutput.close()