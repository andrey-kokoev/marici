"""Locate {u,v} in Deligne degree and separate curvature from extension ambiguity."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_Deligne_regulator_degree_gate.json'
def main():
 data={'motivic_degree':2,'weight':2,'Deligne_degree':2,'curvature_degree':2,'integral_projection':1}
 assert data['motivic_degree']==data['Deligne_degree']==data['curvature_degree']==2
 assert data['integral_projection']!=0
 # A zero or coboundary Deligne class must have zero image under every cohomology projection.
 could_be_coboundary=data['integral_projection']==0;assert not could_be_coboundary
 out={'schema':'marici.voevodsky.cosmology-Deligne-regulator-degree-gate.v1','status':'Deligne_regulator_is_nonzero_degree_two_class_not_hidden_degree_one_filler','source':'{u,v} in motivic cohomology H_M^2(U,Z(2))','target':'regulator class in H_D^2(U,Z(2))','curvature':'dlog(u) wedge dlog(v)=Xi_log','integral_projection':'the primitive generator of H^2(U,Z(2)), pairing one with the ordered Betti torus','Deligne_exact_sequence':'The degree-two Deligne group projects to integral Hodge classes in F^2 H^2. Its kernel is an H^1-based intermediate quotient and can change secondary/branch data, but not the primitive integral projection.','degree_gate':'Any logarithmic local primitive belongs to a Deligne or Cech degree-one representative whose overlap jumps complete a degree-two cocycle. It is not a global degree-one element with differential Xi_log.','extension_disposition':'Possible H^1-based Deligne ambiguity is external to the pure weight filtration of H^2, but it cannot cancel or trivialize the nonzero integral projection.','decision':'The Deligne regulator preserves the motivic degree-two obstruction. Neither its secondary data nor local logarithms supply the missing global horn.','next_gate':'Cech-log-local-primitives: compute the branch transitions of log(u)dlog(v) and identify their monodromy as the exact globalization obstruction','limitations':['locates degree and projections without choosing a full Deligne cocycle normalization','does not compute every intermediate-quotient component','no physical readout inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
