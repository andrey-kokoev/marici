"""Fixture-only synthetic codiagonal/Green composition audit."""
import json,sys
from fractions import Fraction
from pathlib import Path
sys.set_int_max_str_digits(0)
ROOT=Path('research/nima')
contract=json.loads((ROOT/'contracts/g4-radial-interface-candidate.v1.json').read_text())
source=json.loads((ROOT/'results/preconditioned_spline_weil.json').read_text())
assert contract['status']=='test_fixture_only'
assert contract['radial_codiagonal']['endpoint_coefficients']==[1,1]
assert contract['radial_codiagonal']['wronskian_coefficients']==[-0.5,-0.5]
lo,hi=map(Fraction,source['intervals']['gram'])
assert 0 < lo <= hi

# Synthetic composition data: these values test interface laws; they are not a G4 map.
def validate(arithmetic_coefficient=-2,pole_residue=0,metric=None):
 errors=[]
 if arithmetic_coefficient!=-2: errors.append('arithmetic_sign_or_factor_erased')
 if pole_residue!=0: errors.append('pole_annihilation_leak')
 metric = contract['green_form']['metric'] if metric is None else metric
 if metric!='declared_full_polarized_metric': errors.append('positive_scalar_promoted_to_metric')
 return errors

baseline=validate()
hostile={
 'sign_erasure':validate(arithmetic_coefficient=2),
 'pole_leak':validate(pole_residue=1),
 'one_scalar_as_metric':validate(metric=[str(lo),str(hi)]),
}
assert baseline==[]
assert hostile['sign_erasure']==['arithmetic_sign_or_factor_erased']
assert hostile['pole_leak']==['pole_annihilation_leak']
assert hostile['one_scalar_as_metric']==['positive_scalar_promoted_to_metric']
out={
 'schema':'marici.synthetic-zeta-g4-codiagonal-green.v1','status':'passed',
 'contract_status':'test_fixture_only','source_gram_positive':True,
 'source_gram_interval':[str(lo),str(hi)],'baseline_errors':baseline,
 'hostile_results':hostile,
 'claim_boundary':'The source scalar can populate one synthetic Green-form evaluation only; it neither supplies the declared full metric nor establishes a G4 comparison.'
}
(ROOT/'results/synthetic-zeta-g4-codiagonal-green.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'source_gram_interval':['positive rational lower bound','positive rational upper bound']}))
