import nltk
from nltk.tokenize.toktok import ToktokTokenizer
# Tokenizador TokTok (palabras)
toktok = ToktokTokenizer()
# Tokenizador de oracionesa
es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
# Obtener oraciones de un parrafo
with open ("C:/Users/lore_/OneDrive/Documentos/Escuela/tercer  semestre/LN/recursos/practica3.txt", 'r', encoding="utf8") as file: #ass fp:
	parrafo=file.read()
	oraciones = es_tokenizador_oraciones.tokenize(parrafo)
	# Obtener tokens de cada oraci´on
	var=[]
	freq = []
	for s in oraciones:
		var=var+[t for t in toktok.tokenize(s)]
		for w in var:
			freq.append(var.count(w))
	#print (var)
	frecuenciaPalabras = [var.count(p) for p in var]
	print(dict(zip(var,frecuenciaPalabras)))
file.close()
