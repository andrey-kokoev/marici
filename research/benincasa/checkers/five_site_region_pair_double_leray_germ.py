import json
from pathlib import Path

pl=json.loads(Path('research/benincasa/results/five-site-region-pair-picard-lefschetz-packet.json').read_text())
assert pl['orbit_size']==5

# Zero-based edge order is (e12,e23,e34,e45,e51).  For the ordered base pair
# (g123,g125), use transported pivots (e34,e23) and retain (e12,e45,e51).
base_order=[2,1,0,3,4]


def parity(order):
    return -1 if sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))%2 else 1


records=[]
for shift,pair in enumerate(pl['labelled_C5_orbit']):
    def rotate(label):
        return 'g_'+''.join(map(str,sorted(((int(c)-1+shift)%5)+1 for c in label[2:])))
    ordered_pair=[rotate('g_123'),rotate('g_125')]
    assert sorted(ordered_pair)==pair
    transported=[(edge+shift)%5 for edge in base_order]
    # Compare with the cyclically transported source measure, whose five-cycle
    # has even parity and therefore preserves orientation.
    rotated_source=[(edge+shift)%5 for edge in range(5)]
    rank={edge:i for i,edge in enumerate(rotated_source)}
    relative=[rank[edge] for edge in transported]
    sign=parity(relative)
    records.append({
        'shift':shift,'pair':pair,'ordered_pair':ordered_pair,
        'ordered_pivots':transported[:2],
        'ordered_retained_edges':transported[2:],
        'jacobian_matrix':[[1,0],[0,1]],
        'jacobian_determinant':1,
        'source_measure_orientation_sign':sign,
        'negative_tube_side':['negative','negative'],
    })

assert all(r['source_measure_orientation_sign']==-1 for r in records)
packet={
 'schema':'marici.five_site_region_pair_double_leray_germ.v1',
 'ordered_representative':['g_123','g_125'],
 'source_tube':'Im(t)<0 and Im(y_e)<0 for every labelled edge',
 'local_wall_coordinates':['q_1=3t+y_34+y_51','q_2=3t+y_23+y_45'],
 'records':records,
 'double_leray_factor':'-(2*pi*i)^2 in the frozen source-measure orientation',
 'cyclic_orientation_constant':True,
 'local_germ_canonical':True,
 'global_relative_chain_pairing':'undefined from the current five-cycle incidence packet',
 'classification':'canonical local boundary-value germ; no global activation claim',
}
Path('research/benincasa/results/five-site-region-pair-double-leray-germ.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('double_leray_factor','cyclic_orientation_constant','local_germ_canonical','global_relative_chain_pairing')},sort_keys=True))
