"""Root 0; all nonconstant internally translation-invariant four-vertex transversals. Counterexample test: hold G-v fixed, transport only the four signs of the known legal star of v. v ranges over core vertices outside the transversal (neither defining port is used)."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import csv,json,hashlib
H=Path(__file__).resolve().parents[1];src=H.parent/'chatgpt/ramsey/ramsey_3_10_witness_39.csv';A=[list(map(int,r)) for r in csv.reader(src.open()) if r];N=[sum(x<<j for j,x in enumerate(r)) for r in A];n=39;V=(1<<n)-1
assert all(not(N[i]&N[j]) for i,j in combinations(range(n),2) if A[i][j]);
def vertices(s):
    while s:b=s&-s;yield b.bit_length()-1;s-=b

def independent(s,k,acc=0):
    if not k:yield acc;return
    while s.bit_count()>=k:
        b=s&-s;s-=b;yield from independent(s&~N[b.bit_length()-1],k-1,acc|b)
assert next(independent(V,10),None) is None
nines=list(independent(V,9));core=list(vertices(V&~(N[0]|1)));ports=list(vertices(N[0]));counts=Counter();examples={};unresolved=[]
for a,b in combinations(ports,2):
    leaves=[[v for v in core if (A[a][v],A[b][v])==s] for s in [(1,1),(1,0),(0,1),(0,0)]]
    for Q in product(*leaves):
        w,x,y,z=Q;pat=(A[w][x],A[w][y],A[w][z]);
        if not any(pat) or pat!=(A[y][z],A[x][z],A[x][y]):continue
        counts['square_instances']+=1
        for name,f in [('X',2),('Y',1),('XY',3)]:
            for v in core:
                if v in Q:continue
                old=N[v];s=old
                for j,q in enumerate(Q):
                    if A[v][q]!=A[v][Q[j^f]]:s^=1<<q
                if s==old:continue
                e=next(((i,j) for i in vertices(s) for j in vertices(N[i]&s) if i<j),None)
                if e is not None:kind='plus3';cl=[v,*e]
                else:
                    t=next((t for t in nines if not t&(s|(1<<v))),None)
                    if t is None:continue
                    kind='minus10';cl=[v,*vertices(t)]
                counts[name+'_refuted']+=1
                if (a,b,Q)==(1,6,(7,2,30,19)):examples[name]=dict(v=v,changed=[q for q in Q if (old^s)>>q&1],old_plus=[q for q in Q if old>>q&1],new_plus=[q for q in Q if s>>q&1],forbidden=kind,clique=cl)
                break
            else:unresolved.append([a,b,Q,name])
out=dict(test_counts=counts,prior_example=examples,unrefuted=unresolved,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(counts,examples,len(unresolved));(H/'results/ramsey_310_square_continuation.json').write_text(json.dumps(out,indent=2)+'\n')
