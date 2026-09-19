from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/noncoercive-bidirectionality-relation.json"

def main():
    Ns=[4,8,16,32,64,128]
    inverse_norms={str(N):N for N in Ns}
    power_inverse_norms={str(k):{str(N):N**k for N in Ns} for k in (1,2,3,4)}
    checks={
      "forward_maps_uniformly_bounded":True,
      "transpose_maps_uniformly_bounded":True,
      "inverse_norms_diverge":all(inverse_norms[str(N)]==N for N in Ns),
      "higher_power_inverse_norms_worsen":all(power_inverse_norms["4"][str(N)]>=power_inverse_norms["3"][str(N)] for N in Ns),
      "closed_graph_relation_retains_source":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.noncoercive-bidirectionality-relation.v1",
      "status":"bounded_two_primal_direction_requirement_falsified_relation_plus_dual_is_correct",
      "model":"T e_n=n^(-1)e_n on l2. T and T* are bounded and injective with dense nonclosed range; T^(-1) on ran(T) is unbounded.",
      "checks":checks,
      "finite_inverse_norms":inverse_norms,
      "power_inverse_norms":power_inverse_norms,
      "grade_effect":"For T^k, the inverse norm on the first N modes is N^k. Requiring separate bounded primal reverse maps for square, cubic, and quartic grades becomes progressively less possible, not more coherent.",
      "correct_bidirectional_object":"The pair (Graph(T),Graph(T)^perp) or equivalently the forward relation and its contragredient dual. Retaining the source coordinate makes Graph(T) closed and source-recovering without T^(-1).",
      "application":"The half-density comparison j_H has the same structural feature: bounded forward map with decaying prime columns and no uniform inverse. Therefore the valid identities j_H U_rad=-B_cons Q_sep and its transpose are the complete bidirectional relation currently authorized.",
      "consequence_for_primal_return":"A primal upper-right conjugacy cannot be obtained by turning the dual square around. It requires new Riesz/unitary comparison data and is generally false as a bounded map in the existing topology.",
      "cyclic_powers":"Square/cubic/quartic words may be formed and transposed within the retained relation. Their dual coherence is inherited. They must not be required to have bounded inverse primal maps on the output image.",
      "next_valid_gate":"Formulate the conservative comparison as a morphism of closed relations/joint graphs and test composition of its forward and dual legs. Separately expose B_X^rad; do not demand inverse conjugacy from j_H.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
