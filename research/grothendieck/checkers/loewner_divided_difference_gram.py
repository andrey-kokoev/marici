"""Exact check of the bivariate generator as a Loewner Gram kernel."""
import json
from fractions import Fraction
from pathlib import Path
atoms=[(Fraction(2,3),1),(Fraction(7,5),2),(Fraction(11,2),1)]
def S(t):return sum(mult/(t+lam) for lam,mult in atoms)
def F(t):return (4*t-1)*S(t)
def K(x,y):return (F(y)-F(x))/(y-x) if x!=y else sum(mult*(1+4*lam)/(x+lam)**2 for lam,mult in atoms)
def gram(x,y):return sum(mult*(1+4*lam)/((x+lam)*(y+lam)) for lam,mult in atoms)
points=[Fraction(1,4),Fraction(2,5),Fraction(3,4)]
assert all(K(x,y)==gram(x,y) for x in points for y in points)
# Exact Gram quadratic forms for hostile rational coefficient vectors.
vectors=[[1,-2,3],[3,0,-1],[-4,5,2]]
forms=[]
for c in vectors:
    value=sum(Fraction(c[i]*c[j])*K(points[i],points[j]) for i in range(3) for j in range(3))
    assert value>0;forms.append(str(value))
x,y=Fraction(2,5),Fraction(3,4);z=1-4*x;w=1-Fraction(1,4*y)
M=lambda q:S((1-q)/4)
G=(z*M(z)+w/(1-w)*M(-w/(1-w)))/(z*(1-w)+w)
assert G==y*K(x,y)
# Hostile negative lambda makes its rank-one coefficient 1+4 lambda negative.
bad_lambda=Fraction(-1,2)
assert 1+4*bad_lambda<0
result={'loewner_gram_identity_exact':True,'bivariate_generator_equals_y_times_kernel':True,
        'positive_hostile_quadratic_forms':forms,'negative_lambda_rank_one_weight':str(1+4*bad_lambda),
        'negative_spectral_coordinate_falsifier_passed':True,'zero_locations_used':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'loewner-divided-difference-gram.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
