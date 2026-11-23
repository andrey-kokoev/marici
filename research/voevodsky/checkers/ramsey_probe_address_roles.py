"""Classify the source probes before using any wiring values or P/N/E map. Test all label permutations preserving the address catalogue and the allowed slots; if no such permutation exchanges the probes, neither can a subgroup preserving the wirings."""
from pathlib import Path
from itertools import permutations
import json
D=Path(__file__).resolve().parents[1];s=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=s['address_masks'];E=list(map(tuple,s['edge_order']));bits=lambda m:[i for i in range(7) if m>>i&1];profiles=[[sum(m.bit_count()==k and (m>>i)&1 for m in S) for k in (2,4)] for i in range(7)];orbits={i:set() for i in (0,4,6)};autos=0
for p in permutations(range(7)):
 T=[sum(1<<p[j] for j in bits(m)) for m in S];
 if set(T)!=set(S):continue
 idx=[S.index(t) for t in T];edges=[tuple(sorted((idx[a],idx[b]))) for a,b in E];
 if set(edges)!=set(E):continue
 autos+=1
 for i in orbits:orbits[i].add(E.index(edges[i]))
assert orbits[0].isdisjoint(orbits[6]);out=dict(probes={i:[bits(S[j]) for j in E[i]] for i in orbits},profiles=profiles,automorphisms=autos,slot_orbits={k:sorted(v) for k,v in orbits.items()});print(out);(D/'results/ramsey_probe_address_roles.json').write_text(json.dumps(out,indent=2)+'\n')
