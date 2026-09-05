from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

import check_six_point_nmhv_ordering_relations as rel
from check_six_point_nmhv_all_gluon_color_dressing import component, dressed, prepare
from check_six_point_nmhv_universal_ddm_dressing import basis_orders

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-nmhv-multifixture-color-dressing.json"
FIXTURES=[
    [(2,17),(11,5),(23,31),(7,29),(37,13),(19,41)],
    [(3,23),(17,7),(29,43),(11,37),(47,19),(31,53)],
    [(5,31),(13,2),(41,17),(23,47),(7,37),(43,11)]
]


def main():
    basis16=basis_orders(1,6); basis26=basis_orders(2,6)
    orders=set(basis16+basis26)
    rows=[]
    for fixture_index,values in enumerate(FIXTURES):
        mus={i:tuple(map(sp.Integer,values[i-1])) for i in rel.LABELS}
        rel.TILDE=rel.derive_tilde(rel.LABELS,rel.LAM,mus)
        momentum_sum=[sp.expand(sum(rel.LAM[i][a]*rel.TILDE[i][d] for i in rel.LABELS)) for a in range(2) for d in range(2)]
        prepared={order:prepare(order) for order in orders}
        component_rows=[]
        for target in itertools.combinations(range(1,7),3):
            amps={order:component(prepared[order],target) for order in orders}
            left=dressed(basis16,amps); right=dressed(basis26,amps)
            residual_count=sum(sp.cancel(left.get(word,0)-right.get(word,0))!=0 for word in set(left)|set(right))
            finite=all(value not in (sp.nan,sp.zoo,sp.oo,-sp.oo) and not value.has(sp.zoo,sp.nan,sp.oo,-sp.oo) for value in amps.values())
            component_rows.append({"negative_helicity_legs":list(target),"basis_residual_word_count":residual_count,"all_partial_amplitudes_finite":finite})
        rows.append({
            "fixture_index":fixture_index,
            "momentum_conserved":all(value==0 for value in momentum_sum),
            "all_20_components_basis_independent":all(row["basis_residual_word_count"]==0 for row in component_rows),
            "all_960_partial_amplitude_values_finite":all(row["all_partial_amplitudes_finite"] for row in component_rows),
            "components":component_rows
        })
    assertions={
        "all_three_exact_fixtures_conserve_momentum":all(row["momentum_conserved"] for row in rows),
        "all_60_component_fixture_pairs_basis_independent":all(row["all_20_components_basis_independent"] for row in rows),
        "all_2880_ordered_partial_amplitude_evaluations_finite":all(row["all_960_partial_amplitude_values_finite"] for row in rows)
    }
    out={
        "schema":"marici.nima.six_point_nmhv_multifixture_color_dressing.result.v1",
        "status":"passed" if all(assertions.values()) else "failed",
        "assertions":assertions,
        "fixture_count":len(rows),
        "pure_gluon_component_count_per_fixture":20,
        "ddm_orderings_per_component":48,
        "fixtures":rows,
        "claim_boundary":"Three exact nonsingular rational fixtures verify DDM endpoint-basis independence for all 20 pure-gluon six-point NMHV helicity components. Finite samples do not prove a symbolic kinematic identity or cover non-gluon supermultiplet components."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed": raise SystemExit(1)

if __name__=="__main__": main()
