#!/usr/bin/env python3
"""Floating full weighted variation Gram (smooth derivative plus jumps) at L=.6495."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre,iv
from numpy.polynomial.legendre import legval,legder
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');U=d['packet'];Z=U-d['tail_maps'][4];L=.6495;N=1000;n=np.arange(N);sc=np.sqrt((2*n+1)/(2*L));qR=(digamma(.25+125j).real-math.log(math.pi))/2;terms=[(math.log(p),math.log(p)/math.sqrt(p)) for p in (2,3)];A0=np.load(root/'gamma_floor_L06495_rank1000_midpoint.npz')['matrix'];proj=U.T@A0@Z;breaks=sorted(set([-L,L]+[-L+a for a,c in terms]+[L-a for a,c in terms]));z,w=roots_legendre(300);xs=[];ws=[];gp=[]
def vals_der(x,C):
 y=x/L;V=np.column_stack([legval(y,C[:,j]*sc) for j in range(C.shape[1])]);D=np.column_stack([legval(y,legder(C[:,j]*sc))/L for j in range(C.shape[1])]);return V,D
xx=L/2;ap=np.array([2*L*np.sqrt((2*k+1)/(2*L))*np.sqrt(np.pi/(2*xx))*iv(k+.5,xx) for k in n]);am=ap*((-1.)**n);epplus=am@Z;epminus=ap@Z
for left,right in zip(breaks[:-1],breaks[1:]):
 x=(left+right)/2+(right-left)*z/2;ww=(right-left)*w/2;base,der=vals_der(x,Z);H=qR*der
 for a,c in terms:
  sh=np.zeros_like(H);mp=x+a<=L;mm=x-a>=-L
  if np.any(mp):sh[mp]=vals_der(x[mp]+a,Z)[1]
  if np.any(mm):sh[mm]+=vals_der(x[mm]-a,Z)[1]
  H-=.5*c*sh
 H+=.25*(np.exp(x[:,None]/2)*epplus-np.exp(-x[:,None]/2)*epminus);H-=vals_der(x,U@proj)[1];xs.append(x);ws.append(ww);gp.append(H)
x=np.concatenate(xs);ww=np.concatenate(ws);Gprime=np.vstack(gp);# Add derivative of band multiplier output.
o=np.arange(N);norm=2*L*np.sqrt((2*o+1)/(2*L));phase=np.array([(-1)**(k//2)*(1 if k%2==0 else -1j) for k in o]);qz,qw=roots_legendre(180)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*qz/2;wu=(bb-aa)*qw/2;V=(norm[:,None]*phase[:,None]*spherical_jn(o[:,None],L*u[None,:])).T;F=V@Z;m=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;Gprime+=np.real((np.exp(1j*x[:,None]*u[None,:])*(1j*u)[None,:])@((wu*m/math.pi)[:,None]*F))
wt=(1-(x/L)**2)**(-.25);nr=np.linalg.norm(Gprime,axis=1);At=float(np.sum(ww*wt*nr));Bt=np.zeros((40,40))
for i in range(len(x)):
 if nr[i]:Bt+=ww[i]*wt[i]*np.outer(Gprime[i],Gprime[i])/nr[i]
# Add jump atoms to the same dominating measure.
fplus=np.array([legval(1,Z[:,j]*sc) for j in range(40)]);fminus=np.array([legval(-1,Z[:,j]*sc) for j in range(40)])
for a,c in terms:
 for t,row in (((L-a)/L,.5*c*fplus),((-L+a)/L,-.5*c*fminus)):
  wa=(1-t*t)**(-.25);nrj=np.linalg.norm(row);At+=wa*nrj;Bt+=wa*np.outer(row,row)/nrj
VG=At*Bt;factor=4*L/(math.pi*(4000-1));tail=factor*VG;alpha=1.067569476012246;S=d['schur'][4];lower=(S-tail/alpha);lower=(lower+lower.T)/2;out={'schema':'marici.voevodsky.full-residual-variation-gram-L06495-scout.v1','physical_nodes':len(x),'weighted_total_variation':At,'variation_gram_norm':float(np.linalg.norm(VG,2)),'tail_gram_norm':float(np.linalg.norm(tail,2)),'lower_after_full_variation_tail':float(np.linalg.eigvalsh(lower)[0]),'status':'floating quadrature scout','passed':float(np.linalg.eigvalsh(lower)[0])>0,'rh_proved':False};p=root/'full_residual_variation_gram_L06495_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'full_residual_variation_gram_L06495_scout.npz',variation_gram=VG,tail_gram=tail);print(json.dumps(out,indent=2))
