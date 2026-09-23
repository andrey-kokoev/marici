"""Affine Farkas bridge and a genuine two-input postcomposition on the square."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
rows=((-Q(1),Q(0)),(Q(1),Q(0)),(Q(0),-Q(1)),(Q(0),Q(1)))
b=(Q(0),Q(1),Q(0),Q(1));dx=(Q(1),Q(1),Q(0),Q(0));dy=(Q(0),Q(0),Q(1),Q(1))
def dot(a,c):return sum((x*y for x,y in zip(a,c)),Q(0))
def cert(m,c,v,T):return min((*m,c))>=0 and tuple(dot(tuple(r[j] for r in rows),m) for j in range(2))==tuple(v) and dot(b,m)+c==Q(T)
def mix(x,y,t):return tuple((1-t)*a+t*z for a,z in zip(x,y))
def post(m,c,T,k,ell,delta):
 assert cert(m,c,(1,0),T) and min((k,ell,delta))>=0
 # Second input is primitive y<=1 with proof m_y=(0,0,0,1).
 ym=(Q(0),Q(0),Q(0),Q(1));q=tuple(k*m[i]+ell*ym[i] for i in range(4));s=k*c+delta;U=k*T+ell+delta
 assert cert(q,s,(k,ell),U);return q,s,U
checks=0;nonzero=0
for T,k,ell,delta,t in product((Q(2),Q(3)),(Q(1),Q(2)),(Q(1),Q(2)),(Q(0),Q(1,2),Q(1)),(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))):
 base=(Q(0),Q(1),Q(0),Q(0));c=T-1
 x=tuple(base[i]+c*dx[i] for i in range(4));y=tuple(base[i]+c*dy[i] for i in range(4))
 assert cert(x,0,(1,0),T) and cert(y,0,(1,0),T)
 bridge=mix(x,y,t)
 p,s,U=post(bridge,Q(0),T,k,ell,delta)
 px,sx,_=post(x,Q(0),T,k,ell,delta);py,sy,_=post(y,Q(0),T,k,ell,delta)
 assert p==mix(px,py,t) and s==sx==sy==delta
 # Extra slack is consumed with interpolated source witness d_t, B=1.
 dt=mix(dx,dy,t);assert dot(b,dt)==1
 norm=tuple(p[i]+delta*dt[i] for i in range(4))
 assert norm==mix(tuple(px[i]+delta*dx[i] for i in range(4)),tuple(py[i]+delta*dy[i] for i in range(4)),t)
 assert cert(norm,Q(0),(k,ell),U)
 if delta:nonzero+=1
 checks+=1
assert checks>50 and nonzero>0
report={'passed':True,'two_input_postcomposition_squares':checks,'positive_added_slack_cases':nonzero,'bridge':'P_k,ell,delta(interp_t(x,y))=interp_t(P(x),P(y)) for fixed second proof','residual_normalization':'N_d_t P(interp_t)=interp_t(N_dx P(x),N_dy P(y)), d_t=(1-t)dx+t dy','fine_replay':'retains two distinct witness histories; no declared 2-cell naturality or higher filler','scope':'Fixed irredundant unit-square source; second input primitive y<=1, nonnegative k,ell,delta. Packet-affine equality only, not arbitrary proof composition or analytic authority.'}
out=Path(__file__).resolve().parents[1]/'results/square-affine-bridge-postcomposition.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
