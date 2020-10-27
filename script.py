from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord 
import os
filename= ("nombre del archivo genbank")
def summarize_contents(filename):
	listaOs = os.path.split(filename)
	listaExt = os.path.splitext(filename)
	if (listaExt[1] == ".gbk"):
		type_file= "genbank"
	else: 
		type_file= "fasta"
	record = list(SeqIO.parse(filename, type_file))
	#Esta funcion es para creacion de diccionario
	dic = {}
	dic['File:'] = listaOs[1]
	dic['Path:'] = listaOs[0]
	dic['Num_records:'] = len(record)
	#Esta funcion es el diccionario con listas
	dic['Names:'] = []
	dic['IDs:'] = []
	dic['Descriptions'] = []
	#Esta funcion es el registro de records
	for seq_rcd in SeqIO.parse(filename,type_file):
		dic['Names:'].append(seq_rcd.name)
		dic['IDs:'].append(seq_rcd.id)
		dic['Descriptions'].append(seq_rcd.description)
	return dic
#Imprimir la funcion
if _name_ == "_main_":
	resultados = summarize_contents(filename)
	print(resultados)	
