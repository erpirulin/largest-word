txt = input()

#tu código va aquí
txt1 = txt.split(' ')
txt2 = max(txt1, key=len)
print(txt2)
