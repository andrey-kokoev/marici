"""Preserve each forward edge; count executable reversed-complement orders from the same address."""
from itertools import permutations
from ramsey_39_simplex_phase_depth import layer,phase,M,W,test

def orders(x,i):
    dest=list(x);dest[i]-=1;dest[(i+1)%4]+=1;count=0
    for order in permutations(j for j in range(4) if j!=i):
        y=list(x)
        for j in order:
            donor=(j+1)%4
            if not y[donor]:break
            y[donor]-=1;y[j]+=1
        else:
            assert y==dest;count+=1
    assert count>=1 and (count==6)==all(x[j] for j in range(4) if j!=(i+1)%4)
    return count
if __name__=='__main__':
    first={}
    for n in range(1,11):
        best={}
        for x in layer(n):
            p=phase(x)
            for i in range(4):
                if not x[i]:continue
                q=(p+W[(i+1)%4]-W[i])%M;e=tuple(sorted((p,q)));best[e]=max(best.get(e,0),orders(x,i))
        assert set(best)==test(n)[1];counts=[sum(c>=k for c in best.values()) for k in range(1,7)]
        for k,c in enumerate(counts,1):
            if c==140:first.setdefault(k,n)
        print(n,counts)
    print('first full depths',first)
