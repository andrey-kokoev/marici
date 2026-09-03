"""Refine the horn target by its mod-two tame-sign layer and test cancellation."""
from __future__ import annotations
import json
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_integral_horn_target_refinement.json'
def add(x,y):return tuple((a+b)%2 for a,b in zip(x,y))
def main():
 base=(0,0,1) # -1 only on Z
 udiag=(1,0,1);vdiag=(0,1,1)
 span={add(tuple((p*a)%2 for a in udiag),tuple((q*a)%2 for a in vdiag)) for p,q in product((0,1),repeat=2)}
 assert span=={(0,0,0),(1,0,1),(0,1,1),(1,1,0)}
 assert base not in span and all(sum(x)%2==0 for x in span) and sum(base)%2==1
 out={'schema':'marici.voevodsky.cosmology-integral-horn-target-refinement.v1','status':'integral_target_has_odd_tame_sign_consistency_obstruction','refined_target':{'free_regulator_component':'Xi_log','free_secondary_component':'-sigma123, with fixed orientation','primary_sign_component':'epsilon_Z=(0,0,1) in (Z/2)^{X,Y,Z}','all_other_components':'zero'},'sign_convention':'A bit one denotes the constant unit -1. Since order two ignores sign reversal, the opposite-boundary convention leaves epsilon_Z unchanged.','triangle_supported_torsion_span':sorted([list(x) for x in span]),'parity_no_go':'Diagonal symbols and every {f,-1} with principal divisor supported only on X,Y,Z give even-parity sign vectors. epsilon_Z has odd parity, so it cannot be canceled without adding another divisor/sign component.','extra_divisor_gate':'An auxiliary divisor can restore even global parity only by creating an additional nonzero boundary component, violating the required zero residual unless a separately sourced cancellation is supplied.','free_layer':'The earlier nonexactness already blocks the free component. The mod-two sign layer is an additional integral consistency condition, linked to the free coefficient by parity rather than an independent direct summand.','decision':'The complete integral horn target is sign-decorated. Its free projection fails, while its sign projection constrains every integral lift. The rational target is recovered by forgetting epsilon_Z.','next_gate':'integral-obstruction-bigrading: combine the Z-valued primitive class and Z/2 sign parity into one minimal boundary invariant and audit functoriality','limitations':['torsion cancellation tested for corrections supported on the three-line boundary','does not exclude new divisors with a complete separately sourced cancellation complex','no physical sign interpretation inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
