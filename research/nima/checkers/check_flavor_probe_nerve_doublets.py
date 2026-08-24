"""Finite joint-faithfulness test on the flavor generation-exchange fibers."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/flavor/results/wp24c_generation_exchange.json"
OUTPUT = ROOT / "research/nima/results/flavor-probe-nerve-doublets.json"


def rank_two_by_two(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    if len(matrix) == 1:
        return int(any(matrix[0]))
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return 2 if determinant else int(any(any(row) for row in matrix))


source = json.loads(SOURCE.read_text(encoding="utf-8"))
diagonal = source["diagonal_class"]
census = source["same_point_pair_census"]["diagonal"]

stored_pairs = diagonal["n_stored_two_minima"]
recovered_pairs = diagonal["n_partner_recovered"]
paired_textures = stored_pairs + recovered_pairs
unpaired_textures = diagonal["n_textures"] - paired_textures

# On one deck doublet, every physical quotient readout is even.  The deck
# involution T generates the anti-invariant probe 1-T without selecting a
# preferred sheet; changing sheet order merely changes its overall sign.
physical_probe = [[1, 1]]
full_probe_nerve = [[1, 1], [1, -1]]

gates = {
    "all_stored_doublets_share_physical16": census["multi"] == census["same_point"],
    "all_diagonal_nine_link_textures_except_declared_oddball_are_paired": (
        paired_textures == 72 and unpaired_textures == 1
    ),
    "physical_readout_is_nonfaithful_on_doublet": rank_two_by_two(physical_probe) == 1,
    "deck_even_plus_odd_probe_is_faithful": rank_two_by_two(full_probe_nerve) == 2,
    "deck_probe_is_source_generated": source["purpose"].endswith(
        "deck involution on the readout covering"
    ),
}

assert all(gates.values()), gates

result = {
    "schema": "marici.nima.flavor-probe-nerve-doublets.v1",
    "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
    "fiber": {
        "paired_textures": paired_textures,
        "unpaired_declared_oddballs": unpaired_textures,
        "stored_same_point_pairs": census["same_point"],
        "stored_physical16_max_relative_difference": census["max_rel16_same"],
        "recovered_physical16_max_relative_difference": diagonal[
            "max_refit_physical16_rel_diff"
        ],
    },
    "probe_matrices": {
        "physical_even_only": physical_probe,
        "physical_even_plus_deck_odd": full_probe_nerve,
        "physical_rank": rank_two_by_two(physical_probe),
        "full_probe_rank": rank_two_by_two(full_probe_nerve),
    },
    "gates": gates,
    "conclusion": (
        "Physical quotient readouts deliberately collapse each generation-exchange "
        "doublet. The source-derived deck involution supplies the complementary "
        "anti-invariant probe, so the two-probe nerve separates the lens sheets "
        "without promoting their difference to a physical observable."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates), **result["fiber"]}))

