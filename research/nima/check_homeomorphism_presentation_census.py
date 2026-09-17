#!/usr/bin/env python3
"""Aggregate census of the five tested presentation-equivalence candidates."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'research/nima/results'
files={'convolution_product':'homeomorphism-candidate-convolution-product.json','visible_tail':'homeomorphism-candidate-visible-tail.json','operator_graph':'homeomorphism-candidate-operator-graph.json','polarity':'homeomorphism-candidate-polarity.json','four_charts':'homeomorphism-candidate-four-charts.json'}
d={k:json.loads((R/f).read_text()) for k,f in files.items()}
records={
 'convolution_product':{'number':1,'target_dimensions':['4:q chart/successor'],'status':'proved_canonical','quotient':'product label becomes transported monoidal presentation','boundary':'not direct oriented-radial Fourier'},
 'visible_tail':{'number':2,'target_dimensions':['8:R regulator/completion','face 4x8:q x R'],'status':'proved_retained','quotient':'block decomposition becomes atlas data','boundary':'visible-only compression is lossy; no ninth axis'},
 'operator_graph':{'number':3,'target_dimensions':['5:L convolution successor','7:O observation','8:R completion'],'status':'proved_closed_conditional_source','quotient':'closed domain and graph are identical presentations','boundary':'arithmetic joint closability missing'},
 'polarity':{'number':4,'target_dimensions':['3:D polarity'],'status':'proved_signed','quotient':'two sheets become a Real C2 orbit','boundary':'orientation action retained; positive quotient conditional'},
 'four_charts':{'number':5,'target_dimensions':['4:q chart/successor'],'status':'proved_canonical_conditional_historical','quotient':'one base chart plus C4/stable monodromy','boundary':'native historical fourth-chart inverse missing'},
}
checks={'all_candidate_audits_pass':all(x['passed'] for x in d.values()),'five_candidates':len(records)==5,'graph_closability_correction_retained':d['operator_graph']['checks']['retaining_source_coordinate_alone_proves_closability'] is False,'lossy_visible_projection_rejected':d['visible_tail']['checks']['visible_only_projection_has_kernel'],'historical_chart_overclaim_rejected':d['four_charts']['checks']['historical_oriented_radial_conjugacy_rejected']}
out={'schema':'marici.nima.homeomorphism-presentation-census.v1','files':files,'records':records,'checks':checks,'passed':all(checks.values()),'conclusion':'A nontrivial homeomorphism-groupoid core exists, but quotienting must retain Real polarity, stable monodromy, leakage/tail data, and joint-closability boundaries.'}
p=R/'homeomorphism-presentation-census.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
