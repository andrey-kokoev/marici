#!/usr/bin/env python3
"""Aggregate audit of four charts as one periodic presentation object."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
files={'canonical':'canonical-tate-torus-realization.json','products':'four-chart-fourier-product-intertwiner.json','positive':'positive-hilbert-tate-promotion.json','historical_hostile':'tate-torus-vs-oriented-log-radial.json'}
d={k:json.loads((R/f).read_text()) for k,f in files.items()}
checks={'canonical_fourier_order_four':d['canonical']['checks']['pontryagin_fourier_has_order_four'],'all_four_charts_equidimensional':d['canonical']['checks']['four_charts_exactly_equidimensional'],'products_transport_around_cycle':d['products']['checks']['all_typed_intertwining_squares_commute'],'unitary_chart_transport':d['positive']['checks']['pontryagin_transport_unitary'],'positive_fourth_power':d['positive']['checks']['fourth_power_identity_before_graded_lift'],'historical_oriented_radial_conjugacy_rejected':d['historical_hostile']['checks']['explicit_phase_mismatch']}
out={'schema':'marici.nima.homeomorphism-candidate-four-charts.v1','candidate':'four canonical charts are one periodic object with C4 presentation monodromy','classification':'proved canonical; stable lift has q^4=Sigma; historical native semilocal identification conditional','files':files,'checks':checks,'passed':all(checks.values()),'axis_effect':'replace four chart objects by one base object plus C4/stable monodromy; do not quotient historical native charts yet'}
p=R/'homeomorphism-candidate-four-charts.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
