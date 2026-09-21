"""Smoke-test the explicit four-tail evaluator on a declared test forcing."""
from pathlib import Path
import sys, cmath
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from clark_feature_evaluator import Shell,ClarkFeatureEvaluator,phi_one,phi_completed,phi_one_pair_shell

def main():
    ev=ClarkFeatureEvaluator([Shell(0.1,0.4)],lambda x:phi_completed(x,64),quadrature=1024)
    z=0.7+1.4j; w=0.3+1.1j
    C=[[0,0,-.5,.5],[0,0,-.5,.5],[-.5,-.5,0,0],[.5,.5,0,0]]
    u=[(0.1,0.4)]; v=[(0.1,0.4)]
    h=ev.event_feature(u,z)
    pieces=ev.shell_features([(0.1,0.2),(0.2,0.4)],z)
    joined=[sum(piece[i] for piece in pieces) for i in range(4)]
    h_join=ev.event_feature([(0.1,0.2),(0.2,0.4)],z)
    assert max(abs(a-b) for a,b in zip(joined,h_join))<1e-12
    assert len(h)==4 and any(abs(x)>1e-8 for x in h)
    # Explicitly lock the canonical (+0,-0,+1,-1) port order.
    expected=[]
    for j in (0,1):
        for sigma in (1,-1):
            total=0j
            for k in range(1024):
                t=.1+(k+.5)*(.3/1024)
                total += cmath.exp(sigma*1j*z*t)*(t**j)*phi_completed(t,64)*(.3/1024)
            expected.append(total)
    assert max(abs(a-b) for a,b in zip(h,expected))<1e-12
    k=ev.divided_difference(u,v,w,z,C)
    exact=phi_one_pair_shell(1,1,.1,.4,.2)
    assert abs(phi_completed(.2,64)-phi_completed(.2,32))<1e-20
    assert abs(exact)>0
    # upper-half-plane denominator is nonzero and the finite quadrature is stable.
    assert abs(-1j*(z-w.conjugate()))>0 and abs(k)<100
    print({'passed':True,'feature_components':4,'divided_difference_finite':True,
           'scope':'Numerical adapter only; completed arithmetic Phi is still an input'})
if __name__=='__main__':main()
