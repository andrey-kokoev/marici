"""A three-color (3,9,9) product and its pin reflection, not an optimality claim."""
from itertools import combinations, product
from collections import Counter
S={1,34,7,28,11,24,16,19}
V=list(product(range(8),range(35)))
def color(u,v):
    if u[0]!=v[0]:return 'green'
    return 'red' if (u[1]-v[1])%35 in S else 'blue'
def reflect(v,c):return ((2*c[0]-v[0])%8,(2*c[1]-v[1])%35)
def clique(mask,neighbors,k):
    if k==0:return True
    while mask.bit_count()>=k:
        b=mask&-mask;mask^=b
        if clique(mask&neighbors[b.bit_length()-1],neighbors,k-1):return True
    return False
if __name__=='__main__':
    for col,k in [('red',3),('blue',9)]:
        N=[sum(1<<j for j in range(35) if i!=j and color((0,i),(0,j))==col) for i in range(35)]
        assert not clique((1<<35)-1,N,k)
    c=(0,1);cnt=Counter()
    for u,v in combinations(V,2):
        col=color(u,v);cnt[col]+=1
        assert color(reflect(u,c),reflect(v,c))==col
    print(len(V),cnt)
