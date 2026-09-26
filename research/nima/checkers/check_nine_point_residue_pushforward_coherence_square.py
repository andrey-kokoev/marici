"""Independent interior and boundary Jacobians for four local residue squares.
All computations at the exact regular common facet e=44/445.
"""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    import check_nine_point_four_cell_two_zero_column_facet_full_pole as base

# Actual target chart coordinates vec(B), rather than the unframed C*z columns.
J={}
for name,C in base.C.items():
    J[name]=s.Matrix.hstack(*[s.Matrix(list(base.H.inv()*C.diff(v).subs(base.point)*base.z))
                              for v in base.vars])
T=J['zero2_E_B'][:,1:]
assert T.rank()==7 and all(A[:,1:]==T for A in J.values())
n=T.T.nullspace()[0]
m=next(i for i in range(8) if n[i]!=0)
n=n/n[m]
retained=[i for i in range(8) if i!=m]
# z = seven retained target chart coordinates. Locally the face is the graph
# y_m=f(z). x=y_m-f(z) has differential n at this point.
boundary_J=T[retained,:].det(method='domain-ge')
assert boundary_J!=0
coordinate_sign=(-1)**m
remaining=s.prod(base.point[v] for v in base.vars[1:6])*base.point[base.u]*(base.point[base.t]-base.point[base.u])
assert remaining>0
rows=[]
for name,A in J.items():
    orientation=base.cube.orient[name.split('_',1)[1]]
    rho=s.factor(orientation/remaining)
    det=A.det(method='domain-ge')
    transverse=s.factor((n.T*A[:,0])[0])
    assert det!=0 and transverse!=0
    # route I: push eight-form, then extract target residue in dx/x wedge dz.
    route_I=s.factor(coordinate_sign*rho*transverse/det)
    # route II: take dw2/w2 source residue, then push on the boundary chart.
    route_II=s.factor(rho/boundary_J)
    assert route_I==route_II
    assert det==coordinate_sign*transverse*boundary_J
    # Verify the physical-pair fermionic components as exact numerical witnesses.
    components=[]
    C0=base.C[name].subs(base.point)
    for i,j in itertools.combinations(range(9),2):
        numerator=s.factor(C0[:,[i,j]].det()**4)
        assert s.factor(route_I*numerator-route_II*numerator)==0
        components.append({'physical_labels':[i+1,j+1],
                           'common_residue':str(s.factor(route_II*numerator))})
    rows.append({'cell':name,'orientation':int(orientation),
                 'source_log_residue_density':str(rho),
                 'full_target_jacobian':str(det),
                 'target_normal_derivative':str(transverse),
                 'push_then_residue':str(route_I),
                 'residue_then_boundary_push':str(route_II),
                 'physical_pair_components':components})
by={r['cell']:s.Rational(r['push_then_residue']) for r in rows}
for family in ('zero2','zero3'):
    assert by[family+'_E_B']+by[family+'_F_B']==0
for role in ('E_B','F_B'):
    assert by['zero2_'+role]==by['zero3_'+role]
# Symbolic equality of restricted source matrices supplies the common full
# fermionic polynomial, beyond the 36 component witnesses.
assert all(C.subs(base.w2,0)==base.facet for C in base.C.values())
report={'passed':True,'target_control_e':str(base.wall.root),
 'target_chart':'row-major B=(C Z_first2)^(-1) C Z_last4',
 'omitted_target_coordinate_zero_based':m,
 'normalized_conormal':[str(v) for v in n],
 'independent_seven_dimensional_boundary_jacobian':str(boundary_J),
 'local_defining_function':'x=y_m-f(z); face graph existence follows from nonzero boundary minor',
 'four_retained_route_records':rows,
 'local_residue_pushforward_squares_agree':True,
 'cross_family_restricted_face_identifications_agree':True,
 'full_fermionic_equality_basis':'common symbolic face matrix plus equality of scalar residue factors',
 'cube_status':'boundary comparison data instantiated; off-face source/target comparison maps and bulk higher filler remain unspecified',
 'scope':'Exact regular facet control and local inverse branches; no global canonical-form equality or contour assignment.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/nine-point-residue-pushforward-coherence-square.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'independent_squares':4,'component_checks':len(rows)*36,
 'boundary_rank':7,'offface_cube_filler':'unspecified'},indent=2))
