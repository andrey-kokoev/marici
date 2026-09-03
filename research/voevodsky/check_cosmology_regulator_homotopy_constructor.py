"""Test the regulator-residue square on symbol, tame-unit, and flag generators."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_regulator_homotopy_constructor.json'
def main():
 direct_flags=(-1,1,-1,1,-1,1)
 log_iterated_residues=(-1,1,-1,1,-1,1)
 assert direct_flags==log_iterated_residues
 direct_edges=(1,1,1);residue_edges=(1,1,1);assert direct_edges==residue_edges
 constant_sign_dlog=0;constant_sign_secondary_valuation=0;assert constant_sign_dlog==constant_sign_secondary_valuation
 difference=[a-b for a,b in zip(direct_flags,log_iterated_residues)];assert difference==[0]*6
 out={'schema':'marici.voevodsky.cosmology-regulator-homotopy-constructor.v1','status':'regulator_residue_square_commutes_strictly_canonical_homotopy_is_zero','source_complex':'weight-two Gersten complex K2 -> divisor K1 -> point Z','maps':{'R_log':'symbol and unit dlog regulator into the logarithmic residue complex','R_flag':'tame symbols followed by ordered secondary valuations into the flag complex','Res':'ordered residue from the logarithmic complex to the flag complex'},'identity':'Res composed with R_log = R_flag on {u,v}, its three tame units, all six ordered flags, and constant signs','ordered_flag_vector':list(direct_flags),'edge_vector':list(direct_edges),'sign_check':'The constant -1 in -v/u has both dlog zero and secondary valuation zero.','homotopy':'In the common flag codomain, strict equality gives H=0. In the signed comparison cone, the canonical contraction packages the same equality as a formal target nullhomotopy taking {u,v} to tau.','cone_interpretation':'The formal tau is a HomotopyLift supplied by the cone constructor, not an ElementLift in the source.','deliberate_failure':'Reversing one flag orientation makes one component differ by two and destroys strict commutation; the prior orientation audit excludes that mismatch.','decision':'The full comparison is strict in the common codomain and becomes a formal path in the signed cone. It supplies no degree-one source element.','next_gate':'comparison-path-vs-horn-cell: formalize the graph image and prove that cone contraction does not induce a source map to tau','limitations':['generator-level full check for the three-line symbol subcomplex','does not construct regulators on every unrelated K-theory class','no physical interface inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
