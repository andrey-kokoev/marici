"""Prove generic sourced-Y0 two-sheet trace is an eighth-degree polynomial in h."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_rank_six_Y0_regular_witness as witness
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'four-mass-rank-six-Y0-regular-witness.json').read_text());assert prior['passed']
Z,D,variables=witness.Z,witness.D,witness.variables
rows=[]
for row,record in zip(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'],prior['witnesses']):
 init=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);Y=C*Z
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)]);G[:,0]=G[:,0]/G.det()
 E=Z*G;z,h=E[:,0:4],E[:,4:6]
 assert z.rank()==4
 indices=next(i for i in itertools.combinations(range(8),4) if z[list(i),:].det()!=0)
 rest=[i for i in range(8) if i not in indices]
 basis=z[list(indices),:].inv()
 Q0=h[rest,:]-z[rest,:]*basis*h[list(indices),:]
 qvars=s.symbols('Q0:8');Qsym=s.Matrix(4,2,qvars)
 hformal=s.zeros(8,2)
 for j,index in enumerate(rest):hformal[index,:]=Qsym[j,:]
 coefficients=[]
 for root,point in witness.fibre(C):
  Ci=D.subs(point);assert Ci*z==s.zeros(2,4)
  cols=[]
  for v in variables:
   differential=(D.diff(v).subs(point)*z)
   cols.append(s.Matrix([differential[i,j] for i in range(2) for j in range(4)]))
  Jz=s.Matrix.hstack(*cols).det(method='domain-ge');assert Jz!=0
  source=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  H=Ci*h;assert H.det()!=0
  # Projective Y0 chart: U=(C h)^-1 (C z). At Cz=0, the derivative of
  # the inverse drops out, giving JU=det(Ch)^-4 Jz exactly.
  pivot=H.inv();jucols=[]
  for v in variables:
   differential=pivot*(D.diff(v).subs(point)*z)
   jucols.append(s.Matrix([differential[i,j] for i in range(2) for j in range(4)]))
  Ju=s.Matrix.hstack(*jucols).det(method='domain-ge')
  assert Ju==Jz/H.det()**4
  assert Ci*hformal==Ci[:,rest]*Qsym
  coefficients.append((source/Jz,Ci))
 symbolic=sum(weight*(Ci*hformal).det()**4 for weight,Ci in coefficients)
 poly=s.Poly(symbolic,*qvars)
 assert poly.total_degree()==8 and all(sum(m)==8 for m in poly.monoms())
 assert poly.eval(dict(zip(qvars,list(Q0))))==s.Rational(record['Y0_chart_two_sheet_coefficient'])
 # A second h (not a shift by zM) changes the quotient but cannot
 # change the roots or the h-independent source-to-Cz Jacobian.
 h2=h.copy();h2[rest[0],0]+=s.Rational(1,13)
 Q2=h2[rest,:]-z[rest,:]*basis*h2[list(indices),:]
 assert Q2!=Q0 and all((Ci*h2).det()!=0 for _,Ci in coefficients)
 predicted=poly.eval(dict(zip(qvars,list(Q2))))
 observed=sum(weight*(Ci*h2).det()**4 for weight,Ci in coefficients)
 assert predicted==observed
 rows.append({'source_weights':row['weights'],'two_fibre_roots_independent_of_bottom_two_external_columns':True,
  'each_source_to_target_jacobian_factors_as_det_Ch_inverse_fourth_power':True,
  'quotient_polynomial_total_degree':poly.total_degree(),
  'quotient_polynomial_monomial_count':len(poly.monoms()),
  'base_trace_matches_prior':True,'independent_bottom_deformation_matches':True})
report={'schema':'marici.nima.four-mass-Y0-polynomial-trace.v1','passed':True,'witnesses':rows,
 'generic_formula':'At Y0 with Z=[z|h], solve C(v)z=0 (two simple solutions v_i) independent of h. Then omega_U(Y0;z,h)=sum_i source_density(v_i)*det(C(v_i)h)^4/det[d(C(v)z)/dv]_(v_i). On the open set of simple roots and nonzero z-dependent Jacobians this is a homogeneous polynomial of degree eight in the eight quotient coordinates of h modulo z; no h-denominator survives.',
 'bosonization':'The polynomial can be specialized as h=phi eta in an even Grassmann algebra BEFORE integration. The primary-source superamplitude theorem supplies the on-shell Grassmann-integral identification; this checker does not independently evaluate its eight-fermion integral, compare the complete component, or establish generic validity at degenerate z.',
 'scope':'Local-at-Y0 generic-z polynomiality and two exact rank-six fibre witnesses; NOT an expanded global omega(Y;Z), nor an independently checked Berezin normalization/pole residue or nine-point generalized-R history.'}
(OUT/'four-mass-Y0-polynomial-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(rows),'Y0_nilpotent_polynomiality_on_simple_fibre_open_set':True,
 'global_Y_dependent_form_computed':False},indent=2))
