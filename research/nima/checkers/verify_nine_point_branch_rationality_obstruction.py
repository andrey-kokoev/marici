"""Replay the quadratic irreducibility/non-invariance deduction and reject mutations."""
import copy,json
from math import isqrt
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
def verify(paired,trace,claim):
 q=s.symbols('q');P=s.Poly(s.sympify(paired['quadratic_graph_polynomial'],locals={'q':q}),q)
 assert paired['passed'] and trace['passed'] and P.degree()==2
 disc=s.discriminant(P.as_expr(),q);assert disc==s.Rational(claim['fixed_target_quadratic_discriminant']) and disc!=0
 n,d=map(int,s.fraction(s.cancel(disc)))
 assert n>0 and d>0 and (isqrt(n)**2!=n or isqrt(d)**2!=d)
 assert not claim['discriminant_rational_square']
 assert len(claim['two_regular_rational_target_specializations_with_unequal_sheet_densities'])==len(trace['rows'])==2
 for sample,row in zip(claim['two_regular_rational_target_specializations_with_unequal_sheet_densities'],trace['rows']):
  assert sample['source_weights']==row['weights']
  sheets=row['sheets'];assert len(sheets)==2 and sum(bool(z['positive_sheet']) for z in sheets)==1
  assert s.Rational(sheets[0]['kernel_area'])!=s.Rational(sheets[1]['kernel_area'])
  delta=s.Rational(sheets[1]['continued_target_coefficient'])-s.Rational(sheets[0]['continued_target_coefficient'])
  assert delta!=0 and delta==s.Rational(sample['difference_nonzero'])
  total=sum((s.Rational(z['continued_target_coefficient']) for z in sheets),s.Rational(0))
  assert total==s.Rational(sample['two_sheet_trace'])==s.Rational(row['two_sheet_algebraic_trace_coefficient'])
 return True
def main():
 paired=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text())
 trace=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())
 claim=json.loads((OUT/'nine-point-single-sheet-rationality-obstruction.json').read_text());assert verify(paired,trace,claim)
 refused=[]
 for defect in ('square-discriminant','wrong-discriminant','fake-sheet-equality','wrong-trace'):
  bad=copy.deepcopy(claim)
  if defect=='square-discriminant':bad['discriminant_rational_square']=True
  if defect=='wrong-discriminant':bad['fixed_target_quadratic_discriminant']='1'
  if defect=='fake-sheet-equality':bad['two_regular_rational_target_specializations_with_unequal_sheet_densities'][0]['difference_nonzero']='0'
  if defect=='wrong-trace':bad['two_regular_rational_target_specializations_with_unequal_sheet_densities'][1]['two_sheet_trace']='0'
  try:verify(paired,trace,bad)
  except (AssertionError,ValueError):refused.append(defect)
  else:raise AssertionError('mutation accepted')
 result={'passed':True,'nonsquare_discriminant_specialization':True,'unequal_rational_sheet_specializations':2,
  'mutations_refused':refused,'scope':'Replays field-theoretic obstruction from independently frozen exact pair and trace packets. Does not identify any physical generalized-R form.'}
 (OUT/'nine-point-single-sheet-rationality-obstruction-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
