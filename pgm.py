import fnmatch
f=open("spamlog","r")
cont=f.read();
sep=cont.split()
word=fnmatch.filter(sep,'score*')
print word
print "Bye bye..."

