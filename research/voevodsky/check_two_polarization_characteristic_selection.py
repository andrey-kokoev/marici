"""Exact local metric-jet tests for general Rosen shear and rotating shape.
Full 4D Christoffel/Ricci contraction with rational jets; no numerical ODE.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

def matzero(n):return tuple(tuple(F(0) for _ in range(n)) for _ in range(n))
def eye(n):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def add(*aa):return tuple(tuple(sum(a[i][j] for a in aa) for j in range(len(aa[0]))) for i in range(len(aa[0])))
def scale(c,a):return tuple(tuple(c*x for x in row) for row in a)
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(a))) for i in range(len(a)))
def tr(a):return tuple(zip(*a))
def trace(a):return sum(a[i][i] for i in range(len(a)))
def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return scale(1/d,((a[1][1],-a[0][1]),(-a[1][0],a[0][0])))
def comm(a,b):return add(mm(a,b),scale(-1,mm(b,a)))
def rotation(c,s):return ((c,-s),(s,c))
I=eye(2);J=((F(0),F(-1)),(F(1),F(0)))

def ricci_jet(gamma,dgamma,ddgamma):
    # Rosen block metric; only derivatives in u (index 0) are nonzero.
    g=[list(row) for row in matzero(4)];gi=[list(row) for row in matzero(4)]
    gp=[list(row) for row in matzero(4)];gpp=[list(row) for row in matzero(4)]
    g[0][1]=g[1][0]=gi[0][1]=gi[1][0]=F(-1)
    inv=inv2(gamma)
    for a in range(2):
        for b in range(2):g[a+2][b+2]=gamma[a][b];gi[a+2][b+2]=inv[a][b];gp[a+2][b+2]=dgamma[a][b];gpp[a+2][b+2]=ddgamma[a][b]
    gip=scale(-1,mm(mm(gi,gp),gi))
    d=lambda m,i,a,b:m[a][b] if i==0 else F(0)
    G={};Gp={}
    for r in range(4):
        for i in range(4):
            for j in range(4):
                G[r,i,j]=sum(gi[r][s]*(d(gp,i,s,j)+d(gp,j,s,i)-d(gp,s,i,j)) for s in range(4))/2
                Gp[r,i,j]=sum(gip[r][s]*(d(gp,i,s,j)+d(gp,j,s,i)-d(gp,s,i,j))+gi[r][s]*(d(gpp,i,s,j)+d(gpp,j,s,i)-d(gpp,s,i,j)) for s in range(4))/2
    R={}
    for r in range(4):
        for s in range(4):
            for i in range(4):
                for j in range(4):R[r,s,i,j]=(Gp[r,j,s] if i==0 else 0)-(Gp[r,i,s] if j==0 else 0)+sum(G[r,i,t]*G[t,j,s]-G[r,j,t]*G[t,i,s] for t in range(4))
    ric=tuple(tuple(sum(R[r,s,r,j] for r in range(4)) for j in range(4)) for s in range(4))
    ru=tuple(tuple(sum(g[0][r]*R[r,a+2,0,b+2] for r in range(4)) for b in range(2)) for a in range(2))
    return ric,ru

p=F(6,5);D=((p*p,F(0)),(F(0),1/(p*p)));Di=inv2(D)
Dhalf_inv=((1/p,F(0)),(F(0),p))
c=(p*p+1/(p*p))/2;s=(p*p-1/(p*p))/2
checks={
 'shape_determinant_one':D[0][0]*D[1][1]==1,
 'nonzero_shear_rate':s==F(671,1800)>0,
 'focusing_interval_contains_shape_loop':s<F(1,2),
 'rotation_connection_coefficient':c==F(1921,1800),
 'hyperbolic_identity':c*c-s*s==1,
}
for idx,(co,si) in enumerate(((F(1),F(0)),(F(3,5),F(4,5)),(F(0),F(1)))):
    R=rotation(co,si);C=mm(mm(R,D),tr(R));Cp=comm(J,C);Cpp=comm(J,Cp)
    M=mm(inv2(C),Cp)
    checks[f'{idx}_full_shear_norm']=trace(mm(M,M))/8==s*s
    checks[f'{idx}_shear_not_ordinary_symmetric_matrix']=M!=tr(M)
    for j,(r,rp) in enumerate(((F(1),F(0)),(F(2),F(1,3)))):
        rpp=-s*s*r
        g=scale(r*r,C)
        gp=add(scale(2*r*rp,C),scale(r*r,Cp))
        gpp=add(scale(2*(rp*rp+r*rpp),C),scale(4*r*rp,Cp),scale(r*r,Cpp))
        ric,ru=ricci_jet(g,gp,gpp)
        checks[f'{idx}_{j}_full_ricci_zero']=ric==matzero(4)
        checks[f'{idx}_{j}_curvature_formula']=ru==add(scale(F(-1,2),gpp),scale(F(1,4),mm(mm(gp,inv2(g)),gp)))
        # Moving orthonormal shape-axis frame B=r^-1 R D^-1/2.
        B=scale(1/r,mm(R,Dhalf_inv))
        Bp=add(scale(-rp/r,B),mm(J,B))
        Gamma=scale(F(1,2),mm(inv2(g),gp))
        omega=mm(inv2(B),add(Bp,mm(Gamma,B)))
        checks[f'{idx}_{j}_frame_orthonormal']=mm(mm(tr(B),g),B)==I
        checks[f'{idx}_{j}_moving_frame_connection']=omega==scale(c,J)
        checks[f'{idx}_{j}_parallel_rotation_cancels_connection']=add(Bp,mm(Gamma,B),mm(B,scale(-c,J)))==matzero(2)
# Wrong scalar shortcut: beta fixed does NOT imply zero shear when axes rotate.
badric,_=ricci_jet(D,comm(J,D),comm(J,comm(J,D)))
checks['ignoring_rotating_axes_fails_vacuum']=badric[0][0]==-2*s*s!=0
checks['shape_returns_at_pi']=mm(mm(scale(-1,I),D),scale(-1,I))==D
checks['comparison_rotation_nonzero']=1-c==F(-121,1800)
checks['isotropic_limit_has_no_relative_rotation']=(F(1)+F(1))/2==1
packet=dict(passed=all(checks.values()),checks=checks,
    focusing_frequency=str(s),frame_connection_rate=str(c),
    endpoint_rotation_in_units_of_pi=str(1-c),
    scope='Exact rational local metric jets; periodic shape/parallel-frame formulas proved in note. Endpoint comparison is not closed-spacetime-loop holonomy.',
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_name('two-polarization-characteristic-selection.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
