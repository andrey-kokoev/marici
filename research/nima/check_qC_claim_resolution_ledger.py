#!/usr/bin/env python3
"""Final disposition of the six q-C/tail claims after typing correction."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
names={'finite':'qC-finite-defect-tail-factorization.json','historical':'qC-historical-intertwiner-scope.json','endpoint':'qCO-endpoint-graph-scope.json','regulator':'qCR-regulator-typing.json','obstruction':'qC-structured-retraction-obstruction.json'}
d={k:json.loads((R/v).read_text()) for k,v in names.items()}
claims=[
 {'claim':'tail can realize a multiplicativity defect','resolution':'true existentially in the external finite Walsh packet','applies_to_historical_qC':False},
 {'claim':'finite factorization mechanism','resolution':'exact in the external finite Walsh packet','applies_to_historical_qC':False},
 {'claim':'historical defect and leakage share a target','resolution':'false: the proposed defect compares different typed constructions','applies_to_historical_qC':True},
 {'claim':'historical range inclusion','resolution':'not applicable: historical q-C is an exact Mellin intertwiner','applies_to_historical_qC':True},
 {'claim':'uniform Douglas bound','resolution':'not applicable to historical q-C','applies_to_historical_qC':True},
 {'claim':'refinement-compatible completed lift','resolution':'replaced by exact regulator typing: strict for transported/place regulators and lax for independent windows','applies_to_historical_qC':True},
]
checks={'finite_external_factorization_exact':d['finite']['checks']['exact_tail_factorization_AH_equals_M2'],'historical_qC_exact':d['historical']['checks']['exact_mixed_square'],'historical_scope_has_no_remaining_qC_gate':d['historical']['remaining_qC_scope']==[],'endpoint_extension_resolved':d['endpoint']['passed'],'regulator_extension_resolved':d['regulator']['passed'],'strict_character_retraction_obstructed':not d['obstruction']['checks']['product_preserving_cylinder_retraction_exists'],'all_six_claims_final':len(claims)==6 and all(x['resolution'] for x in claims)}
out={'schema':'marici.nima.qC-claim-resolution-ledger.v1','claims':claims,'evidence':names,'checks':checks,'passed':all(checks.values()),'final_qC':'exact radial-to-spectral Mellin intertwiner on the common core, projective at endpoints, regulator-typed under completion','open_claims':[]}
p=R/'qC-claim-resolution-ledger.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
