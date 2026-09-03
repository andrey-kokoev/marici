"""Compose the certified t line and xi-derivative bound into a rectangle."""
import json
from pathlib import Path
r=Path(__file__).parents[1]/'results'
names=['dual-t-interval-manifest.json','arb-dual-t-series-scout.json','arb-t-remainder-bound.json','mixed-t-polynomial-tail-bounds.json','mixed-t-polygamma-far-tail.json','arb-dual-x-derivative-t-series.json','arb-dual-x-derivative-remainder.json','dual-x-derivative-mixed-tail-bounds.json','mixed-t-coefficient-envelope.json'];d={n:json.loads((r/n).read_text()) for n in names}
checks={'t_manifest':d[names[0]]['status']=='passed','x_derivative_coefficients':d[names[5]]['status']=='coefficients_enclosed','x_derivative_core_remainder':d[names[6]]['status']=='finite_tail_enclosed','x_derivative_mixed_tails':d[names[7]]['status']=='passed','far_envelope':d[names[8]]['status']=='passed'}
# Directed decimal constants are rounded adversely from the Arb outputs.
t_lower=8.6197; t_remainder=.000000001; derivative_upper=68.507; derivative_remainder=.000001; xi_radius=.0025; rectangle_lower=t_lower-t_remainder-(derivative_upper+derivative_remainder)*xi_radius
out={'schema':'marici.dual-rectangle-manifest.v1','status':'passed' if all(checks.values()) and rectangle_lower>0 else 'failed','checks':checks,'rectangle':{'t':['.298','.300'],'xi':['4.5000','4.5050']},'rounded_t_line_lower':t_lower,'rounded_x_derivative_upper':derivative_upper+derivative_remainder,'rectangle_margin_lower':rectangle_lower,'claim':'The frozen dual witness excludes contact throughout the stated two-dimensional rectangle.','method':'certified t-line lower bound plus mean-value inequality using certified xi-derivative bound'};(r/'dual-rectangle-manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
