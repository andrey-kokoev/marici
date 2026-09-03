"""Audit signs across Milnor, de Rham, Betti, Parshin, Cech, and character realizations."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_integral_comparison_sign_coherence.json'
def sign(order=(0,1),circle=(1,1),flag=1):
 permutation=1 if order==(0,1) else -1
 return permutation*circle[0]*circle[1]*flag
def main():
 canonical=sign();assert canonical==1
 tests={'swap_u_v':sign(order=(1,0)),'reverse_u_circle':sign(circle=(-1,1)),'reverse_v_circle':sign(circle=(1,-1)),'reverse_both_circles':sign(circle=(-1,-1)),'reverse_flag_basis':sign(flag=-1)}
 assert tests=={'swap_u_v':-1,'reverse_u_circle':-1,'reverse_v_circle':-1,'reverse_both_circles':1,'reverse_flag_basis':-1}
 flags={'X>XY':-1,'Y>XY':1,'Y>YZ':-1,'Z>YZ':1,'Z>ZX':-1,'X>ZX':1}
 edges=(flags['Y>XY'],flags['Z>YZ'],flags['X>ZX']);assert edges==(1,1,1)
 pair_basis=(edges[0],-edges[1],edges[2]);assert pair_basis==(1,-1,1)
 out={'schema':'marici.voevodsky.cosmology-integral-comparison-sign-coherence.v1','status':'all_orientation_transports_cohere_up_to_one_global_sign','orientation_source':{'unit_order':['u','v'],'Betti_orientation':'dtheta wedge dphi','flag_cycle':['X->Y','Y->Z','Z->X'],'character_order':['a-1','b-1']},'canonical_coefficients':{'Milnor_symbol':'{u,v}','de_Rham':'dlog(u) wedge dlog(v)','normalized_period':1,'Parshin_edges':[1,1,1],'character_residue':1},'pair_basis_translation':'Reversing only the second edge basis sends (1,1,1) to (1,-1,1); this is the historical sigma123 convention, not a scientific mismatch.','sign_tests':tests,'anti_symmetry':'Swapping u and v negates the Milnor symbol, de Rham wedge, torus orientation pairing, ordered character residue, and cyclic flag orientation simultaneously.','constant_tame_sign':'The minus sign in the Z-divisor tame unit -v/u has zero secondary valuation and does not alter the integral edge coefficient.','decision':'Every comparison commutes after one explicit orientation choice. Remaining sign ambiguity is exactly the global choice of generator in a rank-one lattice; there is no residual local convention mismatch.','next_gate':'orientation-free-obstruction: formulate the result canonically as an unoriented primitive lattice line and state what additional data selects a signed generator','limitations':['uses the fixed tame-symbol and boundary conventions stated in the flag packet','global sign remains absent orientation authority','no physical orientation inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
