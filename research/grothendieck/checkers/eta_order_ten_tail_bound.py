"""Exact Euler-tail theorem for eta derivatives through order ten."""
import json,math
from fractions import Fraction
from pathlib import Path
N,M,J=500_000,10,10
def qcoeff(m):
    q=[Fraction(1)]
    for k in range(1,m+1):
        b=q+[Fraction(0)]
        for r,v in enumerate(q):b[r+1]+=v/k
        q=b
    return q
def P(m,j,y):
    q=qcoeff(m);return sum(Fraction(math.comb(j,r))*(-1)**r*math.factorial(r)*q[r]*y**(j-r) for r in range(j+1))
assert all(P(m,j,Fraction(13))>0 for m in (M,M+1) for j in range(J+1))
bounds=[Fraction(math.factorial(M))*P(M,j,Fraction(14))/(Fraction(2)**M*Fraction(N)**(M+1)) for j in range(J+1)]
assert max(bounds)<Fraction(6,10**50)
result={'tail_start':N,'euler_transforms':M,'maximum_eta_derivative_order':J,'sign_polynomials_positive_at_log_x_13':True,'remainder_bounds':[f'{float(x):.7e}' for x in bounds],'all_remainders_below_6e-50':True}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'eta-order-ten-tail-bound.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
