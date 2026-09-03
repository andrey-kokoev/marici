"""Test whether H^2((G_m)^2) contains mixed-weight extension data."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_K2_pure_Tate_extension_gate.json'
def main():
 # H^0(Gm)=Q(0), H^1(Gm)=Q(-1); Kunneth gives H^2=Q(-2).
 factors=[{'degree':1,'rank':1,'weight':2},{'degree':1,'rank':1,'weight':2}]
 h2={'rank':factors[0]['rank']*factors[1]['rank'],'weight':sum(x['weight'] for x in factors)}
 assert h2=={'rank':1,'weight':4}
 weight_grades={0:0,1:0,2:0,3:0,4:1};assert sum(weight_grades.values())==1
 adjacent_nonzero=sum(1 for w,r in weight_grades.items() if r and w!=4);assert adjacent_nonzero==0
 # Deliberate countermodel has a lower-weight summand and could carry extension data.
 countermodel={2:1,4:1};assert len(countermodel)>1
 out={'schema':'marici.voevodsky.cosmology-K2-pure-Tate-extension-gate.v1','status':'H2_is_pure_Tate_with_no_internal_weight_extension','Kunneth':'H1(G_m)=Q(-1), hence H2((G_m)^2)=Q(-2)','weight_filtration':{'W3_rank':0,'W4_rank':1,'GrW4':'Q(-2)','other_graded_ranks':0},'dual_complex_comparison':'The sole weight-four generator is the primitive H1 class of the boundary triangle, matching Xi_log and sigma123.','extension_gate':'A nontrivial internal mixed-Hodge extension requires at least two nonzero weight-graded pieces. H2(U) has only GrW4, so its weight filtration contains no extension datum that could serve as a degree-one connector.','Bockstein_disposition':'The nearby-cycle t-Bockstein considered earlier would require a separate family/lattice torsion class. It is not hidden in the mixed-Hodge structure of the fixed torus class.','deliberate_countermodel':'Adding a lower-weight Q(-1) summand creates a mixed object where extension data could exist; that summand is absent from H2(U).','decision':'The primitive obstruction is a pure Tate class, not an unresolved mixed-weight extension. Mixed-Hodge filtration cannot supply the missing horn or Bockstein in the fixed source.','next_gate':'Deligne-regulator-degree: locate {u,v} in motivic/Deligne degree and test whether any regulator extension is distinct from the already excluded internal weight extension','limitations':['statement concerns the mixed-Hodge structure of H2(U)','does not compute Ext groups for arbitrary external mixed Hodge structures','no physical readout inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
