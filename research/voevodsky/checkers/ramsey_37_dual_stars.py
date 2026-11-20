"""Recover both five-star systems from red adjacency, then test their transport by a full-graph pole reflection. First compatible example in the existing enumeration."""
from pathlib import Path
from itertools import combinations
import sys,json
H=Path(__file__).resolve().parents[1];sys.path.insert(0,str(H.parent/'chatgpt/ramsey'));import check_ramsey_six_direction_bitransversals as w
rows=[[1,2,3,4,5],[7,12,16,19,10],[8,13,17,9,14],[11,15,18,20,21]];mid=sorted(rows[1]+rows[2]);r=list(range(22));s=list(range(22));s[0],s[6]=6,0
for i,row in enumerate(rows):
    for k,v in enumerate(row):r[v]=row[(k+1)%5];s[v]=rows[[3,1,2,0][i]][([0,1,4,0][i]-k)%5]
for d in w.enumerate_transversals():
    a=w.graph(d);e=lambda u,v:a[u]>>v&1
    if all(e(p[u],p[v])==e(u,v) for p in [s,r] for u,v in combinations(range(22),2)):break
else:raise AssertionError
assert w.alpha(a)==6 and w.trianglefree(a) and all(s[s[u]]==u and s[r[s[r[u]]]]==u for u in range(22))
stars=[[{u for u in mid if e(u,v)} for v in row] for row in (rows[0],rows[3])];assert all({s[u] for u in x}==stars[1][-i%5] for i,x in enumerate(stars[0]));operators=[]
for family in stars:
    assert all(len(x)==4 for x in family) and all(len(x&y)==1 for x,y in combinations(family,2)) and all(sum(u in x for x in family)==2 for u in mid)
    L={u:{v for v in mid if v!=u and any({u,v}<=x for x in family)} for u in mid};operators.append(L)
    for x in family:
        g={u:5*int(u in x)-2 for u in mid};assert all(sum(g[v] for v in L[u])==g[u] for u in mid)
assert operators[0]!=operators[1];fixed=[v for v in range(22) if s[v]==v];assert len(fixed)==2
out=dict(rows=rows,reflection=s,central_pairs={v:sorted(w.D[v-7]) for v in mid},stars=[list(map(sorted,f)) for f in stars],fixed=fixed,red_edges=[(u,v) for u,v in combinations(range(22),2) if e(u,v)]);(H/'results/ramsey_37_dual_stars.json').write_text(json.dumps(out,indent=2)+'\n');print('verified two K5 star systems, two distinct line-graph operators, fixed pair states',fixed)
