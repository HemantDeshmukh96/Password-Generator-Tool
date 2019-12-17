import random
def random_ch(password):
    n = len(password)
    x=random.randint(0, n - 1)
    return password[x]
def shuffle(ch,x):
    n=len(ch)
    loc = random.randint(0,n)
    result=""
    for k in range(0, loc):
        result=result+ch[k]
    result=result+x
    for j in range(loc,n):
        result=result+ch[j]
    return result
noc=int(input("Enter the length of your Password (in numbber):"))
n=""
for m in range(0,noc-2):
    name="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p=random_ch(name)
    n=n+p
m="0123456789"
digit=random_ch(m)
special = "+-*/?<>/{}[]|\=_-!@#$%^&()"
sp = random_ch(special)
rsymbol=shuffle(n,sp)
rdigit=shuffle(rsymbol,digit)
print(rdigit)