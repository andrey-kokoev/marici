"""Same two-port leaf test, root 0 on the 39-vertex witness. Additionally test regular sign-word translations on induced four-vertex selections, not on exterior continuations."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import csv,json
H=Path(__file__).resolve().parents[1];src=H.parent/'chatgpt/ramsey/ramsey_3_10_witness_39.csv';A=[list(map(int,r)) for r in csv.reader(src.open()) if r];n=len(A);assert n==39 and all(A[i][j]==A[j][i] for i in range(n) for j in range(n));ports=[v for v in range(1,n) if A[0][v]];core=sorted(set(range(1,n))-set(ports));rows=[];hist=Counter()
for a,b in combinations(ports,2):
    leaves=[[v for v in core if (A[a][v],A[b][v])==s] for s in [(1,1),(1,0),(0,1),(0,0)]];ct=tuple(map(len,leaves));hist[ct]+=1;counts=Counter();ex=None
    for w,x,y,z in product(*leaves):
        if (A[w][x],A[w][y],A[w][z])!=(A[y][z],A[x][z],A[x][y]):continue
        nplus=sum((A[w][x],A[w][y],A[w][z]));counts[nplus]+=1
        if nplus and ex is None:ex=[w,x,y,z]
    rows.append(dict(ports=[a,b],sizes=ct,leaves=leaves,translation_squares_by_plus_matchings=counts,nonconstant_example=ex))
out=dict(root=0,ports=ports,core=core,order=['++','+-','-+','--'],rows=rows);(H/'results/ramsey_310_port_leaf_square.json').write_text(json.dumps(out,indent=2)+'\n');print(ports,len(core),hist);print('full',sum(min(r['sizes'])>0 for r in rows),'nonconstant',sum(r['nonconstant_example'] is not None for r in rows));print(rows[0]);print(next((r for r in rows if r['nonconstant_example']),None))
