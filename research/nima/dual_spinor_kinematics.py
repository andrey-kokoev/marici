"""Exact rational spinor-helicity and dual-coordinate transport primitives."""
import sympy as s


def adjugate2(m):
    return s.Matrix([[m[1,1],-m[0,1]],[-m[1,0],m[0,0]]])


def momentum_conserving_kinematics(lambdas, tilde_prefix):
    """Complete the last two tilde spinors and construct cyclic dual x_i."""
    n=len(lambdas)
    if len(tilde_prefix)!=n-2: raise ValueError('need n-2 seed tilde spinors')
    lam={i+1:s.Matrix(v) for i,v in enumerate(lambdas)}
    til={i+1:s.Matrix(v) for i,v in enumerate(tilde_prefix)}
    L=s.Matrix.hstack(lam[n-1],lam[n])
    if L.det()==0: raise ValueError('last two lambda spinors must be independent')
    residual=-sum((lam[i]*til[i].T for i in range(1,n-1)),s.zeros(2))
    solved=L.inv()*residual
    til[n-1]=s.Matrix([solved[0,0],solved[0,1]])
    til[n]=s.Matrix([solved[1,0],solved[1,1]])
    x={1:s.zeros(2)}
    for i in range(1,n+1):x[i+1]=s.simplify(x[i]-lam[i]*til[i].T)
    return lam,til,x


def x_interval(x,a,b):
    return s.simplify(x[a]-x[b])


def lower_bispinor(m):
    eps=s.Matrix([[0,1],[-1,0]])
    return eps*m*eps.T


def transport_spinor(lam,x,vertices):
    """Evaluate <v0| x_v0v1 x_v1v2 ... with alternating index type."""
    eps=s.Matrix([[0,1],[-1,0]])
    row=lam[vertices[0]].T*eps
    for j,(a,b) in enumerate(zip(vertices,vertices[1:])):
        interval=x_interval(x,a,b)
        row=s.simplify(row*(interval if j%2==0 else adjugate2(interval)))
    return row


def angle(lam,a,b):
    return s.det(s.Matrix.hstack(lam[a],lam[b]))
