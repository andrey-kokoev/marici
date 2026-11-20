"""Identify endpoint-quarter-turn target cycle by local boundary flags among every ten-cycle, rather than by applying the global map."""
from ramsey_all_ten_cycle_layers import cycles,N
from ramsey_strip_layer_quarter_turn import C,r
from ramsey_strip_ordered_boundary_dualities import solutions,entry,exit
edge=lambda a,b:tuple(sorted((a,b)))
sets=[(set(p),{edge(a,b) for a,b in zip(p,p[1:]+p[:1])}) for p in cycles]
for f in solutions:
 if not all(f[f[x]]==r[x] for x in range(30)):continue
 target={f[x] for x in C};targetedges={edge(f[a],f[b]) for a,b in zip(C,C[1:]+C[:1])};boundary={e for e in targetedges if 0 in e or 29 in e};hits=[S for S,E in sets if boundary<=E and {r[x] for x in S}==S];assert target in hits
 oneleg={edge(0,16),next(e for e in boundary if 29 in e)};simple=[S for S,E in sets if oneleg<=E and {r[x] for x in S}==S]
 print('quarter-turn port bits',exit.index(f[entry[0]]),entry.index(f[exit[0]]),'target cycle',sorted(target),'shared with original',sorted(target&set(C)),'all four boundary flags candidates',len(hits),'one entry/exit flag candidates',len(simple));assert len(hits)==2
 remaining=[S for S in hits if S!=set(C)];assert remaining==[target]
 print('exclude the old cycle: unique alternative',True)
 print('local target cycle neighbors',[ (v,sorted(N[v]&target)) for v in (0,16,17,29)])
