"""Uniform fixed-chart orbit experiment, no graph colors in group/orbit formation."""
from itertools import combinations,permutations
from collections import Counter
from pathlib import Path
import json
from ramsey_address_to_cube import S as nine
D=Path(__file__).parent;load=lambda n:json.loads((D/n).read_text());norm=lambda x:min(x,x^255)
def audit(S,W):
    n=max(S).bit_length();E=[ij for ij in combinations(range(len(S)),2) if not S[ij[0]]&S[ij[1]]];ix={e:i for i,e in enumerate(E)};G=[];subs=[tuple(j for j in range(n) if s>>j&1) for s in S];inv={s:i for i,s in enumerate(S)}
    for p in permutations(range(n)):
        try:m=[inv[sum(1<<p[j] for j in t)] for t in subs]
        except KeyError:continue
        G.append((p,[ix[tuple(sorted((m[i],m[j])))] for i,j in E]))
    todo=set(range(len(E)));O=[]
    while todo:
        i=min(todo);orb=sorted({g[i] for _,g in G});todo-=set(orb);O.append(orb)
    encode=lambda w,o:sum((w>>a&1)<<j for j,a in enumerate(o));actions=set();invol=set()
    for p,g in G:
        action=tuple(W.index(sum((w>>i&1)<<k for i,k in enumerate(g))) for w in W);actions.add(action)
        if any(i!=j for i,j in enumerate(p)) and all(p[j]==i for i,j in enumerate(p)):invol.add(action)
    col=[sum((w>>i&1)<<j for j,w in enumerate(W)) for i in range(len(E))];B=sorted({norm(x) for x in col if x.bit_count()==4});sets=[]
    for t in combinations(B,3):
        if len({tuple(x>>i&1 for x in t) for i in range(8)})<8:continue
        if all({norm(sum((x>>i&1)<<k for i,k in enumerate(a))) for x in t}==set(t) for a in actions):sets.append(t)
    small=[]
    for o in O:
        codes=[encode(w,o) for w in W];small.append(dict(size=len(o),representative=[S[j] for j in E[o[0]]],states=len(set(codes)),splits=len({norm(col[i]) for i in o}-{0})))
    cut=[]
    for k in sorted({len(o) for o in O}):
        u=sorted(i for o in O if len(o)<=k for i in o);code=[encode(w,u) for w in W];cut.append(dict(max_orbit=k,probes=len(u),states=len(set(code)),move_spectrum=sorted({(code[i]^code[a[i]]).bit_count() for a in invol for i in range(8)})))
    return dict(group=len(G),actions=len(actions),orbit_report=small,cutoffs=cut,balanced_splits=len(B),invariant_Q3=sets,representative_links=[[[list(subs[j]) for j in E[next(i for i,v in enumerate(col) if norm(v)==x)]] for x in t] for t in sets])
a=load('ramsey_seven_all_wirings.json');assert [list(e) for e in combinations(range(len(a['address_masks'])),2) if not a['address_masks'][e[0]]&a['address_masks'][e[1]]]==a['edge_order'];r={'3,8':audit(a['address_masks'],a['wirings']),'3,9':audit(nine,load('ramsey_nine_frame_readout.json')['coordinate_ordered_wirings'])};print([(k,v['group'],v['actions'],v['balanced_splits'],len(v['invariant_Q3']),v['cutoffs'],[(o['size'],o['splits']) for o in v['orbit_report'] if o['states']==8]) for k,v in r.items()]);(D/'ramsey_intrinsic_cube_orbits.json').write_text(json.dumps(r,indent=2)+'\n')
