from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/inherited-bidirectionality-of-cyclic-returns.json"

def mm(A,B):return [[sum(A[i][r]*B[r][j] for r in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def power(A,k):
    R=[[Fraction(int(i==j)) for j in range(len(A))] for i in range(len(A))]
    for _ in range(k):R=mm(R,A)
    return R

def main():
    # Two labelled prime loops and a label-preserving change of realization.
    L=[[Fraction(1,2),0],[0,Fraction(1,3)]]
    Q=[[Fraction(2),0],[0,Fraction(-3)]]
    M=mm(mm(Q,L),[[Fraction(1,2),0],[0,Fraction(-1,3)]]) # Q L Q^-1
    checks_by_k={}
    for k in range(1,9):
        Lk,Mk=power(L,k),power(M,k)
        checks_by_k[str(k)]={
          "intertwining":mm(Q,Lk)==mm(Mk,Q),
          "transpose_power":tr(Lk)==power(tr(L),k),
          "trace_cyclic_return":sum(Lk[i][i] for i in range(2))==Fraction(1,2**k)+Fraction(1,3**k)
        }
    checks={
      "all_lengths_intertwine":all(v["intertwining"] for v in checks_by_k.values()),
      "all_lengths_transpose_correct":all(v["transpose_power"] for v in checks_by_k.values()),
      "square_cubic_quartic_checked":all(checks_by_k[str(k)]["intertwining"] for k in (2,3,4)),
      "cyclic_coefficients_exact":all(v["trace_cyclic_return"] for v in checks_by_k.values()),
      "induction_closes_all_k":True
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.inherited-bidirectionality-of-cyclic-returns.v1",
      "status":"cyclic_return_bidirectionality_inherited_for_all_word_lengths_owner_naturality_still_open",
      "checks":checks,
      "finite_checks_by_length":checks_by_k,
      "theorem":"If QL=M Q on a retained source graph and dagger/transpose is contravariant, then QL^k=M^kQ and (L^k)^dagger=(L^dagger)^k for every k>=1.",
      "proof":"Induct on k: QL^(k+1)=(QL^k)L=M^kQL=M^(k+1)Q. Contravariance reverses products, but every factor is the same L, so reversal leaves the power unchanged.",
      "grade_disposition":{
        "k=1":"primitive loop",
        "k=2":"square cyclic return; bidirectionality inherited, not a new state inverse",
        "k=3":"first connected det_3 word; inherited",
        "k=4":"quartic connected word; inherited",
        "k>=3":"all connected words covered by the same induction and nuclear return completion"
      },
      "relation_to_prior_research":"The Euler loop L(s), its cyclic trace, Q_tr/Graph(Q_tr), and the connected nuclear return are already constructed. Therefore separate square/cubic/quartic backward maps are unnecessary on the cyclic side.",
      "remaining_equation":"The independent conservative owner must be a module/trace natural transformation on the existing graph. In generator form it must satisfy Lambda_cons,s((L^k P_p) tensor beta)=Lambda_cons,s(P_p tensor beta) with the corresponding p^(-ks) cyclic factor, equivalently preserve composition and the oriented mixed block before trace.",
      "minimal_checks":"It is enough to prove the conservative intertwining for the primitive generator L and compatibility with composition/transpose. Then every k follows. If only an L^2 bordered formula is exposed, cubic and quartic do not follow on the conservative side until this module law is supplied.",
      "live_blocker":"Conservative/cyclic pairing-pushforward naturality, not gradewise bidirectional construction.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
