"""Exhaust both diagonals and every one-link common exterior flip, including links to the root and ports. Cross-check legal verdicts via enumerated minus nines on every encountered triangle-safe proposal."""
from ramsey_310_diagonal_mode import A,N,U,H,core,has_ind
from itertools import combinations,product
from functools import lru_cache
from collections import Counter
import json,hashlib
from pathlib import Path

def indsets(s,k,chosen=0):
    if k==0:yield chosen;return
    while s.bit_count()>=k:
        b=s&-s;s-=b;yield from indsets(s&~N[b.bit_length()-1],k-1,chosen|b)
nines=list(indsets(U,9)); pairs=[(i,j) for i,j in combinations(range(39),2) if A[i][j]]
@lru_cache(None)
def triangle(s):
    t=s
    while t:
        b=t&-t;t-=b
        if N[b.bit_length()-1]&t:return True
    return False
@lru_cache(None)
def verdict(v,s):
    if triangle(s):return False
    T=U&~(s|1<<v);ok=not has_ind(T,9);assert ok==all(m&~T for m in nines);return ok

def main():
    count=Counter();example=None;base_trials=0
    for a,b in combinations([v for v in range(1,39) if A[0][v]],2):
        leaves=[[v for v in core if (A[a][v],A[b][v])==s] for s in [(1,1),(1,0),(0,1),(0,0)]]
        for q in product(*leaves):
            w,x,y,z=q;p=(A[w][x],A[w][y],A[w][z]);
            if not any(p) or p!=(A[y][z],A[x][z],A[x][y]):continue
            Q=sum(1<<j for j in q)
            for v in sorted(set(core)-set(q)):
                base=N[v]&~Q;diags=[base|(1<<w)|(1<<z),base|(1<<x)|(1<<y)];assert not any(verdict(v,s) for s in diags);base_trials+=1
                for u in range(39):
                    if u==v or (Q>>u)&1:continue
                    stars=[s^(1<<u) for s in diags];r=[verdict(v,s) for s in stars];count[sum(r)]+=1
                    if sum(r)==1 and example is None:
                        bad=stars[r.index(False)];cert=next(([v,i,j] for i,j in pairs if bad>>i&1 and bad>>j&1),None) or [v,*[i for i in range(39) if next(m for m in nines if not m&(bad|1<<v))>>i&1]]
                        example=dict(ports=[a,b],corners=q,reattached=v,flipped=u,flip_from_plus=bool(N[v]>>u&1),legal_by_diagonal=r,forbidden_clique=cert)
    assert base_trials==46748 and sum(count.values())==base_trials*34
    out=dict(trials=sum(count.values()),zero_flip_cases=base_trials,both_illegal=count[0],split=count[1],both_legal=count[2],example=example,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(out);(H/'results/ramsey_310_one_exterior_diagonal.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
