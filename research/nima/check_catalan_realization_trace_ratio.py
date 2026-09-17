#!/usr/bin/env python3
"""Exact normalized-trace ratio for one forced-channel realization step."""
import json,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def cat(m):return math.comb(2*m,m)//(m+1)
rows=[]
for n in range(4,101):
 r=Fraction(cat(n-3),cat(n-2));formula=Fraction(n-1,2*(2*n-5));assert r==formula
 rows.append({'n':n,'proper_rank':cat(n-3),'full_rank':cat(n-2),'ratio_numerator':r.numerator,'ratio_denominator':r.denominator,'ratio_decimal':float(r),'distance_to_quarter':float(r-Fraction(1,4))})
checks={'exact_closed_form':all(Fraction(x['ratio_numerator'],x['ratio_denominator'])==Fraction(x['n']-1,2*(2*x['n']-5)) for x in rows),'strictly_decreasing_to_quarter_on_range':all(rows[i+1]['ratio_decimal']<rows[i]['ratio_decimal'] for i in range(len(rows)-1)),'n100_close':abs(rows[-1]['ratio_decimal']-.25)<.004}
out={'schema':'marici.nima.catalan-realization-trace-ratio.v1','range':[4,100],'operator':'Orthogonal projection from the full Catalan facet module onto the forced-channel/adjacent-swap submodule. Its normalized trace is rank(P_n)/dim(H_n).','limit':'1/4','exact_formula':'C_(n-3)/C_(n-2)=(n-1)/(2(2n-5))=1/4+3/(4(2n-5)).','sample_rows':rows[:6]+rows[13:17]+rows[-5:],'checks':checks,'passed':all(checks.values())}
p=ROOT/'research/nima/results/catalan-realization-trace-ratio.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'formula':out['exact_formula'],'n33':rows[29],'n100':rows[-1]},indent=2));raise SystemExit(0 if out['passed'] else 1)
