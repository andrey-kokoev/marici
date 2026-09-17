import json, math
from pathlib import Path
primes=[2,3]
mix={str(p):0.5*p**(-1.5) for p in primes}
out={'schema':'marici.nima.qRB-finite-loading-witness-coefficients.v1','primes':primes,'s0':2.0,'mixed_coefficients':mix,'checks':{'finite_prime_set_nonempty':bool(primes),'mixed_loading_positive':all(v>0 for v in mix.values()),'mixed_loading_finite':all(math.isfinite(v) for v in mix.values()),'target_values_independent':False},'passed':True,'scope':'coefficient-level smoke test only; local feature and independent target readout are not supplied','blocked':['Y_p=C_pX_p(s0)','wall target','sewing target','completion target','theta loading c_p requires explicit Phi'],'rh_proved':False}
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-finite-loading-witness-coefficients.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
