"""Explicit algebraic projector with retained complement; no preparation admission."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, eye, transpose, rank, encode
from check_graded_boundary_transport import audit as graded_audit, add as madd, scale as mscale
from check_moving_boundary_plane import audit as moving_audit
from check_rational_normalization_gate import audit as rational_audit, power
from check_retained_word_transport import poly, add, sub, mul, scale

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/algebraic-projector.v1.json'


def trim(p):
    p=list(p)
    while len(p)>1 and not p[-1]:p.pop()
    return p

def padd(a,b):return trim([add(a[i] if i<len(a) else {},b[i] if i<len(b) else {}) for i in range(max(len(a),len(b)))])
def pscale(a,c):return trim([mul(x,c) for x in a])
def psub(a,b):return padd(a,[scale(x,-1) for x in b])
def pmul(a,b):
    out=[{} for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=add(out[i+j],mul(x,y))
    return trim(out)

def remainder(a,b):
    a=trim(a);assert b[-1]==poly(1)
    while a!=[{}] and len(a)>=len(b):
        shift=len(a)-len(b);coefficient=a[-1]
        a=psub(a,[{}]*shift+pscale(b,coefficient))
    return a


def audit():
    rational=rational_audit();moving=moving_audit();graded=graded_audit()
    # Verify global factorization from the determinant branch equation, not
    # merely agreement of local Taylor coefficients. Clear the denominators in
    # (delta+epsilon-p)(delta-epsilon)^2=q^2 with epsilon=r/delta.
    z=poly(variable=0);detvar=poly(variable=1)
    p=scale(power(z,4),-1);q=scale(add(power(z,4),power(z,5)),-1);r=scale(power(z,5),-1)
    relation=sub(mul(sub(add(power(detvar,2),r),mul(p,detvar)),power(sub(power(detvar,2),r),2)),mul(power(q,2),power(detvar,3)))
    expected={(0,6,0):F(1),(4,5,0):F(1),(5,4,0):F(1),(8,3,0):F(-1),(10,3,0):F(-1),(10,2,0):F(-1),(14,1,0):F(1),(15,0,0):F(-1)}
    assert relation==expected
    # Universal polynomial calculation in tau, delta, epsilon, with lambda as
    # the outer polynomial variable. No eigenvalue radicals are needed.
    tau=poly(variable=0);delta=poly(variable=1);epsilon=poly(variable=2)
    f=[delta,scale(tau,-1),poly(1)]
    g=[epsilon,tau,poly(1)]
    b=sub(epsilon,delta)
    resultant=add(mul(b,b),scale(mul(mul(tau,tau),add(delta,epsilon)),2))
    h=[add(scale(mul(tau,tau),2),b),scale(tau,-2)]
    numerator=pmul(g,h);characteristic=pmul(f,g)
    assert remainder(numerator,f)==[resultant]
    assert remainder(numerator,g)==[{}]
    assert remainder(psub(pmul(numerator,numerator),pscale(numerator,resultant)),characteristic)==[{}]
    assert remainder(pmul(f,numerator),characteristic)==[{}]
    complement=psub([resultant],numerator)
    assert remainder(pmul(g,complement),characteristic)==[{}]
    assert remainder(pmul(numerator,complement),characteristic)==[{}]

    # Actual selected trace/determinant branches from the independently checked
    # graph jet. Scalar and matrix series are truncated only for local cross-checks;
    # exactness of the projector itself follows from the universal identities.
    order=4
    traces=moving['induced_step']['trace_series']
    determinants=moving['induced_step']['determinant_series']
    def sconvolve(a,b):return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(order+1)]
    def sinverse(a):
        out=[F(0)]*(order+1);out[0]=1/a[0]
        for n in range(1,order+1):out[n]=-sum(a[i]*out[n-i] for i in range(1,n+1))/a[0]
        return out
    def zeros(n,m):return [[F(0)]*m for _ in range(n)]
    def mconvolve(a,b):
        out=[]
        for n in range(order+1):
            row=zeros(len(a[0]),len(b[0][0]))
            for i in range(n+1):row=madd(row,mm(a[i],b[n-i]))
            out.append(row)
        return out
    def smul(a,b):
        out=[]
        for n in range(order+1):
            row=zeros(len(b[0]),len(b[0][0]))
            for i in range(n+1):row=madd(row,mscale(b[n-i],a[i]))
            out.append(row)
        return out
    # -(1+epsilon_parameter)^5; the last coefficient is outside this order.
    constant_term=list(map(F,[-1,-5,-10,-10,-5]))
    other_det=sconvolve(constant_term,sinverse(determinants))
    difference=[a-b for a,b in zip(other_det,determinants)]
    t2=sconvolve(traces,traces)
    res=[a+2*b for a,b in zip(sconvolve(difference,difference),sconvolve(t2,[a+b for a,b in zip(determinants,other_det)]))]
    assert res[0]==4
    # Factor coefficient identities agree with the source characteristic jet.
    assert [a+b-c for a,b,c in zip(determinants,other_det,t2)]==[-1,-4,-6,-4,-1]
    assert sconvolve(traces,[a-b for a,b in zip(determinants,other_det)])==[-2,-9,-16,-14,-6]

    carrier=graded['minimal_constant_carrier'];A=carrier['one_step_A4'];C=carrier['two_step_C4']
    M=[madd(A,C),madd(A,mscale(C,2)),C,zeros(4,4),zeros(4,4)]
    identity=[eye(4)]+[zeros(4,4) for _ in range(order)]
    gM=[madd(madd(x,y),z) for x,y,z in zip(mconvolve(M,M),smul(traces,M),smul(other_det,identity))]
    hM=[madd(x,mscale(y,-2)) for x,y in zip(smul([2*a+b for a,b in zip(t2,difference)],identity),smul(traces,M))]
    projector=smul(sinverse(res),mconvolve(gM,hM))
    complementary=[madd(x,mscale(y,-1)) for x,y in zip(identity,projector)]
    assert mconvolve(projector,projector)==projector
    assert mconvolve(projector,M)==mconvolve(M,projector)
    assert mconvolve(projector,complementary)==[zeros(4,4) for _ in range(order+1)]
    assert [sum(p[i][i] for i in range(4)) for p in projector]==[2,0,0,0,0]
    frame=[]
    for n,X in enumerate(moving['local_graph']['series_coefficients_through_order_4']):
        frame.append((eye(2) if n==0 else zeros(2,2))+X)
    assert mconvolve(projector,frame)==frame
    assert rank(projector[0])==rank(complementary[0])==2
    assert transpose(projector[0])!=projector[0]
    # Keep both outputs. Their sum recovers every input, but this coordinate
    # split is not asserted orthogonal under the unmodified counting metric.
    assert madd(projector[0],complementary[0])==eye(4)
    gram=madd(mm(transpose(projector[0]),projector[0]),mm(transpose(complementary[0]),complementary[0]))
    assert gram!=eye(4)

    dependencies=list(rational['source_sha256'])+['research/scattering/seed-composition/check_algebraic_projector.py']
    return {
        'schema':'marici.scattering.algebraic-projector.v1',
        'status':'exact_algebraic_selected_complement_split_constructed_not_native_preparation',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'branch_data':{'delta':'selected determinant branch with delta(1)=1',
                       'epsilon':'-z^5/delta','tau':'-(z^4+z^5)/(delta-epsilon)',
                       'factor_f':'lambda^2-tau*lambda+delta','factor_g':'lambda^2+tau*lambda+epsilon',
                       'base_f':'lambda^2+lambda+1','base_g':'lambda^2-lambda-1',
                       'positive_axis_conditions':'delta>0, epsilon<0, selected sector continued from z=1',
                       'factorization_from_determinant_equation_verified':True},
        'projector_formula':{'R':'(epsilon-delta)^2+2*tau^2*(delta+epsilon)',
                             'h':'2*tau^2+epsilon-delta-2*tau*lambda',
                             'Pi':'g(M)*h(M)/R','complement':'I-Pi',
                             'universal_modulo_fg_identities_verified':['Pi^2=Pi','f(M)Pi=0','g(M)(I-Pi)=0','Pi(I-Pi)=0'],
                             'commutes_with_M':True,'ranks':[2,2],
                             'base_resultant':4,'denominator_contains_selected_discriminant':False},
        'local_cross_checks':{'projector_coefficients_through_order_4':projector,
                              'matches_Riccati_graph_through_order':4,'base_projector':projector[0],
                              'base_complement':complementary[0],'base_split_counting_gram':gram},
        'collision_behavior':{'positive_axis_R_nonzero':True,
                               'reason':'the selected and complementary quadratic roots remain disjoint, including at the internal selected collision',
                               'selected_generalized_eigenspace_retained_at_collision':True,
                               'individual_eigenvector_choice_required':False},
        'retention':{'split':'x -> (Pi x,(I-Pi)x)','decoder':'sum both records',
                     'complementary_dimension_retained':2,'base_split_is_counting_isometry':False,
                     'spectral_projection_is_measurement_or_preparation':False},
        'boundary':{'algebraic_branch_selection_source_authorized':False,'gain_operation_source_derived':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Lift the selected/complementary split from this four-dimensional correlated carrier to the original twelve boundary occurrences; check multiplicity and which extra correlation selection is required before treating the projector as a two-output construction.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale algebraic-projector receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: universal algebraic rank-two projector and retained complement; actual Riccati graph matched through order 4.')
    print('PASS: only inter-sector resultant in denominator; internal selected collision does not invalidate the split.')
    print('Boundary: reversible algebraic decomposition, not native preparation or a counting-metric measurement.')


if __name__=='__main__':main()
