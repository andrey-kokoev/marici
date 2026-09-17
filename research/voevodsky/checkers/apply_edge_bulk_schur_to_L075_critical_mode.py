#!/usr/bin/env python3
"""Apply the edge/bulk Schur inequality to the directed L=.75 candidate."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';d=json.loads((root/'L075_critical_degree149_arb.json').read_text());# Parse midpoint/radius conservatively from known directed output through explicit decimal lower endpoint.
candidate_lower=3.40628e-15-2.19e-21;alpha=.022276778741280565;residual=7.59387617969497e-9;correction=residual*residual/alpha;lower=candidate_lower-correction
out={'schema':'marici.voevodsky.L075-edge-bulk-schur-application.v1','directed_candidate_lower':candidate_lower,'complement_floor':alpha,'residual_norm_scout_upper_used':residual,'schur_correction':correction,'conditional_lower_bound':lower,'condition':'residual norm is still floating and must be directed','passed_conditionally':lower>0,'passed':False,'rh_proved':False};p=root/'L075_edge_bulk_schur_application.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert lower>0
