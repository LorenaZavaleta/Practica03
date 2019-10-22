import nltk
from nltk.metrics.distance 
import edit_distance

def correcto(rutamal, rutabien):
    var=20
    txtbien=[]
    with open(rutamal, 'r') as file:
    	auxmal = file.read()
    textomal=auxmal.split()
    with open(rutabien, 'r') as file:
    	auxdic=file.read()
    	diccionario=auxdic.split()
    for i in range(len(textomal)):
    	for j in range(len(diccionario)):
    		distancia=edit_distance(textomal[i], diccionario[j], false)
    		if(distancia<var):
    			var=distancia
    			palabra=diccionario[j]
    	txtbien.append(palabra∫)
    cadena=" ".join(txtbien)
    with open (rutanueva="corregido.txt", 'w', encoding"utf-8") as file:
    	file.write(cadena)