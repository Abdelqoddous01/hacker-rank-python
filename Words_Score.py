def score_words(word):
    count=0
    for i in range(0,len(word)):
        if word[i]=='a' or  word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u' or word[i]=='y':
            count+=1
            
    if count%2==0 :
        return 2
    else:
        return 1 
        
n=int(input())
word=input()
l1=word.split()
res=0
for i in range(0,n):
    res+=score_words(l1[i])

print(res)    