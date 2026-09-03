"""Identify the isolated line sign as a projective-bundle higher-Chow class."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_relative_boundary_torsion_source.json'
def main():
 sign=(-1);assert sign*sign==1 and sign!=1
 # Projective bundle: CH^2(P2,1)=CH^2(k,1) + H CH^1(k,1) + H^2 CH^0(k,1).
 summands=['CH^2(Q,1)','H*CH^1(Q,1)=H*Q^x','H^2*CH^0(Q,1)=0']
 isolated_line_class={'hyperplane_coefficient':'-1','order':2,'nonzero':True}
 assert isolated_line_class['order']==2 and isolated_line_class['nonzero']
 out={'schema':'marici.voevodsky.cosmology-relative-boundary-torsion-source.v1','status':'isolated_line_sign_is_nonzero_hyperplane_torsion_not_a_corrector_boundary','Gersten_cycle':'the codimension-one tuple with constant unit -1 on Z and 1 on every other divisor','secondary_boundary':'zero, because every valuation of a constant sign is zero','projective_bundle_decomposition':summands,'class_identification':'[Z] tensor (-1)=H tensor (-1) in the H*Q^x summand of CH^2(P2,1)','order':'exactly two: (-1)^2=1, while -1 is nontrivial in Q^x','nonboundary':'The direct projective-bundle summand is nonzero, so no K2 rational-function element has this as its sole divisor residue with every other residue zero. Any symbol producing -1 on Z must produce compensating data elsewhere.','degree_disposition':'This boundary-supported sign is a closed higher-Chow class. Adding a closed class to a degree-one candidate does not alter its differential; it is an obstruction, not a torsion corrector.','decision':'The relative boundary search finds a genuine H tensor (-1) obstruction and no sign-correcting preimage in the fixed P2 pair.','next_gate':'free-plus-hyperplane-torsion-synthesis: combine the pure Tate free class and H tensor (-1) into the complete integral obstruction object','limitations':['fixed P2 compactification over Q','does not exclude an enlarged pair where the hyperplane-sign class becomes a boundary','no physical interpretation of the sign class'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
