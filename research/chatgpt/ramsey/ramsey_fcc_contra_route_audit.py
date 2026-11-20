"""Read source route records. Preserve the outward multiset of move types; test nonliteral return and omitted-axis proxy."""
from pathlib import Path
from collections import Counter
import json
P=Path(__file__).resolve().parents[2]/'strominger'/'results'
f=json.loads((P/'fcc-first-transport.json').read_text());g=json.loads((P/'fcc-face-flag-binding.json').read_text());coords={v['id']:v['fcc'] for v in f['vertices']};edge={(m['source'],m['target']):tuple(m['sector']) for m in f['directed_moves']};rev=lambda a:a[::-1]
records={};hist=Counter()
for r in g['route_face_bindings']:
    a,b=r['diagonal'];m=r['middle'];records.setdefault((r['octahedron'],a,b),[]).append((m,(edge[a,m],edge[m,b])))
for (_,a,b),routes in records.items():
    assert len(routes)==4
    for m,(x,y) in routes:
        assert edge[b,m]==rev(y) and edge[m,a]==rev(x)
        matches=[w for w,(u,v) in routes if (u,v)==(y,x)];assert len(matches)==1 and matches[0]!=m
        w=matches[0];assert (edge[b,w],edge[w,a])==(rev(x),rev(y));assert set(x).isdisjoint(y)
        def omitted(u,v):
            zeros=[k for k,(i,j) in enumerate(zip(coords[u],coords[v])) if i==j];assert len(zeros)==1;return zeros[0]
        h,k=omitted(a,m),omitted(m,b);assert h==k==omitted(b,w)==omitted(w,a);hist[h]+=1
print('diagonals',len(records),'outward routes',sum(hist.values()),'unique nonretracing returns preserving sector multiset',sum(hist.values()),'same omitted FCC axis by coordinate',dict(sorted(hist.items())))
