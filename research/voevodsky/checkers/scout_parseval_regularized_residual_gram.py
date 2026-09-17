#!/usr/bin/env python3
"""Floating Parseval scout of the complete 92x92 regularized residual Gram."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,spherical_jn,roots_legendre
from numpy.polynomial.legendre import legval
root=Path(__file__).parents[1]/'results';d=np.load(root/'two_prime_regularized_rank670_vectors.npz');Z=d['schur_vectors'];P=d['retained'];S=d['finite_schur'];L=.55;N=670;k=np.arange(N);sc=np.sqrt((2*k+1)/(2*L));qR=(digamma(.25+125j).real-math.log(math.pi))/2;terms=[(math.log(p),math.log(p)/math.sqrt(p)) for p in (2,3)]
# Physical H=(qR I+Pprime+E)Z, integrated piecewise.
breaks=sorted(set([-L,L]+[-L+a for a,c in terms]+[L-a for a,c in terms]));xp,wp=roots_legendre(900);G=np.zeros((92,92));am=sc*np.array([2*L/(n+1) if False else 0 for n in k]) # overwritten by endpoint moments below
# endpoint moments from stored midpoint construction formula
from scipy.special import iv
xx=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*xx))*iv(n+.5,xx) for n in k]);am=ap*((-1.)**k);ep_plus=am@Z;ep_minus=ap@Z
for left,right in zip(breaks[:-1],breaks[1:]):
 x=(left+right)/2+(right-left)*xp/2;w=(right-left)*wp/2;base=np.column_stack([legval(x/L,Z[:,j]*sc) for j in range(92)]);H=qR*base
 for a,c in terms:
  shifted=np.zeros_like(H);mp=x+a<=L;mm=x-a>=-L
  if np.any(mp):shifted[mp]+=np.column_stack([legval((x[mp]+a)/L,Z[:,j]*sc) for j in range(92)])
  if np.any(mm):shifted[mm]+=np.column_stack([legval((x[mm]-a)/L,Z[:,j]*sc) for j in range(92)])
  H-=.5*c*shifted
 H+=.5*(np.exp(x[:,None]/2)*ep_plus+np.exp(-x[:,None]/2)*ep_minus);G+=H.T@(w[:,None]*H)
# Band correction from K=M_{1_band(q-qR)}.
orders=np.arange(N);norm=2*L*np.sqrt((2*orders+1)/(2*L));ph=(-1.)**(orders//2);z,w=roots_legendre(420)
for aa,bb in [(0,1),(1,2),(2,4),(4,8),(8,16),(16,32),(32,64),(64,128),(128,250)]:
 u=(aa+bb)/2+(bb-aa)*z/2;ww=(bb-aa)*w/2;V=(norm[:,None]*ph[:,None]*spherical_jn(orders[:,None],L*u[None,:])).T;FZ=V@Z;m=(digamma(.25+.5j*u).real-math.log(math.pi))/2-qR;b0=qR-sum(c*np.cos(u*a) for a,c in terms)
 # Endpoint Fourier amplitudes in the same real parity convention are already represented by V@Ecoeff.
 Ecoeff=.5*(np.outer(ap,ep_plus)+np.outer(am,ep_minus));FE=V@Ecoeff;FH=b0[:,None]*FZ+FE;G+=(FZ.T@((ww/math.pi*m*m)[:,None]*FZ)+2*FH.T@((ww/math.pi*m)[:,None]*FZ));
# Enforce exact parity: the real positive-frequency representation suppresses the missing i phase only within parity blocks.
parity=np.array([0 if np.linalg.norm(Z[0::2,j])>=np.linalg.norm(Z[1::2,j]) else 1 for j in range(Z.shape[1])])
for i in range(92):
 for j in range(92):
  if parity[i]!=parity[j]:G[i,j]=0
# subtract retained projection
A=np.load(root/'rank670_gamma_floor_midpoint.npz')['matrix'];finite_A2=Z.T@A@A@Z;parseval_minus_finite=(G-finite_A2);parseval_minus_finite=(parseval_minus_finite+parseval_minus_finite.T)/2;PAZ=P.T@A@Z;RG=(G-PAZ.T@PAZ);RG=(RG+RG.T)/2;alpha=.5897761979384148;lower=(S-RG/alpha);lower=(lower+lower.T)/2;ev=np.linalg.eigvalsh(lower)
out={'schema':'marici.voevodsky.parseval-regularized-residual-gram-scout.v1','parseval_norm_gram_range':[float(np.linalg.eigvalsh((G+G.T)/2)[0]),float(np.linalg.eigvalsh((G+G.T)/2)[-1])],'finite_A2_gram_range':[float(np.linalg.eigvalsh((finite_A2+finite_A2.T)/2)[0]),float(np.linalg.eigvalsh((finite_A2+finite_A2.T)/2)[-1])],'parseval_minus_finite_range':[float(np.linalg.eigvalsh(parseval_minus_finite)[0]),float(np.linalg.eigvalsh(parseval_minus_finite)[-1])],'residual_gram_min':float(np.linalg.eigvalsh(RG)[0]),'residual_gram_max':float(np.linalg.eigvalsh(RG)[-1]),'complete_residual_norm':float(math.sqrt(max(0,np.linalg.eigvalsh(RG)[-1]))),'a_posteriori_lower_form_min':float(ev[0]),'negative_residual_gram_eigenvalues_below_minus_1e-9':int(np.sum(np.linalg.eigvalsh(RG)<-1e-9)),'status':'floating Parseval scout','passed':float(ev[0])>0 and np.linalg.eigvalsh(RG)[0]>-1e-8,'rh_proved':False};p=root/'parseval_regularized_residual_gram_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
