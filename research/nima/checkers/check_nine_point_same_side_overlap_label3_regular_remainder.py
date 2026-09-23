"""Same-side A/E images overlap openly, but E has a nonzero regular chi3 component."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_composite_neighbors_target_sides as sides
 import check_nine_point_label3_cell_composite_local_cancellation as adjacent
 import check_nine_point_positive_label3_cell_missing_from_zero_column_trace as positive
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,E=adjacent.A,adjacent.E
vars=adjacent.vars
w2,w4,w5,w6,w7,w8,t,u=vars
assert all(record['E_relative_target_normal_side_to_A']==1 for record in sides.checks)
assert all(record['three_target_jacobian_ranks']=={'A':8,'V':8,'E':8} for record in sides.checks)
assert A[:,2]==s.zeros(2,1) and E[:,2]==s.Matrix([w2,0])
minor_E=s.factor(s.det(s.Matrix.hstack(E[:,2],E[:,4])))
assert minor_E==w2*w4
source_E=s.factor(adjacent.rho_E*minor_E**4)
expected=s.factor(w2**3*w4**3/(w5*w6*w7*w8*u*(t-u)))
assert source_E==expected
assert s.factor(source_E.subs(w2,0))==0
minor_A=s.factor(s.det(s.Matrix.hstack(A[:,2],A[:,4])))
assert minor_A==0
assert len(positive.checks)==3 and all(z['source_to_target_chart_rank']==8 for z in positive.checks)
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
controls=[]
for name,raw in [('first',('1/20','1','1','1','1','1','3','2')),
                 ('second',('1/40','3','1','4','2','5','7/2','3/2'))]:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 Y=E.subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 cols=[]
 for parameter in vars:
  delta=E.diff(parameter).subs(p)*Z
  cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                  delta[:,list(fixed)]*target))))
 J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
 local=s.factor(source_E.subs(p)/J);assert local!=0
 controls.append({'positive_E_interior_point':name,'w2':str(p[w2]),
  'nonzero_chi3_power4_chi5_power4_local_pushed_coefficient':str(local)})
report={'schema':'marici.nima.nine-point-same-side-overlap-label3-regular-remainder.v1','passed':True,
 'same_side_overlap_proof':'At three exact shared positive boundary points, A and E have invertible 8x8 target maps, common rank-seven tangent image, and positive ratio of their target-normal directions. The inverse function theorem yields a nonempty OPEN overlap of their strictly positive target images near each boundary point.',
 'A_chi3_power4_chi5_power4_component':'identically zero (physical column3 zero)',
 'E_chi3_power4_chi5_power4_source_coefficient':str(source_E),
 'E_component_w2_boundary_vanishing_order':3,
 'exact_nonzero_E_local_sheet_controls':controls,
 'consequence':'A/E simple w2 boundary poles cancel on their same-side overlap, but their complete local pushed SUPERSYMMETRIC forms do not cancel identically there: E has a nonzero chi3^4 chi5^4 regular component (order w2^3), A has none.',
 'scope':'Local branch comparison, not full two-sheet E field trace. Other E inverse sheets/cells may cancel the label3-sensitive component in a complete amplitude; no full n9 form or image coverage follows.'}
(OUT/'nine-point-same-side-overlap-label3-regular-remainder.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'open_positive_A_E_target_overlap':True,
 'E_chi3_component_source_order_w2':3,
 'nonzero_local_E_interior_controls':len(controls)},indent=2))
