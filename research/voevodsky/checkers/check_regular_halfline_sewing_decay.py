"""Exact soluble regular half-line sewing decay fixture."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
rows=[]
for T in (1,2,4,8,16,32,64):
 piE=F(T,1+T*T)
 rows.append({'T':T,'pi_times_sewing':str(piE),'positive':piE>0,'at_most_inverse_T':piE<=F(1,T),'scaled_T_piE':str(T*piE)})
checks={'all_positive':all(r['positive'] for r in rows),'inverse_frequency_bound':all(r['at_most_inverse_T'] for r in rows),'strict_decay_samples':all(F(rows[i+1]['pi_times_sewing'])<F(rows[i]['pi_times_sewing']) for i in range(len(rows)-1)),'scaled_T_piE_increases_to_one':all(F(rows[i+1]['scaled_T_piE'])>F(rows[i]['scaled_T_piE']) for i in range(len(rows)-1))}
out={'schema':'marici.voevodsky.regular-halfline-sewing-decay.v1','observer_boundary':'h(-u)=exp(u) for u<0','exact_formula':'E_T=T/(pi*(1+T^2))','rows':rows,'checks':checks,'all_exact':all(checks.values()),'meaning':'The regular translation-invariant sewing cell decays exactly at order 1/T and therefore vanishes simultaneously at every dyadic depth.','semilocal_gate':'Construct recentering maps for the prolate transition and observer Hankel blocks and prove summable norm-one-fiber descent.'}
if __name__=='__main__':
 p=ROOT/'results'/'regular-halfline-sewing-decay.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
