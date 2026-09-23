"""Exact specialization tests for non-rational single-sheet versus rational trace."""
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
paired=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text());assert paired['passed']
trace=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text());assert trace['passed']
samples=json.loads((OUT/'nine-point-paired-pushforward-samples.json').read_text());assert samples['passed']
q=s.symbols('q');P=s.Poly(s.sympify(paired['quadratic_graph_polynomial'],locals={'q':q}),q);assert P.degree()==2
D=s.discriminant(P.as_expr(),q);assert D>0
numer,denom=map(int,s.fraction(s.cancel(D)))
assert numer>0 and denom>0
numroot,denroot=isqrt(numer),isqrt(denom)
assert numroot*numroot!=numer or denroot*denroot!=denom
# For every target in a regular open set, the same fixed two-dimensional
# row kernel and four paired-minor conditions define P_Y(q) over Q(Y).
# All entries come from linear source observation and rational elimination;
# its denominators are nonzero at this specialization (paired packet).
# A nonzero nonsquare rational discriminant at that regular rational target
# rules out P_Y splitting over the rational-function field Q(Y).
rows=[]
for sample,row in zip(samples['rows'],trace['rows']):
 branches=row['sheets'];assert len(branches)==2
 positive=next(b for b in branches if b['positive_sheet'])
 rival=next(b for b in branches if not b['positive_sheet'])
 assert s.Rational(positive['continued_target_coefficient'])==s.Rational(sample['pushed_local_target_coefficient'])
 assert s.Rational(rival['kernel_area'])!=s.Rational(positive['kernel_area'])
 difference=s.Rational(positive['continued_target_coefficient'])-s.Rational(rival['continued_target_coefficient'])
 assert difference!=0
 total=sum((s.Rational(b['continued_target_coefficient']) for b in branches),s.Rational(0))
 assert total==s.Rational(row['two_sheet_algebraic_trace_coefficient'])
 assert not rival['positive_sheet']
 rows.append({'source_weights':sample['weights'],'unequal_sheet_coefficients':True,
              'difference_nonzero':str(difference),'two_sheet_trace':str(total)})
result={'schema':'marici.nima.nine-point-single-sheet-rationality-obstruction.v1','passed':True,
 'fixed_target_quadratic_discriminant':str(D),'discriminant_rational_square':False,
 'nonsquare_discriminant_witness':'positive numerator or denominator fails exact integer-square test',
 'two_regular_rational_target_specializations_with_unequal_sheet_densities':rows,
 'deduction':'Generic paired-cell two-sheet cover is irreducible over Q(target); its oriented single-sheet local density is not Galois invariant, hence is not a rational differential form in target coordinates. The two-sheet algebraic trace is rational by quadratic-field trace. Neither statement identifies a sourced physical history.',
 'scope':'Algebraic obstruction to equating ONE generic local branch to a rational generalized-R history. It does not rule out the rational two-sheet trace or a sum over other cells.'}
(OUT/'nine-point-single-sheet-rationality-obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'min8_discriminant_square':False,'unequal_regular_sheet_samples':len(rows),
 'single_sheet_rational_target_form':False,'two_sheet_trace_rational':True},indent=2))
