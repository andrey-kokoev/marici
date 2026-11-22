"""Execute the adjacent protocol. Compare only within the same marked layout."""
from pathlib import Path
import json,csv
from itertools import combinations,product
from collections import Counter
D=Path(__file__).parent

def graph(name):
    with (D/f'ramsey_3_7_{name}_22.csv').open() as f:m=[list(map(int,row)) for row in csv.reader(f)]
    o=[0]+sorted(range(1,21),key=lambda i:(-m[0][i],i));return [[m[i][j] for j in o] for i in o]

def read(m,q):
    a,b,c,d=q;return (m[a][c]+m[b][d],m[a][d]+m[b][c])

def borders(m):
    I=[0]
    for i,row in enumerate(m):
        h=sum(x<<j for j,x in enumerate(row));I.extend([s|1<<i for s in I if not s&h])
    six=[s for s in I if s.bit_count()==6];assert max(map(int.bit_count,I))==6;return [s for s in I if all(t&s for t in six)]

M=[graph(n) for n in ('pair_rotation','target_two_rings')];assert M[0][0]==M[1][0]==[0]+[1]*6+[0]*14
Q=[(*r,*b) for r,b in product(combinations(range(1,7),2),combinations(range(7,21),2))];reads=[[read(m,q) for m in M] for q in Q];B=list(map(borders,M));assert list(map(len,B))==[1,1];stats=Counter();examples={}
for q,(x,y) in zip(Q,reads):
    a,b,c,d=q;mask=1<<a|1<<c;ans=[any(s&mask==mask for s in sets) for sets in B];
    if ans[0]==ans[1]:continue
    stats['disagree']+=1
    for mode,v in dict(merged=sorted(x)==sorted(y),ordered=x==y,first=x[0]==y[0],second=x[1]==y[1],swap_only=x!=y and sorted(x)==sorted(y)).items():
        if v:stats[mode]+=1;examples.setdefault(mode,dict(layout=q,readings=[x,y],answers=ans,cross_edges=[[m[a][c],m[b][d],m[a][d],m[b][c]] for m in M]))
six=next(s for s in combinations(range(21),6) if all(M[0][3][v] or M[0][9][v] for v in s) and all(not M[0][i][j] for i,j in combinations(s,2)));r=dict(layouts=len(Q),counts=stats,examples=examples,negative_certificate_for_pair_3_9=six,positive_border=[i for i in range(21) if B[1][0]>>i&1]);print(r);D.joinpath('ramsey_37_mixed_incidence.json').write_text(json.dumps(r,indent=2)+'\n')
