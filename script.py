from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord 
import os
filename= ("nombre del archivo genbank")
def summarize_contents(filename):
	rtodos = []
	runo= list(SeqIO.parse(filename, "genbank"))
	print("Path:",os.path.dirname(filename))
	print("Num_record= %len(runo))
	print("\n")
	for seq_r in SeqIO.parse(filename, "genbank"):
	
	rtodos.append(seq_r.name)
		print("Name:",seq_r.name)
		print(ID:",seq_r.id)
		print("Description:"seq_record.description, "\n")

summarize_contents(filename)	
