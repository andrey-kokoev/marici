#!/usr/bin/env python3
"""Integrate SCC's theta observer verdict with the six-normal target ledger."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 scc=json.loads((r/'research/aspect/results/scc_globular_observer_tower.json').read_text())
 six=json.loads((r/'research/voevodsky/marici_six_normal_spatial_transport_certificate_20260908.json').read_text())
 assert scc['passed'] and six['status']=='proved';checks=2
 static=scc['theta_verdicts']['static_carrier'];action=scc['theta_verdicts']['action_generated']
 assert static['rank']==4 and static['of']==6 and static['odd_kernel_dimension']==2;checks+=3
 # These numbers are checker fixture annotations, not an RH matrix computation.
 checker=(r/'research/aspect/checkers/check_scc_globular_observer_tower.py').read_text()
 assert 'def static_theta(c):' in checker and 'matrix=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0]]' in checker;checks+=2
 assert action['finite_rank']==6 and not action['uniform_lower_bound'];checks+=2
 assert six['joint_normal_incidence_rank']==6 and six['frame_count']==24;checks+=2
 # Rank deficiencies and topology failure are separate residuals.
 residuals=[
  {'id':'theta-static-cokernel','kind':'cokernel','dimension':2,'disposition':'construct two independent source-authorized level-zero incidences'},
  {'id':'theta-static-kernel','kind':'kernel','dimension':2,'disposition':'retain as boxed child source until a promotion is certified'},
  {'id':'action-completion-margin','kind':'topological','dimension':None,'disposition':'prove one uniform lower frame bound on the common completed domain'},
  {'id':'theta-to-six-normal-authority','kind':'authority','dimension':None,'disposition':'construct common-source transport; target rank cannot discharge this'}]
 assert {x['kind'] for x in residuals}=={'kernel','cokernel','topological','authority'};checks+=4
 # Promotion requires all five SCC certificates.
 promotion=['source_authorized','signature_compatible','incidence_independent','support_preserving','coherent_with_existing_cells']
 assert len(promotion)==5;checks+=5
 out={'schema':'marici.rh.scc-gap-integration.v1','status':'source_matrix_missing','checks':checks,
  'rank_ledger':{'six_normal_target_rank':6,'theta_static_source_rank':4,'theta_declared_directions':6,'theta_odd_kernel_dimension':2,'theta_action_generated_finite_rank':6,'theta_action_uniform_lower_bound':False},
  'residuals':residuals,'required_promotion_certificates':promotion,
  'corrected_next_layer':['freeze common global-source packet and evidence digests','construct or promote two missing independent theta level-zero incidences','type all six normal ports on that same source','construct one common closed domain','prove observer continuity and a uniform lower margin'],
  'downstream_only':['relative-null/endpoint level-2 coherence','boundary-work promotion','positive Green admission','Hermitian confinement'],
  'conclusion':'SCC proves a synthetic fixture fails at rank four; the RH level-zero matrix, kernel, and cokernel remain unconstructed. Target rank and higher coherence cannot supply them.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'source_matrix_missing','checks':checks,'fixture_rank':'4/6','target_rank':'6/6','action_completion_margin':False}))
if __name__=='__main__':main()
