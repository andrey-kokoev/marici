"""Cyclotomic root-ratio exclusion; absolute simplicity of one auxiliary Prym."""
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json
from check_hodge_asymmetric_frobenius import report as frobenius_report
from check_hodge_indecomposable_principal_model import report as target_report
from check_hodge_asymmetric_scalar_cover import modgcd_degree

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-asymmetric-absolute.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-asymmetric-absolute-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-asymmetric-absolute-v1.json'
POLICY=['Prym_End0_computed','all_scalar_parameters_excluded','conditional_root_census_changed',
    'actual_cover_matching_Y2_constructed','theta_dimension_computed','finite_field_cycles_transferred_to_X',
    'Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved','algebraic_representative_of_alpha_constructed',
    'all_cycle_annihilation_proved','global_witness_search_completed']


def require(c,m):
    if not c: raise ValueError(m)


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)


def monic_quotient(a,b):
    require(b[-1]==1,'monic cyclotomic divisor')
    a=list(a);q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b);v=a[-1];q[k]=v
        for j,c in enumerate(b): a[k+j]-=v*c
        a=list(trim(a))
    require(not any(a),'cyclotomic exact division')
    return trim(q)


@lru_cache(maxsize=None)
def cyclotomic(m):
    require(type(m) is int and m>=1,'positive cyclotomic order')
    f=(-1,)+(0,)*(m-1)+(1,)
    for d in range(1,m):
        if m%d==0: f=monic_quotient(f,cyclotomic(d))
    return f


def possible_orders(degree):
    # phi(m)^2 >= m/2, so this is a proven finite search, not a cutoff guess.
    limit=2*degree*degree
    phi=list(range(limit+1))
    for p in range(2,limit+1):
        if phi[p]==p:
            for k in range(p,limit+1,p): phi[k]-=phi[k]//p
    return [m for m in range(2,limit+1) if phi[m]<=degree]


