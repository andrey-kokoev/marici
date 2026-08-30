import json
from pathlib import Path

old=json.loads(Path('research/benincasa/results/five-site-region-pair-active-soft-existence.json').read_text())
assert len(old['cases'])==4

packet={
 'schema':'marici.five_site_region_pair_active_soft_radial_correction.v1',
 'surviving_equations':[x['soft']+'; '+x['equality'] for x in old['cases']],
 'withdrawn_interpretations':['triangle-inequality saturation','three-center collinearity','Gram-divisor support'],
 'reason':'after y_e=0, the remaining y_i are radial distances from the soft loop point to three different centers and are not the three side lengths of one triangle',
 'correct_support':'existing intersection of the labelled edge-soft divisor with the two active region-wall divisors, together with the positive radial-distance chamber',
 'generic_edge_soft_existence':False,
 'additional_carrier_divisor_derived':False,
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-radial-correction.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
