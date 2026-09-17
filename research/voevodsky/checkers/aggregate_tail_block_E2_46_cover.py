#!/usr/bin/env python3
"""Aggregate 46-node tail-block contour cover."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for a,b in ((0,12),(12,24),(24,35),(35,46)):rows+=json.loads((root/f'tail_block_E2_46_chunk_{a}_{b}.json').read_text())['rows']
b=json.loads((root/'tail_block_E2_contour_cover_budget.json').read_text());mn=min(x['minimum_singular'] for x in rows);directed=min(x['directed_style_lower'] for x in rows);var=b['half_arc_variation_bound'];out={'schema':'marici.voevodsky.tail-block-E2-46-cover.v1','nodes':46,'minimum_sampled_singular':mn,'maximum_sampled_norm':max(x['norm'] for x in rows),'minimum_directed_style_node_lower':directed,'maximum_reconstruction_error':max(x['reconstruction_error'] for x in rows),'maximum_orthogonality_defect':max(max(x['orthogonality_defects']) for x in rows),'arc_variation_bound':var,'covered_polynomial_singular_floor':directed-var,'passed_polynomial_scout':directed>var,'passed':False,'remaining':'directed node singular bounds, directed derivative coefficients, and true-source remainder','rh_proved':False};p=root/'tail_block_E2_46_cover.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_polynomial_scout']
