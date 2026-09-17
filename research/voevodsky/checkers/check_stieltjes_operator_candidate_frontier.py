#!/usr/bin/env python3
"""Record the prior no-go boundary for source Stieltjes operator candidates."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[3]
dep=root/'research/grothendieck/theta-bernstein-fiber-spread-deutsch-popper-conjecture.md'
out={'schema':'marici.voevodsky.stieltjes-operator-candidate-frontier.v1','verified_prior_results':{
'free_carrier_measure_class':'absolutely continuous, incompatible with the required discrete meromorphic measure',
'scalar_ground_state_operator':'confining and bounded below, but reconstructed spectrum misses the first required rate near 200.04046',
'finite_order_two_tests':'ordinary Hankel through size 7 and shifted Hankel through size 6 survived at x=0.251,10,400 (reconnaissance, not interval proof)'},
'surviving_constructor':'label-retaining matrix/canonical system or arithmetic Jacobi operator','dependency':{'path':str(dep.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(dep.read_bytes()).hexdigest()},'passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'stieltjes_operator_candidate_frontier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
