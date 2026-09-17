#!/usr/bin/env python3
"""Aggregate the exact and hostile checks for the first homeomorphism candidate."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
files={'canonical':'canonical-tate-torus-realization.json','intertwiner':'four-chart-fourier-product-intertwiner.json','hilbert':'positive-hilbert-tate-promotion.json','hostile':'tate-torus-vs-oriented-log-radial.json'}
data={k:json.loads((R/v).read_text()) for k,v in files.items()}
checks={'canonical_realization_passes':data['canonical']['passed'],'four_chart_product_intertwiner_passes':data['intertwiner']['passed'],'pontryagin_transport_unitary':data['hilbert']['checks']['pontryagin_transport_unitary'],'fourth_power_identity':data['hilbert']['checks']['fourth_power_identity_before_graded_lift'],'physical_radial_direct_conjugacy_rejected':data['hostile']['checks']['explicit_phase_mismatch'] and data['hostile']['checks']['jacobian_cannot_repair_phase']}
out={'schema':'marici.nima.homeomorphism-candidate-convolution-product.v1','candidate':'convolution and pointwise product are transported presentations of one monoidal object','classification':'exact in canonical channel-lattice/Pontryagin model; rejected as direct conjugacy to oriented radialized additive Fourier','homeomorphism':'Plancherel-Pontryagin Fourier','transported_law':'F(f*g)=F(f)F(g)','files':files,'checks':checks,'passed':all(checks.values()),'axis_effect':'convolution/product chart is presentation data; fourfold phase remains monodromy/grading data'}
p=R/'homeomorphism-candidate-convolution-product.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
