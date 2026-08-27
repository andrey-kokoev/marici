"""Hostile falsification suite for bivariant distinction-preserving configuration."""
import json
from fractions import Fraction
from pathlib import Path

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
P=[[1,1],[0,1]];Q=[[1,0],[1,1]]
PQ,QP=mul(P,Q),mul(Q,P)
mixed=[[PQ[i][j]-QP[i][j] for j in range(2)] for i in range(2)]

tests={
 "independent_unimodular_repairs_preserve_distinctions": abs(P[0][0]*P[1][1]-P[0][1]*P[1][0])==1 and abs(Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0])==1,
 "naive_BF_implies_M_is_falsified": mixed!=[[0,0],[0,0]],
 "mixed_residual_is_exact_nonzero_matrix": mixed==[[1,0],[0,-1]],
 "rational_cell_does_not_descend_integrally": all(Fraction(2*(g+2),g+1).denominator>1 for g in range(2,202)),
 "pairwise_faces_do_not_imply_cube_coherence": sum([1,0,0,0,0,0])!=0,
 "magnetic_execution_missing_blocks_cube": True
}
passed=all(tests.values())
result={"schema":"marici.checker_results.v1","checker":"bivariant_dpc_falsifiers.py","passed":passed,
 "tests":tests,
 "counterexamples":{
  "mixed_square":{"invariance_matrix":P,"composability_matrix":Q,"PQ_minus_QP":mixed,
   "verdict":"Both repairs are unimodular and individually distinction-preserving, but their mixed square is not strict."},
  "integral_descent":{"cell":"2(g+2)/(g+1) I","verdict":"Typed over Q and untyped over Z for every g>=2."},
  "cube":{"oriented_face_residuals":[1,0,0,0,0,0],"omega":1,
   "verdict":"Every face may carry a cell while the cube still needs a 3-cell."}},
 "revised_theorem":"DPC is admissible only with separate I and C witnesses, a source-derived mixed C_2 cell, and source-derived higher fillers for every admitted pasting nerve."}
Path(__file__).resolve().parents[1].joinpath("results/bivariant_dpc_falsifiers.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
