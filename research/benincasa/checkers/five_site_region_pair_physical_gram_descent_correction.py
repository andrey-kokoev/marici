import json
from pathlib import Path

current=json.loads(Path('research/benincasa/results/five-site-d3-physical-current.json').read_text())
polar=json.loads(Path('research/benincasa/results/five-site-region-pair-polar-double-morse-correction.json').read_text())
trace=json.loads(Path('research/benincasa/results/five-site-region-pair-gram-root-trace.json').read_text())
assert 'sqrt(det(H))' in current['physical_current']
assert 'square-root' in polar['local_period_type']
assert trace['invariant_pushdown_rank']==0

packet={
 'schema':'marici.five_site_region_pair_physical_gram_descent_correction.v1',
 'corrected_entries':[1841,1842],
 'invariant_gram_equation':'D=det(H)',
 'oriented_root':'z=det(Q_ext), z^2=D',
 'physical_current':'d3ell=(du_1 wedge du_2 wedge du_3)/z',
 'deck_characters':{'z^(-1)':-1,'du_1 wedge du_2 wedge du_3':-1,'d3ell':1},
 'bare_coefficient_trace':'Tr(z^(-1))=0 (retained)',
 'physical_current_descent':'Tr_or_invariant_descent((du_1 wedge du_2 wedge du_3)/z) is nonzero and canonical',
 'polar_kummer_identification':'the polar D^(-1/2) character is the already frozen external-Gram Kummer density of Entry 1216',
 'additional_betti_sign_required_for_local_current':False,
 'global_relative_chain_still_required':True,
 'new_carrier_datum':False,
 'new_coefficient_primitive':False,
 'classification':'existing Gram carrier plus already frozen physical-current Kummer/orientation pair',
}
Path('research/benincasa/results/five-site-region-pair-physical-gram-descent-correction.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('deck_characters','polar_kummer_identification','additional_betti_sign_required_for_local_current','global_relative_chain_still_required','new_coefficient_primitive')},sort_keys=True))
