"""Decompose degree-one motivic cohomology of the split two-torus by torus weight."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_degree_one_torsion_corrector.json'
def main():
 # H^p(Gm^2,Z(q)) = sum_j binom(2,j) H^(p-j)(k,Z(q-j)).
 summands=[{'multiplicity':1,'group':'H^3(Q,Z(2))','torus_weight':0,'boundary_capable':False},{'multiplicity':2,'group':'H^2(Q,Z(1))=Pic(Q)=0','torus_weight':1,'boundary_capable':False},{'multiplicity':1,'group':'H^1(Q,Z(0))=0','torus_weight':2,'boundary_capable':False}]
 assert summands[1]['group'].endswith('=0') and summands[2]['group'].endswith('=0')
 torus_dependent_nonzero=any(s['torus_weight']>0 and not s['group'].endswith('=0') for s in summands);assert not torus_dependent_nonzero
 out={'schema':'marici.voevodsky.cosmology-degree-one-torsion-corrector.v1','status':'absolute_degree_one_group_has_no_torus_dependent_sign_corrector','degree_identification':'CH^2(U,1)=H_M^3(U,Z(2)) for U=(G_m)^2','split_motive_decomposition':summands,'survivor':'Only the pullback of H_M^3(Q,Z(2)) can remain. This statement does not require deciding its internal torsion.','boundary_gate':'Base-field pullbacks are unramified along X,Y,Z and have zero coordinate-divisor tame boundary. Therefore even an order-two base-field class cannot change the two residual sign coordinates of the horn target.','diagonal_disposition':'{u,u} and {v,v} are coordinate-dependent order-two classes in H_M^2, not H_M^3; shifting them into the precycle degree is inadmissible.','decision':'The absolute higher-Chow degree-one group contains no sourced torus-dependent torsion corrector. Any correction must come from a genuinely relative boundary-supported group, not from CH^2(U,1).','next_gate':'relative-boundary-torsion-source: compute the boundary-supported degree-one localization terms and test whether any sign corrector has zero additional residuals','limitations':['uses the standard split-motive decomposition of the algebraic two-torus','does not compute H_M^3(Q,Z(2)) itself','does not exclude new relative source pairs'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
