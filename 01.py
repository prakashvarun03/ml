import csv

with open('data.csv','r') as f:
    reader = csv.reader(f)
    dlist = list(reader)
    
h = ['0','0','0','0','0','0']
print("Data input is:")
for l in dlist:
    print(l)
print("Training Data:")
for i in dlist:
    if i[-1] == "yes":
        print(i)
        j = 0
        for x in i:
            if x != "yes":
                if x != h[j] and h[j] == '0':
                    h[j] = x
                elif x != h[j] and h[j] != '0':
                    h[j] = '?'
                else:
                    pass
            j = j+1
print("Most specific hypothesis is:")
print(h)
