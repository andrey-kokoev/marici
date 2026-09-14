#!/usr/bin/env python3
"""Exact C2 orientation-torsor audit for a real rank-one shared incidence."""
import json
from pathlib import Path

def main():
 orientations=(-1,1);C2=(-1,1)
 action={(g,o):g*o for g in C2 for o in orientations}
 # Free and transitive C2 action.
 for o in orientations:
  assert [g for g in C2 if action[g,o]==o]==[1]
 for a in orientations:
  for b in orientations:
   assert len([g for g in C2 if action[g,a]==b])==1
 reversal={o:-o for o in orientations}
 assert all(reversal[reversal[o]]==o for o in orientations)
 assert all(reversal[o]!=o for o in orientations)
 # Two oriented planes induce opposite orientations on the shared axis.
 induced={'forward_plane':1,'backward_plane':-1}
 assert induced['forward_plane']+induced['backward_plane']==0
 result={'schema':'marici.voevodsky.shared-axis-orientation-torsor.v1','shared_incidence':'real rank-one line','orientation_torsor':list(orientations),'acting_group':'C2','action_table':{f'{g},{o}':v for (g,o),v in action.items()},'action_free':True,'action_transitive':True,'reversal':{str(o):reversal[o] for o in orientations},'reversal_fixed_points':[],'canonical_orientation_selected':False,'induced_plane_orientations':induced,'internal_boundary_cancels':True,'conclusion':'C2 is the automorphism group of the orientation torsor of the shared line; no preferred sign is produced.','claim_boundary':'Requires a source-derived real rank-one determinant line for the shared incidence.'}
 out=Path(__file__).parents[1]/'results'/'shared_axis_orientation_torsor.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
