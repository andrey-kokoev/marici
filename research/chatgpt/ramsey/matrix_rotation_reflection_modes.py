"""Enumerate the four specified actions and all two-input Boolean readouts.
Coordinates in CSV order, diagonal fixed to zero. Count information independent of
this sample by the components of the XOR comparison graph (D is its known zero).
"""
import csv,json
from pathlib import Path
from itertools import combinations,product
from collections import Counter
P=Path(__file__).parent
with (P/'ramsey_balanced_order_20.csv').open(newline='') as f:h,*rr=csv.reader(f)
M=[list(map(int,row[1:])) for row in rr];n=len(M);pairs=list(combinations(range(n),2));square=list(product(range(n),repeat=2));D=(-1,-1)
def edge(i,j):return tuple(sorted((i,j))) if i!=j else D
def evaluate(entries):
    parent={p:p for p in [D]+pairs}
    def root(p):
        while parent[p]!=p:p=parent[p]
        return p
    def bit(p):return 0 if p==D else M[p[0]][p[1]]
    hist=Counter();streams=[[] for _ in range(16)]
    for a,b in entries:
        parent[root(a)]=root(b);k=2*bit(a)+bit(b);hist[k]+=1
        for m in range(16):streams[m].append((m>>k)&1)
    return dict(outcomes=[hist[i] for i in range(4)],ones=[sum(s) for s in streams],xor_rank=len(pairs)+1-len({root(p) for p in parent}))

def turn(i,j,t):
    for _ in range(t):i,j=n-1-j,i
    return i,j
report={}
for t in range(4):
    for a in range(4):
        report[f'image:{t},{a}']=evaluate((edge(*turn(i,j,t)),edge(*turn(i,n-1-j,a))) for i,j in square)
for t,a in product(range(n),repeat=2):
    report[f'circle:{t},{a}']=evaluate((edge((i+t)%n,(j+t)%n),edge((a-i)%n,(a-j)%n)) for i,j in pairs)
    report[f'one_end:{t},{a}']=evaluate((edge(i,(j+t)%n),edge(i,(a-j)%n)) for i,j in square)
local=lambda i,d:(edge(i,(i+d)%n),edge(i,(i-d)%n))
for d in range(1,n//2+1):report[f'local:{d}']=evaluate(local(i,d) for i in range(n))
report['local:all']=evaluate(local(i,d) for d in range(1,n//2+1) for i in range(n))
for key in ('image:1,0','circle:1,0','one_end:1,0','local:1','local:all'):print(key,report[key])
(P/'matrix_rotation_reflection_modes.json').write_text(json.dumps(report,separators=(',',':')))
