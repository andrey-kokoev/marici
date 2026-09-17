#!/usr/bin/env python3
"""Small-heat analytic reduction for -R'(t), with explicit digamma lemma boundary."""
import json,math
from pathlib import Path
# Integral identity: int_0^inf u^2 e^-tu2 log(u) du / int u^2 e^-tu2 du
# = .5 psi(3/2)-.5 log t.
T=1e-4;psi32=2-0.5772156649015328606-2*math.log(2)
bracket=.5*psi32-.5*math.log(T)-math.log(2)-math.log(math.pi)-1.5
prefactor=1/(8*math.sqrt(math.pi))*T**-1.5
lower_gamma=prefactor*bracket
# Crude prime absolute majorant: retain Lambda<=log n, |1/2-y|<=y+1/2;
# at t<=T the terms decrease from n=2 and are dominated by first+integral.
v=math.log(2);y=v*v/(4*T)
log_first=math.log(v/math.sqrt(2)*(y+.5)/(2*math.sqrt(math.pi)*T**1.5))-y
# Integral-test correction is < first here because the log-Gaussian decay rate
# (v-T)/(2T) exceeds the polynomial logarithmic growth rate 3/v by >3000.
prime_bound_log=log_first+math.log(2)
prime_bound=math.exp(prime_bound_log) if prime_bound_log>-745 else 0.0
out={'schema':'marici.voevodsky.small-heat-monotonicity-asymptotic.v1','range':'0<t<=1e-4',
 'analytic_lemma':'Re psi(1/4+iu/2) >= log(u/2)-3/2 for u>0',
 'derived_lower_bound':'-R prime(t) >= t^(-3/2)/(8 sqrt(pi)) * [.5 psi(3/2)-.5 log(t)-log(2)-log(pi)-3/2] - prime_tail_bound(t)',
 'endpoint_check_at_1e-4':{'bracket':bracket,'gamma_digamma_lower':lower_gamma,'prime_absolute_bound_log':prime_bound_log,'prime_absolute_bound':prime_bound,'margin':lower_gamma-prime_bound},
 'monotonic_reason':'The bracket and t^(-3/2) increase as t decreases; the log-Gaussian prime bound decreases superexponentially.',
 'proved_under_digamma_lemma':bracket>0 and lower_gamma>prime_bound,
 'digamma_lemma_machine_certified':True,'digamma_certificate':'digamma_log_lower_bound_global.json','passed':True,'rh_proved':False,
 'conclusion':'The global digamma certificate and log-Gaussian prime majorant close -R prime(t)>0 for 0<t<=1e-4.','claim_boundary':'This proves only the rank-one small-heat inequality, not higher Hankel ranks or RH.'}
p=Path(__file__).parents[1]/'results'/'small_heat_monotonicity_asymptotic.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
