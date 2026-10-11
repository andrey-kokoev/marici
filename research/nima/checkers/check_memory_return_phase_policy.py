"""Hostile test of the phase policy behind the returning first moment.
Same empty-bank projection and stored contrast, different unitary return phase.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_triangle_half_phase import zadd,zmul,zscale,zconj,znorm
from check_twelve_triangle_positive_geometry import POINTS,mean
from check_four_packet_record_feedback import basis,rank,mm
ROOT=Path(__file__).resolve().parents[1]
ONE=(F(1),F(0));ZERO=(F(0),F(0));OMEGA=(F(-1,2),F(1,2))

def plus(a,b):return tuple(zadd(x,y) for x,y in zip(a,b))
def minus(a,b):return plus(a,tuple(zscale(z,-1) for z in b))
def project(x):
    s=ZERO
    for v in x:s=zadd(s,v)
    return (zscale(s,F(1,12)),)*12

def step(x,w,eta):return plus(project(x),tuple(zmul(eta,z) for z in w)),minus(x,project(x))
def budget(x,w):return F(20,3)*sum(znorm(z) for z in x+w)
def center(x,positions):
    weights=[znorm(z) for z in x];s=sum(weights)
    return tuple(sum(a*p[k] for a,p in zip(weights,positions))/s for k in range(3)) if s else None

def axis_update(eta):
    a,b=eta
    # [active moment, record moment, S, V, R, W], with
    # c_x=(S+i sqrt(3)V)/2 and c_w=(R+i sqrt(3)W)/2.
    return ((0,1,0,0,a,-3*b),(1,0,-1,0,0,0),
            (0,0,0,0,a,-3*b),(0,0,0,0,b,a),
            (0,0,1,0,0,0),(0,0,0,1,0,0))

def main():
    rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
    pts=dict(POINTS)
    for row in rows:
        f=row['triangle'][0];pts[f]=mean([POINTS[k] for k in f[2:]])
    positions=[mean([(F(0),)*3]+[pts[k] for k in row['triangle']]) for row in rows]
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB');j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    u=(ONE,)*12;zero=(ZERO,)*12
    d=tuple((F(int(k==i)-int(k==j)),F(0)) for k in range(12))
    initial=plus(u,d);cases=[]
    for name,eta in (('identity',ONE),('sign reversal',(-F(1),F(0))),('third-root phase',OMEGA)):
        assert znorm(eta)==1
        x,w=initial,zero;history=[]
        for depth in range(4):
            assert budget(x,w)==F(280,3) and project(w)==zero
            history.append(dict(depth=depth,active_center=list(map(str,center(x,positions)))))
            if depth<3:x,w=step(x,w,eta)
        first=step(initial,zero,eta)
        assert first==(u,d)
        second=step(*first,eta)
        assert second==(plus(u,tuple(zmul(eta,z) for z in d)),zero)
        assert center(second[0],positions)==(F(1,12),eta[0]/42,-eta[0]/42)
        # Old full-state agreement-fixing policy discriminates this family.
        aligned=(initial,d)
        fixes=step(*aligned,eta)==aligned
        assert fixes==(eta==ONE)
        # Check reversibility on the physical zero-mean record sector.
        x=tuple((F(k-3,7),F(k*k-4,13)) for k in range(12))
        raw=tuple((F(k,5),F(2-k,11)) for k in range(12));w=minus(raw,project(raw))
        xx,ww=step(x,w,eta)
        assert budget(xx,ww)==budget(x,w)
        inverse=(plus(project(xx),ww),tuple(zmul(zconj(eta),z) for z in minus(xx,project(xx))))
        assert inverse==(x,w)
        T=axis_update(eta);power=basis(6);observed=[]
        # Algebraic observable orbit, not extra body advances.
        for _ in range(6):
            observed.extend((power[0],power[1]));power=mm(T,power)
        dimension=rank(tuple(observed))
        assert dimension==(4 if eta[1]==0 else 6)
        cases.append(dict(return_phase=name,phase_coefficients=list(map(str,eta)),
                          first_step_identical=True,fixes_agreeing_full_state=fixes,
                          generated_axis_readout_dimension=dimension,three_advance_history=history))
    # Two actual states agree on all fifteen prior real-phase readouts, yet
    # the nonreal return law gives different next centers.
    def old_observer(x,w):
        mu=project(x)
        values=[sum(znorm(z) for z in x),sum(znorm(z) for z in w),sum(znorm(z) for z in mu)]
        for axis in range(3):
            values.extend((sum(znorm(z)*p[axis] for z,p in zip(x,positions)),
                           sum(znorm(z)*p[axis] for z,p in zip(w,positions)),
                           2*sum(zmul(zconj(a),b)[0]*p[axis] for a,b,p in zip(mu,x,positions)),
                           2*sum(zmul(zconj(a),b)[0]*p[axis] for a,b,p in zip(mu,w,positions))))
        return tuple(values)
    iw=tuple(zmul((F(0),F(1)),z) for z in d)
    minus_iw=tuple(zscale(z,-1) for z in iw)
    assert old_observer(u,iw)==old_observer(u,minus_iw)
    out1=step(u,iw,OMEGA)[0];out2=step(u,minus_iw,OMEGA)[0]
    assert center(out1,positions)==(F(7,36),F(-1,36),F(1,36))
    assert center(out2,positions)==(F(7,36),F(1,36),F(-1,36))
    result=dict(schema='marici.nima.memory-return-phase-policy.v1',status='pass',
        family='x_next=P x+eta*w; w_next=(I-P)x, with P w=0 and |eta|=1.',
        shared_properties=['same empty-bank projection','same first stored record','same norm budget','invertible','covariant under simultaneous permutations of all twelve slots'],
        cases=cases,
        old_observer_counterexample={'equal_fifteen_readouts':True,'nonreal_return_centers':[list(map(str,center(out1,positions))),list(map(str,center(out2,positions)))]},
        selection='Full-state agreement fixing at w=(I-P)x selects eta=1 in this family. Conservation and the first empty-bank output alone do not.',
        observer_boundary='For a nonreal return phase, imaginary mean-record correlations enter the next first moment; the prior 15-readout real-phase observer is not universally closed.',
        scope='Controlled alternatives, not modifications of the original model. The physical authority of agreement fixing and the spatial/intensity interpretation remain explicit assumptions.')
    (ROOT/'results/memory-return-phase-policy.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
