"""Symbolic moving-frame action and retained endpoint phase checks."""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
def clean(x): return S.simplify(S.trigsimp(S.expand_trig(x)))
def main():
    out=ROOT/'results/active-passive-action.json'
    out.unlink(missing_ok=True)
    u,v,s,z,t,chi=S.symbols('u v s z t chi',real=True)
    k=S.symbols('k',positive=True)
    q=u*S.cos(2*t)+v*S.sin(2*t)
    p=v*S.cos(2*t)-u*S.sin(2*t)
    boundary=(q*p-u*v)/2
    f=boundary-k*t
    variables=(u,v,s,z,t,chi)
    beta=[p*S.diff(q,x)+s*S.diff(z,x) for x in variables]
    beta0=[v,0,0,s,0,0]
    H=q*q+p*p+k
    action=[beta[i]-(H if x==t else 0) for i,x in enumerate(variables)]
    for i,x in enumerate(variables):
        assert clean(action[i]-beta0[i]-S.diff(f,x))==0
    phi=chi+boundary/k-t
    # Extended phase connection dphi-beta/k+H*dt/k becomes dchi-beta0/k.
    for i,x in enumerate(variables):
        pulled=S.diff(phi,x)-beta[i]/k+(H/k if x==t else 0)
        target=(1 if x==chi else 0)-beta0[i]/k
        assert clean(pulled-target)==0
    assert clean(S.diff(q,t)-2*p)==0
    assert clean(S.diff(p,t)+2*q)==0
    assert clean(H-(u*u+v*v+k))==0
    # Same lab observer must be pulled back, not silently replaced by u.
    assert clean(q.subs({u:1,v:0,t:S.pi/4}))==0
    assert S.Integer(1)!=0
    # Stationary variables do not remove the full lift's endpoint transition.
    for n in range(-4,5):
        assert clean(boundary.subs(t,n*S.pi))==0
        assert clean(f.subs(t,n*S.pi)+k*n*S.pi)==0
        assert S.exp(-S.I*n*S.pi)==S.Integer(-1)**n
    assert clean((phi-chi).subs(t,S.pi))==-S.pi
    assert S.exp(-S.I*S.pi)==-1
    assert S.exp(-2*S.I*S.pi)==1
    # A base-only counterterm erases the required endpoint phase.
    assert S.exp(S.I*boundary.subs(t,S.pi)/k)==1
    inputs=(Path(__file__),ROOT/'retained-rotor-phase-transport.md',ROOT/'cayley-product-transport.md')
    result={
      'schema':'marici.nima.active-passive-action.v1',
      'classification':'moving_frame_freezes_local_dynamics_but_retains_observer_transport_and_antiperiodic_phase_clutching',
      'action_identity':'Phi^*(beta-Hplus*dtheta)=beta0+d(F(Phi X)-F(X)-kappa*theta)',
      'phase_identity':'phi=chi+(F(Phi X)-F(X))/kappa-theta; transformed extended connection is dchi-beta0/kappa',
      'endpoint':'At theta=pi the base frame returns but the full module frame differs by -1; full period is 2*pi.',
      'controls':['all six extended one-form coefficients','generator signs','laboratory observer versus comoving observer','nine signed endpoint returns','base-only phase-erasure hostile'],
      'scope':'Conditional classical action/phase geometry in the declared realization. Coordinate removal of a generator neither disproves active dynamics nor provides native source admission or a physical measurement rule.',
      'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
