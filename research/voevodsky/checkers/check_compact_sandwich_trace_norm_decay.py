"""Exact finite-section witness for compact-sandwich trace-norm decay."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# On l2(Z), shifts S^L converge weakly to zero. K,H project onto fixed finite windows.
# K S^L H is exactly zero once the shifted right window misses the left window.
rows=[]
left=set(range(-2,3));right=set(range(-3,4))
for L in (0,1,2,4,6,8,12):
 overlap=len(left & {j+L for j in right})
 # Product of coordinate projections and a shift has 'overlap' singular values equal to one.
 rows.append({'shift':L,'overlap_rank':overlap,'trace_norm':str(F(overlap))})
checks={'initial_product_nonzero':F(rows[0]['trace_norm'])>0,'eventually_trace_norm_zero':all(F(r['trace_norm'])==0 for r in rows[-2:]),'tail_nonincreasing':all(F(rows[i+1]['trace_norm'])<=F(rows[i]['trace_norm']) for i in range(len(rows)-1))}
out={'schema':'marici.voevodsky.compact-sandwich-trace-norm-decay.v1','rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'Two fixed compact localizations around a weakly escaping shift force trace-norm decay; a single translated rank-one factor does not model the physical placement remainder.','theorem':'If U_L converges weakly to zero and K,H are Hilbert-Schmidt, then ||K U_L H||_1 tends to zero.'}
if __name__=='__main__':
 p=ROOT/'results'/'compact-sandwich-trace-norm-decay.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
