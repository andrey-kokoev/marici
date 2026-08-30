import json
from fractions import Fraction
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-legendre-modulus.json').read_text())
assert src['label_swap']=='(1<->2) sends m to 1-m'

for h1,h2 in [(Fraction(2),Fraction(3)),(Fraction(5),Fraction(7)),(Fraction(11),Fraction(13))]:
    def m_of_r(r):
        return h2*r/(h2*r-h1)
    assert m_of_r(Fraction(0))==0
    assert m_of_r(h1/h2-Fraction(1,1000000)) < 0
    assert m_of_r(h1/h2+Fraction(1,1000000)) > 1
    # Inverse Möbius map r=h1*m/[h2*(m-1)].
    for r in (Fraction(1,3),Fraction(3,2),Fraction(9,4)):
        if h2*r==h1:
            continue
        m=m_of_r(r)
        assert h1*m/(h2*(m-1))==r

packet={
 'schema':'marici.five_site_region_pair_polar_normal_blowup.v1',
 'center':'delta_1=delta_2=0',
 'exceptional_divisor':'P(N)=P^1_[delta_1:delta_2]',
 'affine_ratio':'r=delta_1/delta_2',
 'exceptional_modulus':'m=h_2*r/(h_2*r-h_1)',
 'distinguished_rays':{
   'delta_1=0':'r=0 -> m=0',
   'delta_2=0':'r=infinity -> m=1',
   'h_2*delta_1-h_1*delta_2=0':'r=h_1/h_2 -> m=infinity',
 },
 'exceptional_open':'P^1 minus the three distinguished rays, isomorphic to the Legendre modular line P^1 minus {0,1,infinity}',
 'radial_behavior':'the common radial scale leaves m unchanged and contributes only the separately typed Kummer scaling',
 'new_carrier_datum':False,
 'carrier_interpretation':'existing flagged/projectivized two-normal geometry',
}
Path('research/benincasa/results/five-site-region-pair-polar-normal-blowup.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
