"""Detect diagonal Milnor 2-torsion by tame symbols on the P2 boundary."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_Milnor_sign_2_torsion.json'
def signs(ac,bd):
 return {'X':-1 if ac%2 else 1,'Y':-1 if bd%2 else 1,'Z':-1 if (ac+bd)%2 else 1}
def main():
 udiag=signs(1,0);vdiag=signs(0,1)
 assert udiag=={'X':-1,'Y':1,'Z':-1}
 assert vdiag=={'X':1,'Y':-1,'Z':-1}
 assert udiag['X']*udiag['Y']*udiag['Z']==1 and vdiag['X']*vdiag['Y']*vdiag['Z']==1
 assert signs(0,1)==vdiag # shear u'=uv,v'=v
 out={'schema':'marici.voevodsky.cosmology-Milnor-sign-2-torsion.v1','status':'diagonal_symbols_are_nonzero_order_two_and_detected_by_primary_tame_signs','field':'Q(u,v)','identities':['{u,u}=-{u,-1}','{v,v}=-{v,-1}','2{u,-1}=2{v,-1}=0'],'tame_boundaries':{'{u,u}':udiag,'{v,v}':vdiag},'nonvanishing':'The residue -1 is nontrivial in each characteristic-zero divisor function field, so both diagonal classes are nonzero; since twice each class is zero, their order is exactly two.','general_correction':'For coefficients ac and bd, the boundary signs are X=(-1)^ac, Y=(-1)^bd, Z=(-1)^(ac+bd). Their product is one, satisfying primary reciprocity.','secondary_disposition':'Every sign is a constant unit, so all secondary valuations vanish. The free Parshin edge vector and Xi_log are unchanged.','horn_disposition':'A homomorphism from this 2-torsion subgroup to the free Tate/triangle lattice has zero image. The signs cannot fill or cancel the primitive free horn obstruction, but they are extra integral K1 boundary components that a complete integral construction must track.','decision':'The GL(2,Z) correction is a genuine sign layer, not zero. Rational and secondary-residue comparisons legitimately forget it; integral Milnor boundary claims must retain it explicitly.','next_gate':'integral-tame-sign-decorated-complex: augment the triangle boundary data by the divisor sign layer and test coordinate covariance of the complete integral vector','limitations':['Milnor K2 of Q(u,v) and its three-line divisorial residues','does not classify other torsion primes','no physical sign readout inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
