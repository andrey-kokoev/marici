#!/usr/bin/env python3
"""Exact cancellation of a spurious <2456> pole in six-point NMHV BCFW."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
e=s.Symbol('epsilon'); ts=(1,2,4,7,11)
Z={i:s.Matrix([1,s.Integer(t),s.Integer(t)**2,s.Integer(t)**3]) for i,t in enumerate(ts,1)}
# Force <2456> to vanish linearly while retaining generic data on the divisor.
Z[6]=Z[2]+2*Z[4]+3*Z[5]+e*Z[3]
def br(q):return s.factor(s.det(s.Matrix.hstack(*(Z[i] for i in q))))
def five(q):
 a,b,c,d,f=q;num={a:br((b,c,d,f)),b:br((c,d,f,a)),c:br((d,f,a,b)),d:br((f,a,b,c)),f:br((a,b,c,d))}
 den=br((a,b,c,d))*br((b,c,d,f))*br((c,d,f,a))*br((d,f,a,b))*br((f,a,b,c));return num,s.factor(den)
terms=((2,3,4,5,6),(1,2,4,5,6),(1,2,3,4,6));data={q:five(q) for q in terms}
spurious=br((2,4,5,6));linear=s.factor(spurious/e);fail=[];individual_nonzero=0
for mono in itertools.product(range(1,7),repeat=4):
 coeff=[]
 for q in terms:
  num,den=data[q];coeff.append(s.prod(num.get(i,0) for i in mono)/den)
 residues=[s.factor((e*c).subs(e,0)) for c in coeff]
 if any(r!=0 for r in residues):individual_nonzero+=1
 total=s.factor(sum(residues))
 if total!=0:fail.append({'monomial':list(mono),'residue':str(total)})
# Ensure no denominator factor besides the chosen spurious bracket vanishes generically at epsilon=0.
other_regular=True
for q,(num,den) in data.items():
 reduced=s.cancel(den/spurious) if q in terms[:2] else den
 other_regular &= reduced.subs(e,0)!=0
checks={'spurious_bracket_linear_nonzero_slope':linear!=0,'only_first_two_terms_have_pole':spurious!=0 and s.rem(data[terms[0]][1],spurious,e)==0 and s.rem(data[terms[1]][1],spurious,e)==0 and data[terms[2]][1].subs(e,0)!=0,'other_denominator_factors_regular':bool(other_regular),'individual_residues_nontrivial':individual_nonzero>0,'all_1296_total_residues_zero':not fail}
report={'schema':'marici.nima.six-point-nmhv-spurious-pole-cancellation.v1','benchmark':{'result':'cancellation of spurious poles between BCFW cells in the six-point NMHV tree amplitude','context':'positive Grassmannian/amplituhedron triangulation'},'bcfw_terms':['[23456]','[12456]','[12346]'],'spurious_divisor':'<2456>=0','spurious_bracket':str(spurious),'grassmann_coefficients_checked':6**4,'coefficients_with_nonzero_individual_residue':individual_nonzero,'failures':fail,'checks':checks,'passed':all(checks.values()),'scope':'Exact one-parameter transverse test of the complete Grassmann residue on the <2456> spurious divisor.'}
out=ROOT/'research/nima/results/six-point-nmhv-spurious-pole-cancellation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'nontrivial_individual_residues':individual_nonzero,'failures':len(fail)},indent=2));raise SystemExit(0 if report['passed'] else 1)
