#!/usr/bin/env python3
"""Import the stronger prior Grothendieck rank-six central Loewner certificate."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];p=ROOT/'research/grothendieck/results/central-rank-six-third-tensor-seven-chart-cover.json';d=json.loads(p.read_text())
checks={'all_8008_cells_covered':d['all_8008_ordered_half_grid_cells_covered'],'uniform_tensor_bound_below_ceiling':d['uniform_bound_below_required_ceiling'],
 'interval_certified':d['interval_certified'],'directed_rounding':d['directed_decimal_rounding'],'does_not_claim_RH':not d['rh_proved']}
assert all(checks.values())
out={'schema':'marici.voevodsky.prior-central-loewner-rank-six-import.v1','checks':checks,'passed':True,
 'domain':'ordered six-point simplex 0<=x1<=...<=x6<=0.01','rank':6,
 'uniform_third_tensor_l1_bound':d['uniform_third_tensor_l1_bound'],'required_ceiling':d['required_uniform_third_tensor_l1_ceiling'],
 'conclusion':'Prior research already certifies continuum central Loewner positivity through rank six; the new heat-cell rank-two/three work is weaker and should not be treated as the main frontier.',
 'next_gate':'rank seven and higher, extension beyond the certified central/complex region, or one rank-uniform source Gram factorization.',
 'dependency':{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},'rh_proved':False}
outp=ROOT/'research/voevodsky/results/prior_central_loewner_rank_six_import.json';outp.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
