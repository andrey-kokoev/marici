"""Exact trial two-body impulse triangle; no WG physical identification."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
ROOT=Path(__file__).resolve().parents[1]

def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def scale(a,x):return tuple(a*v for v in x)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def impulse(q1,q2,g):
    j=scale(q1*q2,g)
    return j,scale(-1,j)
def via_recoil(q1,q2,m1,m2,g):
    if min(m1,m2)<=0:raise ValueError('positive-mass stratum required')
    a,b=impulse(q1,q2,g)
    return scale(1/m1,a),scale(1/m2,b)
def direct(q1,q2,m1,m2,g):
    return tuple(q1*q2*v/m1 for v in g),tuple(-q1*q2*v/m2 for v in g)
def energy(p,m):return dot(p,p)/(2*m)
def serial(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,(list,tuple)):return [serial(x) for x in v]
    if isinstance(v,dict):return {k:serial(x) for k,x in v.items()}
    return v

def main():
    z=(F(0),)*3;g=(F(1),F(2),F(-1));p1=(F(1),F(-2),F(3));p2=(F(-1),F(1),F(0))
    count=0
    for q1,q2,m1,m2 in product(map(F,(-2,-1,0,1,2)),map(F,(-1,0,1)),map(F,(1,2,5)),map(F,(1,3))):
        j,k=impulse(q1,q2,g);a,b=via_recoil(q1,q2,m1,m2,g)
        assert (a,b)==direct(q1,q2,m1,m2,g)
        assert add(j,k)==z and add(scale(m1,a),scale(m2,b))==z
        assert impulse(-q1,q2,g)==(scale(-1,j),scale(-1,k))
        if q1*q2==0:assert (j,k)==(z,z)
        v1=scale(1/m1,p1);v2=scale(1/m2,p2)
        kinetic=energy(add(p1,j),m1)+energy(add(p2,k),m2)-energy(p1,m1)-energy(p2,m2)
        work=dot(sub(v1,v2),j)+dot(j,j)*(1/m1+1/m2)/2
        assert kinetic==work
        # Norms/units are inputs: the face does not determine absolute scales.
        assert via_recoil(3*q1,3*q2,m1,m2,scale(F(1,9),g))==(a,b)
        assert via_recoil(q1,q2,7*m1,7*m2,scale(7,g))==(a,b)
        count+=1
    q1,q2,m1,m2=map(F,(1,-2,2,3))
    j,k=impulse(q1,q2,g);a,b=via_recoil(q1,q2,m1,m2,g)
    one_body_residual=j
    wrong_mass_residual=sub(scale(1/m1,k),b)
    intensity_residual=sub(impulse(abs(q1),abs(q2),g)[0],j)
    kinetic_from_rest=energy(j,m1)+energy(k,m2)
    assert one_body_residual!=z and wrong_mass_residual!=z and intensity_residual!=z
    assert kinetic_from_rest==10
    inferred_mass_ratios=tuple(-v/u for u,v in zip(a,b) if u)
    assert inferred_mass_ratios==(m1/m2,)*3
    assert impulse(-q1,-q2,g)==(j,k)
    assert impulse(3*q1,q2/3,g)==(j,k)
    rejected=0
    for bad in (F(0),F(-1)):
        try:via_recoil(q1,q2,bad,m2,g)
        except ValueError:rejected+=1
    assert rejected==2
    # Matrix witness: the direct 6x1 column equals inverse inertia times
    # the balanced impulse column. The single-column basis proves equality
    # of these linear maps for every coupling coefficient on this fixture.
    R=g+scale(-1,g)
    inverse_inertia=(1/m1,)*3+(1/m2,)*3
    composite=tuple(x*y for x,y in zip(inverse_inertia,R))
    direct_column=tuple(x/m1 for x in g)+tuple(-x/m2 for x in g)
    assert composite==direct_column
    result=dict(schema='marici.nima.charge-mass-recoil-triangle.v1',status='pass',
        obligation='route/coherencer compatibility',classification='conditional Newtonian impulse model; not source-derived physics',
        stratum='two positive masses, signed charges, supplied integrated impulse kernel, exact rational fixtures',
        route_controls=count,linear_map_residual=sub(composite,direct_column),
        witness={'charges':(q1,q2),'masses':(m1,m2),'kernel':g,'impulses':(j,k),'velocity_increments':(a,b)},
        hostile_residuals={'omitted_partner_total_momentum':one_body_residual,
                          'wrong_partner_mass_velocity':wrong_mass_residual,
                          'unsigned_charge_impulse':intensity_residual,
                          'unfunded_kinetic_energy_from_rest':kinetic_from_rest},
        mass_ratio_from_nonzero_recoil_components=inferred_mass_ratios,
        charge_ambiguity='The pair reads q1*q2, not the individual charges; reciprocal rescaling or flipping both signs is invisible.',
        energy_identity='delta K=(v1-v2).J+|J|^2*(1/m1+1/m2)/2; supplied work is required',
        undetermined_normalizations=['q_i -> lambda*q_i, G -> G/lambda^2 preserves impulse and velocity',
                                    'm_i -> s*m_i, G -> s*G preserves velocity, but rescales impulse and energy'],
        physical_time='not introduced; G is an impulse input, not an iteration-time conversion',
        missing=['WG signed-charge coupling map','WG inertial mass and momentum readout','source-generated impulse kernel and its energy budget','physical clock map for a temporal extension'])
    path=ROOT/'results/charge-mass-recoil-triangle.json'
    path.write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8')
    print(json.dumps(serial(result),indent=2))

if __name__=='__main__':main()
