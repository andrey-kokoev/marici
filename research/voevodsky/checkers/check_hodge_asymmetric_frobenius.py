"""Fresh exact extension counts, degree-16 polynomial, F7 simplicity; not absolute."""
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from math import isqrt
import json
import subprocess
import tempfile
from check_hodge_asymmetric_reflections import report as automorphism_report, BranchRing
from check_hodge_asymmetric_scalar_cover import point_profile, modgcd_degree

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/conjecture_net/contracts/hodge-asymmetric-frobenius.v1.json'
NOTE = ROOT/'research/voevodsky/hodge-asymmetric-frobenius-v1.md'
OUT = ROOT/'research/voevodsky/results/hodge-asymmetric-frobenius-v1.json'
COUNTER = 'research/voevodsky/checkers/count_hodge_asymmetric_frobenius.rs'
COUNTS = 'research/voevodsky/inputs/hodge-asymmetric-frobenius-v1/counts.json'
POLICY = ['geometric_simplicity_proved','Prym_End0_computed','abstract_square_over_Qbar_excluded',
    'actual_cover_matching_Y2_constructed','theta_dimension_computed','conditional_root_census_changed',
    'finite_field_cycles_transferred_to_X','Hodge_proved','Hodge_refuted','alpha_nonalgebraic_proved',
    'algebraic_representative_of_alpha_constructed','all_cycle_annihilation_proved','global_witness_search_completed']
FACTORS = {5:[[1,1],[2,1],[1,4,2,4,1,4,2,1],[3,3,3,1,2,3,3,1]],
    11:[[2,9,9,8,6,4,1],[10,1,3,4,9,3,6,3,7,4,1]]}


def require(c,m):
    if not c:
        raise ValueError(m)


def source_paths():
    return {COUNTER,COUNTS}


@lru_cache(maxsize=1)
def executed_counts():
    # One fresh optimized build and full eight-field enumeration per process.
    with tempfile.TemporaryDirectory(prefix='hodge-frob-') as tmp:
        exe = Path(tmp)/'count.exe'
        subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
        run = subprocess.run([str(exe),'8'],check=True,capture_output=True,text=True,timeout=300)
        return json.loads(run.stdout)


