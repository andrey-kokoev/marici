import json
from pathlib import Path

deform=json.loads(Path('research/benincasa/results/five-site-region-pair-deformation-jacobian.json').read_text())
pl=json.loads(Path('research/benincasa/results/five-site-region-pair-picard-lefschetz-packet.json').read_text())
leray=json.loads(Path('research/benincasa/results/five-site-region-pair-double-leray-germ.json').read_text())
assert deform['full_landau_jacobian_invertible']
assert pl['orbit_size']==5 and leray['cyclic_orientation_constant']

packet={
 'schema':'marici.five_site_region_pair_cyclic_deformation_naturality.v1',
 'labelled_orbit':pl['labelled_C5_orbit'],
 'equivariance_identity':'F_{sigma S}(sigma X, sigma ell, t, lambda)=sigma F_S(X,ell,t,lambda)',
 'uniqueness_identity':'solution_{sigma S}(sigma X)=sigma solution_S(X)',
 'first_jet_identity':'D solution_{sigma S}|_{sigma X} circ sigma = sigma circ D solution_S|_X',
 'threshold_identity':'t_{sigma S}(sigma X)=t_S(X)',
 'multiplier_identity':'lambda_{sigma S}(sigma X)=lambda_S(X)',
 'leray_orientation_compatible':True,
 'local_logarithmic_lines_form_C5_equivariant_family':True,
 'local_family_representation':'Q[C5]',
 'new_carrier_datum':False,
 'remaining_boundary':'global physical relative-chain pairing remains undefined',
}
Path('research/benincasa/results/five-site-region-pair-cyclic-deformation-naturality.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('threshold_identity','leray_orientation_compatible','local_logarithmic_lines_form_C5_equivariant_family','new_carrier_datum')},sort_keys=True))
