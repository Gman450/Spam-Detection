f=open("spmsga1.txt","r")
g=open("myown.txt","r")
str1=f.read();
str2=g.read();
sep1=str1.split()
sep2=str2.split()
un1=set(sep1)
un2=set(sep2)
count=0
print "The unique words from spam file---\n",un1
print "The unique words from our file----\n",un2
for i in un1:
	for j in un2:
		if i==j:
			count=count+1
print "No. of matching cases= ",count
f.close()
g.close()
