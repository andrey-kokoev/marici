import json
from pathlib import Path

source=json.loads(Path('research/benincasa/results/five-site-g5-complement-soft-source-coefficient.json').read_text())
assert source['coefficient_certified_nonzero']

packet={
 'schema':'marici.five_site_g5_complement_soft_divided_log.v1',
 'resolved_measure_identity':'int_0^R dr int_0^U du f(r*u) = int_0^(R*U) dw log(R*U/w) f(w)',
 'two_occurrence_kernel':'1/((h1+a*w)*(h2+a*w))',
 'singular_primitive':'K(h) ~ (1/(2*a))*log(h)^2 modulo lower logarithmic and regular terms',
 'off_diagonal_singular_term':'(K(h1)-K(h2))/(h2-h1)',
 'diagonal_singular_term':'-log(h)/(a*h)',
 'diagonal_semisimple_pole_order':-1,
 'diagonal_nilpotent_rank':1,
 'diagonal_nilpotent_square_zero':True,
 'source_coefficient_certified_nonzero':True,
 'classification':'pole-twisted logarithmic coefficient extension on existing defining-edge soft occurrence corner',
 'new_carrier_generator':False,
}
Path('research/benincasa/results/five-site-g5-complement-soft-divided-log.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
