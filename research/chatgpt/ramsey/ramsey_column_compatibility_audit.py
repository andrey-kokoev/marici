"""Direct seed-only test: compatibility triangles and the obstructions they leave."""
from collections import Counter
from itertools import combinations_with_replacement
from pauli_realization_audit import decode_graph6

SEEDS=[('20-stop',7,'SCiFEB_?H_?LHS?S?Qaog@`PGWHGBiwB?'),('22-stop',8,'U???Ca?BoO?OBPl_BS@?D@BJCK``G@NO@H@YONS?'),('22-grow',8,'UIchUIQ@`_@?@Gg?@GOc@@HEoS_eMA?bOHWGOGPG')]

def audit(name,s,code):
    a=decode_graph6(code);ind=[0]
    for i,r in enumerate(a):ind.extend([m|1<<i for m in ind if not(m&r)])
    assert max(m.bit_count() for m in ind)<s
    def level(k):return [m for m in ind if m.bit_count()==k]
    top,mid,low=map(level,(s-1,s-2,s-3));c=[m for m in ind if all(m&t for t in top)]
    pair={};degrees=[0]*len(c)
    for i,j in combinations_with_replacement(range(len(c)),2):
        u=c[i]|c[j]; edge=not(c[i]&c[j]);nonedge=all(t&u for t in mid)
        if edge or nonedge:pair[i,j]=(edge,nonedge);degrees[i]+=1;degrees[j]+=i!=j
    h=Counter();blockers=[];successful=0
    for i,j in pair:
        for k in range(j,len(c)):
            if (i,k) not in pair or (j,k) not in pair:continue
            opts=[pair[z] for z in ((i,j),(i,k),(j,k))];ways=1 if i==k else 3 if i==j or j==k else 6
            if all(not e for e,n in opts):
                u=c[i]|c[j]|c[k]; missed=[m for m in low if not(m&u)]
                if missed:h['all nonedges, old blocker']+=1;blockers.append(missed);continue
            if all(not n for e,n in opts):h['forced triangle']+=1;continue
            h['survives']+=1
            from itertools import product
            for links in product(*[[v for v,ok in ((1,e),(0,n)) if ok] for e,n in opts]):
                if sum(links)==3:continue
                if not any(links) and any(not(t&(c[i]|c[j]|c[k])) for t in low):continue
                successful+=ways
    print(name,'supports',len(c),'pair types',Counter(pair.values()),'loops',sum(i==j for i,j in pair),'unordered triangles',h,'ordered completions',successful)
    if blockers:
        common=set.intersection(*(set(L) for L in blockers));print('universal blocker supports',[[i for i in range(len(a)) if m>>i&1] for m in sorted(common)]);print('common blockers',len(common),'min/max blockers per triple',min(map(len,blockers)),max(map(len,blockers)))
    return successful

if __name__=='__main__':assert [audit(*v) for v in SEEDS]==[0,0,34122]
