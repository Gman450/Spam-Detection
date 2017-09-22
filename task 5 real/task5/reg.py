import sys

f=open("dataset.txt","a")
h=open("nocspamw.txt","r")
spam=0

hcontent=h.read();
hwords=hcontent.split()

for n in sys.argv[1:]:
	twc=0
	swc=0
	g=open(n,"r")
	gcontent=g.read();
	gwords=gcontent.split()
	for i in gwords:
		twc=twc+1
	for i in gwords:
		for j in hwords:
			if i==j:
				swc=swc+1
	f.write("%d,"%twc);
	f.write("%d,"%swc);
	f.write("%d\n"%spam);
	g.close()
f.close()
h.close()
