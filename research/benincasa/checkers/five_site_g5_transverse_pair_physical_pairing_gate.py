import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-cycle-ofpt-packet.json').read_text())
gys=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-gysin-covariance.json').read_text())
assert gys['strict_local_gysin_map_exists'] and not gys['physical_relative_chain_map_constructed']
available=sorted(src['five_cycle'].keys())
required=['integration_chain','contour_orientation','denominator_regulator_map','relative_boundary_map']
assert not any(q in src or q in src['five_cycle'] for q in required)
packet={'schema':'marici.five_site_g5_transverse_pair_physical_pairing_gate.v1',
 'frozen_source_packet':'five-cycle-ofpt-packet.json','available_five_cycle_fields':available,
 'missing_required_fields':required,
 'local_de_rham_gysin_status':'constructed and cyclically coherent',
 'physical_relative_chain_map_status':'undefined',
 'physical_pairing_status':'undefined, neither zero nor nonzero',
 'prohibited_inference':'source coefficient nonzero does not construct the physical supported chain map',
 'upstream_requirement':'source-derived five-cycle contour-to-denominator regulator and relative-boundary packet'}
Path('research/benincasa/results/five-site-g5-transverse-pair-physical-pairing-gate.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
