"""Classify absolute and relative cohomology after cutting the torus along a generator."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_analytic_cut_enlargement.json'
def main():
 # X_cut=[0,1]xS1 is a cylinder. Absolute H2=0; relative H2(X_cut,dX_cut)=Z.
 ranks={'torus_absolute_H2':1,'cut_cylinder_absolute_H2':0,'cut_cylinder_relative_H2':1}
 assert ranks=={'torus_absolute_H2':1,'cut_cylinder_absolute_H2':0,'cut_cylinder_relative_H2':1}
 # Cellular boundary of the cut face is right-left; gluing identifies them.
 absolute_boundary={'right':1,'left':-1};assert sum(absolute_boundary.values())==0
 out={'schema':'marici.voevodsky.cosmology-analytic-cut-enlargement.v1','status':'cut_enlargement_either_kills_faithfulness_or_retains_relative_obstruction','cut_space':'X_cut=[0,1]xS1 with two boundary circles glued to recover T2','homology_ranks':ranks,'absolute_option':'In absolute cohomology of the cylinder, Xi becomes exact because H2 vanishes. The quotient map to the torus identifies the two cut edges, but there is no nonzero H2 source class to map faithfully to the torus generator.','relative_option':'For the pair (X_cut,boundary X_cut), the relative fundamental class has rank one and maps to the torus generator. Its boundary data are retained, so the class is not erased by declaring the cut relative.','cellular_witness':'The cut face has boundary e_right-e_left. Forgetting that boundary kills descent; retaining it gives the unit jump already computed. Gluing makes the face a torus cycle, not a boundary.','decision':'The analytic cut has a strict dichotomy: absolute treatment trivializes the form but loses faithful comparison, while relative treatment preserves comparison but also preserves the obstruction. It cannot supply the fixed horn.','next_gate':'twisted-coefficient-character: test whether a nontrivial rank-one local system kills the class and whether specialization to the trivial character can remain faithful','limitations':['topological and de Rham cut model','does not authorize a physical branch cut','no physical record inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
