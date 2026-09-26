"""Test all seven relabelled cube neighbors with zero physical3 as possible fourth sheets."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_relabelled_four_pair_outside_cube_candidate as previous
 import check_nine_point_eight_cell_positive_supported_multiplicity as support
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
old=previous.old;cube=old.inside.cube;Z=old.Z;K=old.K;Y=previous.Y
vars=old.vars;w2,w4,w5,w6,w7,w8,t,u=vars
a,b,c,d,q=old.a,old.b,old.c,old.d,old.q;T=old.T
old_columns=[0,2,3,4,5,6,7,8]
B=Y[:,:2].inv()*Y[:,2:]
z=Z[:,2:]-Z[:,:2]*B
zeros={**support.prior.trace.bir.zero_sets,'F_B':tuple(support.five.bir.pairs),
       'F':((1,2),(2,3),(1,3),(4,5),(6,7)),
       'F_C':support.new.pairs['F_C'],'F_D':support.new.pairs['F_D']}
rows=[]
for name in ('E_B','E_C','E_D','F','F_B','F_C','F_D'):
 C=(cube.E if name.startswith('E') else cube.F)[name][:,old_columns]
 pairs=zeros[name]
 assert all(old.minor(C,i,j)==0 for i,j in pairs)
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  P=s.Poly(old.minor(start+T*K,i,j),a,b,c,d)
  assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
  return P.coeff_monomial(1)+sum(P.coeff_monomial(v)*v for v in (a,b,c,d))+P.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 rank=M.rank()
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 active=[v for v in left if s.diff(v,q)!=0]
 if not active:
  assert all(v==0 for v in left)
  raise AssertionError('unexpected one-parameter q family')
 qforced=s.factor(-active[0].subs(q,0)/s.diff(active[0],q))
 assert all(s.factor(v.subs(q,qforced))==0 for v in left)
 sol,parameters=M.gauss_jordan_solve(rhs.subs(q,qforced))
 if rank==4:
  assert len(parameters)==0
  roots=[None] if s.factor(qforced-sol[0]*sol[3]+sol[1]*sol[2])==0 else []
 else:
  assert rank==3 and len(parameters)==1
  tau=parameters[0];P=s.Poly(s.factor(qforced-sol[0]*sol[3]+sol[1]*sol[2]),tau)
  assert 1<=P.degree()<=2
  roots=s.solve(P.as_expr(),tau) if P.degree()==1 or s.discriminant(P.as_expr(),tau)>=0 else []
 sheets=[]
 for root in roots:
  vals=[s.factor(v if root is None else v.subs(tau,root)) for v in sol]
  source=start+T.subs(dict(zip((a,b,c,d),vals)))*K
  pivot=source[:,[0,2]].det()
  assert pivot!=0
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(vars,(gauge[0,1] if name.startswith('E') else gauge[1,1],
           gauge[1,3],-gauge[0,4],-gauge[0,5],
           -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert all(s.factor(v)==0 for v in gauge-C.subs(point))
  signs=[str(s.sign(s.radsimp(point[v]))) for v in vars[:6]]
  signs += [str(s.sign(s.radsimp(point[u]))),str(s.sign(s.radsimp(point[t]-point[u])))]
  positive=all(v=='1' for v in signs)
  if positive:
   J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
   assert J!=0
  sheets.append({'source_signs_w2_w4_w5_w6_w7_w8_u_t_minus_u':signs,
                 'strictly_positive':positive,
                 'regular_target_jacobian_if_positive':bool(positive),
                 'jacobian_sign_if_positive':int(s.sign(J)) if positive else None,
                 'relative_oriented_degree_if_positive':int(cube.orient[name]*s.sign(J)) if positive else None})
 rows.append({'cell':name,'zero_physical_label':3,'linear_lift_rank':rank,
             'real_sheets':sheets,'positive_sheet_count':sum(z['strictly_positive'] for z in sheets)})
assert {r['cell']:r['positive_sheet_count'] for r in rows if r['positive_sheet_count']}=={'E_B':1,'F_B':1}
positive_degrees={r['cell']:s['relative_oriented_degree_if_positive'] for r in rows
                  for s in r['real_sheets'] if s['strictly_positive']}
assert sum(positive_degrees.values())==0
assert all(C[:,1].shape==(2,1) for C in (cube.E['E_B'][:,old_columns],cube.F['F_B'][:,old_columns]))
report={'schema':'marici.nima.nine-point-zero-phys3-relabelled-cube-neighbors.v1',
 'passed':True,'positive_E_cube_target':'(1,1,1,1,1,1,3,2)',
 'two_additional_regular_positive_geometric_sheets':['zero_phys3_E_B','zero_phys3_F_B'],
 'new_pair_relative_calibrated_oriented_degrees':positive_degrees,
 'new_pair_relative_signed_local_mapping_degree':sum(positive_degrees.values()),
 'complete_two_zero_column_embedding_families_positive_count':5,
 'fermionic_chi3_support_of_new_sheets':'zero: both relabelled cells have zero physical column 3, so cannot change the chi3^4 chi5^4 coefficient.',
 'seven_outside_cube_zero_phys3_neighbors':rows,
 'scope':'Seven geometric zero-phys3 order-preserving relabelled 8-point source cells at one positive cube target. Two NEW regular positive sheets exist in addition to three zero-phys2 cube sheets. They are not established nine-point sourced histories, authorized contour terms or complete outside-cell inventory.'}
(OUT/'nine-point-zero-phys3-relabelled-cube-neighbors.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'cells':[{'cell':r['cell'],'real':len(r['real_sheets']),
 'positive':r['positive_sheet_count']} for r in rows]},indent=2))
