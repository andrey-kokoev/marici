"""F_B unique full field trace contains the exact branch cancelling E_B lower interior pole."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_vertical_label3_B_cell_birational_form as bir
 import check_nine_point_vertical_label3_B_neighbor_cancels_lower_EB_pole as neighbor
 import check_nine_point_label3_square_internal_wall_uncancelled_poles as prior
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
chamber=prior.chamber;trace=prior.trace
vars=trace.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z,K,cell=bir.Z,bir.K,bir.cell
T=bir.T;a,b,c,d,q=bir.a,bir.b,bir.c,bir.d,bir.q
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def inverse_at(value):
 p=dict(zip(vars,(value,1,1,1,1,1,3,2)))
 Y=trace.D.subs(p)*Z
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in bir.pairs],(a,b,c,d))
 assert M.rank()==4
 left=s.factor((M.T.nullspace()[0].T*rhs)[0]);assert s.diff(left,q)!=0
 qr=s.factor(-left.subs(q,0)/s.diff(left,q))
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
 gauge=source[:,[0,2]].inv()*source
 point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
          -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert gauge==cell.subs(point)
 assert source[:,[0,2]].inv()*Y==cell.subs(point)*Z
 H=Y[:,:2];B=H.inv()*Y[:,2:];z=Z[:,2:]-Z[:,:2]*B
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0
 return point,qr,J
root=chamber.threshold_low
rows=[]
for value in (s.Rational(1,20),root,s.Rational(1,2)):
 point,qr,J=inverse_at(value)
 signs={str(v):str(s.sign(point[v])) for v in vars[:6]}
 signs['u']=str(s.sign(point[u]));signs['t-u']=str(s.sign(point[t]-point[u]))
 rows.append({'E_source_e':str(value),'F_B_kernel_area':str(qr),
              'F_B_w2':str(point[w2]),'F_B_J_nonzero':True,
              'F_B_positive':all(x=='1' for x in signs.values()),'F_B_source_signs':signs})
 if value==root:
  assert point[w2]==0
  old={var:chamber.parse(chamber.EB['inverse_source_parameters'][str(var)]).subs(chamber.e,root)
       for var in vars}
  assert point==old
assert rows[0]['F_B_w2']!='0' and rows[-1]['F_B_w2']!='0'
for i,value in ((0,s.Rational(1,20)),(2,s.Rational(1,2))):
 p=dict(zip(vars,(value,1,1,1,1,1,3,2)))
 E_sheets=list(trace.G.fibre(trace.D.subs(p),Z))
 assert len(E_sheets)==2
 positive_E=sum(int(bool(all(point[var]>0 for var in vars[:6]) and
                point[u]>0 and point[t]>point[u])) for _,point in E_sheets)
 assert positive_E==1
 EB=next(z for z in chamber.checks if z['cell']=='E_B')
 assert next(z['positive'] for z in EB['positivity_controls'] if z['e']==str(value))==rows[i]['F_B_positive']
 for name in ('E_C','E_D'):
  source=next(z for z in chamber.checks if z['cell']==name)
  assert not next(z['positive'] for z in source['positivity_controls'] if z['e']==str(value))
 rows[i]['five_cell_positive_source_sheet_count']=1+2*int(rows[i]['F_B_positive'])
assert any(q['boundary']=='interior_E_target_lower_wall' and
           q['two_transverse_target_direction_full_superpole_cancellations']
           for q in neighbor.checks)
assert any(z['wall']=='lower' and not z['other_E_sheet_on_same_source_facet']
           for z in prior.rows)
report={'schema':'marici.nima.nine-point-five-cell-lower-internal-full-trace-cancellation.v1',
 'passed':True,'exact_common_E_target_controls':rows,
 'positive_multiplicity_across_lower_wall':'On the exact positive E target ray, at e=1/20 only E has a positive source sheet among E,E_B,E_C,E_D,F_B (multiplicity 1). At e=1/2, E,E_B,F_B each have one and E_C/E_D none (multiplicity 3). The two added cells E_B/F_B have opposite oriented local boundary residues.',
 'full_trace_lower_pole_outcome':'F_B has a UNIQUE algebraic inverse on the regular target open (rank4 five-minor linear lift with nonzero q left-null coefficient). At the exact lower E_B internal wall its unique inverse source equals E_B on w2=0 and its full target Jacobian is nonzero. The earlier independently certified opposite oriented all-component EB/F_B local pushed residues therefore cancel in their COMPLETE meromorphic one-sheet field traces at the wall; there is no other F_B sheet. The other original E-square inverse sheets are regular there, so adding F_B removes the previously uncancelled lower four-cell meromorphic simple superpole.',
 'scope':'Full residue cancellation at the exact lower wall along positive E target curve, not an identity of complete EB+FB forms away from the wall, or a global n9 image canonical form.'}
(OUT/'nine-point-five-cell-lower-internal-full-trace-cancellation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'F_B_unique_sheet_at_lower_wall':True,
 'five_cell_meromorphic_lower_superpole_cancelled':True,
 'positive_source_samples':[{k:r[k] for k in ('E_source_e','F_B_w2','F_B_positive')} for r in rows]},indent=2))
