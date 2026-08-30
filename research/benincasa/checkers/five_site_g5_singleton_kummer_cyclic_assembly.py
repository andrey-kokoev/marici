import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-singleton-kummer-quotients.json').read_text())
assert len(src['records'])==4
n=5
character=[4*n,0,0,0,0]
packet={
 'schema':'marici.five_site_g5_singleton_kummer_cyclic_assembly.v1',
 'relative_label_orbits':4,
 'occurrences_per_orbit':n,
 'assembled_rank':4*n,
 'cyclic_character':character,
 'rational_representation':'Q[C5]^4',
 'kummer_inertia_character':-1,
 'nilpotent_rank':0,
 'cyclic_transport_preserves_relative_label':True,
 'cyclic_transport_commutes_with_kummer_inertia':True,
 'reflected_critical_points_identified_with_kummer_deck':False,
 'classification':'regular occurrence assembly tensored with sector-specific Kummer sign',
}
Path('research/benincasa/results/five-site-g5-singleton-kummer-cyclic-assembly.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
