"""Ordered same-pole comparison at a shared middle position; count overlap with both opposite-pole stars through it. Signs use target minus source. Assert on every incidence, in each pole's local clock."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
g=json.loads((D/'ramsey_37_dual_stars.json').read_text()); addr=json.loads((D/'ramsey_37_star_addresses.json').read_text()); F=[[set(s) for s in f] for f in g['stars']]; edges={tuple(e) for e in g['red_edges']}; out=[]
for k,f in enumerate(F):
    p='pole'+str(6*k);succ=addr[p+'_successor'];other=F[1-k]
    for i,s in enumerate(f):
        for u,d in zip(addr[p][i],addr['powers']):
            j,=[n for n,z in enumerate(f) if n!=i and u in z];through=[t for t in other if u in t];assert len(through)==2
            support=lambda z:sum(len(z&t) for t in through)
            a,b=support(s),support(f[j]);delta=b-a;expected={1:-1,-1:1,2:1,-2:-1};assert delta==expected[d]
            v=addr[p][succ[i]][addr['powers'].index(d)];red=tuple(sorted([u,v])) in edges;assert red==(abs(d)==2)
            out.append(dict(pole=p,source=i,target=j,slot=u,local_step=d,support=[a,b],change=delta,continuation=v,red=red))
assert len(out)==40
(D/'ramsey_37_ordered_star_sign.json').write_text(json.dumps(out,indent=2)+'\n');print(out[:4]);print('40 ordered incidences passed')
