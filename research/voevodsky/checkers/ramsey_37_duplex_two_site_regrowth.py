"""Hold 20 labelled sites fixed. Enumerate legal red neighborhoods for one new site and all compatible two-site completions, without requiring the old reflection or star readout. Distinguish forcing the graph from choosing a semantic center."""
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());E=set(map(tuple,g['red_edges']));V=sorted(set(range(22))-{17,19});N={x:{y for y in range(22) if tuple(sorted((x,y))) in E} for x in range(22)};assert all(not(N[x]&N[y]) for x,y in E);sets=[frozenset()]
for v in V:sets += [s|{v} for s in sets if not N[v]&s]
assert max(map(len,sets))==6;fives=[s for s in sets if len(s)==5];sixes=[s for s in sets if len(s)==6];legal=[s for s in sets if all(s&t for t in sixes)];pairs=[]
for a,b in combinations_with_replacement(range(len(legal)),2):
    x,y=legal[a],legal[b];
    if not x&y:pairs.append((a,b,'red'))
    if all((x|y)&t for t in fives):pairs.append((a,b,'blue'))
old=[legal.index(frozenset(N[v]&set(V))) for v in (17,19)];assert (*sorted(old),'blue') in pairs;refl=g['reflection'];invariant=[i for i,s in enumerate(legal) if set(map(refl.__getitem__,s))==s];fpairs=[p for p in pairs if p[0] in invariant and p[1] in invariant];print(len(sixes),len(fives),len(legal),len(pairs),len(invariant),len(fpairs),old);print('fixed',fpairs,'pairs',pairs[:12]);out=dict(core=V,blue_sixes=len(sixes),blue_fives=len(fives),legal_profiles=[sorted(s) for s in legal],unordered_completions=pairs,original_profiles=old,individually_reflection_fixed=invariant,fixed_completions=fpairs);(D/'ramsey_37_duplex_two_site_regrowth.json').write_text(json.dumps(out,indent=2)+'\n')
