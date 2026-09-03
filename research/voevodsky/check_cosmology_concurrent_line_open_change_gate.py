"""Test the minimal surface open change from a triangle to three concurrent lines."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_concurrent_line_open_change_gate.json'
def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def graph_h1(v,edges,components=1):return len(edges)-v+components
def main():
 triangle=[[1,0,0],[0,1,0],[0,0,1]]
 concurrent=[[1,0,0],[0,1,0],[1,1,0]]
 assert det3(triangle)==1 and det3(concurrent)==0
 triangle_edges=[(0,1),(1,2),(2,0)];star_edges=[(0,1),(0,2),(0,3)]
 assert graph_h1(3,triangle_edges)==1 and graph_h1(4,star_edges)==0
 # Deliberate false attachment model: the star contains none of the old three pairwise edges.
 assert not set(triangle_edges).issubset(set(star_edges))
 out={'schema':'marici.voevodsky.cosmology-concurrent-line-open-change-gate.v1','status':'concurrent_line_change_kills_cycle_but_does_not_fill_original_pair','generic_boundary':{'lines':'X=0,Y=0,Z=0','coefficient_determinant':det3(triangle),'resolved_dual_graph':'3-cycle','H1_rank':1,'complement_H2_rank':1},'changed_boundary':{'lines':'X=0,Y=0,X+Y=0','coefficient_determinant':det3(concurrent),'singularity':'ordinary triple point','log_resolution_dual_graph':'four-vertex three-edge star','H1_rank':0,'complement_description':'A1-bundle over P1 minus three points','complement_H2_rank':0},'minimality':'On a smooth surface an SNC boundary has at most two components through a point. A filled three-vertex face therefore requires either a non-SNC triple point, a higher-dimensional source, or a nongeometric cell attachment.','comparison_obstruction':'Resolving the concurrent arrangement replaces the three old pairwise-intersection edges by a star; it does not attach a face while retaining the original triangle as a subcomplex. The open complement and H2 change, so no identity comparison transports its null class back to Xi_log.','deliberate_failure':'Treating the star as the old triangle plus a face is false because none of the original three pairwise edges survives in that incidence form.','decision':'The concurrent-line degeneration is a genuine geometry in which the primitive class disappears, but it is an open change rather than a filler of the original pair. Without an independently sourced specialization/retraction carrying the required boundary vector, it cannot construct the original horn.','next_gate':'audit the arrangement degeneration comparison map and its vanishing-cycle exact sequence; test whether it transports a filler or instead records Xi_log as the lost class','limitations':['surface arrangement model only','does not exclude a higher-dimensional correspondence','no horn or physical period constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
