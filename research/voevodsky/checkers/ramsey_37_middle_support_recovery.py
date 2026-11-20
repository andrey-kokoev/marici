"""Enumerate possible five-star families on the middle red adjacency alone, using necessary star axioms, then apply the observed opposite-family overlap law. Test ambiguity under exact automorphisms that also preserve each 3+7 cut. External star records are targets for comparison, not inputs to family enumeration."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());V=sorted(g['rows'][1]+g['rows'][2]);E={tuple(e) for e in g['red_edges'] if set(e)<=set(V)};F=lambda xs:frozenset(frozenset(s) for s in xs);actual=frozenset(F(x) for x in g['stars']);cand=[frozenset(x) for x in combinations(V,4) if all(e not in E for e in combinations(x,2))];families=[]
def rec(start,chosen):
    if len(chosen)==5:
        if all(sum(v in s for s in chosen)==2 for v in V):families.append(F(chosen))
        return
    for i in range(start,len(cand)):
        if all(len(cand[i]&s)==1 for s in chosen):rec(i+1,chosen+[cand[i]])
rec(0,[]);assert actual<=set(families);a,b=actual;pattern=sorted(len(s&t) for t in b for s in [next(iter(a))]);assert all(sorted(len(s&t) for t in y)==pattern for x,y in [(a,b),(b,a)] for s in x)
pairs=[(a,b) for a,b in combinations(families,2) if all(sorted(len(s&t) for t in y)==pattern for x,y in [(a,b),(b,a)] for s in x)];
# Enumerate all isomorphisms by backtracking on admissible images.
N={x:{y for y in V if tuple(sorted((x,y))) in E} for x in V};autos=[]
def iso(p,left,unused):
    if not left:autos.append(p);return
    opts=[([v for v in unused if len(N[u])==len(N[v]) and all((x in N[u])==(y in N[v]) for x,y in p.items())],u) for u in left];vs,u=min(opts,key=lambda z:len(z[0]));
    for v in vs:iso(p|{u:v},left-{u},unused-{v})
iso({},set(V),set(V));orbit=lambda p:frozenset(F([[p[v] for v in s] for s in fam]) for fam in actual);hist=Counter()
for cut in map(set,combinations(V,3)):hist[len({orbit(p) for p in autos if {p[v] for v in cut}==cut})]+=1
out=dict(middle_edges=len(E),independent_fours=len(cand),families=len(families),overlap_pattern=pattern,pairs=len(pairs),automorphisms=len(autos),unmarked_orbit=len({orbit(p) for p in autos}),cut_orbit_hist=dict(hist));print(out);(D/'ramsey_37_middle_support_recovery.json').write_text(json.dumps(out,indent=2)+'\n')
