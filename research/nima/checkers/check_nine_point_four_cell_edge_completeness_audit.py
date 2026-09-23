"""Fresh executable four-edge audit: three regular target cancellations, one exceptional edge."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_adjacent_cell_generic_boundary_cancellation as ab
 import check_nine_point_slope_merge_adjacent_cell_cancellation as ac
 import check_nine_point_regular_cd_full_boundary_pole_cancellation as cd
 import check_nine_point_w4_slope_intersection_square as square
 import check_nine_point_slope_face_structural_blowdown as singular
 import check_nine_point_positive_slope_face_normal_cones as cones
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,B,C,D=(square.cells[x] for x in 'ABCD')
w2,w4,w5,w6,w7,w8,t,u=square.vars
assert s.simplify(A.subs(w4,0)-B.subs(w4,0))==s.zeros(2,8)
assert s.simplify(A.subs(t,u)-C.subs(t,u))==s.zeros(2,8)
assert s.simplify(C.subs(w4,0)-D.subs(w4,0))==s.zeros(2,8)
assert s.simplify(B.subs(t,u)-D.subs(t,u))==s.zeros(2,8)
rho=square.rho
for i,j in [('A','B'),('A','C'),('C','D'),('B','D')]:
 assert s.factor(rho[i]+rho[j])==0
assert all(x['nonparallel_for_every_pair_of_positive_face_preimages']
           for x in cones.checks)
assert all(c['rank_C']==c['rank_D']==8 and
           c['two_transverse_target_directions_cancel']
           for c in cd.report['exact_positive_boundary_controls'])
edges=[
 {'cells':'A/B','source_facet':'w4=0','positive_regular_target_controls':len(ab.checks),
  'full_nonlinear_generic_open_target_pole_cancellation':True},
 {'cells':'A/C','source_facet':'t-u=0','positive_regular_target_controls':len(ac.checks),
  'full_nonlinear_generic_open_target_pole_cancellation':True},
 {'cells':'C/D','source_facet':'w4=0','positive_regular_target_controls':len(cd.checks),
  'full_nonlinear_generic_open_target_pole_cancellation':True},
 {'cells':'B/D','source_facet':'t-u=0','positive_regular_target_controls':0,
  'full_nonlinear_generic_open_target_pole_cancellation':False,
  'reason':'Universal target Jacobian rank <=7 on positive slope face; the two positive normal-ray families are disjoint over two exact target planes. Only a paired REGULATED source-boundary-current cancellation and separate local leading normal forms are certified.'}]
assert [e['positive_regular_target_controls'] for e in edges[:3]]==[3,3,3]
assert all(singular.checks[i]['rank']=={'B':7,'D':7}
           for i in range(len(singular.checks)))
report={'schema':'marici.nima.nine-point-four-cell-edge-completeness-audit.v1','passed':True,
 'source_cell_square':{'four_cells_all_positive':True,
  'oriented_source_densities':{x:str(rho[x]) for x in 'ABCD'},
  'all_four_edges_equal_complete_source_matrices_and_opposite_source_residues':True},
 'edges':edges,
 'certified_regular_target_edge_count':3,
 'exceptional_rank_collapsed_target_edge_count':1,
 'positive_target_plane_normal_disjointness_controls':len(cones.checks),
 'next_gate':'An independent arbitrary-Y positive-image canonical form or complete cell/branch/multiplicity accounting; source-edge incidence alone cannot certify a target triangulation.',
 'limits':'This audited four-cell subcomplex is not an exhaustive n9 positroid-cell complex; the nine-point image boundary and full form remain unresolved.'}
(OUT/'nine-point-four-cell-edge-completeness-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'regular_full_target_edges':3,
 'exceptional_rank_collapsed_edges':1,
 'global_image_form_open':True},indent=2))
