"""Exact positive-axis collision audit using Sturm counts and a cyclicity certificate."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import encode
from check_graded_boundary_transport import audit as graded_audit
from check_moving_boundary_plane import audit as moving_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/positive-spectral-collision.v1.json'


def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0:p.pop()
    return p or [F(0)]

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def divide(a,b):
    a=trim(a);b=trim(b)
    if b==[0]:raise ZeroDivisionError()
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        power=len(a)-len(b);coefficient=a[-1]/b[-1];q[power]+=coefficient
        a=sub(a,[F(0)]*power+scale(b,coefficient))
    return trim(q),a

def derivative(a):return trim([i*a[i] for i in range(1,len(a))])
def evaluate(a,x):
    out=F(0)
    for coefficient in reversed(a):out=out*x+coefficient
    return out

def sturm(p):
    out=[trim(p),derivative(p)]
    while out[-1]!=[0]:
        _,remainder=divide(out[-2],out[-1])
        if remainder==[0]:break
        remainder=scale(remainder,-1)
        # Positive rescaling limits coefficient growth without changing signs.
        remainder=scale(remainder,1/abs(remainder[-1]))
        out.append(remainder)
    return out

def sign(x):return (x>0)-(x<0)
def variations(sequence,point):
    if point=='+inf':signs=[sign(p[-1]) for p in sequence]
    elif point=='-inf':signs=[sign(p[-1])*(-1)**(len(p)-1) for p in sequence]
    else:signs=[sign(evaluate(p,point)) for p in sequence]
    signs=[s for s in signs if s]
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def count(sequence,a,b):return variations(sequence,a)-variations(sequence,b)

def determinant(matrix):
    n=len(matrix);out=[F(0)]
    for perm in permutations(range(n)):
        term=[F((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))]
        for i in range(n):term=mul(term,matrix[i][perm[i]])
        out=add(out,term)
    return out

def matvec(matrix,vector):
    return [sum_polys([mul(a,b) for a,b in zip(row,vector)]) for row in matrix]

def sum_polys(terms):
    out=[F(0)]
    for term in terms:out=add(out,term)
    return out


def audit():
    moving=moving_audit();graded=graded_audit()['minimal_constant_carrier']
    assert moving['characteristic']=='lambda^4-z^4*lambda^2-(z^4+z^5)*lambda-z^5'
    assert moving['discriminant']=='z^15*(4*z^7-8*z^6-23*z^5+36*z^4-2*z^3+36*z^2-27*z-256)'
    d=list(map(F,[-256,-27,36,-2,36,-23,-8,4]))
    chain=sturm(d)
    assert len(chain[-1])==1  # gcd(d,d')=1: every root of d is simple.
    assert count(chain,F(0),'+inf')==1
    assert count(chain,F(2),F(3))==1
    lo,hi=F(2),F(3)
    for _ in range(24):
        mid=(lo+hi)/2
        assert evaluate(d,mid)!=0
        if count(chain,lo,mid)==1:hi=mid
        else:lo=mid
    assert count(chain,lo,hi)==1 and hi-lo==F(1,2**24)
    # Base spectrum and post-collision root counts, without floating root solvers.
    samples=[]
    for z in [F(1),F(2),F(3)]:
        quartic=[-z**5,-(z**4+z**5),-z**4,F(0),F(1)]
        qchain=sturm(quartic)
        counts={'below_minus_one':count(qchain,'-inf',F(-1)),
                'between_minus_one_zero':count(qchain,F(-1),F(0)),
                'positive':count(qchain,F(0),'+inf')}
        assert counts==({'below_minus_one':0,'between_minus_one_zero':1,'positive':1} if z<hi else {'below_minus_one':2,'between_minus_one_zero':1,'positive':1})
        assert evaluate(quartic,F(-1))==1 and evaluate(quartic,F(0))==-z**5
        samples.append({'z':z,'root_counts':counts})
    # At -1 the characteristic is identically 1, preventing the two new
    # negative eigenvalues from joining the complementary root in (-1,0).
    # Descartes gives exactly one positive root for every z>0. A simple zero
    # of the discriminant gives precisely one ordinary double-root collision;
    # a triple or two simultaneous doubles would have higher multiplicity.

    A=graded['one_step_A4'];C=graded['two_step_C4']
    M=[[[F(0),A[i][j],C[i][j]] for j in range(4)] for i in range(4)]
    certificates=[]
    for coordinate in range(4):
        vector=[[F(i==coordinate)] for i in range(4)];columns=[]
        for power in range(4):columns.append(vector);vector=matvec(M,vector)
        krylov=[[columns[j][i] for j in range(4)] for i in range(4)]
        det=determinant(krylov)
        # A nonconstant Krylov determinant may vanish elsewhere. Coprimality
        # with d certifies that it does not vanish at the collision parameter.
        a,b=d,det
        while b!=[0]:a,b=b,divide(a,b)[1]
        if len(a)==1:
            certificates.append({'coordinate':coordinate,'krylov_determinant':det,'gcd_with_collision_polynomial_degree':0})
    assert certificates
    assert next(c['krylov_determinant'] for c in certificates if c['coordinate']==1)==[F(0)]*6+[-F(1,8),F(1,4),-F(1,8)]
    # Cyclicity at the double-root collision forces a 2x2 Jordan block there.
    # It does not imply that the selected rank-two Riesz subspace is singular.

    dependencies=list(moving['source_sha256'])+['research/scattering/seed-composition/check_positive_spectral_collision.py']
    return {
        'schema':'marici.scattering.positive-spectral-collision.v1',
        'status':'one_positive_internal_collision_selected_plane_continues_but_step_is_defective',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'collision':{'polynomial_ascending':d,'positive_root_count':1,'squarefree':True,
                     'rational_isolating_interval':[lo,hi],'interval_width':hi-lo,
                     'approximate_interval_for_display_only':[float(lo),float(hi)],
                     'sturm_degrees':[len(p)-1 for p in chain],
                     'sturm_variations':{'zero':variations(chain,F(0)),'positive_infinity':variations(chain,'+inf')}},
        'real_root_controls':samples,
        'sector_identification':{'characteristic_at_minus_one':'1','characteristic_at_zero':'-z^5',
                                 'positive_root_count_all_positive_z':1,
                                 'complementary_negative_root_interval':[-1,0],
                                 'selected_pair_before_collision':'nonreal conjugate pair',
                                 'selected_pair_at_collision':'negative ordinary double root below -1',
                                 'selected_pair_after_collision':'two distinct negative roots below -1',
                                 'collision_between_selected_and_complementary_sectors':False},
        'cyclicity_at_collision':certificates,
        'plane_continuation':{'real_analytic_rank_two_Riesz_plane_on':'all z>0',
                              'reason':'selected spectral cluster remains separated from the two simple complementary roots; patch local spectral projectors along the positive interval',
                              'uniform_gap_at_z_zero_or_infinity_claimed':False,
                              'same_graph_chart_proved_global':False,
                              'eigenvectors_analytic_through_collision':False},
        'metric_boundary':{'collision_has_nontrivial_Jordan_block':True,
                           'nonzero_scalar_rescaling_can_make_collision_step_unitary_in_positive_metric':False,
                           'one_scalar_can_make_both_post_collision_eigenvalues_unit_modulus':False,
                           'physical_metric_or_normalization_derived':False},
        'boundary':{'physical_clock_identified':False,'native_control_or_preparation_derived':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'On the pre-collision interval, examine conditional positive invariant metrics after determinant normalization and their degeneration at the collision; separate this supplied normalization from any native source metric.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale positive-collision receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: one squarefree positive discriminant root isolated rationally; collision is internal to the selected pair.')
    print('PASS: exact cyclicity at collision forces a Jordan block; the separated rank-two plane itself continues.')
    print('Boundary: global positive-axis plane, not global graph coordinates, physical normalization or a unitary collision step.')


if __name__=='__main__':main()
