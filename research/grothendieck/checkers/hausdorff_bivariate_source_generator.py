"""Exact-rational check of the bivariate Hausdorff source identity."""
import json,math
from fractions import Fraction
from pathlib import Path
atoms=[(Fraction(2,3),1),(Fraction(7,5),2),(Fraction(11,2),1)]
def u(lam):return Fraction(4,1+4*lam)
def A(k):return sum(mult*u(lam)**(k+1) for lam,mult in atoms)
def m(k):return A(k)/4**k
def C(k,j):return sum((-1)**r*math.comb(j,r)*m(k+r) for r in range(j+1))
def spectral(k,j):return sum(mult*4**(j+1)*lam**j/(1+4*lam)**(k+j+1) for lam,mult in atoms)
assert all(C(k,j)==spectral(k,j)>0 for k in range(5) for j in range(5))
def M(z):return sum(mult*u(lam)/(1-z*u(lam)/4) for lam,mult in atoms)
z,w=Fraction(1,7),Fraction(1,9);den=z*(1-w)+w
generator=(z*M(z)+w/(1-w)*M(-w/(1-w)))/den
direct=sum(mult*u(lam)/((1-z*u(lam)/4)*(1-w*(1-u(lam)/4))) for lam,mult in atoms)
assert generator==direct
wrong=(z*M(z)+w/(1-w)*M(-w/(1-w)))/(z+w);assert wrong!=direct
result={'tested_k_j_square':'0..4','spectral_binomial_identity_exact':True,'bivariate_generator_identity_exact':True,'deliberately_wrong_denominator_residual':str(wrong-direct),'zero_locations_used':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'hausdorff-bivariate-source-generator.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
