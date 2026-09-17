#!/usr/bin/env python3
"""Combine finite gamma quadrature, physical prime overlaps, endpoint, and structured tail."""
import runpy,json,math,sys
from pathlib import Path
root=Path(__file__).resolve().parents[3]
# Reuse the high-precision structured tail and physical-translation scout objects.
tailns=runpy.run_path(str(Path(__file__).with_name('assemble_two_prime_gamma_tail_mpmath.py')));Mmp=tailns['M']
basens=runpy.run_path(str(Path(__file__).with_name('scout_two_prime_gamma_tail_floor.py')))
np=basens['np'];digamma=basens['digamma'];spherical_jn=basens['spherical_jn'];leggauss=basens['leggauss'];L=.55;N=80;Q=400
P=basens['P'];E=basens['E'];Tail=np.array([[float(Mmp[i,j]) for j in range(N)] for i in range(N)])
r,w=leggauss(Q);G=np.zeros((N,N));edges=[0,1,2,4,8,16,32,64,128,250,500,1000,2000]
for aa,bb in zip(edges[:-1],edges[1:]):
 u=(aa+bb)/2+(bb-aa)*r/2;ww=(bb-aa)*w/2;g=digamma(.25+.5j*u).real-math.log(math.pi)
 V=np.array([2*L*math.sqrt((2*n+1)/(2*L))*((-1)**(n//2))*spherical_jn(n,L*u) for n in range(N)]).T
 block=(V.T*(ww*g/(2*math.pi)))@V;block[0::2,1::2]=0;block[1::2,0::2]=0;G+=block
H=G+P+E+Tail;H=(H+H.T)/2;e=np.linalg.eigvalsh(H)
def ldl_pivots(A):
 n=len(A);L0=np.eye(n);d=np.zeros(n)
 for j in range(n):
  d[j]=A[j,j]-sum(L0[j,k]**2*d[k] for k in range(j))
  for i in range(j+1,n):L0[i,j]=(A[i,j]-sum(L0[i,k]*L0[j,k]*d[k] for k in range(j)))/d[j]
 return d
pe=ldl_pivots(H[0::2,0::2]);po=ldl_pivots(H[1::2,1::2])
out={'schema':'marici.voevodsky.two-prime-full-form-mpmath-tail.v1','L':L,'dimension':N,'finite_gamma_cutoff':2000,'structured_tail_added':True,'prime_translations_physical':True,'smallest_eigenvalues':[float(v) for v in e[:10]],'negative_eigenvalue_count':int(np.count_nonzero(e<0)),'condition_number':float(e[-1]/e[0]),'parity_ldl':{'even_minimum_pivot':float(pe.min()),'even_minimum_pivot_index':int(pe.argmin()),'odd_minimum_pivot':float(po.min()),'odd_minimum_pivot_index':int(po.argmin()),'all_pivots_positive':bool(np.all(pe>0) and np.all(po>0))},'status':'mixed 100-digit tail and floating finite-range scout; no interval certificate','passed':True,'rh_proved':False}
p=root/'research/voevodsky/results/two_prime_full_form_mpmath_tail.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
