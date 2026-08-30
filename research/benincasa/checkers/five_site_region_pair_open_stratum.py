import json
from fractions import Fraction as F
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-source-residue.json').read_text())
deform=json.loads(Path('research/benincasa/results/five-site-region-pair-deformation-jacobian.json').read_text())
assert deform['full_landau_jacobian_invertible']
t=[F(x) for x in src['t_interval']]
y=[[F(x) for x in row] for row in src['edge_energy_intervals']]
walls={k:[F(x) for x in row] for k,row in src['remaining_wall_intervals'].items()}
assert t[1]<0 and all(row[0]>0 for row in y)
assert all(not row[0]<=0<=row[1] for row in walls.values())
margin=min(-t[1],*(row[0] for row in y),*(min(abs(row[0]),abs(row[1])) for row in walls.values()))
assert margin>0

packet={
 'schema':'marici.five_site_region_pair_open_stratum.v1',
 'representative':['g_123','g_125'],
 'certified_rational_margin':str(margin),
 'certified_decimal_margin':float(margin),
 'separated_supports':['total energy t=0','all five edge-soft loci','every remaining frozen source wall'],
 'implicit_neighbourhood_exists':True,
 'local_discriminant_location':'open stratum of the existing labelled pair incidence',
 'excess_nearby_or_gysin_data_required_locally':False,
 'new_carrier_datum':False,
 'scope':'generic neighbourhood only; boundary closure of the multivariate discriminant remains uncomputed',
}
Path('research/benincasa/results/five-site-region-pair-open-stratum.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
