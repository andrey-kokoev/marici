#!/usr/bin/env python3
"""Exact symbolic checks of the Cartan--Hankel generalized spectrum."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/cartan_hankel_pencil_is_a_discrete_green_probe_geometry.md'
RESULT=ROOT/'research/voevodsky/results/cartan_hankel_green_geometry.json'
SETTINGS=(s.Rational(1),s.Rational(5,6),s.Rational(3,4),s.Rational(7,10),s.Rational(2,3))

def cartan(n):return s.Matrix(n,n,lambda i,j:2 if i==j else (-1 if abs(i-j)==1 else 0))
def green(n):return s.Matrix(n,n,lambda i,j:s.Rational(min(i+1,j+1)*(n+1-max(i+1,j+1)),n+1))
def evaluation(n,settings):return s.Matrix([[t**i for i in range(1,n+1)] for t in settings])
def poly_coeff(settings,n):
 z=s.symbols('z');q=s.expand(z*s.prod(z-t for t in settings));p=s.Poly(q,z)
 return s.Matrix([p.coeff_monomial(z**i) for i in range(1,n+1)])
checks={};cartan_data={}
for n in range(1,9):
 c=cartan(n);g=green(n);checks[f'cartan_det_n{n}']=c.det()==n+1;checks[f'green_inverse_n{n}']=c*g==s.eye(n)
 a=s.symbols(f'a0:{n}');v=s.Matrix(a);energy=s.expand((v.T*c*v)[0]);expected=a[0]**2+a[-1]**2+sum((a[i+1]-a[i])**2 for i in range(n-1));checks[f'difference_energy_n{n}']=s.expand(energy-expected)==0
 cartan_data[str(n)]={'determinant':int(c.det())}
lam=s.symbols('lambda');pencil={}
for m in (4,5):
 c=cartan(5);matrix=evaluation(5,SETTINGS[:m]);q=matrix.T*matrix;h=matrix*c.inv()*matrix.T
 lhs=s.factor((q-lam*c).det());rhs=s.factor((-1)**5*lam**(5-m)*c.det()*(lam*s.eye(m)-h).det())
 checks[f'determinant_lemma_m{m}']=s.expand(lhs-rhs)==0
 checks[f'hankel_rank_m{m}']=q.rank()==m
 zero_multiplicity=s.Poly(lhs,lam).terms()[-1][0][0] if False else min(term[0][0] for term in s.Poly(lhs,lam).terms())
 checks[f'zero_multiplicity_m{m}']=zero_multiplicity==5-m
 pencil[str(m)]={'lhs':str(lhs),'effective_characteristic':str(s.factor((lam*s.eye(m)-h).det())),'zero_multiplicity':zero_multiplicity,'effective_rank':h.rank()}
c=cartan(5);m4=evaluation(5,SETTINGS[:4]);q4=m4.T*m4;rad=poly_coeff(SETTINGS[:4],5);cartan_energy=s.factor((rad.T*c*rad)[0]);hankel_energy=s.factor((rad.T*q4*rad)[0])
checks['radical_hankel_energy_zero']=hankel_energy==0
checks['radical_cartan_energy_positive']=cartan_energy>0
text=PACKET.read_text(encoding='utf-8');checks['prime_magnitude_boundary_retained']='prime magnitudes enter the separate arithmetic cutoff filtration' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.cartan-hankel-green-geometry.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'cartan_dimensions':cartan_data,'five_shell_pencils':pencil,'radical_cartan_energy':str(cartan_energy),'radical_hankel_energy':str(hankel_energy),'checks':checks,'passed':all(checks.values()),'disposition':{'established':'exact Green-kernel reduction of the Cartan-Hankel pencil','residual':'test whether generalized spectral data predicts arithmetic cutoff grades'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'zero_multiplicities':[pencil['4']['zero_multiplicity'],pencil['5']['zero_multiplicity']],'radical_cartan_energy':str(cartan_energy)}));raise SystemExit(0 if result['passed'] else 1)
