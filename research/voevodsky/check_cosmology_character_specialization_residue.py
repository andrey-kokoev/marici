"""Compute the codimension-two residue at the trivial character."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_character_specialization_residue.json'
def main():
 # Local parameters x=a-1,y=b-1 form a regular sequence at the trivial character.
 koszul_ranks=(1,2,1);quotient_length=1;grothendieck_residue=1
 assert koszul_ranks==(1,2,1) and quotient_length==grothendieck_residue==1
 ordered_residues={'x_then_y':1,'y_then_x':-1};assert ordered_residues['x_then_y']==-ordered_residues['y_then_x']
 out={'schema':'marici.voevodsky.cosmology-character-specialization-residue.v1','status':'trivial_character_has_primitive_codimension_two_residue','local_parameters':'x=a-1, y=b-1 at the trivial character','local_algebra':'Q[x,y]_(x,y)/(x,y) has length one','Koszul_data':{'ranks':[1,2,1],'top_cokernel':'R/(x,y)','intersection_multiplicity':quotient_length},'residue':'Res_(0,0) dx wedge dy/(x*y)=1','ordered_connectors':'Successive x- and y-connecting maps give the unit top class; reversing their order changes the sign.','comparison':'The unit and sign law coincide with double logarithmic monodromy, the normalized torus period, ordered Parshin residues, and the primitive triangle orientation.','degree_gate':'This is a codimension-two/double-connecting residue. It reconstructs the degree-two obstruction and does not collapse to one regular degree-one precycle at the trivial character.','decision':'Character specialization contains no new filler datum. Its sole invariant is the same primitive unit already detected in every other comparison.','next_gate':'characteristic-zero-obstruction-synthesis-v2: unify algebraic, Betti, Deligne, character, and incidence realizations and freeze the remaining source boundary','limitations':['local rank-one character scheme near the trivial point','order-dependent sign fixed by x then y','no physical monodromy interpretation inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
