import random

punc=[".",",","?","!"]


def scramble_function(expr):
    l=len(expr)
    if l<3:
        return expr
    else:
        if expr[l-1]==punc and l<=4:
            return expr
        if expr[l-1]!=punc:
            temp=expr[1:l-2]
            temp1=''.join(random.sample(temp,len(temp)))
            expr=expr.replace(temp,temp1)
            return expr
        else:
            temp=expr[1:l-3]
            temp1=''.join(random.sample(temp,len(temp)))
            expr=expr.replace(temp,temp1)
            return expr

string = input("Enter the sentence : ")
i=0
s=""
while(i<len(string)):
    if string[i]!=" ":
        s=s+string[i]
    if string[i]==" " or i==len(string)-1:
        string=string.replace(s,scramble_function(s))
        s=""
    i=i+1

print(string)
