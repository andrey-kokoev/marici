"""Exact symmetry obstruction to intrinsic selection on the twelve directed sectors. Preserve sector cyclic order, not individual externally named A/B/C/D labels. For (3,8) mark the singleton and occupied points, retain the three missing pairs as an unordered family. For (3,9) inspect the prior eight-wiring family, then count possible equivariant readers after adding a point or an oriented sector. No target fitting."""
from ramsey_cube_pair_rules import G,V,D,json,combinations
from collections import Counter
src=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text());p=dict(zip('ABCD',('111','100','010','001')));opp=lambda v:''.join('1' if a=='0' else '0' for a in v)
def coord(v):return p[v] if v in p else opp(p[next(iter(set(p)-set(v[2:])))])
sectors={tuple(coord(v) for v in t['triangle']) for t in src['triangles_and_transports']};R=[g for g in G if {tuple(map(g,t)) for t in sectors}==sectors];assert len(R)==12 and all(g(v)==g(v,state=True) for g in R for v in V)
def orbits(S,group,act):return sorted({tuple(sorted({act(g,s) for g in group})) for s in S})
rows=[]
for s in V:
    H=[g for g in R if g(s)==s];lines=[tuple(sorted((v,opp(v)))) for v in V if v<opp(v) and v not in (s,opp(s))];quads=[tuple(sorted(u+v)) for u,v in combinations(lines,2)];orb=orbits(quads,H,lambda g,q:tuple(sorted(map(g,q))));assert len(orb)==1 and len(orb[0])==3;fans=[t for t in sectors if t[0]==s or t[1]==s];assert len(fans)==3
    # Use outer arrow tip to mark one intact line; return the union of the other two.
    choice={t:next(q for q in quads if t[2] not in q) for t in fans};assert set(choice.values())==set(quads) and all(tuple(sorted(map(g,q)))==choice[tuple(map(g,t))] for g in H for t,q in choice.items());rows.append(dict(singleton=s,orbit=orb[0],fan_to_quartet={'/'.join(t):q for t,q in choice.items()}))
state_orbits=orbits(V,R,lambda g,v:g(v,state=True));fixed=lambda H:[v for v in V if all(g(v,state=True)==v for g in H)];s=V[0];t=min(sectors);assert len({tuple(map(g,t)) for g in R})==12
rules=json.loads((D/'ramsey_cube_pair_rules.json').read_text());lookup={}
for key,cs in rules.items():
    for g in G:lookup[tuple(sorted(map(g,key.split())))]=set(g(v,state=True) for v in cs)
colors=[]
for O in state_orbits:
    c=Counter(len(set(O)&z) for z in lookup.values());colors.append(dict(states=O,always_red=c[len(O)],always_blue=c[0],variable=len(lookup)-c[0]-c[len(O)]))
r=dict(rotations=len(R),seven_quartets=rows,state_orbits=colors,unmarked_states=fixed(R),point_mark=dict(point=s,allowed=fixed([g for g in R if g(s)==s])),sector_mark=dict(sector=t,allowed=fixed([g for g in R if tuple(map(g,t))==t])));print(r);(D/'ramsey_sector_mark_selector.json').write_text(json.dumps(r,indent=2)+'\n')
