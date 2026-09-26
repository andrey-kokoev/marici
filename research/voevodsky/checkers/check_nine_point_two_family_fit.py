"""Necessary three-component test after explicit delta-pushforward normalization."""
from pathlib import Path
import json
import sympy as s
root=Path(__file__).resolve().parents[1];data=json.loads((root/'results/nine-point-common-frame.json').read_text());rows=[]
for witness in data['witnesses']:
 columns=[]
 for family in ('zero2','zero3'):
  columns.append(s.Matrix([sum(s.Rational(witness['cells'][family+'_'+suffix]['delta_pushforward_components'][i]) for suffix in ('E_B','F_B')) for i in range(3)]))
 M=s.Matrix.hstack(*columns);target=s.Matrix(list(map(s.Rational,witness['tree_P9_components'])))
 assert M[:2,:].det()!=0
 weights=M[:2,:].inv()*target[:2,:];residual=s.factor(target[2]-(M*weights)[2])
 rows.append({'e':witness['e'],'weights_fitted_to_first_two_components':list(map(str,weights)),'third_component_residual':str(residual),'three_component_match':residual==0})
report={'passed':True,'witnesses':rows,'scope':'Necessary fit diagnostic under unframed delta-function normalization and inherited cell orientations. Nonzero residual excludes these two family sums as this full tree at that target; does not identify missing cells or certify inherited orientation.'}
(root/'results/nine-point-two-family-fit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'three_component_matches':[r['three_component_match'] for r in rows]}))
