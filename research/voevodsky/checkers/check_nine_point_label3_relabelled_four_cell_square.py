"""Relabel the oriented four-cell source square onto physical label 3 and audit fermionic support."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_w4_slope_intersection_square as square
 import check_nine_point_label3_cell_arbitrary_y_two_sheet_trace as Etrace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
vars=square.vars;w2,w4,w5,w6,w7,w8,t,u=vars
labels=('E','E_B','E_C','E_D')
source=dict(zip(labels,(square.cells[k] for k in 'ABCD')))
cells={name:s.Matrix.hstack(D[:,:1],s.zeros(2,1),D[:,1:]) for name,D in source.items()}
assert cells['E']==Etrace.E
sign={name:{'E':1,'E_B':-1,'E_C':-1,'E_D':1}[name] for name in labels}
assert s.factor(Etrace.adjacent.rho_E+square.rho['A'])==0
orientation_relative_original_A={name:-sign[name] for name in labels}
K=w2*w4*w5*w6*w7*w8*u*(t-u)
for name,C in cells.items():
 assert C[:,1]==s.zeros(2,1) and C[:,2]==s.Matrix([w2,0])
 assert s.factor(s.det(C[:,[2,4]])-w2*w4)==0
 assert s.factor(square.rho[{'E':'A','E_B':'B','E_C':'C','E_D':'D'}[name]]-
                 sign[name]*square.rho['A'])==0
 v=s.symbols('v',positive=True)
 for i,j in itertools.combinations(range(9),2):
  det=s.factor(C[:,[i,j]].det().subs(t,u+v))
  num,den=s.fraction(s.cancel(det))
  assert all(z>=0 for z in s.Poly(num,w2,w4,w5,w6,w7,w8,u,v).coeffs())
  assert all(z>=0 for z in s.Poly(den,w2,w4,w5,w6,w7,w8,u,v).coeffs())
assert s.factor(sum(sign.values())*(w2*w4)**4/K)==0
assert cells['E'].subs(w4,0)==cells['E_B'].subs(w4,0)
assert cells['E_C'].subs(w4,0)==cells['E_D'].subs(w4,0)
assert cells['E'].subs(t,u)==cells['E_C'].subs(t,u)
assert cells['E_B'].subs(t,u)==cells['E_D'].subs(t,u)
Z=s.Matrix([[j**deg for deg in range(6)] for j in range(1,10)])
controls=[]
for edge,face,raw in [
 ('E/E_B','w4=0',(1,0,1,1,1,1,3,2)),
 ('E/E_C','t-u=0',(1,1,1,1,1,1,2,2)),
 ('E_C/E_D','w4=0',(1,0,1,1,1,1,3,2)),
 ('E_B/E_D','t-u=0',(1,1,1,1,1,1,2,2))]:
 p=dict(zip(vars,map(s.Rational,raw)))
 L,R=edge.split('/');Y=cells[L].subs(p)*Z
 assert Y==cells[R].subs(p)*Z
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(k for k in range(6) if k not in fixed)
 H=Y[:,list(fixed)];B=H.inv()*Y[:,list(free)]
 ranks={}
 for name in (L,R):
  columns=[]
  for parameter in vars:
   delta=cells[name].diff(parameter).subs(p)*Z
   columns.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-
                        delta[:,list(fixed)]*B))))
  ranks[name]=s.Matrix.hstack(*columns).rank()
 controls.append({'edge':edge,'face':face,'source_boundary_identical':True,
                  'target_jacobian_ranks':ranks})
report={'schema':'marici.nima.nine-point-label3-relabelled-four-cell-square.v1',
 'passed':True,'four_distinct_positive_label3_sensitive_cells':list(labels),
 'oriented_source_density_signs_relative_to_E':sign,
 'calibrated_oriented_source_density_signs_relative_to_original_A':orientation_relative_original_A,
 'all_four_chi3_power4_chi5_power4_source_minors':'w2*w4',
 'equal_parameter_oriented_source_component_sum_zero':True,
 'target_edge_controls':controls,
 'scope':'Four positive label3-sensitive source cells; their signed equal-parameter source-coordinate cancellation does NOT imply pushed target-form cancellation because target maps differ. No complete four-cell traces, contour weights, global n9 form or image coverage.'}
(OUT/'nine-point-label3-relabelled-four-cell-square.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'new_positive_chi3_sensitive_cells':3,
 'edge_ranks':controls},indent=2))
