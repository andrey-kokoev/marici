"""Exact controls for signed covariance and multiplicity; not a proof of RH.
Infinite-dimensional arguments are in the companion note, not inferred here.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT, ZERO, ONE, eye, mzero, mm, adj, rank
from check_rh_two_seed_route_audit import multiply_scalar


def diagonal(values):
    A=mzero(len(values),len(values))
    for i,v in enumerate(values):A[i][i]=(F(v),F(0))
    return A


def main():
    base=ROOT/'research/voevodsky'
    cp=base/'inputs/rh-covariance-quotient-v1.json'
    c=json.loads(cp.read_text())
    previous=ROOT/c['completion'];receipt=json.loads(previous.read_text())
    assert receipt['passed']
    for path,digest in receipt['source_hashes'].items():
        assert sha256(Path(path).read_bytes()).hexdigest()==digest,path
    # Synthetic conjugate node pairs; NOT a claim that zeta has these zeros.
    C=mzero(4,4)
    for i in range(4):C[i][i^1]=ONE
    H=multiply_scalar(C,F(1,2))
    S=diagonal([F(1,2),2,F(1,2),2])
    assert mm(C,C)==eye(4) and C==adj(C)
    assert mm(mm(adj(S),H),S)==H
    assert mm(adj(S),S)!=eye(4)
    e=[[ONE],[ZERO],[ZERO],[ZERO]]
    other=[[ZERO],[ONE],[ZERO],[ZERO]]
    assert mm(mm(adj(e),H),e)==[[ZERO]]
    assert mm(mm(adj(e),H),other)==[[(F(1,2),F(0))]]
    assert rank(H)==4 # The isotropic e is not radical.
    negative=[[ONE],[(F(-1),F(0))],[ZERO],[ZERO]]
    assert mm(mm(adj(negative),H),negative)==[[(F(-1),F(0))]]
    # Repeated scalar evaluations carry weights, not independent coordinates.
    V=[[ONE,ZERO],[ONE,ZERO],[ONE,ZERO],[ZERO,ONE]]
    weighted=diagonal([F(3,2),F(1,2)])
    assert mm(mm(adj(V),multiply_scalar(eye(4),F(1,2))),V)==weighted
    assert rank(V)==2
    D=diagonal([1,1,1,2]);d=diagonal([1,2])
    assert mm(D,V)==mm(V,d)
    invisible=[[(F(1),F(0))],[(F(-1),F(0))],[ZERO],[ZERO]]
    assert mm(adj(V),invisible)==mzero(2,1)
    # Half-divisor convention remains present in the resolvent Gram norm.
    # At z=i and nodes1,2, sum m/(2|u-z|^2)=3/4+1/10.
    assert F(3,2)/2+F(1,2)/5==F(17,20)
    result={
      'schema':'marici.rh-covariance-quotient.v1','iteration':10,'passed':True,
      'previous_receipt_hashes_fresh':True,
      'synthetic_off_axis_signed_covariance':True,
      'synthetic_off_axis_positive_unitarity':False,
      'isotropic_vector_need_not_be_radical':True,
      'multiplicity_weight_is_not_eigenspace_dimension':True,
      'repeated_coordinate_control':{'ambient_dimension':4,'scalar_evaluation_rank':2},
      'half_divisor_resolvent_norm_control':'17/20',
      'analytic_claims_in_note_not_machine_formalized':[
        'Translation invariance of each source form and intertwining on test/antidual carrier',
        'Atomic evaluation density by Gaussian-polynomial localization',
        'Radical equals kernel of divisor evaluation',
        'Under RH the positive quotient completes to weighted l2 on distinct nodes'],
      'all_test_positivity_proved':False,'RH_proved':False,
      'native_processing_equivalence_proved':False,
      'scope':c['scope']}
    files=[cp,previous,ROOT/c['completion_note'],ROOT/c['primary'],
           ROOT/c['paired_product_contract'],ROOT/c['count_note'],
           base/'rh-covariance-quotient-v1.md',Path(__file__)]
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in files}
    (base/'results/rh-covariance-quotient-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','analytic_claims_in_note_not_machine_formalized','scope')},indent=2))


if __name__=='__main__':main()
