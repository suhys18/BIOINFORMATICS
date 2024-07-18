
#open the file and read it
with open('y.txt','r') as file:

    lines = file.readlines()

#stripping each lines 

lines = [line.strip() for line in lines]

#create variables for each line stripped

for i, line in enumerate(lines):
    globals()[f'line{i+1}'] = line

count = 0

#making the patterncount
for i in range(len(line1) - len(line2) + 1):

    if line1[i:i+len(line2)] == line2:

        count +=1 

print(count)

   
