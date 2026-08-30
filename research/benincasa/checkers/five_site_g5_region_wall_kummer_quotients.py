import json
from pathlib import Path

grad=json.loads(Path('research/benincasa/results/five-site-g5-region-wall-tangent-census.json').read_text())
coef=json.loads(Path('research/benincasa/results/five-site-g5-region-wall-source-coefficients.json').read_text())
assert grad['all_thirty_tangent_gradients_certified_nonzero']
assert coef['all_tested_coefficients_certified_nonzero']
supported=sorted(set(q['label'] for q in coef['exact_interval_certificates']))
absent=sorted(set(q['label'] for q in coef['blocked']))
assert len(supported)==9 and len(absent)==6 and not set(supported)&set(absent)
records=[]
for label in supported:
    gs=[q for sh in grad['exact_interval_certificates'] for q in sh['walls'] if q['label']==label]
    cs=[q for q in coef['exact_interval_certificates'] if q['label']==label]
    assert len(gs)==len(cs)==2 and all(q['certified_nonzero'] for q in gs+cs)
    records.append({'label':label,'sheet_count':2,'local_discriminant':'h^2+lambda^2*tau',
                    'quotient_rank':1,'semisimple_monodromy':-1,'nilpotent_rank':0})
packet={'schema':'marici.five_site_g5_region_wall_kummer_quotients.v1',
        'supported_relative_label_count':len(supported),'supported_labels':supported,
        'source_absent_relative_label_count':len(absent),'source_absent_labels':absent,
        'records':records,'cyclic_assembled_rank':5*len(supported),
        'cyclic_character':[5*len(supported),0,0,0,0],
        'classification':'nine Kummer coefficient families and six source-absent carrier incidences',
        'new_carrier_generator':False}
Path('research/benincasa/results/five-site-g5-region-wall-kummer-quotients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
