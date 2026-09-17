#!/usr/bin/env python3
"""Exact six-term NMHV momentum-twistor R-invariant identity."""
import itertools,json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
# A positive rational momentum-twistor configuration on the moment curve.
ts=[s.Integer(q) for q in (1,2,4,7,11,16)]
Z={i:s.Matrix([1,t,t**2,t**3]) for i,t in enumerate(ts,1)}
def bracket(indices): return s.det(s.Matrix.hstack(*(Z[i] for i in indices)))
def five_data(labels):
 a,b,c,d,e=labels
 numer={a:bracket((b,c,d,e)),b:bracket((c,d,e,a)),c:bracket((d,e,a,b)),d:bracket((e,a,b,c)),e:bracket((a,b,c,d))}
 denom=bracket((a,b,c,d))*bracket((b,c,d,e))*bracket((c,d,e,a))*bracket((d,e,a,b))*bracket((e,a,b,c))
 return numer,s.factor(denom)
# Boundary of the ordered 5-simplex: alternating omission signs.
terms=[]
for omitted in range(1,7):
 labels=tuple(i for i in range(1,7) if i!=omitted);num,den=five_data(labels)
 terms.append(((-1)**(omitted-1),labels,num,den))
failures=[];checked=0
# Delta^{0|4} is a product of four linear forms. Check every Grassmann
# coefficient chi_i^1 chi_j^2 chi_k^3 chi_l^4 exactly over Q.
for monomial in itertools.product(range(1,7),repeat=4):
 value=s.factor(sum(sign*s.prod(num.get(i,0) for i in monomial)/den for sign,_,num,den in terms));checked+=1
 if value!=0:failures.append({'monomial':list(monomial),'value':str(value)})
ordered_minors={''.join(map(str,q)):str(bracket(q)) for q in itertools.combinations(range(1,7),4)}
checks={'all_15_ordered_four_brackets_positive':all(int(v)>0 for v in ordered_minors.values()),'six_r_invariants':len(terms)==6,'all_1296_grassmann_coefficients_checked':checked==1296,'six_term_identity':not failures}
report={'schema':'marici.nima.six-point-momentum-twistor-r-invariant-identity.v1','benchmark':{'result':'six-term identity for NMHV momentum-twistor five-brackets','context':'planar N=4 SYM Grassmannian/amplituhedron literature','representative_reference':'Arkani-Hamed et al., The All-Loop Integrand For Scattering Amplitudes in Planar N=4 SYM','arxiv':'1008.2958'},'twistors':{str(i):[str(q) for q in Z[i]] for i in Z},'ordered_four_brackets':ordered_minors,'alternating_terms':[{'sign':q[0],'labels':list(q[1]),'denominator':str(q[3])} for q in terms],'grassmann_coefficients_checked':checked,'failures':failures,'checks':checks,'passed':all(checks.values()),'scope':'Exact evaluation on one positive rational six-twistor configuration; this tests the full Grassmann identity there, not symbolic equality for arbitrary twistors.'}
out=ROOT/'research/nima/results/six-point-momentum-twistor-r-invariant-identity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':report['passed'],'checks':checks,'failure_count':len(failures)},indent=2));raise SystemExit(0 if report['passed'] else 1)
