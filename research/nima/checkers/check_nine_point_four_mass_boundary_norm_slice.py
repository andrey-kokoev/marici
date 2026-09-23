"""Candidate dlog boundary images on a one-parameter rational rank-six target slice."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_four_mass_discriminant_slice as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
epsilon,q,P,branch=previous.epsilon,previous.q,previous.P,previous.branch
factors=(('w2',previous.w[0]),('w4',previous.w[1]),
 ('w5',previous.w[2]),('w6',previous.w[3]),('w7',previous.w[4]),('w8',previous.w[5]),
 ('u',previous.u),('t_minus_u',previous.t-previous.u))
rows=[]
for name,expr in factors:
 numer,denom=s.fraction(s.cancel(expr))
 resultant=s.factor(s.resultant(P.as_expr(),numer,q))
 norm_denom=s.factor(s.resultant(P.as_expr(),denom,q))
 assert resultant!=0 and norm_denom!=0
 polynomial=s.Poly(s.together(resultant).as_numer_denom()[0],epsilon)
 assert s.gcd(polynomial,branch).degree()==0
 rows.append({'source_polar_factor':name,'numerator_resultant_factored':str(resultant),
              'denominator_resultant_factored':str(norm_denom),
              'does_not_meet_simple_discriminant_branch':True,
              'resultant_degree':polynomial.degree()})
report={'schema':'marici.nima.nine-point-four-mass-boundary-norm-slice.v1','passed':True,
 'source_polar_norms':rows,
 'interpretation':'The resultant of the inverse quadratic P(q,epsilon) with the numerator of each source dlog pole factor detects TARGET epsilon values where at least one algebraic source sheet meets that polar divisor, excluding denominator/chart exceptionalities. All eight are disjoint from the regular discriminant fold roots, confirming these are different potential singular loci. Resultant zero is NECESSARY for a pushed-forward pole, not sufficient: numerator cancellations, simultaneous conjugate poles and chart degeneracies require further exact testing.',
 'boundary':'One exact rank-six target slice. Candidate dlog pole loci are not yet certified as actual poles of the two-sheet trace or the full positive-image canonical form.'}
(OUT/'nine-point-four-mass-boundary-norm-slice.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'norms':[{k:r[k] for k in ('source_polar_factor','resultant_degree','numerator_resultant_factored')} for r in rows]},indent=2))
