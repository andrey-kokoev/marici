#!/usr/bin/env python3
"""Aggregate the durable certificates for the Catalan–Tate quarter theorem."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
files=[
 'catalan-realization-trace-ratio.json',
 'catalan-quarter-rotation-characters.json',
 'channel-monomial-c4-realization.json',
 'canonical-tate-torus-realization.json',
 'esd7-source-manifest.json',
 'full-esd7-tate-torus-functor.json',
 'heat-regularized-four-chart-trace.json',
 'quarter-trace-regulator-independence.json',
 'tate-torus-vs-oriented-log-radial.json',
 'simplex-face-cone-graph-package.json',
 'positive-hilbert-tate-promotion.json',
]
records={};checks={}
for name in files:
 p=ROOT/'research/nima/results'/name;d=json.loads(p.read_text());records[name]={'schema':d['schema'],'passed':d['passed'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()};checks[name]=bool(d['passed'])
# Inspect theorem-critical values rather than relying only on component pass flags.
r=ROOT/'research/nima/results'
a=json.loads((r/files[0]).read_text());b=json.loads((r/files[1]).read_text());c=json.loads((r/files[3]).read_text());m=json.loads((r/files[4]).read_text());f=json.loads((r/files[5]).read_text());h=json.loads((r/files[6]).read_text());g=json.loads((r/files[7]).read_text())
checks.update({
 'forced_channel_formula':a['exact_formula']=='C_(n-3)/C_(n-2)=(n-1)/(2(2n-5))=1/4+3/(4(2n-5)).',
 'rotation_characters_computed':b['results'][-1]['n']==12 and len(b['results'][-1]['character_multiplicities'])==4,
 'canonical_torus_exact_chart_weight':all(x['exact_chart_weight']=='1/4' for x in c['results']),
 'esd7_f_vector':[sum(x['dimension']==d for x in m['cells']) for d in range(4)]==[120,560,784,343],
 'full_functor_signed_actions':f['checks']['rho_is_signed_chain_map'] and f['checks']['omega_is_signed_chain_map'],
 'heat_quarter':h['checks']['all_normalized_chart_traces_one_quarter'],
 'regulator_independence':g['checks']['all_shared_regulators_give_exact_quarter'] and g['checks']['all_radial_regulators_preserve_catalan_ratio'],
})
out={'schema':'marici.nima.catalan-tate-quarter-theorem.v1','theorem':'The canonical channel Tate-torus realization carries an exact regulator-independent four-chart trace 1/4; forced-channel and polygon-C4 Catalan traces converge to 1/4 with explicit finite corrections; the graded bounded cone-valued indexing model extends over the all-cell esd_7(Delta^3) profile, with contractible simplex-face cones.','component_certificates':records,'checks':checks,'passed':all(checks.values()),'scope':['finite Catalan representation','canonical channel lattice and Pontryagin dual','signed/relative full esd7 profile','positive trace-class chart regulators transported by conjugacy'],'comparison_results':['direct oriented-log Fourier identification rejected by kernel mismatch','simplex cones are admitted closed packages but historical nonzero-defect identification rejected by homology'],'open_comparisons':['cellwise historical edge-operator assignment over the esd7 registry','arithmetic positivity of the historical signed Weil/Tate form and strong convergence of raw eight-leg features']}
p=r/'catalan-tate-quarter-theorem.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'component_count':len(records),'checks':checks,'passed':out['passed'],'open_comparisons':out['open_comparisons']},indent=2));raise SystemExit(0 if out['passed'] else 1)
