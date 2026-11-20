"""Exact PAP on the 8D side/diagonal zero-sum space. Exhaust every permutation preserving the two five-blocks as an unordered partition (superset of affine seed symmetries)."""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import hashlib,json
L=[tuple(sorted((i,(i+d)%5))) for d in (1,2) for i in range(5)];blocks=[list(range(5)),list(range(5,10))];pairs=set(combinations(range(10),2));aff=[tuple(L.index(tuple(sorted(((a*i+b)%5,(a*j+b)%5)))) for i,j in L) for a in range(1,5) for b in range(5)]
orbits=[]
while pairs:
    i,j=min(pairs);o={tuple(sorted((p[i],p[j]))) for p in aff};orbits.append(o);pairs-=o

def neighborhood_tests(E):
    def complete(vs):return set(combinations(sorted(vs),2))
    if any(complete(s)<=E for s in combinations(range(10),3)) or any(not complete(s)&E for s in combinations(range(10),5)):return None
    minus4=[sum(1<<x for x in s) for s in combinations(range(10),4) if not complete(s)&E];plus2=[(1<<i)|(1<<j) for i,j in E];return {s for s in range(1024) if not any(s&m==m for m in plus2) and all(s&m for m in minus4)}

def contrast(E):
    A=[[int(tuple(sorted((i,j))) in E) for j in range(10)] for i in range(10)];C=[]
    for i in range(10):
        I=blocks[i//5];row=[]
        for j in range(10):
            J=blocks[j//5];row.append(25*A[i][j]-5*sum(A[i][v] for v in J)-5*sum(A[v][j] for v in I)+sum(A[u][v] for u in I for v in J))
        C.append(row)
    return C

def main():
    dec={}
    for mask in range(1<<len(orbits)):
        E=set().union(*(o for k,o in enumerate(orbits) if mask>>k&1));S=neighborhood_tests(E)
        if S is not None:dec[mask]=(E,S,contrast(E))
    assert len(dec)==4;counts=Counter();affine=0;off=0
    for swap in (0,1):
        for a in permutations(blocks[swap]):
            for b in permutations(blocks[1-swap]):
                p=a+b
                for k,(E,S,C) in dec.items():
                    for h,(F,T,D) in dec.items():
                        if not all(C[i][j]==D[p[i]][p[j]] for i in range(10) for j in range(i,10)):continue
                        counts[k,h]+=1;affine+=p in aff;off+=k!=h
                        # Stronger check: full adjacency is transported, hence all subsequent extensions transport fixing fresh labels.
                        assert {tuple(sorted((p[i],p[j]))) for i,j in E}==F
                        assert {sum(1<<p[i] for i in range(10) if s>>i&1) for s in S}==T
    out=dict(decoder_order='orbits sorted by least pair in side-then-diagonal labeling',admissible_masks={k:len(S) for k,(_,S,_) in dec.items()},permutations=28800,operator_matches=sum(counts.values()),affine_matches=affine,cross_decoder_matches=off,by_pair={str(k):v for k,v in counts.items()},checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_contrast_transport.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
