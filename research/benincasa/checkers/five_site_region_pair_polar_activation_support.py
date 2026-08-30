import json
from pathlib import Path

packet={
 'schema':'marici.five_site_region_pair_polar_activation_support.v1',
 'representative':['g_123','g_125'],
 'owner_segment':'[C_2,C_4]',
 'other_segment':'[C_1,C_3]',
 'supporting_line_intersection_equation':'Omega=(C_1-C_2).((C_4-C_2)x(C_3-C_1))=0',
 'invariant_equivalent':'Omega^2 is the four-center Gram/Cayley-Menger volume determinant up to a source-fixed unit',
 'carrier_support':'existing external Gram/Cayley-Menger divisor Omega=0',
 'wall_equation_on_intersection':'|C_2-C_4|=|C_1-C_3|',
 'coefficient_support':'equality of the two labelled focal lengths on the Gram divisor',
 'real_chamber_conditions':['intersection parameters lie in [0,1] for both labelled segments'],
 'occurrence_data_required':True,
 'polar_activation_locus':'Gram divisor AND focal-length equality AND segment chamber inequalities',
 'new_carrier_datum':False,
 'classification':'existing Gram carrier plus sector-specific coefficient equation and labelled real chamber',
}
Path('research/benincasa/results/five-site-region-pair-polar-activation-support.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('carrier_support','coefficient_support','occurrence_data_required','new_carrier_datum')},sort_keys=True))
