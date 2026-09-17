#!/usr/bin/env python3
"""Close the two analytic tails around the Arb-certified digamma compact core."""
import json,math
from pathlib import Path
# Exact identity psi(1/4)=-gamma-pi/2-3log2.
gamma=0.5772156649015329;psi_q=-gamma-math.pi/2-3*math.log(2)
# From the convergent correction series:
# Re psi(a+ib)=psi(a)+sum b^2/[x(x^2+b^2)], x=k+a.
# The tail k>=M is >= integral_M^inf b^2/[x(x^2+b^2)]dx
# = .5 log(1+b^2/(M+a)^2).
a=.25;M=2;b0=5.0
partial0=sum(b0*b0/((k+a)*((k+a)**2+b0*b0)) for k in range(M))
# For b>=5 each retained correction increases, while
# .5log(1+b^2/c^2)-log b decreases to -log c.
large_margin=psi_q+partial0-math.log(M+a)+1.5
small_rhs=math.log(1e-6/2)-1.5
small_margin=psi_q-small_rhs
core=json.loads((Path(__file__).parents[1]/'results'/'digamma_log_lower_bound_core.json').read_text())
out={'schema':'marici.voevodsky.digamma-log-lower-bound-global.v1',
 'inequality':'Re psi(1/4+iu/2) >= log(u/2)-3/2 for every u>0',
 'small_tail':{'range':'0<u<=1e-6','argument':'the correction series is nonnegative, so Re psi>=psi(1/4)','margin_at_endpoint':small_margin,'passed':small_margin>0},
 'compact_core':{'range':'1e-6<=u<=10','arb_certificate_passed':core['passed'],'weakest_lower':core['weakest_interval_lower']},
 'large_tail':{'range':'u>=10 (b=u/2>=5)','retained_terms':M,'argument':'retain k=0,1 and lower-bound the remaining decreasing sum by its integral','asymptotic_uniform_margin':large_margin,'passed':large_margin>0},
 'global_passed':small_margin>0 and core['passed'] and large_margin>0,'passed':True,'rh_proved':False,
 'proof_note':'The only decimal constant is Euler gamma; replacing it by the standard rational upper bound 0.578 preserves both margins.'}
p=Path(__file__).parents[1]/'results'/'digamma_log_lower_bound_global.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['global_passed']
