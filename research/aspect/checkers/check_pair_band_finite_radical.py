#!/usr/bin/env python3
import json,math
from pathlib import Path
# Three diagonal labels have the same ratio shift D=0. W,J see only two moments.
a=0.37
ns=[1,2,3]
alpha=[n**(-1-2*a) for n in ns]
S=[2*math.log(n) for n in ns]
c=[alpha[1]*alpha[2]*(S[2]-S[1]),alpha[2]*alpha[0]*(S[0]-S[2]),alpha[0]*alpha[1]*(S[1]-S[0])]
m0=sum(ci*ai for ci,ai in zip(c,alpha))
m1=sum(ci*ai*si for ci,ai,si in zip(c,alpha,S))
checks={'packet_nonzero':max(abs(z) for z in c)>1e-8,'W_moment_zero':abs(m0)<1e-14,'J_product_moment_zero':abs(m1)<1e-14,'finite_support':len(c)==3,'same_ratio_shift':all(math.log(n/n)==0 for n in ns)}
out={'schema':'marici.aspect.pair-band-finite-radical-check.v1','passed':all(checks.values()),'a':a,'support':['(1,1)','(2,2)','(3,3)'],'coefficients':c,'moments':{'sum_c_alpha':m0,'sum_c_alpha_S':m1},'checks':checks,'conclusion':'The nonzero finite pair packet maps to W=0 and J=0 identically. Therefore the W,J synthesis has a finite-core kernel; no completion or choice of dual can make its source pairing radical-zero without quotienting or retaining more product-degree coordinates.'}
p=Path(__file__).resolve().parents[1]/'results/pair_band_finite_radical.check.v1.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
