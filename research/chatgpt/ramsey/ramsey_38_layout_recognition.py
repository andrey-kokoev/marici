"""Exact layout recognition: clique on compatible injective ordered columns, Python int bitsets."""
from itertools import permutations,combinations
from ramsey_38_cube_inversion import sign
from time import monotonic
import sys

def find(n,e,k,seconds):
 for pattern in (3,1,0,7):
    cols=[c for c in permutations(range(n),3) if sum(e(c[i],c[j])<<h for h,(i,j) in enumerate(combinations(range(3),2)))==pattern];N=len(cols);full=(1<<N)-1
    at=[[0]*n for _ in range(3)]
    for h,c in enumerate(cols):
        for i,v in enumerate(c):at[i][v]|=1<<h
    red=[[sum(at[i][w] for w in range(n) if e(v,w)) for v in range(n)] for i in range(3)];adj=[]
    for c in cols:
        m=full
        for v in c:m&=~(at[0][v]|at[1][v]|at[2][v])
        for i,j in combinations(range(3),2):m&=~(red[j][c[i]]^red[i][c[j]])
        adj.append(m)
    end=monotonic()+seconds;nodes=0
    def dfs(m,left):
        nonlocal nodes
        nodes+=1
        if nodes%8192==0 and monotonic()>end:raise TimeoutError
        if not left:return []
        while m.bit_count()>=left:
            b=m&-m;m^=b;v=b.bit_length()-1;r=dfs(m&adj[v],left-1)
            if r is not None:return [cols[v]]+r
    try:r=dfs(full,k);print('pattern',pattern,'nodes',nodes,'layout',r,flush=True)
    except TimeoutError:print('pattern',pattern,'timeout',nodes,flush=True);continue
    if r:
        assert len(set(sum((list(c) for c in r),[])))==3*k and all(e(x[i],y[j])==e(y[i],x[j]) for x,y in combinations(r,2) for i,j in combinations(range(3),2));return r
if __name__=='__main__':find(27,sign,int(sys.argv[1]) if len(sys.argv)>1 else 8,10)
