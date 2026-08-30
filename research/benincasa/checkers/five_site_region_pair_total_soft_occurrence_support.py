import json
from collections import Counter
from pathlib import Path

root=Path('research/benincasa/results')
base=json.loads((root/'five-site-region-pair-total-soft-active-restriction.json').read_text())
pl=json.loads((root/'five-site-region-pair-picard-lefschetz-packet.json').read_text())

def rs(i,k): return ((i-1+k)%5)+1
def rotate(label,k):
    if label=='G': return label
    if label.startswith('G_minus_e'):
        i,j=map(int,label[len('G_minus_e'):])
        return f'G_minus_e{rs(i,k)}{rs(j,k)}'
    return 'g_'+''.join(map(str,sorted(rs(int(c),k) for c in label[2:])))

records=[]
for shift,pair in enumerate(pl['labelled_C5_orbit']):
    surviving=[rotate(x,shift) for x in base['surviving_occurrence_labels']]
    cancelled=[rotate(x,shift) for x in base['cancelled_occurrence_labels']]
    records.append({'shift':shift,'active_pair':pair,'surviving_labels':surviving,'cancelled_coincident_labels':cancelled})

surviving_occ=[x for r in records for x in r['surviving_labels']]
cancelled_occ=[x for r in records for x in r['cancelled_coincident_labels']]
mult=Counter(surviving_occ)
assert len(surviving_occ)==50
assert len(cancelled_occ)==10
assert len(set(surviving_occ))==16
assert sorted(set(x for x in cancelled_occ if len(x[2:])==2))==['g_12','g_15','g_23','g_34','g_45']
assert sorted(mult.values())==[2]*10+[5]*6

packet={
 'schema':'marici.five_site_region_pair_total_soft_occurrence_support.v1',
 'chart_count':5,
 'ambient_residual_occurrences':60,
 'cancelled_label_occurrences':len(cancelled_occ),
 'physical_pole_occurrences':len(surviving_occ),
 'distinct_physical_source_labels':len(set(surviving_occ)),
 'distinct_physical_labels':sorted(set(surviving_occ)),
 'multiplicities':dict(sorted(mult.items())),
 'cancelled_pair_wall_orbit':['g_12','g_15','g_23','g_34','g_45'],
 'records':records,
 'classification':'occurrence-resolved cyclic support; do not identify chart occurrences before sewing',
 'new_carrier_datum':False,
}
(root/'five-site-region-pair-total-soft-occurrence-support.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('chart_count','ambient_residual_occurrences','cancelled_label_occurrences','physical_pole_occurrences','distinct_physical_source_labels','new_carrier_datum')},sort_keys=True))
