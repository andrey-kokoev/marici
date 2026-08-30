import json
from pathlib import Path

root=Path('research/benincasa/results')
source=json.loads((root/'five-cycle-ofpt-packet.json').read_text())['five_cycle']
residue=json.loads((root/'five-site-disjoint-region-pair-source-residue.json').read_text())
closure=json.loads((root/'five-site-region-pair-total-energy-closure.json').read_text())

active={'g_123','g_125'}
records=[]
for term in source['terms']:
    if not active.issubset(term):
        continue
    residual=list(source['common_prefactor'])+[x for x in term if x not in active]
    records.append({'term':term,'residual_denominator_count':len(residual),'residual_denominators':residual})

assert len(records)==10==residue['source_term_count']
assert {r['residual_denominator_count'] for r in records}=={8}
assert residue['summed_coefficient_certified_nonzero']
assert closure['closure_support']=='existing four-edge multi-soft/external-collapse stratum'

packet={
 'schema':'marici.five_site_region_pair_total_soft_homogeneity.v1',
 'representative':['g_123','g_125'],
 'physical_family':'uniform positive scaling (ell,C_i,t,y_i)=lambda*(ell_*,C_i*,t_*,y_i*) of the certified pinch',
 'source_term_count':len(records),
 'residual_denominators_per_term':8,
 'scalar_double_residue_coefficient':'lambda^(-8) times the certified nonzero coefficient at lambda=1',
 'residual_one_form':'lambda^(-7) after the remaining one-dimensional differential is retained',
 'radial_monodromy':'identity (integral exponent -7)',
 'coefficient_type':'Tate/integral radial grading; no new Kummer character',
 'carrier_support':closure['closure_support'],
 'global_activation':'the positive uniform scaling family is source-defined and reaches the closure',
 'new_carrier_datum':False,
 'records':records,
}
(root/'five-site-region-pair-total-soft-homogeneity.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('source_term_count','residual_denominators_per_term','scalar_double_residue_coefficient','residual_one_form','radial_monodromy','new_carrier_datum')},sort_keys=True))
