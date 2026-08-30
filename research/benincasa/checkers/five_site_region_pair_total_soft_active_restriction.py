import json
from pathlib import Path

p=Path('research/benincasa/results/five-site-region-pair-total-soft-angular-residues.json')
data=json.loads(p.read_text())
records=data['restricted_records']
assert data['active_restriction']==['y5=-3*t-y3','y4=-3*t-y2']
assert data['restricted_coincidence']=='g_1235|active = -g_12|active'

surviving=[r['label'] for r in records if r['simple_residue_nonzero']]
cancelled=[r['label'] for r in records if not r['simple_residue_nonzero']]
assert surviving==['G','G_minus_e34','G_minus_e45','g_1','g_1234','g_1245','g_2','g_3','g_4','g_5']
assert cancelled==['g_12','g_1235']
assert not any(r['double_leading_nonzero'] for r in records)

packet={
 'schema':'marici.five_site_region_pair_total_soft_active_restriction.v1',
 'active_equations':['g_123=3*t+y3+y5=0','g_125=3*t+y2+y4=0'],
 'elimination':['y5=-3*t-y3','y4=-3*t-y2'],
 'restricted_expression':data['restricted_expression'],
 'ambient_candidate_labels':12,
 'restricted_labelled_coincidence':'g_1235=-g_12',
 'cancelled_occurrence_labels':cancelled,
 'surviving_occurrence_labels':surviving,
 'surviving_simple_pole_classes':len(surviving),
 'double_poles':0,
 'classification':'physical restricted coefficient; Entries 1852-1853 ambient physical count corrected',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-total-soft-active-restriction.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('restricted_labelled_coincidence','cancelled_occurrence_labels','surviving_simple_pole_classes','double_poles','new_carrier_datum')},sort_keys=True))
