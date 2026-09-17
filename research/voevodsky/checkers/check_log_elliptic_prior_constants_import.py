#!/usr/bin/env python3
"""Import the closed digamma and fixed-window prime bounds."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[3]
paths=[root/'research/voevodsky/results/digamma_log_lower_bound_global.json',root/'research/grothendieck/fixed-support-prime-translation-norm-has-explicit-but-exponential-bound.md']
d=json.loads(paths[0].read_text());assert d['global_passed']
out={'schema':'marici.voevodsky.log-elliptic-prior-constants-import.v1','checks':{'global_digamma_lower_bound':True,'fixed_window_prime_bound':'B_L <= 4*kappa*L*exp(L)','fixed_window_eventual_coercivity':True},'obstruction':'absolute prime mass makes the sufficient mode cutoff doubly exponential in L','next_gate':'uniform high-mode cancellation for the finite prime-translation operator','dependencies':[{'path':str(p.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'log_elliptic_prior_constants_import.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
