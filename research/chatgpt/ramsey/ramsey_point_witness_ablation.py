"""Separate point-witnessed obstructions by number of points in the seven."""
from itertools import combinations
from collections import Counter
from ramsey_shared_frame_propagation import bits,T
from ramsey_shared_frame_reconstruction import search

def clauses(p):
    masks=set()
    for U in combinations(range(15),7-p):
        unused=6-len(set().union(*(set(T[i]) for i in U)))
        if p and unused<p:continue
        # p=0 denotes six external vertices plus root, handled below
        masks.add(sum(bits.get(e,0) for e in combinations(U,2)))
    return masks

def minimal(ms):
    out=[]
    for m in sorted(ms,key=int.bit_count):
        if not any(m&n==n for n in out):out.append(m)
    return out

if __name__=='__main__':
    families={p:minimal(clauses(p)) for p in range(1,7)}
    families[0]=minimal({sum(bits.get(e,0) for e in combinations(U,2)) for U in combinations(range(15),6)})
    counts=Counter(); common=(1<<len(bits))-1;good=common;examples={}
    def visit(N):
        global common,good
        m=sum(b for (i,j),b in bits.items() if j in N[i]);fail=tuple(p for p,cs in families.items() if any(not m&c for c in cs));counts[fail]+=1
        if not any(fail):common&=m;examples.setdefault(fail,hex(m))
        if not fail:good&=m
    search(set(range(15)),visit)
    print('total',sum(counts.values()),'valid',counts[()],'point-only survivors',sum(v for f,v in counts.items() if not any(f)),'point-forced common edges',common.bit_count(),'examples',examples)
    print('survive p>=k',[(k,sum(v for f,v in counts.items() if not any(p>=k for p in f))) for k in range(1,7)])
    print('full backbone missing under point-only',[(T[i],T[j]) for (i,j),b in bits.items() if b&good&~common])
