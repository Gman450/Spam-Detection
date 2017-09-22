import sys
op=open("db1.txt","a")
print "Program running...."
for n in sys.argv[1:]:
	ip=open(n,"r")
	str1=ip.read();
	sep=str1.split()
	un=set(sep)
	for i in un:
		op.write(" %s" % i);
	ip.close()
op.close()
