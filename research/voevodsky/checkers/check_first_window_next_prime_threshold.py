#!/usr/bin/env python3
"""Register the proved first window and exact next support thresholds."""
import json,math,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[3];dep=root/'research/voevodsky/results/arb_cutoff_form_legendre_matrix.json';d=json.loads(dep.read_text())
out={'schema':'marici.voevodsky.first-window-next-prime-threshold.v1','first_window':{'L':7/20,'certificate_passed':d.get('passed',False),'minimum_pivot_lower_bound':'0.0017645830061413439'},'thresholds':{'prime_3_enters_at_L':math.log(3)/2,'prime_power_4_enters_at_L':math.log(4)/2},'active_channels_immediately_above_log3_over_2':[2,3],'next_gate':'directed bad-set concentration and finite Schur certificate for a declared L just above log(3)/2','dependency_sha256':hashlib.sha256(dep.read_bytes()).hexdigest(),'passed':bool(d.get('passed',False)),'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'first_window_next_prime_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
