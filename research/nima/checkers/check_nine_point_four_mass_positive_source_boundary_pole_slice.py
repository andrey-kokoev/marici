"""Exact genuine dlog pole reached from a positive four-mass source sheet."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_four_mass_boundary_norm_slice as norms
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
old=norms.previous;eps,q,P=old.epsilon,old.q,old.P
D,vars,Z=old.D,old.vars,old.Z
pole=s.Rational(485,12278)
P0=s.Poly(P.as_expr().subs(eps,pole),q)
assert P0.degree()==2 and s.discriminant(P0.as_expr(),q)>0
w4=old.w[1]
num=s.Poly(s.fraction(s.cancel(w4.subs(eps,pole)))[0],q)
common=s.gcd(P0,num).monic();assert common.degree()==1
root=s.factor(-common.nth(0)/common.nth(1));assert root==-s.Rational(13,3374)
other=s.factor(-P0.nth(1)/P0.nth(2)-root);assert other!=root
point=dict(zip(vars,[s.factor(v.subs({eps:pole,q:root})) for v in (*old.w,old.t,old.u)]))
assert point[vars[1]]==0
assert all(point[v]>0 for v in (vars[0],*vars[2:6],vars[7]))
assert point[vars[6]]>point[vars[7]]
assert s.factor(old.gauge_det.subs({eps:pole,q:root}))!=0
assert all(s.factor(expr.subs({eps:pole,q:other}))!=0 for _,expr in norms.factors)
Y=D.subs(point)*Z;H=Y[:,4:6];assert H.det()!=0
B=H.inv()*Y[:,:4]
cols=[]
for v in vars:
 derivative=D.diff(v).subs(point)*Z
 dB=H.inv()*(derivative[:,:4]-derivative[:,4:6]*B)
 cols.append(s.Matrix(list(dB)))
J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
qdot=s.factor(-s.diff(P.as_expr(),eps)/s.diff(P.as_expr(),q))
w4dot=s.factor((s.diff(w4,eps)+s.diff(w4,q)*qdot).subs({eps:pole,q:root}));assert w4dot!=0
otherprod=s.prod(point[v] for v in (vars[0],*vars[2:6]))*point[vars[7]]*(point[vars[6]]-point[vars[7]])
scalar=s.factor(-s.S.One/(otherprod*J*w4dot));assert scalar!=0
px=s.det(s.Matrix.hstack(D.subs(point)[:,0],D.subs(point)[:,4]));assert px!=0
fourflavor=s.factor(scalar*px**4);assert fourflavor!=0
report={'schema':'marici.nima.nine-point-four-mass-positive-source-boundary-pole-slice.v1','passed':True,
 'target_slice_pole_epsilon':str(pole),'positive_cell_boundary':'w4=0 with all other six weights, u and t-u strictly positive',
 'boundary_sheet_inverse_root':str(root),'other_sheet_inverse_root':str(other),
 'boundary_sheet_approaches_from_positive_source_cell':True,
 'distinct_inverse_sheets_and_regular_conjugate':True,
 'row_gauge_regular':True,'full_eight_by_eight_target_jacobian_nonzero':True,
 'dw4_depsilon_transverse_nonzero':True,
 'oriented_scalar_two_sheet_trace_residue':str(scalar),
 'four_flavor_XXXX_component_residue':str(fourflavor),
 'conclusion':'This is a genuine simple pole of the continued fourmass two-sheet source form arising from a boundary of the POSITIVE four-pair source cell. The conjugate sheet is regular and cannot cancel the nonzero scalar or XXXX residue.',
 'boundary':'This proves a sourced positive-cell pushforward pole on one exact rank-six target slice, NOT that the target is on the boundary of the entire n9 top-cell image or that its full canonical form has the same pole. A first-order same-target positive-top-cell LP test exists separately but is not a global exclusion certificate.'}
(OUT/'nine-point-four-mass-positive-source-boundary-pole-slice.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'epsilon':str(pole),'boundary_sheet_source_positive':True,
 'scalar_and_four_flavor_poles':True},indent=2))
