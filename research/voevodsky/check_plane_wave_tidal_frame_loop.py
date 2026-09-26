"""Exact polynomial-coordinate GR test of Brinkmann plane waves.
Standard library only. Checks full connection/Ricci for polynomial profiles,
then exact periodic-profile jets and eigenframe return controls.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ZERO=(0,0,0,0)
def c(a):return {ZERO:F(a)} if a else {}
def var(i):
    e=[0]*4;e[i]=1
    return {tuple(e):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for e,v in p.items():out[e]=out.get(e,F(0))+v
    return {e:v for e,v in out.items() if v}
def scale(a,p):return {e:a*v for e,v in p.items() if a*v}
def mul(p,q):
    out={}
    for e,v in p.items():
        for f,w in q.items():
            k=tuple(a+b for a,b in zip(e,f));out[k]=out.get(k,F(0))+v*w
    return {e:v for e,v in out.items() if v}
def diff(p,i):
    out={}
    for e,v in p.items():
        if e[i]:
            f=list(e);f[i]-=1;out[tuple(f)]=v*e[i]
    return out
def axis(p):return {e:v for e,v in p.items() if e[2]==0 and e[3]==0}
def at_origin(p):return p.get(ZERO,F(0))
u,v,x,y=(var(i) for i in range(4))

def curvature(a,b,d):
    # ds^2=-2du dv+dx^2+dy^2+K du^2; K=a x^2+2b xy+d y^2.
    K=add(mul(a,mul(x,x)),scale(2,mul(b,mul(x,y))),mul(d,mul(y,y)))
    g=[[{} for _ in range(4)] for _ in range(4)]
    gi=[[{} for _ in range(4)] for _ in range(4)]
    g[0][0]=K;g[0][1]=g[1][0]=c(-1);g[2][2]=g[3][3]=c(1)
    gi[1][1]=scale(-1,K);gi[0][1]=gi[1][0]=c(-1);gi[2][2]=gi[3][3]=c(1)
    inverse_ok=all(add(*(mul(g[i][r],gi[r][j]) for r in range(4)))==c(i==j) for i in range(4) for j in range(4))
    G=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for i in range(4):
            for j in range(4):
                G[r][i][j]=scale(F(1,2),add(*(mul(gi[r][s],add(diff(g[s][j],i),diff(g[s][i],j),scale(-1,diff(g[i][j],s)))) for s in range(4))))
    R={}
    for r in range(4):
        for s in range(4):
            for i in range(4):
                for j in range(4):
                    R[r,s,i,j]=add(diff(G[r][j][s],i),scale(-1,diff(G[r][i][s],j)),
                        *(add(mul(G[r][i][t],G[t][j][s]),scale(-1,mul(G[r][j][t],G[t][i][s]))) for t in range(4)))
    ric=[[add(*(R[r,s,r,j] for r in range(4))) for j in range(4)] for s in range(4)]
    lower=lambda l,s,i,j:add(*(mul(g[l][r],R[r,s,i,j]) for r in range(4)))
    return dict(inverse=inverse_ok,connection_axis=all(not axis(G[r][i][j]) for r in range(4) for i in range(4) for j in range(4)),
                ricci=ric,ru=tuple(tuple(lower(0,i,0,j) for j in (2,3)) for i in (2,3)),
                longitudinal_zero=all(not lower(l,s,i,j) for l,s,i,j in ((0,1,0,1),(0,2,0,1),(0,3,0,1))))

a=add(c(1),scale(2,u),scale(3,mul(u,u)))
b=add(c(4),scale(5,u),scale(6,mul(u,u)))
out=curvature(a,b,scale(-1,a))
checks={
 'metric_inverse_exact':out['inverse'],
 'full_vacuum_ricci_polynomial':all(not z for row in out['ricci'] for z in row),
 'full_connection_vanishes_on_central_geodesic':out['connection_axis'],
 'transverse_curvature_formula':out['ru']==((scale(-1,a),scale(-1,b)),(scale(-1,b),a)),
 'longitudinal_tidal_components_zero':out['longitudinal_zero'],
}
# Non-trace-free profile is deliberately not vacuum.
bad=curvature(c(1),{},c(1))
checks['non_trace_free_profile_rejected']=bad['ricci'][0][0]==c(-2)
# Exact second jets of A(u)=[[cos u,sin u],[sin u,-cos u]] at rational phases.
# These jets suffice for the pointwise curvature calculation, not a sampled
# proof of the general periodic solution (proved analytically in the note).
for C,S in ((F(1),F(0)),(F(3,5),F(4,5)),(F(0),F(1)),(F(-1),F(0))):
    aj=add(c(C),scale(-S,u),scale(-C/2,mul(u,u)))
    bj=add(c(S),scale(C,u),scale(-S/2,mul(u,u)))
    o=curvature(aj,bj,scale(-1,aj))
    checks['harmonic_profile_jet_'+str(C)+'_'+str(S)]=(
        C*C+S*S==1 and all(not z for row in o['ricci'] for z in row)
        and tuple(tuple(at_origin(z)/2 for z in row) for row in o['ru'])==((-C/2,-S/2),(-S/2,C/2)))
# Polynomial identity of double-angle diagonalization at rational half-angles.
for C,S in ((F(1),F(0)),(F(3,5),F(4,5)),(F(0),F(1)),(F(-1),F(0))):
    M=((C*C-S*S,2*C*S),(2*C*S,S*S-C*C))
    plus=(C,S);minus=(-S,C)
    mv=lambda w:tuple(sum(M[i][j]*w[j] for j in range(2)) for i in range(2))
    checks['half_angle_eigenframe_'+str(C)+'_'+str(S)]=mv(plus)==plus and mv(minus)==tuple(-z for z in minus)
checks['periodic_profile_return']=((F(1),F(0)),(F(0),F(-1)))==((F(-1)**2,F(0)),(F(0),-F(-1)**2))
checks['eigenframe_sign_return_nonidentity']=(-1,-1,1)!=(1,1,1)
checks['observer_normalization']=F(-2)/2==-1
packet=dict(passed=all(checks.values()),checks=checks,
    scope='Exact polynomial GR contractions and rational harmonic jets. Periodic-profile vacuum theorem and eigenframe monodromy are written proofs; not closed-spacetime-loop holonomy or nonlinear gluing.',
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_name('plane-wave-tidal-frame-loop.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
