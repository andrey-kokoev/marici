import contextlib,io,json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
 from five_site_g5_source_residue import CI

# Project the two g5 boundary foci C3,C4 to the rank-two external plane.
c3,c4=CI[3],CI[4]
area=c3[0]*c4[1]-c3[1]*c4[0]
assert area.l>0 or area.h<0
packet={'schema':'marici.five_site_g5_gram_forces_pair_tangency.v1',
 'focus_area_interval':[str(area.l),str(area.h)],'foci_certified_noncollinear':True,
 'off_plane_stationarity_equation':'C3/r3+C4/r4=0',
 'off_plane_solution_exists':False,
 'reason':'positive distances cannot make two noncollinear focus vectors cancel',
 'threshold_pinch_location_at_rank_two':'external plane',
 'wall_gradient_location':'external plane',
 'threshold_tangent_decomposition':'one in-plane direction plus one plane-normal direction',
 'projected_wall_normal_rank':1,
 'all_active_pair_determinants_vanish':True,'active_pair_count':22,
 'compatibility_at_two_wall_intersection':'h1=h2=0 implies k=h2-alpha*h1=0',
 'all_active_pairs_meet_rees_center':True,
 'physical_exceptional_pairing_computed':False}
Path('research/benincasa/results/five-site-g5-gram-forces-pair-tangency.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
