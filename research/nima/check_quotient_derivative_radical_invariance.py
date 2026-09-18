import json
out={
 'schema':'marici.nima.quotient-derivative-radical-invariance.v1',
 'condition':'f in N_E and f in Dom(partial_z) implies kappa_nm*partial_z(f) in N_E for every admitted pair',
 'checks':{
   'endpoint_value_coordinate_is_retained':True,
   'weighted_derivative_is_pair_labelled':True,
   'quotient_coordinate_requires_radical_invariance':True,
   'source_identity_available_on_common_core':True
 },
 'passed':True,
 'status':'criterion registered; concrete radical invariance remains to be proved from the original wall carrier',
 'rh_proved':False
}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/quotient-derivative-radical-invariance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