@lru_cache(maxsize=1)
def small49_counts():
    """Independent polynomial-basis arithmetic and exhaustive (x,y), not log tables."""
    def add(a,b): return ((a%7+b%7)%7)+7*((a//7+b//7)%7)
    def neg(a): return (-a%7)+7*((-(a//7))%7)
    def sub(a,b): return add(a,neg(b))
    def mul(a,b):
        a0,a1,b0,b1=a%7,a//7,b%7,b//7
        return (a0*b0+4*a1*b1)%7+7*((a0*b1+a1*b0+a1*b1)%7)
    def power(a,n):
        r=1
        for _ in range(n): r=mul(r,a)
        return r
    def inv(a):
        require(a != 0,'GF49 inverse zero')
        r=power(a,47);require(mul(a,r)==1,'GF49 inverse');return r
    def chi(a):
        if a == 0: return 0
        r=power(a,24);require(r in (1,6),'GF49 Euler character');return 1 if r==1 else -1
    def fibre(x,y): return 1+chi(sub(add(power(x,4),y),2))
    c9,c17=4,8
    for u in range(1,49):
        f=mul(u,add(sub(mul(u,u),u),1))
        for y in range(49):
            if mul(y,y) == f:
                z=inv(u);c9+=fibre(add(add(u,6),z),mul(y,sub(1,mul(z,z))))
    for x in range(2,49):
        f=add(mul(mul(x,x),x),x)
        for y in range(49):
            if mul(y,y) == f:
                z=inv(x);u=sub(add(x,z),2);v=inv(u)
                yy=mul(mul(y,sub(1,mul(z,z))),sub(1,mul(v,v)))
                c17+=fibre(add(add(u,6),v),yy)
    return c9,c17


def newton_polynomial(traces):
    require(len(traces)==8 and all(type(v) is int for v in traces),'eight exact traces required')
    c=[1]
    for k in range(1,9):
        v=-sum(c[k-i]*traces[i-1] for i in range(1,k+1))
        require(v%k==0,'Newton divisibility')
        c.append(v//k)
    for k in range(9,17): c.append(7**(k-8)*c[16-k])
    return c


def ring_power(ring,a,n):
    v=(1,)
    while n:
        if n%2: v=ring.mul(v,a)
        a=ring.mul(a,a);n//=2
    return v


def irreducible_mod(f,p):
    d=len(f)-1
    if d==1: return True
    require(f[-1]==1 and d>0,'monic factor')
    ring=BranchRing(p,f);x=(0,1);v=x
    checks={d//q for q in range(2,d+1) if d%q==0 and all(q%r for r in range(2,isqrt(q)+1))}
    for i in range(1,d+1):
        v=ring_power(ring,v,p)
        if i in checks:
            require(modgcd_degree(f,ring.add(v,ring.scale(x,-1)),p)==0,'Rabin proper-degree factor')
    require(v==x,'Rabin full Frobenius identity')
    return True


def factor_degree_certificate(characteristic):
    admissible=set(range(17));rows=[]
    for p,factors in FACTORS.items():
        ring=BranchRing(p,characteristic);product=(1,);degrees={0}
        for f in factors:
            require(irreducible_mod(f,p),'reducible certificate factor')
            product=ring.raw_mul(product,tuple(f))
            degrees |= {a+len(f)-1 for a in tuple(degrees)}
        require(product==ring.trim(characteristic),'modular factor product')
        admissible &= degrees
        rows.append({'prime':p,'monic_irreducible_factors':factors,'possible_rational_factor_degrees':sorted(degrees)})
    require(admissible=={0,16},'factor-degree intersection does not prove irreducible')
    return rows


def verify_counts(data):
    require(data['p']==7 and len(data['rows'])==8,'extension count coverage')
    for n,row in enumerate(data['rows'],1):
        require(row['n']==n and row['q']==7**n and row['full_primitive_generator_cycle_verified'] is True,'field cycle coverage')
        require(row['primitive_trace']==row['C9']-row['C17'] and row['C9']%2==0 and row['C17']%4==0,'trace/deck count identities')
        require(row['primitive_trace']**2<=256*7**n and
            (7**n+1-row['C9'])**2<=324*7**n and
            (7**n+1-row['C17'])**2<=1156*7**n,'point-count Weil bounds')
    r=point_profile(7)
    require((data['rows'][0]['C9'],data['rows'][0]['C17'])==(r['C9'],r['C17']),'independent prime-field count')
    require((data['rows'][1]['C9'],data['rows'][1]['C17'])==small49_counts(),'independent quadratic-field count')
    traces=[r['primitive_trace'] for r in data['rows']]
    c=newton_polynomial(traces);characteristic=list(reversed(c))
    factors=factor_degree_certificate(characteristic)
    require(c[8]%7 != 0,'ordinary middle coefficient')
    return {'prime':7,'extension_degrees':list(range(1,9)),'primitive_traces':traces,
        'L_polynomial_coefficients_ascending':c,'Frobenius_characteristic_coefficients_ascending':characteristic,
        'irreducibility_modular_factor_certificates':factors,
        'Frobenius_polynomial_irreducible_over_Q':True,'reduction_simple_over_F7':True,
        'reduction_ordinary_at_7':True,
        'independent_F49_counts':list(small49_counts()),
        'actual_theta_singularity_dimension':None,'actual_target_isogeny':None,
        'conditional_root_label_count_not_updated':516}


def validate_certificate(c):
    require(c['schema']=='marici.hodge-asymmetric-frobenius.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='asymmetric-prym-frobenius7' and c['verdict']=='constructed','Frobenius identity')
    require(c['resolution_kind']=='fresh_extension_counts_Newton_reconstruction_and_modular_degree_irreducibility','Frobenius resolution')
    require(c['arithmetic']=={'prime':7,'extension_degrees':list(range(1,9)),
        'Prym_dimension':8,'counter':COUNTER,'counts':COUNTS,
        'full_recount_required':True,'simplicity_scope':'over_F7_not_geometric'},'Frobenius arithmetic scope')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'Frobenius promotion')


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_certificate(c)
    require(c['previous_receipt']=='research/voevodsky/results/hodge-asymmetric-reflections-v1.json','Frobenius predecessor binding')
    old=json.loads((ROOT/c['previous_receipt']).read_text(encoding='utf-8'))
    require(old==automorphism_report() and old['full_geometric_curve_automorphism_group']=='C4 x C2','stale automorphism certificate')
    data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'))
    require(data==executed_counts(),'fresh Rust count mismatch')
    certificate=verify_counts(data)
    sources=source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['previous_receipt'],'research/voevodsky/checkers/check_hodge_asymmetric_reflections.py'}
    return {'schema':'marici.hodge-asymmetric-frobenius-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',**certificate,
        'full_extension_counts_reexecuted':True,
        'checks':dict.fromkeys(['fresh_std_only_Rust_full_field_cycles_and_point_enumerations',
            'independent_python_prime_and_quadratic_field_counts',
            'Newton_divisibility_and_dimension_eight_functional_equation',
            'Rabin_verified_modular_factors_and_disjoint_proper_degree_sets',
            'F7_simplicity_and_ordinarity_not_absolute_or_target_matching'],True),
        **c['scope_policy'],'verification_level':c['trust_scope'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
