import json
from pathlib import Path

exact=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-exact-survivor.json').read_text())
residue=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-source-residue.json').read_text())
assert exact['both_physical_gradients_nonzero'] and exact['positive_multiplier_ratio']==1
assert residue['transverse_morse_nondegenerate'] and residue['summed_coefficient_certified_nonzero']


def rotate(label,shift):
    sites=sorted(((int(c)-1+shift)%5)+1 for c in label[2:])
    return 'g_'+''.join(map(str,sites))


orbit=[]
for shift in range(5):
    pair=sorted([rotate('g_123',shift),rotate('g_125',shift)])
    if pair not in orbit: orbit.append(pair)
assert len(orbit)==5

packet={
 'schema':'marici.five_site_region_pair_picard_lefschetz_packet.v1',
 'representative':['g_123','g_125'],
 'labelled_C5_orbit':orbit,
 'orbit_size':5,
 'local_coordinates':'q_1=s+Q_1(z)+..., q_2=-s+Q_2(z)+..., z in R^2',
 'normal_residue_reduction':'Res_s[d^3ell/(q_1*q_2)]=nonzero_unit*d^2z/(delta+Q_1+Q_2+...)',
 'transverse_quadratic_form':'positive definite',
 'local_period_type':'logarithmic rank-one Kummer/vanishing-cycle coefficient',
 'local_monodromy':'additive 2*pi*i times the nonzero source-normalized residue coefficient',
 'cyclic_assembly_dimension':5,
 'C5_character':[5,0,0,0,0],
 'rational_representation':'Q[C5]',
 'carrier_support':'existing labelled pair incidence of connected-region walls',
 'new_carrier_datum':False,
 'scope':'local Picard-Lefschetz coefficient packet; global integration-chain activation and inter-orbit sewing not asserted',
}
Path('research/benincasa/results/five-site-region-pair-picard-lefschetz-packet.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('orbit_size','local_period_type','cyclic_assembly_dimension','C5_character','new_carrier_datum')},sort_keys=True))
