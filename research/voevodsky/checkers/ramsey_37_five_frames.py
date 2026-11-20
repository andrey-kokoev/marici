"""Test a five-frame rotation and a pole-swapping reversal on six-direction witnesses."""
import sys
from pathlib import Path
from itertools import permutations,product
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'chatgpt/ramsey'))
import check_ramsey_six_direction_bitransversals as w
f=lambda i:(i+1)%5 if i<5 else 5
r=[0]+[1+f(i) for i in range(6)]+[7+w.D_INDEX[frozenset(map(f,p))] for p in w.D]
cycles=[];seen={0,6}
for i in range(22):
    if i not in seen:
        c=[i];
        for _ in range(4): c.append(r[c[-1]])
        seen.update(c);cycles.append(c)
assert len(cycles)==4
for d in w.enumerate_transversals():
    A=w.graph(d);e=lambda i,j:A[i]>>j&1
    def auto(p):return all(e(i,j)==e(p[i],p[j]) for i in range(22) for j in range(i))
    if not auto(r):continue
    assert w.trianglefree(A) and w.alpha(A)==6
    hits=[]
    for perm in permutations(range(4)):
        if any(perm[perm[i]]!=i or e(0,cycles[i][0])!=e(6,cycles[perm[i]][0]) or e(6,cycles[i][0])!=e(0,cycles[perm[i]][0]) for i in range(4)):continue
        for offsets in product(range(5),repeat=4):
            if any(offsets[perm[i]]!=offsets[i] for i in range(4)):continue
            p=list(range(22));p[0],p[6]=6,0
            for i,c in enumerate(cycles):
                for k,v in enumerate(c):p[v]=cycles[perm[i]][(offsets[i]-k)%5]
            if auto(p):hits.append((perm,offsets))
    print('cycles',cycles,'fixed',0,6,'pole-swapping reversing involutions',len(hits),hits[:1]);
