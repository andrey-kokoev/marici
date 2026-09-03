"""Compose the source-only t-interval certificate artifacts."""
import json
from pathlib import Path
r=Path(__file__).parents[1]/'results';names=['arb-dual-t-series-scout.json','arb-t-remainder-bound.json','mixed-t-coefficient-envelope.json','mixed-t-polygamma-far-tail.json','mixed-t-polynomial-tail-bounds.json'];d=[json.loads((r/n).read_text()) for n in names]
checks={'series_coefficients_enclosed':d[0]['status']=='coefficients_enclosed','core_and_8_20_tail_enclosed':d[1]['status']=='finite_tail_enclosed','far_envelope_passed':d[2]['status']=='passed','far_gaussian_tail_passed':d[3]['status']=='passed','orders_1_10_tail_passed':d[4]['status']=='passed'}
out={'schema':'marici.dual-t-interval-manifest.v1','status':'passed' if all(checks.values()) else 'failed','checks':checks,'inputs':names,'claim':'At xi=4.5025 the frozen dual witness excludes contact for every t in [.298,.300].','scope':'one-dimensional t interval only; does not certify the surrounding xi interval or bivariate rectangle'};(r/'dual-t-interval-manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
