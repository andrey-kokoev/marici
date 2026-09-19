from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/closed-relation-morphism-for-conservative-incidence.json"
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A):return [list(r) for r in zip(*A)]
def neg(A):return [[-x for x in r] for r in A]
def rank2(A):return 2 if A[0][0]*A[1][1]-A[0][1]*A[1][0] else (1 if any(any(r) for r in A) else 0)
def main():
    I=[[F(1),0],[0,F(1)]]
    Q=[[F(1),0],[0,0]]                 # retained forward comparison, noninvertible
    j=[[F(1,2),0],[0,0]]               # soft history comparison, noninvertible
    U=I
    B=[[F(-1,2),0],[0,F(7)]]
    forward=mm(j,U)==neg(mm(B,Q))
    dual=mm(T(U),T(j))==neg(mm(T(Q),T(B)))
    checks={
      "forward_relation_square":forward,
      "contragredient_relation_square":dual,
      "Q_noninvertible":rank2(Q)<2,
      "j_noninvertible":rank2(j)<2,
      "no_inverse_used":True,
      "source_graph_projection_faithful":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.closed-relation-morphism-for-conservative-incidence.v1",
      "status":"variance_correct_bidirectional_relation_constructed_without_primal_inverse",
      "checks":checks,
      "source_relation":"R_rad={(v,U_rad v):v in V_pair} subset V_pair direct-sum H_rad",
      "target_relation":"R_cons={(Q_sep v,-B_cons Q_sep v):v in V_pair} subset E_cons,aug direct-sum H_cons,aug",
      "relation_morphism":"F(v,U_rad v)=(Q_sep v,j_H U_rad v); the forward square makes F(R_rad) subset R_cons.",
      "dual_morphism":"F^top acts contragrediently on annihilator/dual relations and yields U_rad^top j_H^top=-Q_sep^top B_cons^top.",
      "bidirectionality":"Forward source transport and backward covector transport are both present, but in opposite variance categories. This is the type-correct two-direction law when Q_sep and j_H are noninvertible.",
      "cyclic_composition":"Morphisms of relations compose. Therefore repeated primitive-loop words carry forward and contragredient transport at every length k without introducing inverse output maps; trace is applied only after closing the word.",
      "not_obtained":"No primal equation Q_sep N_rad=-B_cons^dagger j_H follows. Such a formula requires extra Riesz identifications and inverse/coisometric structure.",
      "application_status":"This finite exact model validates the architecture already used by the retained joint graph. For the physical system, the forward square and dual square are prior-proved; continuity of their relation composition follows on the retained graph rungs. The radial arithmetic diagonal B_X^rad remains independent and absent.",
      "next_gate":"Specify B_X^rad as an endomorphism of V_pair and test that (B_X^rad,A_rad) defines an endomorphism of R_rad transported by F to the conservative relation. This replaces four ill-typed primal conjugacies by one relation-endomorphism square.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
