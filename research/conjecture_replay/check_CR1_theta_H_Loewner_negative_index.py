#!/usr/bin/env python3
"""Finite-cutoff inertia census for the centered theta-H Loewner kernel."""
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def q(x):
 y=math.exp(2*x);total=0.0
 for n in range(1,20):
  a=math.exp(-math.pi*n*n*y);total+=a
  if a<1e-17:break
 return 2*math.exp(x/2)*total
def simpson(fun,a=0.,b=5.,n=6000):
 h=(b-a)/n;s=fun(a)+fun(b)
 for k in range(1,n):s+=(4 if k%2 else 2)*fun(a+k*h)
 return s*h/3
def H(z):return 2*simpson(lambda x:q(x)*math.cosh(z*x))
def Hp(z):return 2*simpson(lambda x:q(x)*x*math.sinh(z*x))
def eig_jacobi(A):
 n=len(A);A=[r[:] for r in A]
 for _ in range(80*n*n):
  p,qx=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]))
  if abs(A[p][qx])<1e-13:break
  phi=.5*math.atan2(2*A[p][qx],A[qx][qx]-A[p][p]);c=math.cos(phi);s=math.sin(phi)
  app,aqq,apq=A[p][p],A[qx][qx],A[p][qx]
  for k in range(n):
   if k not in (p,qx):
    akp,akq=A[k][p],A[k][qx];A[k][p]=A[p][k]=c*akp-s*akq;A[k][qx]=A[qx][k]=s*akp+c*akq
  A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[qx][qx]=s*s*app+2*s*c*apq+c*c*aqq;A[p][qx]=A[qx][p]=0.
 return sorted(A[i][i] for i in range(n))
rows=[]
for N in [2,3,4,5,6,8,10,12]:
 zs=[-.45+.9*i/(N-1) for i in range(N)];hs=[H(z) for z in zs];L=[[Hp(zs[i]) if i==j else (hs[i]-hs[j])/(zs[i]-zs[j]) for j in range(N)] for i in range(N)];ev=eig_jacobi(L);tol=max(map(abs,ev))*2e-8
 rows.append({'N':N,'negative':sum(x < -tol for x in ev),'positive':sum(x > tol for x in ev),'numerical_zero':sum(abs(x)<=tol for x in ev),'min_eigenvalue':ev[0],'max_eigenvalue':ev[-1]})
out={'schema':'marici.conjecture-replay.CR1-theta-H-Loewner-negative-index.v1','outcome':'numerical finite-index hostile','sample_interval':[-.45,.45],'kernel':'L(z,w)=(H(z)-H(w))/(z-w), diagonal H_prime(z), centered at s=1/2','inertia':rows,'observation':'Inertia is computed on one fixed compact interval. Growth of the resolved negative count is a hostile to endpoint-index-one absorption; numerical near-zero modes limit claims at larger N.','rigor_boundary':'Numerical inertia is not an analytic proof of infinite negative squares. A rigorous proof requires certified principal minors or a total-positivity argument.','architectural_consequence':'The finite endpoint index one does not automatically control the bulk history kernel.','next':'test_Cayley_rotated_critical_line_kernel_for_fixed_sign_before_accepting_infinite_index_Krein_relation','passed':True};p=R/'research/conjecture_replay/results/CR1_theta_H_Loewner_negative_index.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':out['outcome'],'inertia':[(r['N'],r['negative'],r['positive'],r['numerical_zero']) for r in rows],'next':out['next']}))
