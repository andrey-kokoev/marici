"""Universal fibre-Jacobian factorization and two-root trace reduction."""
import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
packet=json.loads((OUT/'nine-point-paired-cell-exact.json').read_text());assert packet['passed']
witness=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
labels=witness['retained_labels'];Z=s.Matrix([[j**k for k in range(6)] for j in labels]);C=s.Matrix([[s.Rational(v) for v in row] for row in witness['source_rows']])[:,[j-1 for j in labels]]
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');variables=(a,b,c,d);T=s.Matrix([[a,b],[c,d]])
matching=((0,1),(2,3),(4,5),(6,7));rows=[]
for i,j in matching:
 P=s.Poly(s.expand((C+T*K)[0,i]*(C+T*K)[1,j]-(C+T*K)[0,j]*(C+T*K)[1,i]),*variables)
 assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
 rows.append(P.coeff_monomial(1)+sum(P.coeff_monomial(z)*z for z in variables)+P.coeff_monomial(a*d)*q)
M,rhs=s.linear_eq_to_matrix(rows,variables);detM=s.factor(M.det());assert detM!=0
sol=list(M.inv()*rhs);P=s.Poly(s.factor(q-sol[0]*sol[3]+sol[1]*sol[2]),q)
assert P.degree()==2 and s.expand(P.as_expr()-s.sympify(packet['quadratic_graph_polynomial'],locals={'q':q}))==0
actual=[s.expand(expr.subs(q,a*d-b*c)) for expr in rows]
J=s.factor(s.Matrix(actual).jacobian(variables).det().subs(dict(zip(variables,sol))))
assert s.factor(J-detM*P.diff().as_expr())==0
# General algebra: let P=A*q^2+B*q+C with distinct roots r+,r-.
# If F(q)=H(q)/P'(q) and H mod P=h0+h1*q, then
# F(r+)+F(r-)=h1/A. In particular the sheet-odd h0 vanishes.
A,B,C0,h0,h1,plus,minus=s.symbols('A B C0 h0 h1 plus minus')
trace=(h0+h1*plus)/(A*(plus-minus))+(h0+h1*minus)/(A*(minus-plus))
assert s.cancel(trace-h1/A)==0
# Failure controls: reversing the derivative sign or summing only one root
# does not reproduce the exact fibre determinant / rational trace.
assert s.factor(J+detM*P.diff().as_expr())!=0
assert s.cancel((h0+h1*plus)/(A*(plus-minus))-h1/A)!=0
result={'schema':'marici.nima.nine-point-trace-derivative-reduction.v1','passed':True,
 'fixed_target_source_fibre_constraint_jacobian_factor':'det(M)*P_prime(q)',
 'fixed_target_linear_constraint_determinant':str(detM),
 'graph_polynomial':str(P.as_expr()),
 'universal_trace_reduction':'If F=H/P_prime and H mod P=h0+h1*q, then trace(F)=h1/leading_coefficient(P)',
 'independent_negative_controls_refused':2,
 'scope':'The determinant-lemma factorization is structural for every regular target with four affine lifted pair constraints. The exact check uses the fixed rational target; computing global H(B) and comparing COMPLETE sourced psi forms remains open.'}
(OUT/'nine-point-trace-derivative-reduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'jacobian_factorization':True,'trace_reduction':'h1/A','negative_controls':2},indent=2))
