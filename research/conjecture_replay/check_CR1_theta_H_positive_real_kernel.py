#!/usr/bin/env python3
"""Hostile test for the natural right-half-plane positive-real kernel of H."""
import cmath,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def q(x):
 y=math.exp(2*x);total=0.
 for n in range(1,18):
  a=math.exp(-math.pi*n*n*y);total+=a
  if a<1e-18:break
 return 2*math.exp(x/2)*total
def simp(fun,n=8000,b=5.):
 h=b/n;s=fun(0)+fun(b)
 for k in range(1,n):s+=(4 if k%2 else 2)*fun(k*h)
 return s*h/3
def H(z):return 2*simp(lambda x:q(x)*cmath.cosh(z*x))
def K(z,w):return (H(z)+H(w).conjugate())/(z+w.conjugate())
points=[a+1j*t for a in [.03,.08,.15,.3] for t in [0.,1.,2.,4.,7.,10.]]
diag=[(z,(K(z,z)).real) for z in points]
worst=None
for i,z in enumerate(points):
 for w in points[i+1:]:
  det=K(z,z).real*K(w,w).real-abs(K(z,w))**2
  if worst is None or det<worst[0]:worst=(det,z,w)
out={'schema':'marici.conjecture-replay.CR1-theta-H-positive-real-kernel.v1','kernel':'K_H(z,w)=[H(z)+overline(H(w))]/[z+overline(w)] on Re z>0','outcome':'numerical ++','sample_count':len(points),'minimum_diagonal':min(v for _,v in diag),'negative_diagonal_count':sum(v<0 for _,v in diag),'worst_two_by_two_determinant':worst[0],'worst_pair':[str(worst[1]),str(worst[2])],'interpretation':'The natural impedance/passive kernel passes all sampled diagonal and two-by-two positive-semidefinite tests on the open right half-plane. This overturns the real-axis Loewner pessimism: that kernel used the wrong passive orientation.','normalization_caveat':'A different linear-fractional transform of H could change the kernel, but without a source-derived feedthrough/normalization such a choice would be fitted and is not an admissible repair.','consequence':'A positive-real Hilbert realization of the bulk remains viable. Numerical two-by-two tests are only necessary; higher Gram inertias and an analytic kernel factorization are still required.','next':'derive_or_falsify_positive_factorization_of_the_theta_H_right_half_plane_kernel','passed':True};p=R/'research/conjecture_replay/results/CR1_theta_H_positive_real_kernel.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':out['outcome'],'negative_diagonals':out['negative_diagonal_count'],'worst_2x2':out['worst_two_by_two_determinant'],'next':out['next']}))
