import json
from pathlib import Path

generic=json.loads(Path('research/benincasa/results/five-site-region-pair-active-soft-blowup.json').read_text())
polar=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-double-morse-correction.json').read_text())
support=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-activation-support.json').read_text())
assert generic['first_nonanalytic_normal_order']==2
assert 'monodromy -1' in polar['local_period_type']
assert 'Gram' in support['carrier_support']

packet={
 'schema':'marici.five_site_region_pair_soft_polar_monodromy_gate.v1',
 'generic_soft_object':'delta^2*log(delta) extension with semisimple monodromy +1',
 'polar_object':'delta_G^(-1/2) Kummer line with semisimple monodromy -1',
 'ordinary_equivariant_hom_rank':0,
 'ordinary_cartier_gysin_comparison':'forbidden by unequal semisimple inertia characters',
 'required_cover':'z^2=Omega, where Omega is the existing Gram normal',
 'pullback_monodromy':'(-1)^2=+1 on the mu_2 cover',
 'typed_comparison_after_cover':True,
 'remaining_data':['Rees/weight shift','source orientation','mu_2 trace back to the Gram divisor'],
 'carrier_change_required':False,
 'coefficient_enlargement_required':'rank-one Kummer twist/ramified nearby cycle',
 'classification':'shared Gram carrier and ramified nearby-cycle calculus; sector-specific coefficient characters',
}
Path('research/benincasa/results/five-site-region-pair-soft-polar-monodromy-gate.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('ordinary_equivariant_hom_rank','required_cover','pullback_monodromy','carrier_change_required')},sort_keys=True))
