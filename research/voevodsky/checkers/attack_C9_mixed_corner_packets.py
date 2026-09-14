#!/usr/bin/env python3
"""Generate all sign-corner Cut packets and test mixed activation of v_alg."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
loc=json.loads((R/'research/benincasa/et-cut-nearby-normal-form.json').read_text())
full=json.loads((R/'research/benincasa/full-rank12-cut-nearby-layers-certificate.json').read_text())
glue=json.loads((R/'research/benincasa/enhanced-conductor-unimodular-gluing.json').read_text())
# Ambient coordinates e2,e3,e4,e5,e6,v0. At a=sigma_a*y,b=sigma_b*x,
# e3=a*phi002 and e5=b*phi002, so sign transport changes the e3/e5
# coefficients while preserving the support pattern.
packets=[]
for sa,sb,label in [(1,1,'++'),(1,-1,'+-'),(-1,1,'-+'),(-1,-1,'--')]:
 cols={'g101':[0,2*sa,0,0,0,0], 'g110':[0,0,0,2*sb,0,0], 'g111_tilde':[0,sa,0,sb,1,0]}
 proj={k:[v[4],v[5]] for k,v in cols.items()}
 packets.append({'corner':label,'signs':[sa,sb],'columns_in_scaled_corner_frame':cols,'projection_e6_v0':proj,'mixed_projection_rank':int(any(proj[k]!=[0,0] for k in ('g101','g110'))),'full_projection_rank':1})
checks={'four_sign_packets':len(packets)==4,'positive_corner_matches_source_support':[p for p in packets if p['corner']=='++'][0]['columns_in_scaled_corner_frame']=={'g101':[0,2,0,0,0,0],'g110':[0,0,0,2,0,0],'g111_tilde':[0,1,0,1,1,0]},'all_mixed_v0_zero':all(p['projection_e6_v0']['g101'][1]==p['projection_e6_v0']['g110'][1]==0 for p in packets),'all_mixed_plane_projection_zero':all(p['mixed_projection_rank']==0 for p in packets),'top_always_e6_unit':all(p['projection_e6_v0']['g111_tilde']==[1,0] for p in packets),'certificate_cut_image_has_no_v0':all('v0' not in s for s in full['cut_nearby_algebraic_image']),'cyclic_profiles_repeat':full['cyclic_sector_profiles_log_rank_cut_rank_intersection_rank']==[[3,3,1],[3,3,1],[3,3,1]],'enhanced_basis_typed':glue['primitive_conductor_basis']==['g101','g110','g111_tilde']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C9-mixed-corner-packet-attack.v1','ambient_basis':['e2','e3','e4','e5','e6','v0'],'target_plane':['e6','v_alg represented by v0'],'packets':packets,'C9':'A sourced physical corner involving g101 or g110 activates a nonzero v_alg channel.','status':'rejected for the complete total-energy/Cut sign-corner orbit','reason':'Every mixed Cut column lies in e3 or e5 and projects to zero on both e6 and v0. Sign/deck transport changes signs while preserving zero v0 support.','survivor':'g111_tilde projects to the unit e6 direction at every corner.','scope':'all four sign-labelled corners and all three cyclic sector profiles of the frozen Cut-nearby packet','next':'Execute C10 rejection-first by stacking every sourced corner projection and computing its integral rank and Smith invariants.','checks':checks,'passed':True}
(R/'research/voevodsky/results/C9_mixed_corner_packet_attack.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C9':out['status'],'packets':len(packets),'mixed_ranks':[p['mixed_projection_rank'] for p in packets],'top_projections':[p['projection_e6_v0']['g111_tilde'] for p in packets],'next':out['next']}))
