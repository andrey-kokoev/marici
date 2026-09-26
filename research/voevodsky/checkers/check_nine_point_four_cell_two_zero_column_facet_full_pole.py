"""Prove regular common-face all-component pushed-pole cancellation for four EB/FB cells."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_zero_phys3_EB_FB_exact_entry_wall as wall
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
first=wall.first;cube=wall.cube;Z9=wall.old.Z9
vars=wall.vars;w2,w4,w5,w6,w7,w8,t,u=vars
C={}
for family in ('zero2','zero3'):
 for name in ('E_B','F_B'):
  old=(cube.E if name=='E_B' else cube.F)[name]
  C[family+'_'+name]=old if family=='zero2' else wall.embed_zero3(old[:,first.old_columns])
facet=C['zero2_E_B'].subs(w2,0)
assert all(mat.subs(w2,0)==facet for mat in C.values())
point={v:s.factor(wall.points['E_B'][v].subs(wall.e,wall.root)) for v in vars}
assert point[w2]==0
Y=facet.subs(point)*Z9
H=Y[:,:2];assert H.det()!=0
B=H.inv()*Y[:,2:];z=Z9[:,2:]-Z9[:,:2]*B
jac={key:s.Matrix.hstack(*[s.Matrix(list(mat.diff(v).subs(point)*z)) for v in vars])
     for key,mat in C.items()}
tangent=jac['zero2_E_B'][:,1:]
assert tangent.rank()==7
assert all(J[:,1:]==tangent and J.det(method='domain-ge')!=0 for J in jac.values())
normal=tangent.T.nullspace()[0]
assert normal.shape==(8,1)
ratios={key:s.factor((normal.T*J[:,0])[0]/J.det(method='domain-ge')) for key,J in jac.items()}
assert all(v==next(iter(ratios.values())) for v in ratios.values())
assert next(iter(ratios.values()))!=0
oriented={key:s.factor(cube.orient[key.split('_',1)[1]]*ratios[key]) for key in jac}
assert oriented['zero2_E_B']+oriented['zero2_F_B']==0
assert oriented['zero3_E_B']+oriented['zero3_F_B']==0
# Every fermionic numerator C chi, face frame det(C h)^4, and
# source-residue denominator in remaining seven controls coincide.
assert all(mat.subs(w2,0)==facet for mat in C.values())
report={'schema':'marici.nima.nine-point-four-cell-two-zero-column-facet-full-pole.v1',
 'passed':True,'shared_positive_E_target_ray_entry_e':str(wall.root),
 'symbolically_identical_seven_dimensional_source_facets':True,
 'face_tangent_rank':7,'all_four_full_target_jacobians_nonzero':True,
 'normal_over_full_jacobian_ratio':str(next(iter(ratios.values()))),
 'four_normal_over_jacobian_ratios':{k:str(v) for k,v in ratios.items()},
 'calibrated_oriented_normalized_superpole_residue_factors':{k:str(v) for k,v in oriented.items()},
 'full_superpole_cancels_within_each_family_for_all_fermionic_components':True,
 'consequence':'The common rank-seven target face is an ordinary target hypersurface; all four source-map normals lie in the same one-dimensional quotient, and the exact ratio normal-derivative/full-Jacobian is identical. Equal face fermionic numerator, frame and other log denominators then make EB/FB opposite oriented FULL pushed superpole residues cancel separately in EACH zero-column family near the regular shared face point.',
 'scope':'Local common-face simple superpole cancellation with each family internally calibrated, NOT cancellation of entire forms, cross-family contour-weight assignment, all global inverse sheets or n9 canonical form.'}
(OUT/'nine-point-four-cell-two-zero-column-facet-full-pole.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'face_target_codimension':1,'regular_maps':4,
 'independent_within_family_full_superpole_cancellations':2},indent=2))
