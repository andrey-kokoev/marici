#!/usr/bin/env python3
"""Mechanical completeness check of the acquired all-n N2MHV source packet."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
f=json.loads((ROOT/'research/nima/fixtures/all-n-n2mhv-tree-source.v1.json').read_text());text=(ROOT/f['paper']['source']).read_text()
need={
 'generalized_R_definition':r'\label{generalR}',
 'summation_superscripts':r'\label{superscripts}',
 'lower_boundary_rule':r'\label{Lrep}',
 'upper_boundary_rule':r'\label{Urep}',
 'amplitude_factorization':r'\label{ANNMHV}',
 'complete_nested_sum':r'\label{PNNMHVnew}',
 'six_point_base_case':'formula (\\ref{PNNMHVnew}) is correct for the six-point amplitudes',
 'pair_separation':'a<b-1'
}
checks={k:v in text for k,v in need.items()};checks.update({'fixture_grassmann_degree_eight':f['total_ratio_function_grassmann_degree']==8,'two_generalized_R_factors_per_term':f['formula'].count('R_')==3})
out={'schema':'marici.nima.all-n-n2mhv-tree-source-packet.v1','source_fixture':'research/nima/fixtures/all-n-n2mhv-tree-source.v1.json','source_landmarks':checks,'passed':all(checks.values()),'implementation_warning':'Do not infer minimal-n term counts by naive strict-pair enumeration: the source separately asserts the six-point base case and prescribes nontrivial endpoint replacements. Implement boundary limits before counting surviving terms.','scope':'Source-packet completeness and structural Grassmann degree; no generalized-R algebra yet.'}
p=ROOT/'research/nima/results/all-n-n2mhv-tree-source-packet.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
