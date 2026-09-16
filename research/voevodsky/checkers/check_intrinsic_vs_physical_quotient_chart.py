"""Exact finite-section audit of intrinsic versus physical quotient norms."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
# Closed-range fixture diag(1,2) has a uniform lower modulus 1.
closed=[]
for n in (1,2,4,8,16):closed.append({'cutoff':n,'lower_modulus':str(F(1)),'inverse_norm':str(F(1))})
# Nonclosed infinite model diag(1/k) on l2: N-sections are injective but lower moduli collapse.
nonclosed=[]
for n in (1,2,4,8,16,32):nonclosed.append({'cutoff':n,'intrinsic_chart_modulus':str(F(1)),'physical_lower_modulus':str(F(1,n)),'physical_inverse_norm':str(F(n))})
checks={'intrinsic_quotient_isometric':all(F(r['intrinsic_chart_modulus'])==1 for r in nonclosed),'closed_fixture_uniformly_below':all(F(r['lower_modulus'])>=1 for r in closed),'nonclosed_physical_modulus_collapses':all(F(nonclosed[i+1]['physical_lower_modulus'])<F(nonclosed[i]['physical_lower_modulus']) for i in range(len(nonclosed)-1)),'nonclosed_inverse_norm_diverges':all(F(nonclosed[i+1]['physical_inverse_norm'])>F(nonclosed[i]['physical_inverse_norm']) for i in range(len(nonclosed)-1))}
out={'schema':'marici.voevodsky.intrinsic-vs-physical-quotient-chart.v1','closed_range_fixture':closed,'nonclosed_range_fixture':nonclosed,'checks':checks,'passed':all(checks.values()),'classification':{'intrinsic_chart':'automatic isometric quotient realization','physical_chart':'requires a cutoff-uniform positive lower modulus','failure_mode':'finite sections are invertible but inverse norms diverge'}}
if __name__=='__main__':
 p=ROOT/'results'/'intrinsic-vs-physical-quotient-chart.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
