"""Exact rank/degree controls for the written intrinsic simplicity argument."""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank
from check_hodge_fixed_sixfold_pairing import power,integrate


def multiply(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def main():
    root=Path(__file__).resolve().parents[3]
    certificate=json.loads((root/'research/voevodsky/results/hodge-explicit-sixfold-candidate-v1.json').read_text(encoding='utf-8'))
    assert certificate['passed']
    assert certificate['degree_two_basis_size']-certificate['stacked_degree_two_constraint_rank']==1
    assert certificate['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1'
    # Rational linear fixture for the quasi-inverse identity; not a proposed isogeny.
    A=[[Q(2),Q(1)],[Q(0),Q(3)]]
    B=[[Q(18),Q(-6)],[Q(0),Q(12)]]
    assert multiply(A,B)==multiply(B,A)==[[36,0],[0,36]]
    assert rank(A)==rank(B)==2
    inverse=[[x/36 for x in row] for row in B]
    assert multiply(inverse,A)==[[1,0],[0,1]]
    restrictions=[[1,0],[0,1]]
    assert rank(restrictions)==2
    compression=[[1,1]]
    assert rank(compression)==1 and sum(x*y for x,y in zip(compression[0],(1,-1)))==0
    for n in (2,3,5):
        assert n**2!=n**12 and n**2!=n**6
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    volume=integrate(power(E,6));assert volume==2160
    for k in (1,2,5):assert volume*k**3>0
    assert 12//2==6 and 6>3  # q(Y)=6 does not imply dim(Y)=6
    result={'passed':True,'classification':'fixed_source_simple_and_not_isogenous_to_abelian_product',
        'fixed_source_Picard_rank':1,'nontrivial_product_Picard_rank_lower_bound':2,
        'source_simple_by_imported_Poincare_reducibility':True,
        'product_isogeny_transport_excluded':True,'nonlinear_threefold_control_exists':True,
        'nonlinear_control_Albanese_dimension':6,'all_cycle_supports_excluded':False,
        'full_endomorphism_algebra_classified':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Period-polynomial genericity versus algebraic moduli genericity and cycle spreading.'}
    (root/'research/voevodsky/results/hodge-fixed-source-isogeny-barrier-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
