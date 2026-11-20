"""Test a row-sensitive boundary condition on the 12 literal square exchanges. Orient each path by the first row's entry convention; identify its actual exit block by that row's literal BR and NN edges. Neither closure nor witness type enters the selection."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
from ramsey_strip_prism_proof import rep,r,X,P,T,labels,E
rows=('BRNN','BNRN');edge=lambda i,j:X.index(tuple(sorted((i,j))));pair=lambda i,j:tuple(sorted((i,j)))
records=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());paths={tuple(labels[rep(x)] for x in z['path'][1:-1]):z for z in records if (z['path'][0],z['path'][-1])==(0,29)}
def phase(p,rows):
 B=rows[0].index('B');Q,=[i for i,(a,b) in enumerate(zip(*rows)) if a==b=='N'];U=rows[0].index('R');f=pair(edge(B,Q),edge(U,Q));assert (f in T[p[1]-15])!=(f in T[r[p[1]]-15]);p=p if f in T[p[1]-15] else [r[x] for x in p];blocks=[P.index(pair(edge(w.index('B'),w.index('R')),edge(*[i for i,v in enumerate(w) if v=='N']))) for w in rows];return blocks.index(p[-2])
H=Counter();accepted=Counter()
for w,z in paths.items():
 ph=phase(z['path'],rows);assert ph==phase(z['path'],rows[::-1]);accepted[ph,len(w),z['closes']]+=1
 for i in range(len(w)-3):
    if tuple(sorted((w[i],w[i+3]))) not in E:continue
    v=w[:i+1]+w[i+3:];sh=phase(paths[v]['path'],rows);assert ph==1-sh and z['closes']==paths[v]['closes'];H[len(w),sh,z['closes']]+=1
print('long length / exit row of shorter route (0 first, 1 second) / closes:',sorted(H.items()));print('exit row / chosen length / closes',sorted(accepted.items()));assert sum(H.values())==12
