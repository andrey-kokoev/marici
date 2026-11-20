"""Three 13-rings on 39 vertices, rotation only. Exact exhaustive offset test.
Run: python ramsey_39_rotating_triple.py. No catalogue or SAT package.
"""
from itertools import combinations, combinations_with_replacement
from functools import lru_cache
from collections import Counter
from pathlib import Path
from pauli_realization_audit import triangle_free,independent_witness
L=13;F=(1<<L)-1

def rot(m,i): return ((m<<i)|(m>>(13-i)))&F
@lru_cache(None)
def seq(m):return [rot(m,i) for i in range(L)]
@lru_cache(None)
def neg(m):return sum(1<<((-i)%L) for i in range(L) if m>>i&1)
@lru_cache(None)
def independent(m):
    sets=[0]
    for i,neighbors in enumerate(seq(m)):sets += [s|1<<i for s in sets if not s&neighbors]
    return sets
@lru_cache(None)
def allowed(a,b):
    # A cross-offset set must be independent for the union of internal differences.
    out=[]
    for s in independent(a|b):
        if s.bit_count()+max(a.bit_count(),b.bit_count())>9:continue
        if s!=min(seq(s)):continue
        rows=[x|(y<<13) for x,y in zip(seq(a),seq(s))]+[x|(y<<13) for x,y in zip(seq(neg(s)),seq(b))]
        if independent_witness(rows,9,((1<<26)-1)&~(rows[0]|1)) is not None:continue
        # Check the other orbit as well.
        if independent_witness(rows,9,((1<<26)-1)&~(rows[13]|1<<13)) is None:out.append(s)
    return out

def main():
    internal=[]
    for v in range(64):
        a=(v<<1)|neg(v<<1)
        if not triangle_free(seq(a)) or any(s.bit_count()>=10 for s in independent(a)):continue
        internal.append(a)
    counts=Counter(); seen=set()
    for a,b,c in combinations_with_replacement(internal,3):
        def scale(m,u):return sum(1<<(i*u%13) for i in range(13) if m>>i&1)
        key=min(tuple(sorted(scale(m,u) for m in (a,b,c))) for u in range(1,13))
        if key in seen:continue
        seen.add(key)
        for x in allowed(a,b):
            for y in allowed(a,c):
                if a.bit_count()+x.bit_count()+y.bit_count()>9:continue
                # Offsets 1->2 prohibited by a common vertex on ring 0.
                forbidden=0
                for i in range(13):
                    if x>>i&1:forbidden|=rot(y,(-i)%13)
                for z0 in allowed(b,c):
                    if z0.bit_count()+max(b.bit_count()+x.bit_count(),c.bit_count()+y.bit_count())>9:continue
                    for z in set(seq(z0)):
                        if z&forbidden:continue
                        rows=[p|(q<<13)|(r<<26) for p,q,r in zip(seq(a),seq(x),seq(y))]+[p|(q<<13)|(r<<26) for p,q,r in zip(seq(neg(x)),seq(b),seq(z))]+[p|(q<<13)|(r<<26) for p,q,r in zip(seq(neg(y)),seq(neg(z)),seq(c))]; counts['tested']+=1
                        R=(1<<39)-1
                        if any(independent_witness(rows,9,R&~(rows[i]|1<<i)) is not None for i in (0,13,26)):continue
                        assert triangle_free(rows) and independent_witness(rows,10) is None
                        print('SAT',a,b,c,x,y,z,counts,flush=True);Path(__file__).with_name('ramsey_3_10_three_rotating_rings_39.csv').write_text(''.join(','.join(str(r>>j&1) for j in range(39))+'\n' for r in rows));return
    print('UNSAT; internal triples modulo scaling and permutation',len(seen),'surviving full tables tested',counts['tested'])
if __name__=='__main__':main()
