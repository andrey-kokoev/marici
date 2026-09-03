"""Compose the Arb center result with its two discharged side conditions."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results'
files={'center':'arb-dual-witness-center.json','digamma_tail':'digamma-gaussian-tail-bound.json','moment_tail':'integer-tail-moment-arb-bound.json'}
data={k:json.loads((root/v).read_text()) for k,v in files.items()}
checks={'center_conditional_certificate':data['center']['status']=='conditional_certificate','digamma_tail_passed':data['digamma_tail']['status']=='passed','moment_tail_passed':data['moment_tail']['status']=='passed'}
out={'schema':'marici.dual-center-composite-manifest.v1','status':'passed' if all(checks.values()) else 'failed','checks':checks,'inputs':files,'claim':'At the stated center, the frozen dual witness strictly separates the contact demand from every positive tail obeying the proved all-integer moment majorants.','scope':'single parameter point only; no continuum neighborhood claim'}
(root/'dual-center-composite-manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
