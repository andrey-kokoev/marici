"""Scope/normalization controls; not a transcendence or moduli-coordinate computation."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['stacked_degree_two_constraint_rank']==65
    assert prior['degree_two_basis_size']==66
    # Exact Taylor expansion of exp(M*(z0+w))-2, using exp(M*z0)=2.
    # Transcendence of z0=log(2)/M is a written Lindemann consequence.
    M=2**20
    coefficients=[Q(0)]+[Q(2*M**n,factorial(n)) for n in range(1,9)]
    assert coefficients[0]==0 and coefficients[1]==2**21
    assert all(c>0 for c in coefficients[1:])
    for n in range(1,8):assert (n+1)*coefficients[n+1]==M*coefficients[n]
    # Dimension fixture only: a nonempty four-dimensional inclusion is not dominant in dimension9.
    inclusion=[[int(i==j) for j in range(4)] for i in range(9)]
    assert rank(inclusion)==4<9
    # Conditional rational trace arithmetic, not existence of a multisection.
    for denominator,degree in ((1,1),(2,3),(5,7)):
        class_sum=sum(Q(denominator) for _ in range(degree))
        assert class_sum/Q(denominator*degree)==1
    # Determinant monodromy units of the actual integral Gaussian lattice are finite.
    units=((1,0),(-1,0),(0,1),(0,-1))
    assert all(a*a+b*b==1 for a,b in units)
    result={'passed':True,'classification':'period_polynomial_genericity_does_not_supply_cycle_dominance',
        'original_Picard_certificate_retained':True,'analytic_coordinate_hostile_derivative':2**21,
        'actual_fixed_moduli_coordinates_computed':False,
        'fixed_moduli_algebraic_genericity_proved':False,
        'cycle_component_dominating_full_base_constructed':False,
        'control_locus_complex_dimension':4,'full_base_complex_dimension':9,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Construct relative rational cycles on a dense open of the product control locus from pointwise existence and countable parameter spaces.'}
    (root/'research/voevodsky/results/hodge-period-genericity-spread-audit-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
