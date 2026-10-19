"""Conditional rejection of the source object's weak semiregularity criterion."""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
from math import factorial
from pathlib import Path
import json
from check_hodge_secant_local_ext_gate import report as local_report, local_models
from check_hodge_eightfold_literature_audit import secant_character

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-secant-source-semiregularity.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-secant-source-semiregularity-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-secant-source-semiregularity-v1.json'
POLICY=['Question11_4_refuted','all_higher_genus_secants_excluded',
    'precise_eightfold_transform_criterion_evaluated','all_commutative_Hodge_locus_deformations_obstructed','target_cycle_constructed',
    'Hodge_proved','Hodge_refuted','actual_deformation_obstruction_nonzero',
    'local_Ext_length_used_as_global_dimension','all_cycle_annihilation_proved',
    'global_witness_search_completed']


def require(c,m):
    if not c:raise ValueError(m)


def add(p,q):
    r=dict(p)
    for k,v in q.items():r[k]=r.get(k,Q(0))+v
    return {k:v for k,v in r.items() if v}


def scale(p,c):return {k:v*c for k,v in p.items() if v*c}


def wedge(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            if a&b:continue
            sign=(-1)**sum((b&((1<<i)-1)).bit_count() for i in range(8) if a>>i&1)
            k=a|b;r[k]=r.get(k,Q(0))+sign*c*d
    return {k:v for k,v in r.items() if v}


def contract(p,i):
    require(type(i) is int and 0<=i<4,'holomorphic contraction index')
    return {k^(1<<i):v*(-1)**((k&((1<<i)-1)).bit_count()) for k,v in p.items() if k>>i&1}


def bivector(p,i,j):
    require(0<=i<j<4,'ordered bivector indices')
    return contract(contract(p,i),j)


def theta():return {(1<<i)|(1<<(i+4)):Q(1) for i in range(4)}


def character(d=9):
    r={};power={0:Q(1)}
    for c in secant_character(d,3):
        r=add(r,scale(power,c));power=wedge(power,theta())
    return r


def hkr_columns(ch):
    columns=[]
    for i,j in combinations(range(4),2):
        columns.append(wedge({(1<<(i+4))|(1<<(j+4)):Q(1)},ch))
    for i in range(4):
        for j in range(4):
            columns.append(wedge({1<<(i+4):Q(1)},contract(ch,j)))
    for i,j in combinations(range(4),2):columns.append(bivector(ch,i,j))
    return columns


def rank(columns):
    rows=sorted(set().union(*(set(c) for c in columns)))
    a=[[c.get(r,Q(0)) for c in columns] for r in rows];k=0
    for j in range(len(columns)):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
        for i in range(k+1,len(a)):
            if a[i][j]:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
        k+=1
    return k


def annihilator_residual(d,i,j,bfield_factor=None):
    ch=character(d)
    gamma=scale(bivector(wedge(theta(),theta()),i,j),Q(1,2))
    return add(bivector(ch,i,j),wedge(scale(gamma,d if bfield_factor is None else bfield_factor),ch))


def local_at_square(i,j):
    require(type(i) is int and type(j) is int and 0<=i<j<4,'ordered local tangent pair')
    d0,dm1,*_=local_models()
    def linear(p,index):
        return p.get(tuple(int(k==index) for k in range(4)),0)
    # Antisymmetrized derivative composition, up to the universal nonzero HKR factor.
    return [sum(linear(d0[0][k],i)*linear(dm1[k][c],j)-
                linear(d0[0][k],j)*linear(dm1[k][c],i) for k in range(4)) for c in range(2)]


def euler_pairing(d=9):
    ch=secant_character(d,3)
    return 24*sum(((-1)**i*ch[i]*ch[4-i] for i in range(5)),Q(0))


def exact_core():
    ch=character();cols=hkr_columns(ch)
    require(len(cols)==28 and rank(cols)==12,'Hochschild character rank')
    for i,j in combinations(range(4),2):
        require(not annihilator_residual(9,i,j),'compensated bivector annihilator')
    require(bool(annihilator_residual(9,0,1,8)),'wrong B-field negative control')
    require(local_at_square(0,1)==[2,0] and local_at_square(2,3)==[0,-2], 'nonzero local Atiyah square')
    require(all(local_at_square(i,j)==[0,0] for i,j in ((0,2),(0,3),(1,2),(1,3))), 'mixed local controls')
    require(euler_pairing()==1296,'Euler pairing')
    return {'HKR_dimension':28,'character_action_rank':12,'character_annihilator_dimension':16,
        'compensated_bivector_checks':6,'evaluation_rank_lower_bound':14,
        'trace_kernel_on_evaluation_image_lower_bound':2,'local_antisymmetric_At_square_ab':[2,0],
        'local_antisymmetric_At_square_cd':[0,-2],'Euler_self_pairing':1296}


def validate_scope(c):
    require(c['schema']=='marici.hodge-secant-source-semiregularity.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
        c['node']=='secant-source-weak-semiregularity-transplant','source semiregularity identity')
    require(c['hypotheses']=={'secant_d':9,'corrected_twist':3,'source_dimension':4,
        'normalized_nodes':306,'transverse_incidence_as_iteration32':True,
        'HKR_Todd_correction':'trivial_on_abelian_variety',
        'evaluation_formula':'Atiyah_square_up_to_nonzero_universal_factor'},'source semiregularity hypotheses')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'source semiregularity promotion')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_scope(c)
    prior=local_report();p=ROOT/'research/voevodsky/results/hodge-secant-local-ext-gate-v1.json'
    require(json.loads(p.read_text(encoding='utf-8'))==prior and prior['passed'],'prior local receipt stale')
    names={CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
        Path(__file__).relative_to(ROOT).as_posix(),p.relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-secant-source-semiregularity-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
        'verification_level':'Conditional source-object criterion failure from written HKR/Atiyah argument and exact exterior/local controls; not a target or Hodge verdict.',
        'checks':{'exact_exterior_action':True,'local_Atiyah_square_controls':True,
                  'source_scope_frozen':True,'prior_receipt_fresh':True},
        **exact_core(),'source_weak_criterion_fails':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
