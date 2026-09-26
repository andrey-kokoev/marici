"""Symbolic identifiability controls for the declared rotor observation class."""
from pathlib import Path
import hashlib
import json
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
def clean(x): return S.simplify(S.trigsimp(S.expand_trig(x)))
def main():
    out=ROOT/'results/clock-calibration-identifiability.json'
    out.unlink(missing_ok=True)
    k,w,lam=S.symbols('k w lam',positive=True)
    t,u,v,Fi,Ff,theta1,theta2=S.symbols('t u v Fi Ff theta1 theta2',real=True)
    q=u*S.cos(2*w*t)+v*S.sin(2*w*t)
    p=v*S.cos(2*w*t)-u*S.sin(2*w*t)
    assert clean(S.diff(q,t)-2*w*p)==0
    assert clean(S.diff(p,t)+2*w*q)==0
    B=(q*p-u*v)/2
    action=B-k*w*t
    H=w*(q*q+p*p+k)
    assert clean(S.diff(action,t)-(p*S.diff(q,t)-H))==0
    # All positive rates have the same retained quarter-turn sample,
    # but at different readings of a fixed external clock.
    assert clean(q.subs(t,S.pi/(2*w))+u)==0
    assert clean(p.subs(t,S.pi/(2*w))+v)==0
    assert clean(q.subs({u:1,v:0,t:S.pi/4,w:1}))==0
    assert clean(q.subs({u:1,v:0,t:S.pi/4,w:2}))==-1
    for orientation in (1,-1):
        phase1=(Ff-orientation*Fi)/k-theta1
        phase2=(Ff-orientation*Fi)/k-theta2
        difference=S.simplify(phase2-phase1)
        assert difference==theta1-theta2
        assert S.diff(difference,k)==0
    # Unit rescaling is a different argument from the fixed-data cancellation.
    beta,dphi,energy,dt=S.symbols('beta dphi energy dt',real=True)
    alpha=dphi-beta/k
    assert S.simplify(dphi-lam*beta/(lam*k)-alpha)==0
    assert S.simplify((lam*action)/(lam*k)-action/k)==0
    # A possible additional horizontal-loop probe DOES depend on k.
    a,b,x,y=S.symbols('a b x y',positive=True)
    # Counterclockwise rectangle: bottom/right/top/left; beta=p*dq.
    circulation=S.integrate(b,(x,a,0))
    assert circulation==-a*b
    horizontal_phase=circulation/k
    assert S.diff(horizontal_phase,k)==a*b/k**2
    assert horizontal_phase.subs(k,1)!=horizontal_phase.subs(k,2)
    # Equal positions alone do not guarantee the endpoint chart cancellation.
    dF=S.symbols('dF',real=True)
    mismatch=dF/k+theta1-theta2
    assert S.diff(mismatch,k)==-dF/k**2
    inputs=(Path(__file__),ROOT/'retained-relative-phase-readout.md',ROOT/'retained-rotor-phase-transport.md')
    result={
      'schema':'marici.nima.clock-calibration-identifiability.v1',
      'classification':'common_endpoint_rotor_phases_do_not_identify_kappa_or_an_external_clock_rate',
      'time_family':'theta=omega*t; H_t=omega*(q^2+p^2+kappa), with every omega>0 preserving angular source samples',
      'phase_cancellation':'For equal endpoints and parity, phase2-phase1=theta1-theta2, independent of kappa',
      'scope_control':'Horizontal connection transport around a calibrated q,p rectangle gives phase -area/kappa and can distinguish kappa; it is a new probe, not the rotor dynamical transport.',
      'controls':['rate-rescaled Hamilton equations and action','same angular sample at different external times','different observations at a fixed clock reading','both common parity cases','action-unit rescaling','horizontal-loop counterexample to universal unobservability','endpoint mismatch hostile'],
      'limits':'No physical second, Planck constant, horizontal-loop apparatus, native product policy or universal impossibility theorem is established. Unit covariance is distinguished from nonidentifiability in the fixed observation class.',
      'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
