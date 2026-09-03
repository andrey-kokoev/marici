#!/usr/bin/env python3
"""Compare pivot-normalized rational residual bases across D=26,27,28."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/'results';files=[R/'cosmology_rees_rational_residual_nullspace.json',R/'cosmology_rees_rational_residual_nullspace_D27.json',R/'cosmology_rees_rational_residual_nullspace_D28.json'];data=[json.loads(p.read_text()) for p in files]
def sig(rep):return {(tuple(t['input'][:3])):t['coefficient'] for t in rep}
base=[sig(x) for x in data[0]['representatives']];matches=[]
for j in range(10):matches.append({'class':j,'D27_same_relative_coefficients':sig(data[1]['representatives'][j])==base[j],'D28_same_relative_coefficients':sig(data[2]['representatives'][j])==base[j],'support_sizes':[len(d['representatives'][j]) for d in data]})
out={'schema':'marici.benincasa.cosmology-rees-rational-degree-pattern.v1','degrees':[26,27,28],'matches':matches,'all_same':all(x['D27_same_relative_coefficients'] and x['D28_same_relative_coefficients'] for x in matches)};(R/'cosmology_rees_rational_degree_pattern.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
