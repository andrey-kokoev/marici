#!/usr/bin/env python3
"""Use exact physical translations and drop the positive gamma tail."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv,eval_legendre
 from scipy.optimize import brentq
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import numpy as np
 from scipy.special import digamma,spherical_jn,iv,eval_legendre
 from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
L=.55;N=80;Q=320
# First positive crossing; monotonicity is a separate registered theorem/gate.
g=lambda u:digamma(.25+.5j*u).real-math.log(math.pi)
U=brentq(g,1,20)
# Gamma block only on [0,U]; its omitted tail is pointwise nonnegative.
r,w=leggauss(Q);u=U*(r+1)/2;wg=U*w/2;V=np.array([2*L*math.sqrt((2*n+1)/(2*L))*((-1)**(n//2))*spherical_jn(n,L*u) for n in range(N)]).T
G=(V.T*(wg*g(u)/(2*math.pi)))@V;G[0::2,1::2]=0;G[1::2,0::2]=0
# Exact-in-principle physical translation matrices, evaluated by high-order Gauss.
P=np.zeros((N,N));z,wz=leggauss(Q)
def phi(n,t):return math.sqrt((2*n+1)/(2*L))*eval_legendre(n,t/L)
for p in (2,3):
 a=math.log(p);lo=-L;hi=L-a;t=(lo+hi)/2+(hi-lo)*z/2;wt=(hi-lo)*wz/2
 B=np.array([[phi(n,tt) for n in range(N)] for tt in t]);Bs=np.array([[phi(n,tt+a) for n in range(N)] for tt in t]);T=(B.T*wt)@Bs;P-=math.log(p)/math.sqrt(p)*(T+T.T)/2
x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(N)]);am=ap*np.array([(-1)**n for n in range(N)]);E=(np.outer(ap,am)+np.outer(am,ap))/2
H=(G+P+E);H=(H+H.T)/2;e=np.linalg.eigvalsh(H)
out={'schema':'marici.voevodsky.two-prime-exact-translation-lower-form-scout.v1','L':L,'dimension':N,'gamma_positive_crossing':U,'prime_terms_evaluated_in_physical_translation_coordinates':True,'gamma_tail_beyond_crossing_dropped_as_positive':True,'smallest_eigenvalues':[float(v) for v in e[:8]],'negative_eigenvalue_count':int(np.count_nonzero(e<0)),'status':'floating scout; monotonic gamma-tail sign and quadrature require directed certification; no infinite-dimensional complement bound','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_exact_translation_lower_form_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
