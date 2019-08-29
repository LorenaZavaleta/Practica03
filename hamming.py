def hamming(str1, str2):
	tam= len(str1)
	pos = 0
	dis = 0
	while pos <= tam-1:
		if not str1[pos] == str2[pos]:
			dis += 1
		pos += 1
	print (dis)

print ("Ingresa una palabra")
str1 = input()
print ("ingresa otra palabra")
str2 = input()
hamming(str1, str2)
