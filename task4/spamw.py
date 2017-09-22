f=open("db2.txt","r")
g=open("spamword.txt","a")
words=f.read();
sep=words.split()
uniq=sorted(set(sep))
for i in uniq:
	count=words.count(i)
	if count<5:
		g.write("%s "%i);
		g.write("%d\n"%count);
f.close()
g.close()
