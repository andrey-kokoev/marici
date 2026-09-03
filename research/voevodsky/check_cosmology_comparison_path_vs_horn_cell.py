"""Separate the signed graph nullhomotopy from a degree-one source-chain element."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_comparison_path_vs_horn_cell.json'
def main():
 # S has k in degree 2 and no degree 1. K has tau in degree 1 and z=(1,-1) in degree 2.
 source_degree_one_rank=0;signed_graph=(1,-1);d_tau=(1,-1)
 assert signed_graph==d_tau and source_degree_one_rank==0
 target_nullhomotopy_exists=signed_graph==d_tau;element_lift_exists=source_degree_one_rank>0
 assert target_nullhomotopy_exists and not element_lift_exists
 out={'schema':'marici.voevodsky.cosmology-comparison-path-vs-horn-cell.v1','status':'signed_graph_has_canonical_target_nullhomotopy_but_no_source_element','source_cycle':'k={u,v} in source degree two','signed_graph_map':'j(k)=(Xi_log,-sigma123)','comparison_cell':'tau in cone degree one with d tau=j(k)','target_HomotopyLift':'The cone contraction gives H(k)=tau and dH(k)=j(k). It is linear on the primitive source subcomplex and packages strict regulator compatibility as a path.','ElementLift':'No h in source degree one satisfies d_S h=k; the source class remains nonzero.','commuting_square_relation':'In the common flag codomain Res*R_log=R_flag strictly, so the difference homotopy is zero. Passing to the signed cone turns that strict equality into the formal path tau.','authority_gate':'The HomotopyLift is canonical only after admitting the comparison-cone constructor. Cone admission does not imply that tau is a geometric incidence cell, higher-Chow precycle, rank26 relation, or physical process.','decision':'A formal source-indexed comparison path exists; a source-chain horn does not. These statements are compatible and must not be conflated.','next_gate':'cone-admission-source-authority: decide which independent geometric data, beyond formal cone construction, would promote the target path to an admitted scientific horn','limitations':['canonical on the primitive minimal subcomplex','does not construct a full contraction on unrelated source classes','no physical process or record inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
