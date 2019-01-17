from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
import sys
import csv
import uuid
inputfiles=sys.argv[1:]
print("Input fasta-files:%s" %inputfiles)

csvfilename=str(uuid.uuid4())+".csv"
print("Output file: %s" % csvfilename)
field_names=["Accession number","Molecular Weight","Aromaticity","Instability index","Gravy index","pI","Molar exctinction coefficient"]
with open(csvfilename,"w") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=field_names)
    writer.writeheader()
    for inputfile in inputfiles:
        for record in SeqIO.parse(inputfile,"fasta"):
                print(record.id)
                protein=ProteinAnalysis(str(record.seq))
                writer.writerow({"Accession number":record.id,"Molecular Weight":protein.molecular_weight(),"Aromaticity":protein.aromaticity(),"Instability index":protein.instability_index(),"Gravy index":protein.gravy(),"pI":protein.isoelectric_point(),"Molar exctinction coefficient":protein.molar_extinction_coefficient()[1]})
                print("%s %s %s %s %s %s" % (protein.molecular_weight(), protein.aromaticity(),protein.instability_index(),protein.gravy(),protein.isoelectric_point(),protein.molar_extinction_coefficient()[1]))
