"""Check archived independently computed turns against held-out execution bits."""
from pathlib import Path
from itertools import permutations
from collections import defaultdict,Counter
import json
D=Path(__file__).parent;load=lambda s:json.loads((D/(s+'.json')).read_text());v='ABCD';perms=list(permutations(v));t=load('ramsey_three_rim_axes')['vertex_cycle'];inv={a:b for b,a in t.items()};raw=load('ramsey_exit_triad_axis_lift');seam=set.intersection(*(set(f) for f in json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text())['retained_face_cycles']));maps=[p for p in perms if {p[0],p[3]}==seam];even=[p for p in perms if sum(x>y for i,x in enumerate(p) for y in p[i+1:])%2==0]
def orbit(mapping):return {tuple(p[v.index(mapping[v[p.index(a)]])] for a in v) for p in even}
T,U=orbit(t),orbit(inv);assert len(T)==len(U)==4 and not T&U;pred={}
for i,row in enumerate(raw):
    g=row['column_map'];assert sorted(g)==[1,2,3,4]
    for p in maps:
        z=tuple(p[g[p.index(a)]-1] for a in v);assert (z in T)^(z in U);pred[i,''.join(p)]=('native' if z in T else 'inverse',z==tuple(t[a] for a in v),z[v.index('A')]=='A')
# Outcome withheld until groups defined. No named-axis agreement required to predict arrival.
execs=load('ramsey_execution_rim_bit')['rows'];stats=Counter();fixed=defaultdict(set);rows=[]
for r in execs:
    i,p=r['row'],r['binding'];k,exact,atA=pred[i,p];arr=r['first'][1]==p[0];stats[k,arr]+=1;fixed[i,atA].add(arr);rows.append(dict(row=i,binding=p,turn=k,stationary_arrival=arr,exact=exact));assert arr==(k=='native') and arr!=r['native_order']
assert all(pred[0,''.join(p)][0]!=pred[1,''.join(p)][0] for p in maps);paths=[a['path'] for a in load('ramsey_boundary_role_table')];prefixes={}
for n in (2,3):
    ks=defaultdict(set)
    for w in paths:ks[tuple(w[:n])].add(w[-2]);prefixes[n]={str(k):sorted(vs) for k,vs in ks.items()}
r=dict(groups={str(k):n for k,n in stats.items()},rows=rows,fixed_axis_control={str(k):sorted(vs) for k,vs in fixed.items()},prefix_exit_choices=prefixes,constant_native_policy_maps=sum(all(pred[i,''.join(p)][0]=='native' for i in (0,1)) for p in maps));print(r);(D/'ramsey_unbound_turn.json').write_text(json.dumps(r,indent=2)+'\n')
