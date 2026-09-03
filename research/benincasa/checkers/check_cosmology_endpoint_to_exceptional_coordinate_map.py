#!/usr/bin/env python3
"""Classify coordinate maps from the soft endpoint chain to exceptional points."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
st=json.loads((B/'soft-endpoint-stokes-cospan.json').read_text());tor=json.loads((B/'soft-endpoint-log-primitive-torsor.json').read_text());rel=json.loads((B/'relative-stokes-pairing-gate.json').read_text())
assert st['bulk_chain']=='Gamma_xi=[-1,1]' and tor['local_coordinate']=='t=xi+1'
assert rel['scope_correction']['direct_exceptional_pullback_is_valid'] is False
# A Mobius map f=(a*x+b)/(c*x+d) fixing -1,0,+1 has b=c=0 and a=d.
constraints={'f(0)=0':'b=0','f(1)=1':'a=c+d','f(-1)=-1':'a=d-c','solution_up_to_scale':'b=0,c=0,a=d'}
out={'schema':'marici.benincasa.cosmology-endpoint-to-exceptional-coordinate-map.v1','source_coordinate':{'xi':'soft endpoint-chain parameter','local_endpoint_coordinate':'t=xi+1'},'target_coordinate':{'r':'exceptional wall-intersection coordinate','marked_points':[-1,0,1]},'mobius_classification':constraints,'unique_three_point_preserving_candidate':'r=xi','candidate_is_source_derived':False,'reason':'the two coordinates belong to different source constructions; matching three numerical marks fixes a presentation map but supplies no morphism between the soft chain and weighted exceptional space','wall_label_compatibility_proved':False,'continued_cycle_compatibility_proved':False,'disposition':'unique candidate classified but source authority absent','next_route':'the endpoint cospan cannot be promoted; return to provenance-preserving Rees generator extraction','passed':True};(R/'cosmology_endpoint_to_exceptional_coordinate_map.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
