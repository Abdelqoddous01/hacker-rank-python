l1=[]
word=input()
lenght=len(word)
res1=False
res2=False
res3=False
res4=False
res5=False


for i in range(0,lenght):
    l1.append(word[i])

for x in l1:
    if x.isalnum():
        res1=True
        break
for x in l1:
    if x.isalpha():
        res2=True
        break
for x in l1:
    if x.isdigit():
        res3=True
        break
for x in l1:
    if x.islower():
        res4=True
        break
for x in l1:
    if x.isupper():
        res5=True
        break
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
