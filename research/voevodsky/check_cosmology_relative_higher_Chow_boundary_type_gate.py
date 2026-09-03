"""Audit the localization boundary type of the Milnor symbol against sigma123."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_relative_higher_Chow_boundary_type_gate.json'
def tame(ordu,ordv):
 # {u,v} -> (-1)^(ab) u^b/v^a; record residual monomial exponents (u,v).
 return (ordv,-ordu)
def main():
 divisors={'u=0':(1,0),'u=infinity':(-1,0),'v=0':(0,1),'v=infinity':(0,-1)}
 symbols={D:tame(*ab) for D,ab in divisors.items()}
 assert symbols=={'u=0':(0,-1),'u=infinity':(0,1),'v=0':(1,0),'v=infinity':(-1,0)}
 assert tuple(sum(x[i] for x in symbols.values()) for i in (0,1))==(0,0)
 # Deliberate invalid collapse: no homomorphism from both residual function fields to Z is specified.
 integer_triangle=(1,-1,1);assert len(integer_triangle)==3 and len(symbols)==4
 out={'schema':'marici.voevodsky.cosmology-relative-higher-Chow-boundary-type-gate.v1','status':'localization_boundary_is_K1_valued_not_sigma123','source_class':'{u,v} in the Milnor/higher-Chow model of G_m^2','tame_boundary_table':{D:{'u_exponent':a,'v_exponent':b} for D,(a,b) in symbols.items()},'reciprocity_exponent_sum':[0,0],'target_mismatch':{'higher_Chow_boundary':'four divisor-indexed residual units in K1 of their function fields','sigma123':'three-edge integral incidence cycle with coefficients (1,-1,1)'},'comparison_gate':'Converting a residual unit to an integer requires an additional sourced valuation flag and orientation on each boundary divisor. No such flag comparison to the three exceptional edges is currently defined.','boundary_consequence':'A relative precycle cannot be claimed to have boundary (Xi_log,-sigma123) merely because its regulator has logarithmic residues. Its complete K1-valued tame boundary must first descend through a canonical flag map to the incidence complex.','deliberate_failure':'Counting signs or exponent sums without a declared secondary valuation erases the residual functions and changes a four-divisor boundary into an unrelated three-edge vector.','decision':'The naive relative higher-Chow route is type-blocked, not constructed. The next admissible test is a Parshin-flag/iterated-residue comparison with the exceptional triangle, including orientation and the fourth toric divisor.','limitations':['does not exclude a correctly flagged relative cycle','uses the standard toric compactification boundary census','no horn or Bockstein constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
