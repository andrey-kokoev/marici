#!/usr/bin/env python3
"""Verify the degree count and floating Q=80/Q=160 agreement for prime overlaps."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from scipy.special import eval_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
 from scipy.special import eval_legendre
from numpy.polynomial.legendre import leggauss
L=.55;N=80
def matrix(Q):
 z,w=leggauss(Q);P=np.zeros((N,N))
 def phi(n,t):return math.sqrt((2*n+1)/(2*L))*eval_legendre(n,t/L)
 for p in (2,3):
  a=math.log(p);lo=-L;hi=L-a;t=(lo+hi)/2+(hi-lo)*z/2;wt=(hi-lo)*w/2
  B=np.array([[phi(n,tt) for n in range(N)] for tt in t]);Bs=np.array([[phi(n,tt+a) for n in range(N)] for tt in t]);T=(B.T*wt)@Bs;P-=math.log(p)/math.sqrt(p)*(T+T.T)/2
 return P
A=matrix(80);B=matrix(160);err=float(np.max(np.abs(A-B)))
out={'schema':'marici.voevodsky.two-prime-overlap-gauss-exactness.v1','maximum_basis_order':79,'maximum_product_degree':158,'gauss_order':80,'gauss_exact_polynomial_degree':159,'degree_condition_closes':2*80-1>=158,'floating_Q80_Q160_max_difference':err,'directed_plan':'Use 80 Arb Legendre roots and weights on each overlap interval; polynomial exactness leaves only ball-evaluation radius.','passed':2*80-1>=158 and err<1e-12,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_overlap_gauss_exactness.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
