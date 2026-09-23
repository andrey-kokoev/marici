"""Distinguish positive-source-supported push from algebraic continuation at a V target."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_opposite_side_positive_target_zero_column_fibre as old
 import check_nine_point_vertical_cell_fibre_degree as vertical
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=old.D,old.vars
w2,w4,w5,w6,w7,w8,t,u=vars
Z=old.Z;e=s.Rational(1,20)
p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
V=D.subs(p).copy();V[0,1]=0;V[1,1]=e
Y=V*Z;H=Y[:,:2];B=H.inv()*Y[:,2:]
z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
K=old.K;T=old.T;a,b,c,d,q=old.a,old.b,old.c,old.d,old.q
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def lifted(i,j):
 poly=s.Poly(minor(V+T*K,i,j),a,b,c,d)
 assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
 return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
assert M.det()!=0
sol=M.inv()*rhs;P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q)
roots=s.solve(P.as_expr(),q);assert len(roots)==2
sheets=[]
for root in roots:
 source=V+T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in sol))))*K
 gauge=source[:,[0,2]].inv()*source
 point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert s.simplify(D.subs(point)*z)==s.zeros(2,4)
 Jz=s.Matrix.hstack(*[s.Matrix(list(D.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert Jz!=0
 rho=-s.S.One/(s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u]))
 continued=s.cancel(rho*(D.subs(point)*h).det()**4/Jz)
 sheets.append({'root':str(s.N(root,12)),
  'nonpositive':str(s.sign(s.radsimp(point[w4])))=='-1',
  'continued_value':str(s.N(continued,16)),
  'continued_sign':str(s.sign(s.radsimp(continued))),
  '_exact':continued})
assert all(sheet['nonpositive'] for sheet in sheets)
total=s.simplify(sum(sheet['_exact'] for sheet in sheets))
assert total!=0
for sheet in sheets:del sheet['_exact']
V_coefficient=s.Rational(next(row['nonzero_single_sheet_arbitrary_Y_target_coefficient']
 for row in vertical.rows if row['positive_V_w2']=='1/20'))
assert s.sign(total)==1 and s.sign(V_coefficient)==-1
report={'schema':'marici.nima.nine-point-supported-vs-meromorphic-trace-vertical-target.v1','passed':True,
 'positive_vertical_source_w2':'1/20','A_positive_source_preimages':0,
 'A_two_nonpositive_algebraic_sheets':sheets,
 'A_two_sheet_meromorphic_continuation_at_positive_V_target':str(total),
 'V_one_sheet_target_coefficient':str(V_coefficient),
 'continued_A_and_single_sheet_V_scalar_coefficient_opposite_signs':True,
 'distinction':'The supported push from positive A source is zero at this V target, yet its algebraic two-sheet rational continuation is nonzero. Therefore exclusion from a source-cell positive image proves lack of positive cell coverage, NOT inequality of an analytically continued rational form with a conjectural global canonical form.',
 'scope':'Exact one positive target, scalar eight-form coefficient only; no independent full n9 canonical form comparison.'}
(OUT/'nine-point-supported-vs-meromorphic-trace-vertical-target.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'A_supported_sheet_count':0,
 'A_meromorphic_continuation_nonzero':bool(total!=0),
 'two_sheet_trace':str(total)},indent=2))
