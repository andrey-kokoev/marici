"""Exact induced embedding into the unique order-35 host + border witness at 36."""
from ramsey_39_from_27 import g6
from itertools import combinations
host='bsaCCA?O?O_aC??`c@O@b?RcHQ?DcA@H?PC_@QO@@Q?DA@MP?RgKADoH?aR?KCbOC_JE?xO@AALC@AJPG?__V?_K@ROO_A@dOG@?_'
def decode(s):
    n=ord(s[0])-63;b=''.join(f'{ord(c)-63:06b}' for c in s[1:]);a=[0]*n
    for j in range(n):
        for i in range(j):
            if b[j*(j-1)//2+i]=='1':a[j]|=1<<i;a[i]|=1<<j
    return a
A,B=map(decode,(g6,host));full=(1<<35)-1

def embed(dom):
    if not dom:return True
    u=min(dom,key=lambda i:dom[i].bit_count());d=dom[u]
    while d:
        bit=d&-d;d^=bit;v=bit.bit_length()-1
        child={j:c & (B[v] if A[u]>>j&1 else ~(B[v]|bit)) for j,c in dom.items() if j!=u}
        if all(child.values()) and embed(child):return True
    return False

def independent():
    sets=[0]
    for i,r in enumerate(B):sets += [s|1<<i for s in sets if not s&r]
    return sets
I=independent();octets=[s for s in I if s.bit_count()==8]
def obstruction(p):
    for i,j in combinations(range(35),2):
        if p>>i&1 and p>>j&1 and B[i]>>j&1:return ('positive triangle',i+1,j+1,36)
    s=next(s for s in octets if not p&s);return ('negative nine-set',*[i+1 for i in range(35) if s>>i&1],36)
if __name__=='__main__':
    print('embeds:',embed({i:full for i in range(27)}),flush=True)
    assert max(s.bit_count() for s in I)==8 and all(not (B[i]&B[j]) for i,j in combinations(range(35),2) if B[i]>>j&1)
    print('independent candidates, octets:',len(I),len(octets));assert all(any(not p&s for s in octets) for p in I);print(obstruction(0))
