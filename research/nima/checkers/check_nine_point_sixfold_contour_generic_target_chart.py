"""Exact generic (not Y0) rank-six two-sheet contour and Gr(2,6) chart covariance."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_sixfold_fibre_contour_two_sheet_trace as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
emb=previous.embedded
D,D9,vars,Z8,Z9=emb.D,emb.D9,emb.variables,emb.Z8six,emb.Z9six
rank_six=emb.rank_six
K=rank_six.K;assert K.shape==(2,8) and K*Z8==s.zeros(2,6)
source_rows=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']
prior=json.loads((OUT/'four-mass-rank-six-Y0-regular-witness.json').read_text())['witnesses']

def jacobian(point,external):
 C=D.subs(point);Y=C*external
 H=Y[:,4:6];assert H.det()!=0
 B=H.inv()*Y[:,:4]
 columns=[]
 for v in vars:
  delta=D.diff(v).subs(point)*external
  dB=H.inv()*(delta[:,:4]-delta[:,4:6]*B)
  columns.append(s.Matrix(list(dB)))
 return s.Matrix.hstack(*columns).det(method='domain-ge'),H.det(),B

results=[]
for index,row in enumerate(source_rows):
 initial=dict(zip(vars,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);Y=C*Z8
 assert Y[:,:4]!=s.zeros(2,4)
 # Four pair-minor equations linear in T and q=det T; eliminating T
 # gives a quadratic for the GENERIC rank-six target, not only Y0.
 a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
 def lifted(i,j):
  P=s.Poly(s.det(s.Matrix.hstack((C+T*K)[:,i],(C+T*K)[:,j])),a,b,c,d)
  assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
  return (P.coeff_monomial(1)+sum(P.coeff_monomial(v)*v for v in (a,b,c,d))
          +P.coeff_monomial(a*d)*q)
 equations=[lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))]
 M,rhs=s.linear_eq_to_matrix(equations,(a,b,c,d));assert M.det()!=0
 solution=M.inv()*rhs
 quad=s.Poly(q-solution[0]*solution[3]+solution[1]*solution[2],q)
 assert quad.degree()==2 and quad.eval(0)==0
 roots=s.solve(quad.as_expr(),q);assert len(roots)==2 and roots[0]!=roots[1]
 fibre=list(rank_six.fibre(C));assert len(fibre)==2
 assert {r for r,p in fibre}==set(roots)
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det();assert G.det()==1
 positive_Z9=Z9*G
 # Original n9 moment curve is strictly positive; the same SL6
 # transformation preserves ALL ordered external six-brackets.
 assert D9.subs(initial)*Z9==Y
 assert (D9.subs(initial)*positive_Z9)[:,:4]==s.zeros(2,4)
 H_initial=Y[:,4:6];assert H_initial.det()!=0
 records=[]
 for root,point in fibre:
  source=-s.S.One/(s.prod(point[v] for v in vars[:6])*point[vars[7]]*(point[vars[6]]-point[vars[7]]))
  Jraw,Hraw,Braw=jacobian(point,Z8)
  Jzero,Hzero,Bzero=jacobian(point,Z8*G)
  assert Jraw!=0 and Jzero!=0
  assert Braw==jacobian(initial,Z8)[2] and Bzero==s.zeros(2,4)
  ratio=s.factor(Hzero/Hraw)
  assert s.factor(Jzero/Jraw-ratio**(-6))==0
  coeffraw=s.factor(source/Jraw);coeffzero=s.factor(source/Jzero)
  assert s.factor(coeffzero/coeffraw-ratio**6)==0
  records.append({'positive_sheet':root==0,'algebraic_fibre_root':str(root),
    'nonzero_generic_chart_jacobian':True,'nonzero_Y0_chart_jacobian':True,
    'SL6_chart_jacobian_weight_six_verified':True,
    'generic_target_local_residue':str(coeffraw),
    'generic_exact':coeffraw,'Y0_exact':coeffzero})
 rawtrace=s.factor(sum(z['generic_exact'] for z in records))
 zerotrace=s.factor(sum(z['Y0_exact'] for z in records))
 assert rawtrace!=0 and zerotrace==s.Rational(prior[index]['Y0_chart_two_sheet_coefficient'])
 assert zerotrace==s.factor(rawtrace/H_initial.det()**6)
 assert rawtrace!=next(z['generic_exact'] for z in records if z['positive_sheet'])
 results.append({'source_weights':row['weights'],'four_pair_inverse_degree':2,
   'generic_rank_six_target_not_Y0':True,'rank_six_SL6_chart_weight':6,
   'two_sheet_generic_target_coefficient':str(rawtrace),
   'Y0_to_generic_trace_chart_relation_exact':True,
   'two_sheet_trace_differs_from_positive_only':True,
   'sheets':[{k:z[k] for k in ('positive_sheet','algebraic_fibre_root','generic_target_local_residue')} for z in records]})
report={'schema':'marici.nima.nine-point-sixfold-contour-generic-target-chart.v1','passed':True,
 'witnesses':results,
 'structural_formula':'For fixed rank-six external Z8, every inverse source Cprime of the same generic Gr(2,6) target is gauge-equivalent to Cbar+T*K, K Z8=0, T 2x2. Four parallel-pair minors are linear in T and q=det(T), so elimination gives a quadratic in q; an open regular source target has precisely two algebraic sheets. The local complex sixfold cyclic contour sums their oriented source-density/Jacobian residues. Under SL6 chart change the Gr(2,6) 8-volume Jacobian scales as (det Hnew/det Hold)^(-6), checked exactly on both sheets and trace.',
 'boundary':'Two generic non-Y0 rank-six target witnesses and an algebraic generic-degree upper bound where the inverse 4x4 linear system and quadratic leading coefficient are nonzero. No equality to the full positive-image canonical contour, global image coverage or full scattering amplitude.'}
(OUT/'nine-point-sixfold-contour-generic-target-chart.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'generic_non_Y0_targets':len(results),'inverse_degree':2,'chart_exponent':6},indent=2))
