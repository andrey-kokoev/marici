import json
from fractions import Fraction
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-legendre-modulus.json').read_text())
assert src['legendre_modulus']=='m=T(a)=h_2*delta_1/(h_2*delta_1-h_1*delta_2)'

def j_inverse(m):
    return m*m*(1-m)*(1-m)/(256*(1-m+m*m)**3)

# Exact checks of the universal cusp coefficients in local coordinates.
for n in (100,1000,10000):
    e=Fraction(1,n)
    assert (j_inverse(e)/e**2-Fraction(1,256)).numerator != 0
    assert abs(float(j_inverse(e)/e**2-Fraction(1,256))) < 1/n
    assert abs(float(j_inverse(1-e)/e**2-Fraction(1,256))) < 1/n
    assert abs(float(j_inverse(1/e)/e**2-Fraction(1,256))) < 1/n

packet={
 'schema':'marici.five_site_region_pair_polar_modular_normal_order.v1',
 'legendre_j_inverse':'j^-1=m^2*(1-m)^2/[256*(1-m+m^2)^3]',
 'universal_cusp_orders':{'m=0':'m^2/256+O(m^3)','m=1':'(1-m)^2/256+O((1-m)^3)','m=infinity':'m^-2/256+O(m^-3)'},
 'resolved_normal_expansions':{
   'delta_1=0':'j^-1=h_2^2*delta_1^2/(256*h_1^2*delta_2^2)+O(delta_1^3)',
   'delta_2=0':'j^-1=h_1^2*delta_2^2/(256*h_2^2*delta_1^2)+O(delta_2^3)',
   'c=h_2*delta_1-h_1*delta_2=0':'j^-1=c^2/(256*h_2^2*delta_1^2)+O(c^3)',
 },
 'ordinary_first_grade':'zero at every cusp',
 'ordinary_second_grade':'nonzero generically at every cusp',
 'interpretation':'each labelled linear normal is a square-root coordinate over the coarse modular cusp',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-polar-modular-normal-order.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
