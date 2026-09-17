#!/usr/bin/env python3
"""Floating dyadic step-floor lower form for the monotone gamma multiplier."""
from pathlib import Path
exec(Path(__file__).with_name('scout_two_prime_gamma_tail_floor.py').read_text().split("rows=[]")[0])
# G0,P,E,integ,U,g are initialized by the shared scout prefix.
rows=[];prev=integ(U,False);H=G0+P+E
for k in range(12):
 R=U*(2**(k+1));cur=integ(R,False);floor=g(U*(2**k))/2
 H+=floor*(cur-prev);prev=cur
 # Outside R receives the current endpoint floor.
 trial=H+(g(R)/2)*(np.eye(N)-cur);trial=(trial+trial.T)/2;e=np.linalg.eigvalsh(trial)
 rows.append({'bands':k+1,'outer_radius':R,'min_eigenvalue':float(e[0]),'negative_count':int(np.count_nonzero(e<0))})
out={'schema':'marici.voevodsky.two-prime-dyadic-gamma-floor-scout.v1','L':L,'dimension':N,'rows':rows,'method':'monotone gamma multiplier bounded below on each dyadic band by its left endpoint; outer tail by final endpoint','status':'floating scout; relies on monotonicity and non-directed quadrature','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_dyadic_gamma_floor_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
