"""Find a diagonal-swap witness with fixed exterior links and verify both full colorings directly. f is the 0/1 external plus-link indicator in (++,+-,-+,--) order."""
from pathlib import Path
from itertools import combinations,product
import csv,json
from functools import lru_cache
H=Path(__file__).resolve().parents[1];A=[list(map(int,r)) for r in csv.reader((H.parent/'chatgpt/ramsey/ramsey_3_10_witness_39.csv').open()) if r];U=(1<<39)-1;N=[sum(x<<j for j,x in enumerate(row)) for row in A]
@lru_cache(maxsize=100000)
def has_ind(t,k):
    if not k:return True
    while t.bit_count()>=k:
        b=t&-t;t-=b
        if has_ind(t&~N[b.bit_length()-1],k-1):return True
    return False
assert not has_ind(U,10) and not any(N[i]&N[j] for i,j in combinations(range(39),2) if A[i][j]);core=[v for v in range(1,39) if not A[0][v]]
def find():
    trials=both_legal=0
    for a,b in combinations([v for v in range(1,39) if A[0][v]],2):
        leaves=[[v for v in core if (A[a][v],A[b][v])==s] for s in [(1,1),(1,0),(0,1),(0,0)]]
        for q in product(*leaves):
            w,x,y,z=q;p=(A[w][x],A[w][y],A[w][z]);
            if not any(p) or p!=(A[y][z],A[x][z],A[x][y]):continue
            for v in set(core)-set(q):
                base=N[v]&~sum(1<<j for j in q);verdict=[]
                for i,j in [(w,z),(x,y)]:
                    s=base|(1<<i)|(1<<j);tri=next(((v,t,(N[t]&s & -(N[t]&s)).bit_length()-1) for t in range(39) if s>>t&1 and N[t]&s),None)
                    verdict.append(tri or ('minus10' if has_ind(U&~(s|1<<v),9) else 'legal'))
                trials+=1;both_legal+=int(verdict.count('legal')==2)
                if verdict.count('legal')==1:return dict(ports=[a,b],square=q,vertex=v,original=[A[v][j] for j in q],diagonal_verdicts=verdict)
    return dict(result='no separating diagonal on this fixed-exterior workload',trials=trials,both_legal=both_legal,both_illegal=trials-both_legal)
if __name__=='__main__':
    r=find();assert r;print(r);(H/'results/ramsey_310_diagonal_mode.json').write_text(json.dumps(r,indent=2)+'\n')
