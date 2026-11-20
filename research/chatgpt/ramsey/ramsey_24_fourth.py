"""Exact 3->4 survival on two frozen R(3,9) seeds. Standard library only.
Candidate bitsets count all fourth columns at once. Reflection is not assumed.
"""
from itertools import combinations_with_replacement,product
from functools import lru_cache
from collections import Counter
from pauli_realization_audit import decode_graph6,triangle_free

SEEDS=[('unconditioned','W_LITmsa?G?GQOG?UO?DACAOc?R?gCkI?H@A?hA?_YGCBQM',103800),('conditioned','WiLITmsQ?K?OOOGCG??B_CASOO_@T?gG_H?ga?wODCJQoK?',1546047)]

def audit(name,code,expected):
    a=decode_graph6(code);assert triangle_free(a);ind=[0]
    for i,r in enumerate(a):ind += [x|1<<i for x in ind if not x&r]
    assert max(x.bit_count() for x in ind)==8
    lev={k:[x for x in ind if x.bit_count()==k] for k in range(5,9)}
    C=[x for x in ind if all(x&t for t in lev[8])];n=len(C);full=(1<<n)-1
    @lru_cache(None)
    def miss(t):return sum(1<<i for i,x in enumerate(C) if not x&t)
    @lru_cache(150000)
    def cover(k,u):
        # Fourth support must hit each k-set missed by the union u.
        forbidden=0
        for t in lev[k]:
            if not t&u:forbidden|=miss(t)
        return full^forbidden
    for k in (5,6,7):
        for t in lev[k]:miss(t)
    L=[[cover(7,x),miss(x)] for x in C]; hist=Counter();triangle_tests=0
    def indices(m):
        while m:
            b=m&-m;yield b.bit_length()-1;m-=b
    for i in range(n):
        for j in indices((L[i][0]|L[i][1]) & (full<<i)):
            for k in indices((L[i][0]|L[i][1])&(L[j][0]|L[j][1])&(full<<j)):
                pairs=((i,j),(i,k),(j,k));u=C[i]|C[j]|C[k];w=1 if i==k else 3 if i==j or j==k else 6
                # For repeated supports, canonical support order still retains ALL labeled link patterns.
                for links in product(*[[v for v in (0,1) if L[h][v]>>g&1] for h,g in pairs]):
                    if sum(links)==3 or (not any(links) and not cover(6,C[i]|C[j])>>k&1):continue
                    ways=0
                    for b,d,e in product((0,1),repeat=3):
                        cand=L[i][b]&L[j][d]&L[k][e]
                        if not cand:continue
                        for (h,g),old,(p,q) in zip(pairs,links,((b,d),(b,e),(d,e))):
                            if old and p and q:cand=0;break
                            if not(old or p or q):cand &= cover(6,C[h]|C[g])
                            if not cand:break
                        if cand and not(any(links) or b or d or e):cand &= cover(5,u)
                        ways+=cand.bit_count()
                    hist[ways]+=w
    assert sum(hist.values())==expected
    print(name,'triples',expected,'survive',expected-hist[0],'four-column extensions',sum(t*h for t,h in hist.items()),'max choices',max(hist),flush=True)

if __name__=='__main__':
    for args in SEEDS:audit(*args)
