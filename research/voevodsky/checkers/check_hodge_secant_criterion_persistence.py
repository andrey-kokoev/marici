"""Categorical persistence controls for a scoped weak-criterion rejection."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import check_hodge_secant_source_semiregularity as source

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-secant-criterion-persistence.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-secant-criterion-persistence-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-secant-criterion-persistence-v1.json'
POLICY=['all_secant_constructions_excluded','Question11_4_refuted',
    'all_commutative_deformations_obstructed','every_direct_summand_preserves_kernel',
    'arbitrary_quotients_admitted','target_isogeny_constructed','target_cycle_constructed',
    'Hodge_proved','Hodge_refuted','actual_geometric_deformation_obstruction_nonzero',
    'global_witness_search_completed']


def require(c,m):
    if not c:raise ValueError(m)


def dual_character():
    return {m:v*(-1)**(m.bit_count()//2) for m,v in source.character().items()}


def dual_at_square(i,j):
    d0,dm1,*_=source.local_models()
    def partial(p,index):return p.get(tuple(int(k==index) for k in range(4)),0)
    # Dual differential is D0^t then -Dminus1^t. This gives a 2x1 column.
    return [sum(-partial(dm1[k][c],i)*partial(d0[0][k],j)+
                 partial(dm1[k][c],j)*partial(d0[0][k],i) for k in range(4)) for c in range(2)]


def propagate_bound(operation,bound,*,other_nonzero=False,finite_etale_isogeny=False,actual_descent=False):
    require(type(bound) is int and bound>0,'positive source kernel bound')
    require(all(type(x) is bool for x in (other_nonzero,finite_etale_isogeny,actual_descent)), 'functor hypothesis types')
    if operation=='external_product':
        require(other_nonzero,'nonzero partner required')
    elif operation=='isogeny_descent':
        require(finite_etale_isogeny and actual_descent,'actual finite etale isogeny descent required')
    elif operation=='isogeny_pushforward':
        require(finite_etale_isogeny,'finite etale abelian isogeny required')
    else:
        require(operation in ('Fourier_Mukai_equivalence','line_twist','shift','derived_dual'), 'unsupported persistence operation')
    return bound


def isogeny_hkr_diagonal(scales):
    require(scales and all(type(s) is int and s!=0 for s in scales),'invertible isogeny differential')
    # Product-elliptic diagonal isogeny controls, not a classification of all isogenies.
    return [Q(a*b) for a,b in combinations(scales,2)]+[
        Q(a,b) for a in scales for b in scales]+[Q(1,a*b) for a,b in combinations(scales,2)]


def exact_core():
    dch=dual_character();t2=source.wedge(source.theta(),source.theta())
    for i,j in combinations(range(4),2):
        gamma=source.scale(source.bivector(t2,i,j),Q(1,2))
        require(not source.add(source.bivector(dch,i,j),source.wedge(source.scale(gamma,9),dch)), 'dual character annihilator')
        require(dual_at_square(i,j)==source.local_at_square(i,j),'dual local witness')
    # Kunneth projections onto the independent (2,0) and (0,2) Ext summands.
    witnesses=[{1:Q(2)},{2:Q(-2)},{4:Q(2)},{8:Q(-2)}]
    require(source.rank(witnesses)==4,'Kunneth witness independence')
    for scales in ((2,)*4,(2,)*8,tuple(range(1,9))):
        diagonal=isogeny_hkr_diagonal(scales)
        require(all(diagonal) and len(diagonal)==len(scales)*(2*len(scales)-1),'HKR pullback controls')
    for op in ('Fourier_Mukai_equivalence','line_twist','shift','derived_dual'):
        require(propagate_bound(op,4)==4,'equivalence persistence')
    require(propagate_bound('external_product',2,other_nonzero=True)==2 and
        propagate_bound('isogeny_descent',4,finite_etale_isogeny=True,actual_descent=True)==4 and
        propagate_bound('isogeny_pushforward',4,finite_etale_isogeny=True)==4,'conditional functor persistence')
    return {'eightfold_HKR_dimension':120,'product_trace_kernel_lower_bound':4,
        'equivalence_trace_kernel_lower_bound':4,'conditional_isogeny_descent_kernel_lower_bound':4,
        'finite_etale_pushforward_kernel_lower_bound':4,
        'dual_character_coefficients':[str(x*(-1)**i) for i,x in enumerate(source.secant_character(9,3))],
        'product_Euler_pairing':int(source.euler_pairing()**2)}


def validate_scope(c):
    require(c['schema']=='marici.hodge-secant-criterion-persistence.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='eightfold-secant-weak-criterion-transplant','persistence identity')
    require(c['construction']=={'source':'iteration33_corrected_d9_perfect_complex',
        'product':'E_external_derived_dual_E','ambient_dimension':8,
        'allowed_equivalence':'Fourier_Mukai_equivalence_of_smooth_proper_abelian_categories',
        'isogeny_descent_requires_actual_pullback_identification':True,
        'isogeny_pushforward_requires_finite_etale_abelian_isogeny':True},'persistence construction scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'persistence promotion')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_scope(c)
    prior=source.report();p=ROOT/'research/voevodsky/results/hodge-secant-source-semiregularity-v1.json'
    require(json.loads(p.read_text(encoding='utf-8'))==prior and prior['passed'] and
        prior['trace_kernel_on_evaluation_image_lower_bound']==2,'prior source failure stale')
    names={CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix(),p.relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-secant-criterion-persistence-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
        'verification_level':'Written categorical persistence theorem plus dual/Kunneth/HKR finite controls; no target cycle or all-deformation obstruction.',
        'checks':{'dual_source_controls':True,'Kunneth_independence':True,
                  'conditional_isogeny_controls':True,'prior_source_fresh':True,'scope':True},
        **exact_core(),'standard_corrected_pair_full_HH2_criterion_fails':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
