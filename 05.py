import csv

with open('nbctrain.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	data=list(csv_reader)
        
p=[]
for i in range(len(data[0])-1):
	p.append(dict())
    
y=n=0
for d in data:
	if d[-1]=='yes':
		y+=1
	else:
		n+=1

for d in data:
	for i in range(len(d)-1):
		if p[i].get(d[i],0)==0:
			p[i][d[i]]=dict()
		if d[-1]=='yes':
			p[i][d[i]][d[-1]]=p[i][d[i]].get(d[-1],0)+(1/y)
		else:
			p[i][d[i]][d[-1]]=p[i][d[i]].get(d[-1],0)+(1/n)

with open('nbctest.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	data=list(csv_reader)
        
accuracy=0
for d in data:
	print(d)
	pp=y/(y+n)
	pn=n/(y+n)
	for i in range(len(d)-1):
		pp*=p[i][d[i]].get('yes',0)
		pn*=p[i][d[i]].get('no',0)
	print("P(Yes)=",pp)
	print("P(No)=",pn)
	if (pp>pn and d[-1]=='yes') or (pn>pp and d[-1]=='no'):
		accuracy+=(1/len(data))*100
print('\nAccuracy=',accuracy)