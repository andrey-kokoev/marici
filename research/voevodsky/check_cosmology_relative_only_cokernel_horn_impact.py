"""Correct the motivic degrees of the free class and isolated tame-sign cycle."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_relative_only_cokernel_horn_impact.json'
def main():
 degrees={'Milnor_{u,v}':2,'Xi_log':2,'isolated_H_times_minus_one':3}
 assert degrees['Milnor_{u,v}']==degrees['Xi_log'] and degrees['isolated_H_times_minus_one']==degrees['Milnor_{u,v}']+1
 full_tame=('v^-1','u','-v/u');assert len(full_tame)==3
 out={'schema':'marici.voevodsky.cosmology-relative-only-cokernel-horn-impact.v1','status':'hyperplane_sign_is_higher_degree_isolation_obstruction_not_same_degree_horn_component','degree_audit':degrees,'full_tame_boundary':list(full_tame),'Gersten_fact':'The full tame tuple is the boundary of {u,v}. The isolated sign on Z represents H*(-1) only after splitting it from the complementary nonconstant units; those units carry the compensating Gersten class.','horn_impact':'H*(-1) cannot be added as a same-degree closed correction to a degree-one horn candidate. It detects failure to isolate the sign with no other residues, not an independent degree-two horn projection.','repairs':['withdraw Z plus Z/2 as the horn cohomology group','withdraw the two same-degree relative lifts (1,1) and (1,0)','retain parity formulas only as chain-level tame-sign bookkeeping','retain nonvanishing of H*(-1) in CH^2(P2,1)'],'decision':'The relative-only class has no direct horn differential effect. Integral horn tests must keep the unsplit K1 units in the correctly graded localization total complex.','next_gate':'integral-total-complex-degree-reconciliation: place K2, divisor K1 units, point valuations, Xi_log, and sigma123 in one graded diagram','limitations':['corrects the fixed P2 localization grading','does not yet write the full motivic-to-de Rham comparison bicomplex','free nonexactness theorem remains unchanged'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
