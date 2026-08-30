import json
from pathlib import Path

root=Path('research/benincasa/results')
hom=json.loads((root/'five-site-region-pair-total-soft-homogeneity.json').read_text())
source=json.loads((root/'five-cycle-ofpt-packet.json').read_text())['five_cycle']
leray=json.loads((root/'five-site-region-pair-double-leray-germ.json').read_text())

base=sorted({x for rec in hom['records'] for x in rec['residual_denominators']})
assert len(base)==12

def rotate_site(i,k): return ((i-1+k)%5)+1
def rotate(label,k):
    if label=='G': return label
    if label.startswith('G_minus_e'):
        i,j=map(int,label[len('G_minus_e'):])
        a,b=rotate_site(i,k),rotate_site(j,k)
        # Preserve cyclic edge orientation, including e51.
        return f'G_minus_e{a}{b}'
    assert label.startswith('g_')
    return 'g_'+''.join(map(str,sorted(rotate_site(int(c),k) for c in label[2:])))

closure=sorted({rotate(label,k) for label in base for k in range(5)})
active=sorted({rotate('g_123',k) for k in range(5)})
all_facets=set(source['common_prefactor'])
for term in source['terms']: all_facets.update(term)

assert len(all_facets)==source['facet_count']==26
assert len(closure)==21
assert set(closure).isdisjoint(active)
assert set(closure)|set(active)==all_facets
assert leray['cyclic_orientation_constant']

packet={
 'schema':'marici.five_site_region_pair_total_soft_angular_support.v1',
 'representative_residual_support':base,
 'representative_support_count':len(base),
 'cyclic_residual_support':closure,
 'cyclic_residual_support_count':len(closure),
 'active_residue_wall_orbit':active,
 'active_residue_wall_count':len(active),
 'full_source_facet_partition':'26=21 residual angular support + 5 active residue walls',
 'pole_statement':'the projective ten-term residue can have poles only on the 21 frozen residual OFPT facets; summation may cancel but cannot add support',
 'cyclic_orientation_constant':True,
 'new_carrier_datum':False,
}
(root/'five-site-region-pair-total-soft-angular-support.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('representative_support_count','cyclic_residual_support_count','active_residue_wall_count','full_source_facet_partition','cyclic_orientation_constant','new_carrier_datum')},sort_keys=True))
