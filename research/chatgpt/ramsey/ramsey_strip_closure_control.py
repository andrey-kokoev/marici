"""Frozen 7+3 selectors versus all geometrically admissible half-routes, including failures. No closure labels used to choose rules. Keep ordered profile words as a separate comparison; distinguish absent bridge from count failure."""
from ramsey_strip_first_generator import N,r,fixed,fill
from pathlib import Path
from collections import Counter
import json
H=Path(__file__).parent;rules=[set(map(tuple,v)) for v in json.loads((H/'ramsey_strip_bridge_profiles.json').read_text())['whole']['examples']];dist=[]
for i in range(30):
    q=[i];d={i:0}
    for x in q:
        for y in N[x]-d.keys():d[y]=d[x]+1;q.append(y)
    dist.append(d)
out=[]
def visit(p,used):
    if len(p)<12:
        for y in sorted(N[p[-1]]-used):
            if (y in fixed)==(len(p)==11):visit(p+[y],used|{y,r[y]})
        return
    if p[1]>r[p[1]]:return
    s,t=p[0],p[-1];rem=set(range(30))-used;ok=bool(list(fill(rem)));ds=dist[s][t];bridges=[(s,i,j,t) for i in N[s] for j in N[t] if j in N[i]] if ds==3 else [];sig=None;selected=None
    if len(bridges)==1:
        sig=[tuple(dist[x][i] for i in bridges[0]) for x in p[1:-1]];selected=[[i+1 for i,z in enumerate(sig) if z in rule] for rule in rules]
    out.append(dict(path=p,bridge=bridges,profiles=sig,selected=selected,closes=ok,pole_distance=ds,isolated=sorted(x for x in rem if not N[x]&rem)))
for s in sorted(fixed&set(range(15))):visit([s],{s})
assert len(out)==40 and all(z['selected'] is not None and (list(map(len,z['selected']))==[3,3])==z['closes'] for z in out);print(Counter((z['closes'],z['pole_distance'],tuple(map(len,z['selected'])) if z['selected'] else None) for z in out));
for k in ['profiles','selected']:
    f=lambda z:json.dumps(z[k]);print(k,'shared values',len({f(z) for z in out if z['closes']}&{f(z) for z in out if not z['closes']}))
(H/'ramsey_strip_closure_control.json').write_text(json.dumps(out,indent=2)+'\n')
