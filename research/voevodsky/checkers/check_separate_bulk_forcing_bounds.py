"""Exact noncompact exponential fixtures for separate Green-current bounds."""
from pathlib import Path
from math import factorial
import json
import sympy as s
x=s.symbols('x',nonnegative=True)
sigma=(1,-1,1,-1);moment=(0,0,1,1)
A=(s.I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2)*s.diag(s.I,-s.I,s.I,-s.I)
J=s.diag(1,-1)
beta=s.Integer(3);eta=s.Rational(7,4);Y=s.Rational(9,4)
a=beta-Y;Z=Y
w=s.I*eta;z=s.I*Y
kf=s.Integer(5);kg=s.Integer(6)

def tail_poly(k,parameter,index):
    d=k-sigma[index]*s.I*parameter
    return 1/d if moment[index]==0 else x/d+1/d**2
F=[s.conjugate(tail_poly(kf,w,i)) for i in range(4)]
G=[tail_poly(kg,z,i) for i in range(4)]
den=-s.I*(z-s.conjugate(w))

def norm_squared(k):
    rate=2*(k-beta)
    return 1/rate+2/rate**2+2/rate**3

M=s.sqrt(norm_squared(kf)*norm_squared(kg))

def integrate_poly(poly,absolute_coefficients=False):
    return sum((abs(coef) if absolute_coefficients else coef)*s.factorial(power[0])/(kf+kg)**(power[0]+1)
               for power,coef in s.Poly(s.expand(poly),x).terms())

fixtures=[]
for name,C in (('signed',A.H*J*A),('opposite_signature_parity',A.H*A)):
    S=sum(abs(v) for v in C)
    B=sum(C[i,j]*s.I*(sigma[j]*z-sigma[i]*s.conjugate(w))*F[i]*G[j]
          for i in range(4) for j in range(4))/den
    R=sum(C[i,j]*(x**moment[i]*G[j]+F[i]*x**moment[j])
          for i in range(4) for j in range(4))/den
    CB=S*Z/(4*eta*beta*a)
    CR=S/(2*eta*s.sqrt(beta*a))
    bulk_majorant=integrate_poly(B,True)
    forcing_majorant=integrate_poly(R,True)
    assert s.simplify(CB*M-bulk_majorant).is_positive
    assert s.simplify(CR*M-forcing_majorant).is_positive
    boundary=sum(C[i,j]*F[i].subs(x,0)*G[j].subs(x,0)
                 for i in range(4) for j in range(4))/den
    assert s.simplify(integrate_poly(B)+integrate_poly(R)-boundary)==0
    fixtures.append({'channel':name,'entrywise_matrix_mass':str(S),
                     'bulk_absolute_integral_majorant':str(bulk_majorant),
                     'forcing_absolute_integral_majorant':str(forcing_majorant),
                     'bulk_bound_constant':str(CB),'forcing_bound_constant':str(CR)})
result={'passed':True,'fixtures':fixtures,
 'scope':'Exact noncompact exponential forcings, with separate absolute-integral majorants and boundary identity. General weighted L2 continuity, spatial tails, and theta convergence are proved in the companion note.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/separate-bulk-forcing-bounds.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
