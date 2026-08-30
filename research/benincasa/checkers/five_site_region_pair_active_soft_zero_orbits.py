import json
from decimal import Decimal,getcontext
from pathlib import Path

getcontext().prec=50
sqrt5=Decimal(5).sqrt()

# N/tau^2 after t=-tau and the endpoint substitutions, with the remaining
# positive radial ratio denoted x.
records=[
 {'soft':'y2=0','polynomial':'x^2-7*x+11','discriminant':5,'physical_roots':['(7-sqrt(5))/2']},
 {'soft':'y3=0','polynomial':'x^2-5*x+11','discriminant':-19,'physical_roots':[]},
 {'soft':'y4=0','polynomial':'x^2-x+5','discriminant':-19,'physical_roots':[]},
 {'soft':'y5=0','polynomial':'x^2+x-1','discriminant':5,'physical_roots':['(sqrt(5)-1)/2']},
]

x2=(Decimal(7)-sqrt5)/2
x5=(sqrt5-Decimal(1))/2
assert Decimal(0)<x2<Decimal(3)
assert Decimal(0)<x5<Decimal(3)
assert abs(x2*x2-7*x2+11)<Decimal('1e-48')
assert abs(x5*x5+x5-1)<Decimal('1e-48')
assert all(r['discriminant']<0 for r in records[1:3])

packet={
 'schema':'marici.five_site_region_pair_active_soft_zero_orbits.v1',
 'ordered_representative':['g_123','g_125'],
 'records':records,
 'endpoint_occurrences_per_chart':4,
 'cyclic_charts':5,
 'total_endpoint_occurrences':20,
 'zero_bearing_endpoint_types':['y2=0','y5=0'],
 'zero_free_endpoint_types':['y3=0','y4=0'],
 'physical_zero_occurrences':10,
 'zero_orbit_character':[10,0,0,0,0],
 'rational_zero_orbit':'2*Q[C5]',
 'classification':'two coefficient-zero occurrence orbits; not carrier support',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-zero-orbits.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('zero_bearing_endpoint_types','zero_free_endpoint_types','physical_zero_occurrences','zero_orbit_character','rational_zero_orbit','new_carrier_datum')},sort_keys=True))
