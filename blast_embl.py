################################  HEADERS EMBL
embl= "phg-re" #"rna_phg"  #"htg_phg" #rna_phg
headers= open("/scratch/cluster/monthly/ecabello/Aline/headers_"+embl+".txt", "r").readlines()
dic={}
idlist=[]
phagelist=[]
countphage=[]
for h in headers:
    if 'phage' in h:
        id=h[1:h.index(" ")]
        phage=h[h.index("[")+1:h.index("phage")+5] #("]")]
        idlist.append(id)
        phagelist.append(phage)
        countphage.append(0)
print 'header fini'
############################### BLAST XLS FILE
file=open("/scratch/cluster/monthly/ecabello/Aline/phages/blastn_"+embl+"_all_granules.xls", "r").read()
output=open("/scratch/cluster/monthly/ecabello/Aline/phages/output_blastn_"+embl+"_all_granules_2.xls", "w")
entry=file.split("# BLASTN 2.3.0+")
entry=entry[1:]
idblast=[]
for e in entry:
    if "0 hits found" not in e:
        e=e.split("\t")
        idblast.append(e[-11])
print 'idblast'
print len(idblast)

phagesmatch=[]
for i in idblast:
    if i in idlist:
        match=idlist.index(i)
        phagesmatch.append(phagelist[match])
print len(phagesmatch)
phagesya=[]
output.write("Strain"+"\t"+"Number of hits"+"\t"+"% of total hits"+"\t"+"Number of sequences in Database"+"\n")
for p in phagesmatch:
    if p not in phagesya:
        cuenta=phagesmatch.count(p)
        cuentadb=phagelist.count(p)
        output.write(p+"\t"+str(cuenta)+"\t"+str(float(100.0/72847.0)*float(cuenta))+"\t"+str(cuentadb)+"\n")
        phagesya.append(p)