def ratio_polynomial(c,q,ell):
    """Ascending coefficients mod ell of product_(i,j)(T-alpha_i/alpha_j).

    c is descending monic Frobenius characteristic coefficients. Reciprocity
    makes the ratio power sums s_k^2/q^k. Newton divisions require ell>n^2.
    """
    n=len(c)-1;d=n*n
    require(c[0]==1 and pow(q,n//2)==c[-1] and n%2==0,'polarized polynomial input')
    require(ell>d and q%ell!=0 and all(ell%a for a in range(2,isqrt(ell)+1)),'Newton modulus not an admissible prime')
    require(all(pow(q,n//2-k)*c[k]==c[n-k] for k in range(n//2+1)), 'reciprocal polynomial')
    s=[n]
    for k in range(1,d+1):
        v=sum(c[i]*s[k-i] for i in range(1,min(k,n+1)))
        if k<=n: v+=k*c[k]
        s.append(-v%ell)
    invq=pow(q,-1,ell);invpower=1;ratios=[0]
    for k in range(1,d+1):
        invpower=invpower*invq%ell;ratios.append(s[k]*s[k]*invpower%ell)
    r=[1]
    for k in range(1,d+1):
        r.append(-sum(r[k-i]*ratios[i] for i in range(1,k+1))*pow(k,-1,ell)%ell)
    return tuple(reversed(r))


def determinant_mod(matrix,ell):
    a=[list(row) for row in matrix];v=1
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]%ell),None)
        if pivot is None: return 0
        if pivot!=k: a[k],a[pivot]=a[pivot],a[k];v=-v%ell
        v=v*a[k][k]%ell;inverse=pow(a[k][k],-1,ell)
        for i in range(k+1,len(a)):
            factor=a[i][k]*inverse%ell
            if factor:
                for j in range(k+1,len(a)): a[i][j]=(a[i][j]-factor*a[k][j])%ell
            a[i][k]=0
    return v


def verify_ratio_resultants(c,ell,r):
    # Res_X(f(X),f(tX)) = f(0)^n R(t) for even n.
    # Both sides have degree <=n^2 in t: n^2+1 distinct evaluations certify
    # their whole polynomial identity, not merely a sampled sanity check.
    n=len(c)-1;require(n%2==0 and ell>n*n,'resultant evaluation coverage')
    for t in range(n*n+1):
        g=[v*pow(t,n-i,ell)%ell for i,v in enumerate(c)]
        matrix=[[0]*i+list(c)+[0]*(n-1-i) for i in range(n)]
        matrix += [[0]*i+g+[0]*(n-1-i) for i in range(n)]
        value=0
        for v in reversed(r): value=(value*t+v)%ell
        require(value*pow(c[-1],n,ell)%ell==determinant_mod(matrix,ell),'independent Sylvester identity')
    return n*n+1


@lru_cache(maxsize=1)
def root_ratio_certificate(c):
    require(len(c)==17,'dimension-eight polynomial required')
    orders=possible_orders(256);remaining=set(orders);witnesses=[]
    for ell in (409,419,421,431,433):
        r=ratio_polynomial(c,7,ell)
        evaluations=verify_ratio_resultants(c,ell,r)
        eliminated=[m for m in sorted(remaining) if modgcd_degree(r,cyclotomic(m),ell)==0]
        remaining.difference_update(eliminated)
        witnesses.append({'prime':ell,'ratio_polynomial_coefficients_ascending':list(r),
            'independent_Sylvester_evaluations':evaluations,
            'orders_excluded_by_gcd_one':eliminated,'remaining_orders':sorted(remaining)})
        if not remaining: break
    require(not remaining,'unexcluded root-of-unity ratios')
    return {'ratio_polynomial_degree':256,'totient_search_bound':131072,
        'nontrivial_cyclotomic_orders_checked':len(orders),'largest_candidate_order':max(orders),
        'modular_witnesses':witnesses,'all_nontrivial_root_of_unity_ratios_excluded':True}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-asymmetric-absolute.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='asymmetric-scalar-target-transplant' and c['verdict']=='rejected','absolute identity')
    require(c['resolution_kind']=='cyclotomic_ratio_exclusion_absolute_simple_reduction_and_specialization','absolute resolution')
    require(c['arithmetic']=={'prime':7,'Prym_dimension':8,'ratio_degree':256,
        'totient_search_bound':131072,'exclude_nontrivial_orders_only':True,
        'specialization_direction':'absolute_simple_reduction_implies_absolute_simple_generic_fibre'},'absolute arithmetic scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'absolute promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    require(c['previous_receipt']=='research/voevodsky/results/hodge-asymmetric-frobenius-v1.json','absolute predecessor binding')
    old=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old==frobenius_report() and old['Frobenius_polynomial_irreducible_over_Q'] is True and
        old['full_extension_counts_reexecuted'] is True,'stale Frobenius certificate')
    require(c['target_receipt']=='research/voevodsky/results/hodge-indecomposable-principal-model-v1.json','absolute target binding')
    target=json.loads((ROOT/c['target_receipt']).read_text(encoding='utf-8'))
    require(target==target_report() and target['candidate_id']==c['candidate_id'] and
        target['composite_isogeny_degree']==2304,'stale target isogeny')
    cert=root_ratio_certificate(tuple(old['L_polynomial_coefficients_ascending']))
    sources={p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_asymmetric_frobenius.py',
        c['target_receipt'],'research/voevodsky/checkers/check_hodge_indecomposable_principal_model.py'}
    return {'schema':'marici.hodge-asymmetric-absolute-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',**cert,
        'reduction_absolutely_simple':True,'complex_auxiliary_Prym_absolutely_simple':True,
        'this_auxiliary_Prym_isogenous_to_X6_times_B2':False,
        'this_auxiliary_Prym_square_isogeny_excluded':True,
        'actual_theta_singularity_dimension':None,'conditional_root_label_count_not_updated':516,
        'checks':dict.fromkeys(['previous_full_Frobenius_certificate_reexecuted',
            'totient_bound_covers_all_possible_root_of_unity_orders',
            'modular_ratio_Newton_polynomials_and_cyclotomic_gcd_certificates',
            'independent_Sylvester_polynomial_identities_at_all_257_evaluation_points',
            'all_Frobenius_powers_irreducible_by_transitivity_and_injectivity',
            'absolute_simplicity_specializes_in_the_correct_direction',
            'one_auxiliary_target_transplant_rejected_not_the_family'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','modular_witnesses')},indent=2))
