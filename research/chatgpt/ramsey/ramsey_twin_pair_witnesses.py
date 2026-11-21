"""Test direct (no third assignment) pair witnesses on the established backbone."""
from itertools import combinations, product
from ramsey_shared_frame_propagation import bits, prop, rules
from ramsey_shared_frame_reconstruction import T

def backbone():
    y,n=prop(0,0)
    def dead(y,n,split):
        s=prop(y,n)
        if s is None:return True
        y,n=s
        return split and any(dead(y|b,n,False) and dead(y,n|b,False) for b in bits.values() if not b&(y|n))
    for split in [False,False,True]:
        for b in bits.values():
            if b&(y|n):continue
            if dead(y|b,n,split):n|=b
            elif dead(y,n|b,split):y|=b
        y,n=prop(y,n)
    assert (y.bit_count(),n.bit_count())==(24,16)
    return y,n

def failures(assign,y,n):
    for i,t in assign:
        y|=bits[i,10+t];n|=bits[i,11-t]
    return [j for j,(m,l,h) in enumerate(rules) if (m&y).bit_count()>h or (m&~n).bit_count()<l]

if __name__=='__main__':
    y,n=backbone();forbidden=set()
    for i,j in combinations(range(6),2):
        for u,v in product(range(2),repeat=2):
            f=failures([(i,u),(j,v)],y,n)
            if f:
                forbidden.add((i,u,j,v));print(T[i],u,T[j],v,'direct rule indices',f)
    survivors=[s for s in product(range(2),repeat=6) if not any(s[i]==u and s[j]==v for i,u,j,v in forbidden)]
    valid=[s for s in product(range(2),repeat=6) if not failures(enumerate(s),y,n)]
    print('pair survivors',len(survivors),'fully valid',len(valid),'spurious',set(survivors)-set(valid))
