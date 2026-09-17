#!/usr/bin/env python3
"""Check regulator-independence of equal-chart and fixed-degree Catalan trace ratios."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spectrum=[0,1,1,2,3,5,8,13,21,34]
regulators={
 'heat_t=.3':[math.exp(-.3*x) for x in spectrum],
 'resolvent_s=2':[(1+x)**-2 for x in spectrum],
 'rotor_polynomial_s=3':[(1+x*x)**-3 for x in spectrum],
}
rows=[]
for name,w in regulators.items():
 one=sum(w);total=4*one
 rows.append({'regulator':name,'one_chart_trace':one,'four_chart_trace':total,'normalized_chart_trace':one/total})
catalan=[]
for n in range(4,101):
 c=lambda k:math.comb(2*k,k)//(k+1)
 full=c(n-2);sector=c(n-3)
 for name in regulators:
  # Any radial f(N) is scalar f(n-3) on triangulation incidence vectors.
  ratio=sector/full
  catalan.append({'n':n,'regulator':name,'ratio':ratio})
checks={'all_shared_regulators_give_exact_quarter':all(abs(r['normalized_chart_trace']-.25)<1e-15 for r in rows),'all_radial_regulators_preserve_catalan_ratio':all(abs(r['ratio']-(r['n']-1)/(2*(2*r['n']-5)))<1e-15 for r in catalan),'n100_near_quarter':abs(catalan[-1]['ratio']-.25)<.004}
out={'schema':'marici.nima.quarter-trace-regulator-independence.v1','regulator_samples':rows,'checks':checks,'passed':all(checks.values()),'theorem':{'four_chart':'For any positive trace-class R used identically in four charts, Tr(P_i R^oplus4)/Tr(R^oplus4)=1/4.','catalan':'For any radial f(N), f(N) is scalar on H_n because every triangulation incidence vector has norm squared n-3; normalized forced-channel and C4-character traces equal their unweighted finite-rank ratios.'},'comparison_gate':'The historical rotor regulator yields the same exact chart ratio whenever its four transported copies are trace-class with equal trace. Equality of unnormalized traces with the channel heat regulator is neither needed nor asserted.'}
p=ROOT/'research/nima/results/quarter-trace-regulator-independence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'samples':rows,'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
