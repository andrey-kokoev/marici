"""Exact generalized dual-space R-invariant evaluator."""
from itertools import product
import sympy as s
from dual_spinor_kinematics import adjugate2,angle,transport_spinor,x_interval


def theta_coefficients(lam,n):
    """Return theta_i as sparse two-spinor coefficients with theta_1=0."""
    theta={1:{}}
    for i in range(1,n+1):
        nxt=dict(theta[i]);nxt[i]=nxt.get(i,s.zeros(2,1))-lam[i]
        theta[i+1]=nxt
    return theta


def theta_interval(theta,a,b):
    labels=set(theta[a])|set(theta[b])
    return {i:s.simplify(theta[a].get(i,s.zeros(2,1))-theta[b].get(i,s.zeros(2,1))) for i in labels}


def _sandwich(xi,x,left,middle,ket):
    return s.simplify((xi*x_interval(x,*left)*adjugate2(x_interval(x,*middle))*ket)[0])


def generalized_r(lam,x,n,prefix,pair,lower_spinor,upper_spinor):
    """Evaluate R_{n;prefix;ab} as a sparse degree-four eta polynomial.

    ``prefix`` is the sequence (b1,a1,...,br,ar); its last entry is a_r.
    Boundary spinors are already resolved transported rows for |a-1>, |b>.
    """
    a,b=pair;anchor=prefix[-1] if prefix else n
    xi=transport_spinor(lam,x,(n,)+tuple(prefix))
    eps=s.Matrix([[0,1],[-1,0]])
    ket_b=eps*upper_spinor.T;ket_bm1=lam[b-1]
    ket_a=lam[a];ket_am1=eps*lower_spinor.T
    den_factors=[x_interval(x,a,b).det(),
      _sandwich(xi,x,(anchor,a),(a,b),ket_b),
      _sandwich(xi,x,(anchor,a),(a,b),ket_bm1),
      _sandwich(xi,x,(anchor,b),(b,a),ket_a),
      _sandwich(xi,x,(anchor,b),(b,a),ket_am1)]
    denominator=s.prod(den_factors)
    if denominator==0: raise ValueError('singular generalized R denominator')
    theta=theta_coefficients(lam,n);tb=theta_interval(theta,b,anchor);ta=theta_interval(theta,a,anchor)
    labels=set(tb)|set(ta);q={}
    leftrow=xi*x_interval(x,anchor,a)*adjugate2(x_interval(x,a,b));rightrow=xi*x_interval(x,anchor,b)*adjugate2(x_interval(x,b,a))
    for i in labels:q[i]=s.simplify((leftrow*tb.get(i,s.zeros(2,1)))[0]+(rightrow*ta.get(i,s.zeros(2,1)))[0])
    q={i:v for i,v in q.items() if v!=0}
    angle_a=s.det(s.Matrix.hstack(lam[a],ket_am1))
    angle_b=s.det(s.Matrix.hstack(ket_b,lam[b-1]))
    prefactor=s.factor(angle_a*angle_b/denominator)
    return {m:s.factor(prefactor*s.prod(q[i] for i in m)) for m in product(tuple(q),repeat=4)}, {'denominator_factors':[s.factor(v) for v in den_factors],'xi_coefficients':q,'prefactor':prefactor}
