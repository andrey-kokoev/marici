#!/usr/bin/env python3
"""Cross-check the infinite-phase asymptotic model against prior exact toys."""
import json,math,sys
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from coherence_chain_toy import connected_chain
fit=json.loads((ROOT/'research/nima/results/infinite-phase-power-renormalization.json').read_text());p=fit['parameters'];limit=fit['predicted_limit']
files={3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',20:'twenty',100:'hundred'};rows=[]
for k,name in files.items():
 artifact=json.loads((ROOT/f'research/nima/results/{name}-phase-coherence-history.json').read_text());h,_,c=connected_chain(k);v=h.component(c);exact_match=True
 if 'component_value' in artifact: exact_match=str(v)==artifact['component_value']
 else:
  import hashlib
  exact_match=hashlib.sha256((str(v.p)+'/'+str(v.q)).encode()).hexdigest()==artifact['component_sha256']
 g=float(s.N(-s.log(abs(v)),18));model=6*k*math.log(k)+p['d']*k+p['a']*math.log(k)+p['c']+p['b']/k;renorm=math.exp(-g+6*k*math.log(k)+p['d']*k+p['a']*math.log(k));rows.append({'k':k,'stored_exact_component_matches':exact_match,'action':g,'model_action':model,'action_residual':g-model,'renormalized_weight':renorm,'relative_limit_error':abs(renorm-limit)/limit})
errors=[r['relative_limit_error'] for r in rows]
checks={'all_prior_exact_artifacts_reproduced':all(r['stored_exact_component_matches'] for r in rows),'asymptotic_error_decreases_across_large_known_sections':rows[-1]['relative_limit_error']<rows[-2]['relative_limit_error']<rows[-3]['relative_limit_error'],'k100_within_one_percent_of_limit':rows[-1]['relative_limit_error']<0.01,'model_not_claimed_exact_at_small_k':rows[0]['relative_limit_error']>rows[-1]['relative_limit_error']}
out={'schema':'marici.nima.infinite-asymptotic-against-known-phases.v1','asymptotic_model':'6 k log k+d k+a log k+c+b/k','parameters':p,'predicted_limit':limit,'known_phase_checks':rows,'checks':checks,'passed':all(checks.values()),'scope':'Cross-validation against prior exact chain artifacts; tests this chosen moment-curve toy family, not other kinematics or physical amplitude sums.'}
path=ROOT/'research/nima/results/infinite-asymptotic-against-known-phases.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
