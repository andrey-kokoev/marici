"""Complete the finite eigenline-cycle test: stability, iteration, and scale.

Exact rational linearization and scale-erasure proofs are primary. Numerical
iterations use an internal symmetric 3x3 Jacobi eigensolver with residual checks.
Continuous alignment flow is a separate declared dynamics, not a gravity law.
"""
from fractions import Fraction as F
from math import sqrt, atan2, cos, sin
from pathlib import Path
import json
from check_machian_thing_eigenline_cycle import mm, add, scale, tr, trans


def outer(v): return tuple(tuple(x*y for y in v) for x in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(a,v): return tuple(dot(r,v) for r in a)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def norm(v): return sqrt(dot(v,v))
def normalize(v):
    n=norm(v);return tuple(x/n for x in v)
def comm(a,b): return add(mm(a,b),scale(mm(b,a),-1))
def total(matrices):
    out=tuple(tuple(F(0) for _ in range(3)) for _ in range(3))
    for m in matrices: out=add(out,m)
    return out

def eig3(matrix):
    a=[list(map(float,r)) for r in matrix]
    v=[[float(i==j) for j in range(3)] for i in range(3)]
    for _ in range(80):
        p,q=max(((0,1),(0,2),(1,2)),key=lambda pq:abs(a[pq[0]][pq[1]]))
        if abs(a[p][q])<1e-15: break
        theta=.5*atan2(2*a[p][q],a[q][q]-a[p][p]);c=cos(theta);s=sin(theta)
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        for k in range(3):
            if k not in (p,q):
                x,y=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*x-s*y
                a[k][q]=a[q][k]=s*x+c*y
        a[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        a[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        a[p][q]=a[q][p]=0.
        for k in range(3):
            x,y=v[k][p],v[k][q];v[k][p]=c*x-s*y;v[k][q]=s*x+c*y
    result=sorted((a[i][i],tuple(v[k][i] for k in range(3))) for i in range(3))
    for lam,u in result:
        assert norm(sub(mv(matrix,u),tuple(lam*x for x in u)))<1e-10
        assert abs(dot(u,u)-1)<1e-12
    return result


RAW=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
ANCHORS=tuple(tuple(x/2 for x in v) for v in RAW)

def volume(vectors):
    points=[mv(outer(u),q) for u,q in zip(vectors,ANCHORS)]
    a,b,c=[sub(points[j],points[0]) for j in (1,2,3)]
    determinant=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    return -determinant/6

def measure(vectors,weights):
    Ps=[outer(u) for u in vectors];S=total([scale(p,w) for p,w in zip(Ps,weights)])
    spectra=[eig3(add(S,scale(Ps[i],-weights[i]))) for i in range(4)]
    return {'volume':volume(vectors),'source_minimum':min(e[0][0] for e in spectra),
            'minimum_gap':min(e[1][0]-e[0][0] for e in spectra),
            'energy':float(tr(mm(S,S))/2)},spectra


def run_direct(vectors,weights,limit):
    records=[];reason='iteration_limit'
    for k in range(limit+1):
        m,spectra=measure(vectors,weights);m['iteration']=k;records.append(m)
        if m['volume']<=1e-12: reason='nonpositive_or_degenerate_body';break
        if m['source_minimum']<=1e-12: reason='source_metric_at_numerical_degeneracy';break
        if m['minimum_gap']<=1e-11: reason='nonunique_lowest_line';break
        if k<limit: vectors=[e[0][1] for e in spectra]
    return {'termination':reason,'steps':len(records)-1,'records':records}


def run_flow(vectors,weights,steps=600):
    records=[];dt=.1
    for k in range(steps+1):
        m,_=measure(vectors,weights);m['iteration']=k;records.append(m)
        assert m['volume']>1e-10 and m['source_minimum']>1e-10
        if k==steps: break
        S=total([scale(outer(u),w) for u,w in zip(vectors,weights)])
        tangent=[sub(mv(S,u),tuple(dot(u,mv(S,u))*x for x in u)) for u in vectors]
        trial=dt
        for _ in range(40):
            candidate=[normalize(tuple(x-trial*y for x,y in zip(u,t))) for u,t in zip(vectors,tangent)]
            nxt,_=measure(candidate,weights)
            if nxt['volume']>1e-10 and nxt['source_minimum']>1e-10 and nxt['energy']<=m['energy']+1e-13:
                break
            trial/=2
        else: raise AssertionError('no positive energy-decreasing integration step')
        # This fixture stays in the positive diagonal-strain family. Every
        # normalized interpolation along the accepted step keeps all three
        # diagonal scales positive, certifying the whole interval, not just ends.
        for u,t in zip(vectors,tangent):
            assert all(1-trial*y/x>0 for x,y in zip(u,t))
        for u,signs in zip(candidate,RAW):
            assert all(u[i]*signs[i]>0 for i in range(3))
            assert max(abs(u[i]*signs[i]-candidate[0][i]) for i in range(3))<1e-10
        vectors=candidate
    assert records[-1]['energy']<=records[0]['energy']
    return {'integration':'normalized Euler with positivity/energy backtracking','nominal_step':dt,
            'initial':records[0],'final':records[-1],
            'minimum_body_volume':min(r['volume'] for r in records),
            'minimum_source_eigenvalue':min(r['source_minimum'] for r in records),
            'all_steps_positive':True,
            'between_steps_positive':'Positive diagonal-strain interpolation; all coordinate factors stay positive.'}


def main():
    I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
    P=[scale(outer(tuple(map(F,v))),F(1,3)) for v in RAW]
    assert total(P)==scale(I,F(4,3))
    # Derivative of the lowest-eigenprojector update at the tetrahedral fixed point.
    def jacobian(dP):
        out=[]
        for i in range(4):
            dK=total([dP[j] for j in range(4) if j!=i]);Q=add(I,scale(P[i],-1))
            out.append(scale(add(mm(mm(Q,dK),P[i]),mm(mm(P[i],dK),Q)),-1))
        return out
    def strain(D):
        return [add(add(mm(D,p),mm(p,D)),scale(mm(mm(p,D),p),-2)) for p in P]
    diagonal=(
        ((1,0,0),(0,-1,0),(0,0,0)),
        ((1,0,0),(0,1,0),(0,0,-2)),
    )
    tested=[];tangent_basis=[]
    for d in diagonal:
        dp=strain(tuple(tuple(map(F,r)) for r in d))
        assert jacobian(dp)==[scale(p,F(-5,3)) for p in dp]
        tested.append(('diagonal_shape',F(-5,3)));tangent_basis.append(dp)
    for a,b in ((0,1),(0,2),(1,2)):
        D=tuple(tuple(F((i==a and j==b) or (i==b and j==a)) for j in range(3)) for i in range(3))
        dp=strain(D)
        assert jacobian(dp)==[scale(p,F(1,9)) for p in dp]
        tested.append(('offdiagonal_shape',F(1,9)));tangent_basis.append(dp)
        R=tuple(tuple(F(int(i==a and j==b)-int(i==b and j==a)) for j in range(3)) for i in range(3))
        dr=[comm(R,p) for p in P]
        assert jacobian(dr)==dr
        tested.append(('rigid_rotation',F(1)));tangent_basis.append(dr)
    assert len(tested)==8
    from check_collective_four_state_identity import rank
    basis_matrix=tuple(tuple(mode[p][i][j] for mode in tangent_basis)
                       for p in range(4) for i in range(3) for j in range(3))
    assert rank(basis_matrix)==8
    # Independent exact dissipation check for projector-preserving continuous flow.
    deformed=[tuple(F(v[i]*(2 if i==0 else 1)) for i in range(3)) for v in RAW]
    PP=[scale(outer(v),1/dot(v,v)) for v in deformed]
    S=total(PP)
    velocity=[scale(comm(p,comm(p,S)),-1) for p in PP]
    derivative=tr(mm(S,total(velocity)))
    dissipation=-sum(sum(x*x for row in comm(p,S) for x in row) for p in PP)
    assert derivative==dissipation and derivative<0
    for p,dp in zip(PP,velocity):
        assert add(mm(dp,p),mm(p,dp))==dp and tr(dp)==0
    # Exact scale-erasure test: every normalized line and every source stays fixed.
    for radius in (F(1,2),F(2),F(3)):
        scaled=[tuple(radius*F(x) for x in v) for v in RAW]
        recovered=[scale(outer(v),1/dot(v,v)) for v in scaled]
        assert recovered==P
        assert total(recovered)==total(P)
    # Numerical controls confirm the exact linearization with actual repeated cycles.
    epsilon=1e-4
    perturbed=[normalize((v[0]*(1+epsilon),v[1]*(1-epsilon),v[2])) for v in RAW]
    baseline=[normalize(v) for v in RAW]
    direct=run_direct(perturbed,[1.,1.,1.,1.],100)
    remote=run_direct(baseline,[1.,2.,1.,1.],200)
    flow=run_flow([normalize(v) for v in deformed],[1.,1.,1.,1.])
    assert abs(flow['final']['energy']-8/3)<1e-10
    assert abs(flow['final']['volume']-1/3)<1e-9
    assert direct['steps']>0
    output={'audit_assertions_passed':True,
            'exact_discrete_linearization':{'diagonal_shape':{'multiplicity':2,'multiplier':'-5/3','stable':False},
                                           'offdiagonal_shape':{'multiplicity':3,'multiplier':'1/9'},
                                           'rigid_rotation':{'multiplicity':3,'multiplier':'1'}},
            'direct_update_near_symmetric_body':direct,'direct_update_remote_weight_two':remote,
            'continuous_alignment_alternative':{'equation':'dP_p/dtau = -[P_p,[P_p,S]], S=sum_q w_q P_q',
                                               'energy':'V=Tr(S^2)/2',
                                               'energy_derivative':'-sum_p w_p ||[P_p,S]||_F^2 <= 0',
                                               'exact_deformed_fixture_energy_derivative':str(derivative),
                                               'linearized_rates':{'diagonal_shape':'-8/3','offdiagonal_shape':'-8/9','rotation':'0'},
                                               'equal_weight_integration':flow},
            'scale_obstruction':{'identity':'P_p(a*q_p)=P_p(q_p) for all nonzero a',
                                 'source_response_scale_exponent':0,
                                 'newtonian_acceleration_scale_exponent_at_fixed_masses':-2,
                                 'conclusion':'Normalized eigenline data and fixed source weights erase radial scale. This rule cannot supply a Newtonian inverse-square response.'},
            'completed_verdict':'The proposed full eigenline-replacement dynamics has unstable shape modes. Its continuous alignment alternative preserves projector positivity and relaxes the tested body, but both erase radial scale. The calculation supplies an orientation-alignment mechanism; a gravitational force law has not been derived.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'machian-cycle-dynamics.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print('EXACT: full replacement has two unstable -5/3 shape modes; scale exponent is 0, not inverse-square.')
    print('ITERATION:',direct['termination'],'after',direct['steps'],'steps;',remote['termination'],'after',remote['steps'],'remote-weight steps.')
    print('FLOW: all stages positive; energy',flow['initial']['energy'],'->',flow['final']['energy'],'; volume ->',flow['final']['volume'])

if __name__=='__main__': main()
