"""For a new vertex with red neighborhood S, count new blue sevens and new red triangles. Compare both pole colors on the same S. Exact independent subsets and all six-spoke covers; verify the factorized marginal cost."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());V=range(22);p,q=0,6;P=(1<<p)|(1<<q);edges=set(map(tuple,g['red_edges']));M=g['rows'][1]+g['rows'][2];mask=lambda t:sum(1<<i for i in t);groups=[[mask((i,j)) for i,j in combinations(row,2) if (min(i,j),max(i,j)) not in edges] for row in g['rows'][1:3]];assert list(map(len,groups))==[5,5]
outs=[];ind=[];costs=[]
for bit in [1,0]:
    E=edges if bit else edges-{(p,q)};N=[mask([j for j in V if tuple(sorted((i,j))) in E]) for i in V];A=[0]
    for i in V:A += [s|(1<<i) for s in A if not s&N[i]]
    six={s for s in A if s.bit_count()==6};ind.append(set(A));cost={s:sum(not s&t for t in six) for s in A};costs.append(cost);m=min(cost.values());best=[s for s in A if cost[s]==m];hist=Counter();cover=None
    coverbits=[sum(1<<j for j,t in enumerate(sorted(six)) if t>>i&1) for i in V];allbits=(1<<len(six))-1
    for t in combinations(V,6):
        a,b,c,d,e,f=t
        if coverbits[a]|coverbits[b]|coverbits[c]|coverbits[d]|coverbits[e]|coverbits[f]!=allbits:continue
        s=mask(t);k=sum((N[i]&s).bit_count() for i in t)//2;hist[k]+=1
        if cover is None or k<cover[0]:cover=(k,t)
    outs.append(dict(pole_bit=bit,min_blue_sevens_if_no_red_triangle=m,optimal_sets=len(best),example=[i for i in V if best[0]>>i&1],best_by_number_of_red_pole_spokes=dict(Counter((s&P).bit_count() for s in best)),six_spoke_cover_min=cover,six_spoke_cover_hist=hist))
assert ind[0]<=ind[1];diff=Counter()
for s in ind[0]:
    delta=costs[1][s]-costs[0][s];expected=0 if s&P else sum(not s&t for t in groups[0])*sum(not s&t for t in groups[1]);assert delta==expected;diff[delta]+=1
extra=ind[1]-ind[0];assert all(s&P==P for s in extra);out=dict(cases=outs,common_triangle_free_profiles=len(ind[0]),blue_only_profiles=len(extra),cost_change_on_common=diff,best_blue_only=min(costs[1][s] for s in extra));print(out);(D/'ramsey_37_pole_extension_cost.json').write_text(json.dumps(out,indent=2)+'\n')
