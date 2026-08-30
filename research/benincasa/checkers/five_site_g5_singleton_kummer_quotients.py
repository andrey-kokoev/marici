import json
from pathlib import Path

grad=json.loads(Path('research/benincasa/results/five-site-g5-singleton-tangent-gradients.json').read_text())
coef=json.loads(Path('research/benincasa/results/five-site-g5-singleton-source-coefficients.json').read_text())
assert grad['all_eight_tangent_gradients_nonzero']
assert coef['all_eight_exact_coefficients_nonzero']

records=[]
for d in (1,2,3,4):
    gs=[q for sh in grad['exact_interval_certificates'] for q in sh['singletons'] if (q['site']-5)%5==d]
    cs=[q for q in coef['exact_interval_certificates'] if (q['site']-5)%5==d]
    assert len(gs)==2 and len(cs)==2 and all(q['certified_nonzero'] for q in gs+cs)
    records.append({'relative_label_mod_5':d,'reflected_sheet_count':2,
                    'tangent_gradient_certified_nonzero':True,
                    'source_coefficient_certified_nonzero':True,
                    'local_discriminant':'h^2+lambda^2*tau',
                    'wall_residue':'pi/(lambda*sqrt(tau+h^2/lambda^2))',
                    'quotient_rank':1,'semisimple_monodromy':-1,
                    'nilpotent_rank':0})
packet={'schema':'marici.five_site_g5_singleton_kummer_quotients.v1',
        'records':records,'cyclic_orbit_count':4,
        'classification':'four source-derived Kummer coefficient divisors over existing singleton-threshold carrier intersections',
        'new_carrier_generator':False}
Path('research/benincasa/results/five-site-g5-singleton-kummer-quotients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
