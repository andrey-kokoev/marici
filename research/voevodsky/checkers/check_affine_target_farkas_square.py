"""Positive affine target scaling, source-row rescaling, and surplus slack."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,L,rho,alpha,U):
 a,b,c=map(Q,p);L,rho,alpha,U=map(Q,(L,rho,alpha,U))
 return min(a,b,c)>=0 and min(L,rho,alpha)>0 and rho*b-a==alpha and rho*L*b+c==U
def normalize(p,L,rho,alpha,U):
 assert valid(p,L,rho,alpha,U)
 a,b,c=map(Q,p);q=(a+c/Q(L),b+c/(Q(rho)*Q(L)),Q(0))
 assert valid(q,L,rho,alpha,U);return q
def affine(p,L,rho,alpha,U,k,delta):
 k,delta=Q(k),Q(delta)
 if k<=0 or delta<0:raise ValueError('INVALID_TARGET_AFFINE_MAP')
 assert valid(p,L,rho,alpha,U)
 a,b,c=map(Q,p);q=(k*a,k*b,k*c+delta)
 assert valid(q,L,rho,k*Q(alpha),k*Q(U)+delta);return q
def rescale(p,L,rho,sigma,alpha,U):
 assert valid(p,L,rho,alpha,U) and Q(sigma)>0
 a,b,c=map(Q,p);q=(a,b*Q(rho)/Q(sigma),c)
 assert valid(q,L,sigma,alpha,U);return q
checks=0;strict_fail=0;homogeneous=0
for L,rho,sigma,k,delta in product((Q(1,2),Q(1),Q(2)),(Q(1),Q(2)),(Q(1),Q(3)),(Q(1,2),Q(2)),(Q(0),Q(1,2))):
 U=L+1;p=(Q(0),Q(1)/rho,Q(1));assert valid(p,L,rho,1,U)
 beta=k;V=k*U+delta
 left=rescale(affine(p,L,rho,1,U,k,delta),L,rho,sigma,beta,V)
 right=affine(rescale(p,L,rho,sigma,1,U),L,sigma,1,U,k,delta)
 assert left==right
 endpoint=normalize(left,L,sigma,beta,V)
 assert endpoint==normalize(right,L,sigma,beta,V)==(V/L-beta,V/(sigma*L),Q(0))
 early=rescale(affine(normalize(p,L,rho,1,U),L,rho,1,U,k,delta),L,rho,sigma,beta,V)
 if delta==0:assert early==endpoint;homogeneous+=1
 else:assert early!=endpoint;strict_fail+=1
 checks+=1
for k,delta in ((0,0),(-1,0),(1,-1)):
 try:affine((0,1,0),1,1,1,1,k,delta)
 except ValueError:pass
 else:raise AssertionError('invalid target map accepted')
report={'passed':True,'affine_rescaling_squares_checked':checks,'zero_slack_strict_squares':homogeneous,'positive_slack_strict_failures':strict_fail,'raw_square':'affine target and positive source row rescaling commute strictly','normal_form':'(V/L-beta,V/(sigma*L),0) for beta=k*alpha,V=k*U+delta','invalid_maps_refused':3,'scope':'Positive homogeneous target scale plus nonnegative target slack on fixed [0,L], primitive upper row rescaling; no arbitrary affine translation of x, proof-history 4-cell or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/affine-target-farkas-square.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
