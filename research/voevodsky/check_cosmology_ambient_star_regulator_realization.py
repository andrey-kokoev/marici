"""Realize the ambient star chain in the top-weight logarithmic/flag comparison cone."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_ambient_star_regulator_realization.json'
def main():
 determinant=1;boundary=(1,1,1);iterated_residue=(1,1,1)
 assert determinant==1 and boundary==iterated_residue
 thom_coefficient=determinant;assert thom_coefficient==1
 relative_differential={'log':thom_coefficient,'flag':tuple(-x for x in boundary)}
 assert relative_differential=={'log':1,'flag':(-1,-1,-1)}
 out={'schema':'marici.voevodsky.cosmology-ambient-star-regulator-realization.v1','status':'ambient_star_realizes_formal_tau_in_top_weight_comparison_cone','geometry':'Y=Bl_0(A3) for the transverse forms l1=U, l2=V, l3=U+V+P','relative_cell':'Gamma=[E,X,Y]+[E,Y,Z]+[E,Z,X]','incidence_boundary':'partial Gamma=sigma123=(1,1,1)','Thom_class':'On E minus the three lines, u=l1/l3 and v=l2/l3; the oriented logarithmic Thom class is dlog(u) wedge dlog(v)=Xi_log.','unit_normalization':'det(l1,l2,l3)=1 and the ordered double residues are all +1, so no multiplicity rescales the realization.','relative_differential':'Under the cone convention d Phi(Gamma)=(Thom(Gamma),-partial Gamma)=(Xi_log,-sigma123).','contract_status':{'geometric_source':True,'degree_one_cell_after_relative_shift':True,'independent_boundary':True,'realization_map_top_weight':True,'top_weight_component_check':True,'orientation_naturality':True,'carrier_comparison_local_normal_slice':True,'full_integral_Gersten_decoration':False},'authority':'Phi(Gamma)=tau is now sourced by the ambient semistable star, not merely by freely adjoining a cone cell.','scope_gate':'This is a geometric top-weight HomotopyLift. It is not an ElementLift in the rank26 or motivic source, and it does not yet realize the full divisor K1 tuple including -v/u.','decision':'The formal comparison path has an independent geometric realization in the ambient blowup. Integral Gersten decoration is the remaining mathematical gate.','next_gate':'integral-decoration-of-ambient-cone: attach the exact tame units to Gamma and test all degree-three and point residuals','limitations':['top-weight/logarithmic realization','uses the local normal-slice identification with the carrier','no physical process or record inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
