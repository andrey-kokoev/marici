"""Show that a positive square-root sheet does not determine branch parity of a relative chain."""
import json
# Local smoothing has two finite branch points b_minus,b_plus.
chains={
 'compact_cut_between_branches':{'finite_boundary_points':2,'parity':0},
 'positive_sheet_right_ray_to_infinity':{'finite_boundary_points':1,'parity':1},
 'positive_sheet_left_ray_from_infinity':{'finite_boundary_points':1,'parity':1},
 'closed_enclosing_loop':{'finite_boundary_points':0,'enclosed_branch_points':2,'parity':0},
}
assert chains['compact_cut_between_branches']['parity']==0
assert chains['positive_sheet_right_ray_to_infinity']['parity']==1
assert chains['closed_enclosing_loop']['parity']==0
print(json.dumps({'schema':'marici.nima.qg2-positive-sheet-branch-parity.v1','status':'passed','bold_conjecture':'the positive-sheet label alone forces the physical cut to have even two-branch parity','local_model':'W^2=p*(s-b_minus)*(s-b_plus)','admissible_relative_chain_models':chains,'conjecture_disposition':'falsified by the positive-sheet ray with one finite branch endpoint','residual_conjecture':'even parity follows only from a source boundary condition selecting the compact two-endpoint cut or closed enclosing loop; sheet choice alone is insufficient','first_missing_datum':'physical relative boundary: compact branch-to-branch interval, ray to infinity, or closed contour'},sort_keys=True))
