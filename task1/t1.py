f=open("test.txt","r")
content=f.read();
words=content.split()
unique=set(words)
print "Unique words are---\n",unique
f.close()
