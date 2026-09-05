"""Exact algebra for one RH-conditional transformed zero-pair atom."""
import json
from fractions import Fraction as Q
from pathlib import Path

def atom_F(r,x): return (4*x-1)/(r+x)
def mass(r): return (4*r+1)/(r*r)
def location(r): return 1/r
def reconstructed_increment(r,x): return mass(r)*x/(1+location(r)*x)
def kernel(r,x,y): return (4*r+1)/((r+x)*(r+y))
def gram_kernel(r,x,y): return mass(r)/((1+location(r)*x)*(1+location(r)*y))
def coefficient(r,n): return Q((-1)**(n-1))*(4*r+1)/(r**(n+1))
def moment(r,n): return mass(r)*location(r)**(n-1)

fixtures=[]
for r in (Q(4),Q(9),Q(25,2)):
    assert mass(r)>0 and location(r)>0
    for x,y in ((Q(1,100),Q(1,200)),(Q(2,7),Q(3,11))):
        assert atom_F(r,x)-atom_F(r,Q(0))==reconstructed_increment(r,x)
        assert kernel(r,x,y)==gram_kernel(r,x,y)
    for n in range(1,12):
        assert coefficient(r,n)==Q((-1)**(n-1))*moment(r,n)
    fixtures.append({'gamma_squared':str(r),'location':str(location(r)),'mass':str(mass(r))})
negative_mass=-mass(Q(9))
assert negative_mass<0
result={
    'atom':'(4*x-1)/(gamma_squared+x)',
    'measure_location':'1/gamma_squared',
    'measure_mass':'(4*gamma_squared+1)/gamma_squared^2',
    'increment_identity_verified':True,
    'divided_difference_gram_identity_verified':True,
    'alternating_moment_identity_through_fixture_degree_eleven':True,
    'positive_mass_for_positive_gamma_squared':True,
    'deliberate_negative_mass_fixture':str(negative_mass),
    'deliberate_negative_mass_fixture_is_negative':True,
    'fixtures':fixtures,
    'conditional_on_critical_line_zero_pairing':True,
    'zero_product_convergence_not_verified_here':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'rh-conditional-stieltjes-atom-identity.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
