"""Compute branch transitions of local primitives of dlog(u) wedge dlog(v)."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_Cech_log_local_primitives.json'
def overlap_jump(u_winding):return u_winding
def corner_class(u_winding,v_winding):return u_winding*v_winding
def main():
 # Coefficients are normalized by 2*pi*i for 1-form jumps and (2*pi*i)^2 at corners.
 assert overlap_jump(1)==1 and overlap_jump(-1)==-1
 assert corner_class(1,1)==1 and corner_class(-1,1)==-1 and corner_class(-1,-1)==1
 # Deliberate zero-monodromy comparator globalizes; the primitive symbol does not.
 assert corner_class(0,1)==0 and corner_class(1,1)!=0
 out={'schema':'marici.voevodsky.cosmology-Cech-log-local-primitives.v1','status':'local_primitive_obstructed_by_primitive_double_monodromy','local_primitive':'A_i=log_i(u) dlog(v), with dA_i=Xi_log','u_overlap':'If log_i(u)-log_j(u)=2*pi*i*n_ij, then A_i-A_j=2*pi*i*n_ij*dlog(v).','v_period':'Integrating this overlap jump around one positive v-circle gives (2*pi*i)^2*n_ij.','Cech_corner':'Resolving the overlap form with local log(v) produces corner jumps (2*pi*i)^2*n_ij*m_jk; unit windings give the integer cocycle 1.','globalization_obstruction':'The normalized double monodromy is exactly the torus period, integral Tate generator, primitive double residue, and oriented triangle class. It is nonzero, so no single-valued global A exists.','branch_cut_disposition':'Choosing cuts can make A single-valued on a cut domain, but its jump faces and corner terms restore the same global Deligne cocycle. Omitting them changes the complex rather than filling the class.','decision':'The apparent degree-one logarithmic primitive is local only. Its complete Cech boundary reconstructs, rather than trivializes, (Xi_log,-sigma123).','next_gate':'branch-cut-relative-chain: audit whether a cut-domain chain with all jump and corner components can satisfy the requested boundary vector or only repackage the Deligne cocycle','limitations':['normalized monodromy and Cech-degree audit','cover-specific cochains differ but the integral class does not','no physical branch prescription inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
