f=open("dbase.txt","w")
words = file("db1.txt", "r").read().split() #read the words into a list.
uniqWords = sorted(set(words)) #remove duplicate words and sort
for word in uniqWords:
	cnt=words.count(word)
	f.write(" %s " % cnt);    				
	f.write(" %s\n " % word);
	print words.count(word),word
print "The above is also stored in a text file"


   

