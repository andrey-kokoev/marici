import json
from pathlib import Path

root=Path('research/benincasa/results')
pl=json.loads((root/'five-site-region-pair-picard-lefschetz-packet.json').read_text())
leray=json.loads((root/'five-site-region-pair-double-leray-germ.json').read_text())
ell=json.loads((root/'five-site-region-pair-polar-feynman-elliptic.json').read_text())
split=json.loads((root/'five-site-region-pair-polar-radial-legendre-split.json').read_text())

assert 'global integration-chain activation' in pl['scope']
assert leray['global_relative_chain_pairing'].startswith('undefined')
assert ell['generic_curve_genus']==1
assert split['mixed_extension']=='absent in the resolved local coefficient family'

packet={
 'schema':'marici.five_site_region_pair_polar_global_embedding_gate.v1',
 'available_source_maps':['canonical local ordered double-Leray boundary germ','local Picard-Lefschetz coefficient packet','local polar normal-cone coefficient splitting'],
 'absent_map':'source-derived global residue/Gysin morphism embedding the polar rank-two quotient into the complete five-site marked-relative Gauss-Manin system',
 'global_relative_chain_pairing':leray['global_relative_chain_pairing'],
 'forbidden_inference':'matching carrier support, local rank, or differential equation does not define the global embedding',
 'classification':'local coefficient theorem established; global assembly currently untyped',
 'new_carrier_datum':False,
 'required_next_input':'complete five-site marked-relative source complex with labelled residue maps, or a source-defined global relative-chain specialization',
}
(root/'five-site-region-pair-polar-global-embedding-gate.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
