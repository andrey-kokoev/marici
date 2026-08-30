import json
from pathlib import Path

exact=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-exact-survivor.json').read_text())
assert exact['representative']==['g_123','g_125']
cut_a={2,4};cut_b={1,3}
assert cut_a.isdisjoint(cut_b) and len(cut_a|cut_b)==4

packet={
 'schema':'marici.five_site_region_pair_total_energy_closure.v1',
 'representative':['g_123','g_125'],
 'physical_wall_equations':['3t+y_2+y_4=0','3t+y_1+y_3=0'],
 'nonnegative_internal_energies':True,
 'total_energy_implication':'t=0 implies y_1=y_2=y_3=y_4=0',
 'geometric_implication':'ell=C_1=C_2=C_3=C_4',
 'generic_total_energy_intersection':False,
 'closure_support':'existing four-edge multi-soft/external-collapse stratum',
 'new_carrier_datum':False,
 'scope':'real nonnegative physical closure; complexified intersections may have cancellations and require a separate algebraic audit',
}
Path('research/benincasa/results/five-site-region-pair-total-energy-closure.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
