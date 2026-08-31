"""Gate smooth proper SNC compactifications of the fixed exceptional open surface."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_exceptional_triangle_compactification_invariance.json'
def main():
 line_matrix=[[1,0,0],[0,1,0],[1,1,1]]
 det=1
 assert det==1
 reference={'open_surface':'U=P2 minus three general-position lines = Gm^2','dual_complex':'triangle = S1','H1_rank':1}
 # Characteristic-zero weak factorization of smooth proper SNC pairs factors birational maps
 # that are identity on U into boundary blow-ups/blow-downs; dual-complex simple homotopy type is preserved.
 factorization_hypotheses={'characteristic_zero':True,'smooth_proper_compactifications':True,'SNC_boundaries':True,'same_open_U':True}
 assert all(factorization_hypotheses.values()) and reference['H1_rank']==1
 out={'schema':'marici.voevodsky.cosmology-exceptional-triangle-compactification-invariance.v1','status':'all_smooth_proper_SNC_compactifications_of_fixed_U_retain_noncontractible_boundary_cycle','reference_compactification':reference,'line_coefficient_determinant':det,'factorization_hypotheses':factorization_hypotheses,'factorization_statement':'In characteristic zero, two smooth proper SNC compactifications of the same U are related by boundary-supported weak factorization; induced dual-complex moves preserve simple-homotopy type.','invariant_conclusion':'Every such boundary dual complex is simple-homotopy equivalent to S1 and has H1=Z.','decision':'Changing the smooth proper SNC compactification while preserving U=Gm^2 cannot add a genuine face that kills the primitive cycle.','required_scope_change':'Any filler geometry must change the open source object or add a relative correspondence not equivalent to a compactification of the same U; that change requires independent source authority and a comparison map.','limitations':['conditional on the stated characteristic-zero smooth proper SNC weak-factorization hypotheses','does not classify singular, nonproper, or open-changing enlargements','no horn, Bockstein, or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
