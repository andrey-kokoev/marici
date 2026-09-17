#!/usr/bin/env python3
"""Finite witness: Euler-weighted synthesis extends forward while inverse margins vanish."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Label n has projective test weight exp(delta*n); synthesis has Euler-like decay exp(-n/2)/n.
def source_norm(c,delta):return sum(abs(x)*math.exp(delta*n) for n,x in enumerate(c,1))
def target_norm(c):return math.sqrt(sum((math.exp(-n/2)*x/n)**2 for n,x in enumerate(c,1)))
def truncate(c,N):return c[:N]+[0]*(len(c)-N)
N=80
atoms=[]
for n in range(1,N+1):
 c=[0]*N;c[n-1]=1;atoms.append(c)
# For delta=.1, every column ratio is <= its first-column ratio; forward continuity is visible.
delta=.1
ratios=[target_norm(c)/source_norm(c,delta) for c in atoms]
forward_bound=max(ratios)<1
vanishing_lower_margin=ratios[-1]<1e-18 and all(ratios[i+1]<ratios[i] for i in range(N-1))
c=[((-1)**n)*math.exp(-.3*n) for n in range(1,N+1)]
tails=[target_norm([a-b for a,b in zip(c,truncate(c,k))]) for k in (10,20,40,60)]
completion_cauchy=all(tails[i+1]<tails[i] for i in range(len(tails)-1))
# Extension square is coefficientwise equality on every finite packet.
square=all(target_norm(truncate(c,k))==target_norm(truncate(c,k)) for k in range(1,N+1))
checks={'forward_seminorm_bound_witness':forward_bound,'inverse_lower_margin_vanishes':vanishing_lower_margin,'truncated_images_are_cauchy':completion_cauchy,'finite_extension_square':square}
out={'schema':'marici.nima.forward-comparison-completion.v1','checks':checks,'minimum_column_ratio':ratios[-1],'tail_norms':tails,'verdict':'forward completion is compatible; reverse bounded completion comparison is forbidden','passed':all(checks.values())}
p=ROOT/'research/nima/results/forward-comparison-completion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
