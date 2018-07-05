import csv
with open('eggs.csv', 'r') as f:        # 采用b的方式处理可以省去很多问题
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open('some1.csv', 'w', newline='') as f:      # 采用b的方式处理可以省去很多问题
    writer = csv.writer(f)
    writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    writer.writerows(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('t.csv','w') as myFile:    
    myWriter=csv.writer(myFile)
    myWriter.writerow([7,'g'])
    myWriter.writerow([8,'h'])
    myList=[[1,2,3],[4,5,6]]
    myWriter.writerow(myList)

with open('eggs.csv','r') as myFile:  
    lines=csv.reader(myFile)  
    for line in lines:  
        print(line)  