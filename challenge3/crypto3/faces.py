f = open("faces.txt", "r")
text = f.read()
# print text
icon = text.split()
# print icon

from collections import Counter
c = Counter(i for i in icon if len(i) > 1)
# print c
# for i in c:
#   print i, c[i]

print "Number icon face:",len(c)
k = 0
for i in c:
    if len(i) > 3:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1
for i in c:
    if len(i) == 3:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1
for i in c:
    if len(i) == 2:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1


text = text.replace("   ","___")
text = text.replace(" ","")
text = text.replace("___"," ")
print text
