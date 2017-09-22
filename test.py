f=open("spamw.txt","r")
g=open("myown.txt","r")
wrd2=g.read();
wrd=f.read();
sep=wrd.split()
print sep
sep2=wrd2.split()
count=0
for i in sep2:
	for j in sep:
		if i==j:
			count=count+1
			print i
print "Matching cases= ",count
f.close()
g.close()
