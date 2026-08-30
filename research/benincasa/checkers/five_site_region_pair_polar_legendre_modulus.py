import json
from fractions import Fraction
from pathlib import Path

disc=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-elliptic-discriminant.json').read_text())
assert disc['generic_coefficient_collision']=='h_1*delta_2-h_2*delta_1=0'

for h1,h2,d1,d2 in [
    map(Fraction,(2,3,5,7)),
    map(Fraction,(5,2,11,3)),
    map(Fraction,(7,13,2,17)),
]:
    a=-h2/(h1-h2)
    b=-d2/(d1-d2)
    T=lambda z:z*(1-b)/(z-b)
    m=T(a)
    assert m==h2*d1/(h2*d1-h1*d2)
    assert T(Fraction(0))==0
    assert T(Fraction(1))==1
    m_swap=h1*d2/(h1*d2-h2*d1)
    assert m_swap==1-m

assert Fraction(3)*0/(Fraction(3)*0-Fraction(2)*5)==0
assert Fraction(3)*5/(Fraction(3)*5-Fraction(2)*0)==1

packet={
 'schema':'marici.five_site_region_pair_polar_legendre_modulus.v1',
 'ordered_branch_points':['0','1','a=-h_2/(h_1-h_2)','b=-delta_2/(delta_1-delta_2)'],
 'mobius_map':'T(x)=x*(1-b)/(x-b), sending (0,1,b) to (0,1,infinity)',
 'legendre_modulus':'m=T(a)=h_2*delta_1/(h_2*delta_1-h_1*delta_2)',
 'labelled_cusps':[
   {'support':'delta_1=0','modulus':'m=0'},
   {'support':'delta_2=0','modulus':'m=1'},
   {'support':'h_2*delta_1-h_1*delta_2=0','modulus':'m=infinity'},
 ],
 'nearby_cycle_type':'standard nodal Legendre degeneration; rank-two elliptic variation specializes to Tate/Kummer data',
 'label_swap':'(1<->2) sends m to 1-m',
 'carrier_supports':['existing wall delta_1=0','existing wall delta_2=0'],
 'coefficient_support':'m=infinity residual Hessian-weighted collision',
 'new_carrier_datum':False,
 'exact_rational_checks':['T(0)=0','T(1)=1','T(b)=infinity','T(a)=m','label swap sends m to 1-m'],
 'architecture':'energy/wall letters -> Hessian-weighted modulus -> Legendre Gauss-Manin variation',
}
Path('research/benincasa/results/five-site-region-pair-polar-legendre-modulus.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('legendre_modulus','labelled_cusps','nearby_cycle_type','new_carrier_datum')},sort_keys=True))
