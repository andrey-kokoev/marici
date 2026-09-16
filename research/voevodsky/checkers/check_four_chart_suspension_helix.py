"""Exact indexing model separating chart rotation, suspension, and realization dimension."""
import json
from pathlib import Path

def tau(state):
 k,r,h,i=state
 return (k,r,h,i+1) if i<4 else (k,r,h+1,1)
def sigma(state):
 k,r,h,i=state;return (k,r,h+1,i)
def power(f,x,n):
 for _ in range(n):x=f(x)
 return x
states=[(k,r,h,i) for k in range(3) for r in range(1,4) for h in range(-2,3) for i in range(1,5)]
checks={'tau_four_equals_suspension':all(power(tau,x,4)==sigma(x) for x in states),'tau_preserves_realization_dimension':all(tau(x)[0]==x[0] for x in states),'tau_preserves_convolution_regulator_rung':all(tau(x)[1]==x[1] for x in states),'sigma_preserves_k_r_and_chart':all(sigma(x)[0]==x[0] and sigma(x)[1]==x[1] and sigma(x)[3]==x[3] for x in states),'tau_sigma_commute':all(tau(sigma(x))==sigma(tau(x)) for x in states)}
out={'schema':'marici.voevodsky.four-chart-suspension-helix.v1','state_coordinates':['realization_dimension_k','convolution_or_regulator_rung_r','homological_degree_h','chart_i'],'transition':'tau(k,r,h,i)=(k,r,h,i+1) for i<4 and tau(k,r,h,4)=(k,r,h+1,1)','checks':checks,'all_exact':all(checks.values()),'meaning':'The four-chart helix closes in homological degree h while preserving realization dimension k and the independent convolution/regulator rung r.','physical_k_or_r_successor_constructed':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'four-chart-suspension-helix.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
