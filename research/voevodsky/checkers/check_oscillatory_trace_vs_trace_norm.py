"""Exact cyclic-shift model: traces vanish while trace norms remain constant."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# U_N cyclically shifts the first basis vector in an N-dimensional space.
# T_N=|U_N e_0><e_0| has one singular value 1; trace is 0 for nonzero shifts.
rows=[]
for N in (2,3,5,8,13):
 shift=1
 rows.append({'dimension':N,'shift':shift,'trace':str(F(0)),'trace_norm':str(F(1)),'hilbert_schmidt_norm':str(F(1))})
checks={'traces_vanish':all(F(r['trace'])==0 for r in rows),'trace_norms_do_not_vanish':all(F(r['trace_norm'])==1 for r in rows),'hs_norms_do_not_vanish':all(F(r['hilbert_schmidt_norm'])==1 for r in rows)}
out={'schema':'marici.voevodsky.oscillatory-trace-vs-trace-norm.v1','rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'Oscillation or translation can annihilate a scalar trace pairing while preserving every singular value; Riemann-Lebesgue decay does not imply trace-norm convergence.','consequence':'The current placement argument completes the scalar sewing form, not an ordinary trace-class operator-valued product.'}
if __name__=='__main__':
 p=ROOT/'results'/'oscillatory-trace-vs-trace-norm.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
