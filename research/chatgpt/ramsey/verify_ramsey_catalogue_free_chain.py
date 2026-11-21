"""Independent output verifier: count independent sets by split-half subset DP (no constructor imports)."""
from pathlib import Path
import json
from itertools import combinations
D=Path(__file__).parent

def alpha(A):
    n=len(A);m=n//2;f=(1<<m)-1;ind=bytearray(1<<m)
    for s in range(1,1<<m):
        t=s&-s;i=t.bit_length()-1;ind[s]=max(ind[s^t],1+ind[(s^t)&~A[i]])
    best=0
    def visit(right,available,size):
        nonlocal best
        best=max(best,size+ind[available]);
        while right:
            t=right&-right;right^=t;i=t.bit_length()-1;visit(right&~A[i],available&~A[i],size+1)
    visit(((1<<n)-1)^f,f,0);return best

def verify(A,k):
    n=len(A);assert all(0<=a<1<<n and not a>>i&1 for i,a in enumerate(A));assert all((A[i]>>j&1)==(A[j]>>i&1) for i,j in combinations(range(n),2));assert all(not A[i]&A[j] for i,j in combinations(range(n),2) if A[i]>>j&1);a=alpha(A);assert a<k;return n,sum(map(int.bit_count,A))//2,a
if __name__=='__main__':
    short=json.loads((D/'ramsey_catalogue_free_short.json').read_text());long=json.loads((D/'ramsey_catalogue_free_chain.json').read_text());assert short['seed_graph']==long['seed_graph'];print('common seed',verify(long['seed_graph'],6));print('short',[verify(r['graph'],k) for k,r in enumerate(short['steps'],7)]);print('long',[verify(A,k) for k,A in enumerate(long['graphs'],6)])
