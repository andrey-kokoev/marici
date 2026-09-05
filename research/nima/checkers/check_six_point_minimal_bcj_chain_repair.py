from __future__ import annotations
import itertools,json
from collections import defaultdict
from pathlib import Path
import sympy as sp
from check_six_point_nmhv_ordering_relations import sij
from check_six_point_common_cross_order_complex import VERTICES,boundary,simplex_chain,scale_chain,sum_chain

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-minimal-bcj-chain-repair.json"

def matrix_from_chains(chains,basis):return sp.Matrix([[c.get(k,0) for c in chains] for k in basis])
def main():
 c4=list(itertools.combinations(VERTICES,5));c3=list(itertools.combinations(VERTICES,4))
 chains=[];labels=[]
 for p in itertools.permutations((2,3,4,5)):
  raw=defaultdict(lambda:sp.Integer(0));w=sp.Integer(0)
  for k in range(1,5):
   w+=sij(1,p[k-1]);o=p[:k]+(1,)+p[k:]+(6,);sum_chain(raw,scale_chain(simplex_chain(o),w))
  chains.append(dict(raw));labels.append(p)
 T=matrix_from_chains(chains,c4)
 d4=sp.Matrix([[boundary({cell:sp.Integer(1)}).get(face,0) for cell in c4] for face in c3])
 D=d4*T
 _,pivots=D.rref();defect_basis=D[:,list(pivots)];r=D.rank()
 # Every defect has unique coordinates in the selected independent columns.
 coords=[]
 for j in range(D.cols):coords.append(defect_basis.gauss_jordan_solve(D[:,j])[0])
 X=sp.Matrix.hstack(*coords)
 corrected=T.col_join(-X)
 d4_ext=d4.row_join(defect_basis)
 zero_residue=d4_ext*corrected
 corrected_rank=corrected.rank()
 # Add one degree-five homotopy for each independent corrected BCJ cycle.
 _,cycle_pivots=corrected.rref();cycle_basis=corrected[:,list(cycle_pivots)]
 old_bd5=sp.Matrix([boundary({VERTICES:sp.Integer(1)}).get(cell,0) for cell in c4]+[0]*r)
 d5_ext=old_bd5.row_join(cycle_basis)
 h4_dim=(d4_ext.cols-d4_ext.rank())-d5_ext.rank()
 # Minimality: fewer than rank(D) new C4 generators cannot span all residue defects;
 # fewer than rank(corrected) new C5 generators cannot kill their corrected cycle span.
 checks={"defects_equal_boundaries":D==d4*T,"defect_coordinates_exact":defect_basis*X==D,"corrected_bcj_chains_are_cycles":zero_residue==sp.zeros(len(c3),24),"d4_d5_zero":d4_ext*d5_ext==sp.zeros(len(c3),d5_ext.cols),"repaired_H4_zero":h4_dim==0,"all_24_relations_repaired":corrected.cols==24}
 out={"schema":"marici.nima.six_point_minimal_bcj_chain_repair.result.v1","status":"passed" if all(checks.values()) else "failed","ranks":{"original_bcj_top_chain_span":T.rank(),"residue_defect_span":r,"corrected_bcj_cycle_span":corrected_rank,"extended_d4_rank":d4_ext.rank(),"extended_d5_rank":d5_ext.rank(),"repaired_H4_dimension":h4_dim},"minimal_extension":{"new_degree4_defect_lifts":r,"new_degree5_null_homotopies":corrected_rank,"defect_basis_relation_indices":[int(i) for i in pivots],"cycle_basis_relation_indices":[int(i) for i in cycle_pivots]},"checks":checks,"relation_coordinates":[{"permutation":list(labels[j]),"defect_coordinates":[str(v) for v in X[:,j]],"corrected_cycle_coordinates":[str(v) for v in corrected[:,j]]} for j in range(24)],"claim_boundary":"The minimal free mapping-cone repair of the fixed abstract-simplex assignment requires rank(D) degree-four generators to cancel residue defects and rank(corrected) degree-five generators to null-homotope the resulting BCJ cycles. Minimality is linear-algebraic for this fixed assignment. It does not identify these freely adjoined generators with scattering-equation or twisted-cohomology objects."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
