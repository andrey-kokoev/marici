"""Search relabelled zero-column four-pair positive sheets beyond the eight-cell cube."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_zero_phys3_four_pair_outside_cube_fibre as old
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
vars=old.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z9=old.Z9;Y=old.inside.cube.E['E'].subs(dict(zip(old.inside.vars,map(s.Rational,(1,1,1,1,1,1,3,2)))))*Z9
a,b,c,d,q=old.a,old.b,old.c,old.d,old.q;T=old.T
assert old.old.D[:,:1].row_join(s.zeros(2,1)).row_join(old.old.D[:,1:])==old.inside.cube.E['E']
assert old.rows[0]['positive_four_pair_sheets']==0
rows=[]
for absent in (4,5,6,7,8,9,1):
 retained=[j-1 for j in range(1,10) if j!=absent];Z=Z9[retained,:]
 K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  P=s.Poly(old.minor(start+T*K,i,j),a,b,c,d)
  assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
  return P.coeff_monomial(1)+sum(P.coeff_monomial(v)*v for v in (a,b,c,d))+P.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 rank=M.rank()
 if rank==4:
  sol=M.inv()*rhs
  parameter=q;poly=s.Poly(s.factor(q-sol[0]*sol[3]+sol[1]*sol[2]),q)
 else:
  assert rank==3
  left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
  assert len(left)==1 and s.diff(left[0],q)!=0
  qforced=s.factor(-left[0].subs(q,0)/s.diff(left[0],q))
  sol,parameters=M.gauss_jordan_solve(rhs.subs(q,qforced));assert len(parameters)==1
  parameter=parameters[0]
  poly=s.Poly(s.factor(qforced-sol[0]*sol[3]+sol[1]*sol[2]),parameter)
 assert poly.degree()==2
 discriminant=s.factor(s.discriminant(poly.as_expr(),parameter))
 roots=s.solve(poly.as_expr(),parameter) if discriminant>=0 else []
 sheets=[]
 for root in roots:
  source=start+T.subs(dict(zip((a,b,c,d),(s.factor(v.subs(parameter,root)) for v in sol))))*K
  pivot=source[:,[0,2]].det()
  assert pivot!=0
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
          -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert all(s.factor(v)==0 for v in gauge-old.old.D.subs(point))
  signs=[str(s.sign(s.radsimp(point[v]))) for v in vars[:6]]
  signs += [str(s.sign(s.radsimp(point[u]))),str(s.sign(s.radsimp(point[t]-point[u])))]
  sheets.append({'source_signs_w2_w4_w5_w6_w7_w8_u_t_minus_u':signs,
                 'positive':all(z=='1' for z in signs)})
 rows.append({'zero_physical_label':absent,'linear_rank':rank,
              'real_discriminant_sign':str(s.sign(discriminant)),
              'sheets':sheets,'positive_sheet_count':sum(z['positive'] for z in sheets)})
assert all(r['positive_sheet_count']==0 for r in rows)
report={'schema':'marici.nima.nine-point-relabelled-four-pair-outside-cube-candidate.v1',
 'passed':True,'exact_positive_cube_E_target':'(1,1,1,1,1,1,3,2)',
 'relabelled_zero_column_candidates':rows,
 'all_nine_zero_column_embeddings_at_first_target':{
  'zero_phys2_cube_E_positive_sheets':1,
  'zero_phys3_prior_positive_sheets':old.rows[0]['positive_four_pair_sheets'],
  'other_seven_embedded_cells_positive_sheets':sum(r['positive_sheet_count'] for r in rows),
  'family_positive_sheet_count':1},
 'scope':'All nine order-preserving single-zero-column embeddings of the positive sourced eight-point four-pair matrix at ONE exact common E target; among them only zero-phys2 E is positive. Other n9 cells, n9 sourced-history status of relabelled embeddings and physical contour remain open.'}
(OUT/'nine-point-relabelled-four-pair-outside-cube-candidate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'candidates':[{'zero_label':v['zero_physical_label'],
 'rank':v['linear_rank'],'positive':v['positive_sheet_count']} for v in rows]},indent=2))
