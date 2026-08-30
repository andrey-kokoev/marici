import json
from pathlib import Path

root=Path('research/benincasa/results')
leray=json.loads((root/'five-site-region-pair-double-leray-germ.json').read_text())
natural=json.loads((root/'five-site-region-pair-cyclic-deformation-naturality.json').read_text())
inc=json.loads((root/'five-site-region-pair-total-soft-incidence-kernel.json').read_text())

assert leray['global_relative_chain_pairing'].startswith('undefined')
assert natural['new_carrier_datum'] is False
assert inc['classification']=='pure occurrence redundancy before coefficient differential'

packet={
 'schema':'marici.five_site_region_pair_total_soft_overlap_gate.v1',
 'available':['five source residue sectors','cyclic relabelling isomorphisms','sector-local double-Leray germs','occurrence-forgetting incidence map'],
 'absent':['pairwise overlap coefficient objects','restriction maps to overlaps','source-derived Cech differential','proof of descent or colimit assembly'],
 'rank_34_kernel_status':'incidence redundancy only; not cohomology',
 'cyclic_covariance_status':'equivariant direct sum, not gluing',
 'missing_map_status':'undefined, not zero',
 'new_carrier_datum':False,
 'required_source_input':'pre-residue correspondence or iterated-residue object relating two distinct region-pair sectors on their common all-soft boundary',
}
(root/'five-site-region-pair-total-soft-overlap-gate.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
