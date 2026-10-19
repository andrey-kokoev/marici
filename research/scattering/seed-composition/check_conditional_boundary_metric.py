"""Conditional positive invariant metric and its collision degeneration.

Normalization is declared, not derived as a physical operation. Universal
polynomial identities are tied to the actual selected step's checked local jet.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, transpose, eye, encode
from check_graded_boundary_transport import add as madd, scale as mscale
from check_retained_word_transport import add, sub, mul, scale
from check_moving_boundary_plane import audit as moving_audit
from check_positive_spectral_collision import audit as collision_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/conditional-boundary-metric.v1.json'


def constant(x):return {(0,0,0,0):F(x)} if x else {}
def variable(i):return {tuple(int(i==j) for j in range(4)):F(1)}
def pmm(a,b):
    out=[]
    for row in a:
        next_row=[]
        for col in zip(*b):
            entry={}
            for x,y in zip(row,col):entry=add(entry,mul(x,y))
            next_row.append(entry)
        out.append(next_row)
    return out

def ptranspose(a):return list(map(list,zip(*a)))
def zero():return [[F(0),F(0)],[F(0),F(0)]]


def audit():
    moving=moving_audit();collision=collision_audit()
    a,b,c,d=[variable(i) for i in range(4)]
    tau=add(a,d);delta=sub(mul(a,d),mul(b,c));eta=sub(scale(delta,4),mul(tau,tau))
    T=[[a,b],[c,d]]
    G=[[scale(c,-2),sub(a,d)],[sub(a,d),scale(b,2)]]
    assert pmm(pmm(ptranspose(T),G),T)==[[mul(delta,x) for x in row] for row in G]
    assert sub(mul(G[0][0],G[1][1]),mul(G[0][1],G[1][0]))==eta
    # The linear equivalent of invariance has a one-dimensional solution space
    # when the eigenvalues are nonreal (b,c nonzero with opposite signs).
    u,v,w=G[0][0],G[0][1],G[1][1]
    assert add(mul(sub(a,d),u),scale(mul(c,v),2))=={}
    assert add(mul(b,u),mul(c,w))=={}
    assert add(scale(mul(b,v),2),mul(sub(d,a),w))=={}

    # A regular cyclic basis gives the companion chart even at the Jordan point.
    # Reuse a,b here as independent formal trace/determinant variables.
    t,det=a,b
    companion=[[{},scale(det,-1)],[constant(1),t]]
    H=[[constant(1),scale(t,F(1,2))],[scale(t,F(1,2)),det]]
    assert pmm(pmm(ptranspose(companion),H),companion)==[[mul(det,x) for x in row] for row in H]
    assert sub(mul(H[0][0],H[1][1]),mul(H[0][1],H[1][0]))==sub(det,scale(mul(t,t),F(1,4)))

    # Actual source-derived local jet, not a standalone model substituted for it.
    step=moving['induced_step']['series_coefficients_through_order_4']
    determinants=moving['induced_step']['determinant_series'];order=4
    metrics=[[[-2*m[1][0],m[0][0]-m[1][1]],[m[0][0]-m[1][1],2*m[0][1]]] for m in step]
    assert metrics[0]==[[3,0],[0,1]]
    assert metrics[1]==[[F(21,4),F(1,2)],[F(1,2),F(1,4)]]
    def series_product(left,right):
        out=[zero() for _ in range(order+1)]
        for i,x in enumerate(left):
            for j,y in enumerate(right):
                if i+j<=order:out[i+j]=madd(out[i+j],mm(x,y))
        return out
    def scalar_product(left,right):
        return [sum(left[i]*right[n-i] for i in range(n+1)) for n in range(order+1)]
    def scalar_matrix(left,right):
        out=[]
        for n in range(order+1):
            entry=zero()
            for i in range(n+1):entry=madd(entry,mscale(right[n-i],left[i]))
            out.append(entry)
        return out
    unnormalized=series_product(series_product([transpose(m) for m in step],metrics),step)
    assert unnormalized==scalar_matrix(determinants,metrics)
    # Positive inverse-square-root branch near det=1. This is an explicit
    # added scalar weighting, not an already authorized source operation.
    normalization=[F(0)]*(order+1);normalization[0]=1
    for n in range(1,order+1):
        known=scalar_product(determinants,scalar_product(normalization,normalization))[n]
        normalization[n]=-known/2
    assert scalar_product(determinants,scalar_product(normalization,normalization))==[1,0,0,0,0]
    assert normalization[1]==-F(5,4)
    U=scalar_matrix(normalization,step)
    assert series_product(series_product([transpose(m) for m in U],metrics),U)==metrics
    normalized_trace=[m[0][0]+m[1][1] for m in U]
    assert normalized_trace[:2]==[-1,-F(3,4)]
    # Normalization fixes modulus but not the C3 angle.
    phi=series_product(U,U)
    phi=[madd(madd(phi[i],U[i]),eye(2) if i==0 else zero()) for i in range(order+1)]
    assert phi[0]==zero() and phi[1]!=zero()

    controls=[]
    for tr in [F(-1),F(-3,2),F(-7,4),F(-15,8),F(-2),F(-9,4)]:
        C=[[F(0),F(-1)],[F(1),tr]]
        Hc=[[F(1),tr/2],[tr/2,F(1)]]
        determinant=1-tr*tr/4
        assert mm(mm(transpose(C),Hc),C)==Hc
        assert (determinant>0)==(-2<tr<2)
        controls.append({'trace':tr,'determinant_of_step':1,'metric_determinant':determinant,
                         'scope':'universal companion identity control, not a sampled source z value'})
    # Actual source collision is simple and internally separated; its selected
    # discriminant eta has a simple zero because total Delta = -eta*Dc*Res^2,
    # and Dc and Res remain nonzero there.
    assert collision['collision']['squarefree']
    assert collision['sector_identification']['collision_between_selected_and_complementary_sectors'] is False
    assert any(c['coordinate']==1 for c in collision['cyclicity_at_collision'])

    dependencies=list(collision['source_sha256'])+['research/scattering/seed-composition/check_conditional_boundary_metric.py']
    return {
        'schema':'marici.scattering.conditional-boundary-metric.v1',
        'status':'positive_metric_exists_after_declared_normalization_and_degenerates_at_collision',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'universal_identity':{'step':'T=[[a,b],[c,d]]','tau':'a+d','delta':'a*d-b*c','eta':'4*delta-tau^2',
                              'metric':'G=[[-2*c,a-d],[a-d,2*b]]','identity':'T^t G T=delta G','det_G':'eta',
                              'positive_condition':'eta>0 and choose orientation/sign with b>0,c<0',
                              'uniqueness':'all positive invariant forms for T/sqrt(delta) are positive scalar multiples in this real two-dimensional elliptic sector'},
        'local_source_metric':{'coefficients_through_order_4':metrics,'base_metric':[[3,0],[0,1]],
                               'normalization_delta_inverse_sqrt_coefficients':normalization,
                               'normalized_step_coefficients':U,'normalized_trace_coefficients':normalized_trace,
                               'verified_invariance_order':4,'C3_angle_still_changes':True},
        'collision_chart':{'frame':'(v,Tv), with v the selected spectral projection of a cyclic source vector near the collision',
                            'step':'[[0,-delta],[1,tau]]','metric':'[[1,tau/2],[tau/2,delta]]',
                            'metric_determinant':'eta/4','trace_normalized_determinant':'eta/(4*(1+delta)^2)',
                            'limit_rank_at_collision':1,
                            'condition_number_asymptotic':'4*(1+delta_c)^2/eta',
                            'eta_near_collision':'positive constant*(z_c-z)+higher order on approach from below',
                            'uniform_positive_equivalence_through_collision':False,
                            'after_collision_signature':'(1,1), an indefinite invariant form, not a positive norm'},
        'algebraic_controls':controls,
        'boundary':{'determinant_normalization_is_source_derived':False,'physical_energy_metric_derived':False,
                    'physical_clock_identified':False,'native_parse_control_or_preparation_derived':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Audit whether the declared determinant normalization and changing metric can arise from an existing source-authorized transport with retained residuals, rather than parameter-dependent gain inserted to repair the mode.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale conditional-metric receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: universal T^t G T=det(T)G; positive normalized metric and actual source jet verified through order 4.')
    print('PASS: regular collision-chart metric loses rank; condition number diverges and no scalar fixes uniform positivity.')
    print('Boundary: determinant normalization is declared, not a derived physical source operation; C3 angle still changes.')


if __name__=='__main__':main()
