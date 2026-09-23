"""Certify one actual (not merely resultant-candidate) two-sheet form pole."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_four_mass_boundary_norm_slice as norms
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
old=norms.previous;eps,q,P=old.epsilon,old.q,old.P
D,vars,Z=old.D,old.vars,old.Z
pole=s.Rational(181,4336)
P0=s.Poly(P.as_expr().subs(eps,pole),q)
assert P0.degree()==2 and s.discriminant(P0.as_expr(),q)!=0
w8=old.w[5]
number=s.Poly(s.fraction(s.cancel(w8.subs(eps,pole)))[0],q)
common=s.gcd(P0,number).monic();assert common.degree()==1
root=s.factor(-common.nth(0)/common.nth(1));assert root.is_Rational
other=s.factor(-P0.nth(1)/P0.nth(2)-root)
assert other!=root and s.factor(w8.subs({eps:pole,q:other}))!=0
values=[s.factor(expr.subs({eps:pole,q:root})) for expr in (*old.w,old.t,old.u)]
point=dict(zip(vars,values));assert point[vars[5]]==0
assert all(point[v]!=0 for v in vars[:5])
assert point[vars[7]]!=0 and point[vars[6]]-point[vars[7]]!=0
assert s.factor(old.gauge_det.subs({eps:pole,q:root}))!=0
# The other Galois sheet is regular for every source dlog polar factor.
assert all(s.factor(expr.subs({eps:pole,q:other}))!=0 for _,expr in norms.factors)
other_w4=s.factor(old.w[1].subs({eps:pole,q:other}))
assert point[vars[1]]<0 and other_w4<0
Y=D.subs(point)*Z;H=Y[:,4:6];assert H.det()!=0
B=H.inv()*Y[:,:4]
columns=[]
for v in vars:
 derivative=D.diff(v).subs(point)*Z
 dB=H.inv()*(derivative[:,:4]-derivative[:,4:6]*B)
 columns.append(s.Matrix(list(dB)))
J=s.Matrix.hstack(*columns).det(method='domain-ge');assert J!=0
Pder=s.diff(P.as_expr(),q);qdot=s.factor(-s.diff(P.as_expr(),eps)/Pder)
w8dot=s.factor((s.diff(w8,eps)+s.diff(w8,q)*qdot).subs({eps:pole,q:root}));assert w8dot!=0
otherprod=s.prod(point[x] for x in vars[:5])*point[vars[7]]*(point[vars[6]]-point[vars[7]])
scalar_residue=s.factor(-s.S.One/(otherprod*J*w8dot));assert scalar_residue!=0
px=s.det(s.Matrix.hstack(D.subs(point)[:,0],D.subs(point)[:,4]));assert px!=0
flavor_xxxx_residue=s.factor(scalar_residue*px**4);assert flavor_xxxx_residue!=0
report={'schema':'marici.nima.nine-point-four-mass-true-boundary-pole-slice.v1','passed':True,
 'target_slice_pole_epsilon':str(pole),
 'source_polar_divisor':'w8=0, unique algebraic sheet at this epsilon',
 'inverse_root_on_polar_divisor':str(root),
 'other_inverse_root':str(other),
 'two_inverse_roots_distinct':True,
 'source_gauge_and_other_dlog_factors_regular':True,
 'other_sheet_all_source_dlog_factors_regular':True,
 'both_sheets_outside_positive_four_pair_cell_w4_negative':True,
 'source_to_target_eight_by_eight_jacobian_nonzero':True,
 'polar_coordinate_derivative_dw8_depsilon_nonzero':True,
 'oriented_scalar_two_sheet_trace_residue':str(scalar_residue),
 'four_flavor_XXXX_component_residue':str(flavor_xxxx_residue),
 'conclusion':'This is an ACTUAL simple pole of the two-sheet sourced complex fibre trace, not a discriminant caustic or merely a candidate resultant zero: one regular sheet meets the w8=0 dlog boundary transversely, the other sheet remains regular, and both scalar and four-flavor XXXX residues are nonzero.',
 'boundary':'The polar sheet AND the other sheet both have w4<0 and hence are outside the positive four-pair cell at this epsilon. This is an actual pole of the analytically continued algebraic two-sheet contour, NOT a certified pole of the positive source image, full n9 positive-image canonical form, or full n9 amplitude.'}
(OUT/'nine-point-four-mass-true-boundary-pole-slice.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'epsilon':str(pole),'genuine_simple_pole':True,
 'four_flavor_residue_nonzero':True},indent=2))
