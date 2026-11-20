"""Flat zipper annulus: choose any full-layer simple alternating blue outer cycle jointly with a monotone cyclic triangulation. No new vertices; every cross edge must respect one common binary potential. Rotation convention: start when arriving at the least Z site and close with an outer step. Reject repeated bridges. Verify Euler, boundary and vertex links for positive certificates."""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations
import json
D=Path(__file__).resolve().parents[1]/'results';E=set(map(tuple,json.loads((D/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges']));red=lambda u,v:int(tuple(sorted((u,v))) in E);data=json.loads((D/'ramsey_38_correction_continuation.json').read_text());out=[]
def verify(faces,I,O):
    ed=Counter(tuple(sorted(e)) for f in faces for e in combinations(f,2));bound={tuple(sorted((x,y))) for L in [I,O] for x,y in zip(L,L[1:]+L[:1])};assert set(ed.values())=={1,2} and {e for e,v in ed.items() if v==1}==bound and len(I)+len(O)-len(ed)+len(faces)==0
    for u in I+O:
        link=defaultdict(set)
        for f in faces:
            if u in f:
                a,b=set(f)-{u};link[a].add(b);link[b].add(a)
        assert sorted(map(len,link.values()))==[1,1]+[2]*(len(link)-2);seen=set();q=[next(iter(link))]
        while q:
            v=q.pop();seen.add(v);q+=list(link[v]-seen)
        assert set(link)==seen
    assert all(sum(red(a,b) for a,b in combinations(f,2))%2==0 for f in faces)
def solve(o):
    I=o['ring'];m=len(I);Z=set(o['Z']);W=set(o['W']);l=2*len(Z);z=min(Z);p=o['poles'][0];trials=0
    for c in (0,1):
        ok={u:{v for v in Z|W if red(u,v)==(red(p,u)^c)} for u in I}
        for s,u in enumerate(I):
            if z not in ok[u]:continue
            def walk(i,outer,used,faces):
                nonlocal trials
                trials+=1;x=I[(s+i)%m];y=outer[-1];x1=I[(s+i+1)%m];start=(u,z)
                if i==m and len(outer)==l and not red(y,z):return outer,faces+[[x,y,z]]
                if i<m and y in ok[x1] and (x1,y) not in used:
                    sol=walk(i+1,outer,used|{(x1,y)},faces+[[x,y,x1]])
                    if sol:return sol
                if len(outer)<l:
                    for v in sorted(((W if y in Z else Z)&ok[x])-set(outer)):
                        if red(y,v):continue
                        sol=walk(i,outer+[v],used|{(x,v)},faces+[[x,y,v]])
                        if sol:return sol
            sol=walk(0,[z],{(u,z)},[])
            if sol:
                O,F=sol;assert len(F)==m+l;verify(F,I,O);return dict(outer=O,triangles=F,potential=c,states_tried=trials)
    return dict(outer=None,states_tried=trials)
for o in data:out.append(dict(ring=o['ring'],poles=o['poles'],**solve(o)))
print(sum(bool(o['outer']) for o in out),'of',len(out),'overall states',sum(o['states_tried'] for o in out));print(next((o for o in out if o['outer']),None));(D/'ramsey_38_annulus_glue.json').write_text(json.dumps(out,indent=2)+'\n')
