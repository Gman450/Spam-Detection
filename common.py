f=open("db1.txt","r")
g=open("sp2.txt","a")
words=f.read();
sep=sorted(words.split())
uniq=set(sep)
for i in uniq:
	count=words.count(i)
	if count<10:
		g.write("%s "%i);
		g.write("%d\n"%count);
f.close()
g.close()
