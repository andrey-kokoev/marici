import json
from pathlib import Path

gate=json.loads(Path('research/benincasa/results/five-site-region-pair-soft-polar-monodromy-gate.json').read_text())
assert gate['required_cover'].startswith('z^2=Omega')

packet={
 'schema':'marici.five_site_region_pair_gram_root_trace.v1',
 'cover':'pi:z -> Omega=z^2',
 'deck_action':'tau(z)=-z',
 'polar_generator_on_cover':'z^(-1)',
 'deck_character':'tau(z^(-1))=-z^(-1)',
 'ordinary_normalized_trace':'(z^(-1)+(-z)^(-1))/2=0',
 'invariant_pushdown_rank':0,
 'anti_invariant_pushdown_rank':1,
 'nonzero_descent_requirement':'tensor/pair with an independently derived anti-invariant orientation or physical relative-chain character',
 'cover_alone_activates_physical_scalar':False,
 'carrier_change_required':False,
 'coefficient_data_required':'mu_2 sign/Kummer local system',
 'classification':'monodromy is trivialized upstairs, but deck descent retains sector-specific polarity data',
}
Path('research/benincasa/results/five-site-region-pair-gram-root-trace.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('ordinary_normalized_trace','invariant_pushdown_rank','anti_invariant_pushdown_rank','cover_alone_activates_physical_scalar','carrier_change_required')},sort_keys=True))
