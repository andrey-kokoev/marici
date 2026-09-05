"""Exact local residue audit after descent of centered xi to the squared coordinate."""
import json
from fractions import Fraction as Q
from pathlib import Path

def logarithmic_derivative_residue(multiplicity): return Q(multiplicity)
def F_residue(root,multiplicity): return Q(multiplicity)*(4*root-1)
fixtures=[]
for root in (Q(-4),Q(-9),Q(2,9),Q(7,3)):
    for multiplicity in (1,2,5):
        residue=F_residue(root,multiplicity)
        assert residue!=0
        fixtures.append({'root':str(root),'multiplicity':multiplicity,'F_residue':str(residue)})
for multiplicity in (1,2,5):
    assert F_residue(Q(1,4),multiplicity)==0
assert Q(1,4)==Q(1,2)**2==Q(-1,2)**2
result={
    'local_factorization':'G(t)=(t-tau)^m*h(t), h(tau)!=0',
    'logarithmic_derivative_residue':'m',
    'implemented_F_residue':'m*(4*tau-1)',
    'only_prefactor_cancellation_locus':'tau=1/4',
    'cancellation_locus_centered_preimages':['1/2','-1/2'],
    'cancellation_locus_s_preimages':['1','0'],
    'nontrivial_root_residue_uncancelled_if_tau_not_one_quarter':True,
    'fixtures':fixtures,
    'requires_entire_squared_coordinate_descent_from_xi_functional_equation':True,
    'requires_source_value_xi_zero_and_one_nonzero':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'xi-squared-coordinate-pole-residue.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
