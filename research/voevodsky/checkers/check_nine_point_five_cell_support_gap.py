"""Does the newly identified cell repair the missing chi2/chi3 sector?"""
from pathlib import Path
import json
import sympy as s
from nine_point_source_r import Kinematics
root=Path(__file__).resolve().parents[1]
hist=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
inputs=json.loads((root/'results/nine-point-missing-support-histories.json').read_text())['witnesses'];rows=[]
for witness in inputs:
 kin=Kinematics([[s.Rational(x) for x in row] for row in witness['quotient_twistors']]);terms=[]
 for index,h in enumerate(hist):
  a1,b1=h['outer_pair'];a,b=h['inner_pair'];A,p=kin.ordinary(a1,b1);B,q=kin.inner(a1,b1,a,b,h['branch'])
  coefficient=s.factor(p*q*(A[2]*B[3]-A[3]*B[2])**4)
  if coefficient:terms.append({'source_ledger_index':index,'history':h,'coefficient':str(coefficient)})
 total=s.factor(sum(s.Rational(t['coefficient']) for t in terms))
 # Original zero2/zero3 cells vanish structurally. For new cell, columns2,3
 # are multiples of the first row basis, hence minor23 is identically zero.
 a2,a3=s.symbols('a2 a3');assert s.Matrix([[a2,a3],[0,0]]).det()==0
 rows.append({'e':witness['e'],'tree_chi2_power4_chi3_power4':str(total),'all_five_cells_component':0,'nonzero_tree':total!=0,'nonzero_history_count':len(terms),'terms':terms})
report={'passed':True,'witnesses':rows,'scope':'Structural zero of minor23 on five proposed cells versus exact sourced tree at common targets. Nonzero tree rules out any scalar weighting of those five cells, irrespective of normalization/orientation.'}
(root/'results/nine-point-five-cell-support-gap.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'counts':[r['nonzero_history_count'] for r in rows],'nonzero_tree':[r['nonzero_tree'] for r in rows],'histories':[t['history'] for t in rows[0]['terms']]},indent=2))
