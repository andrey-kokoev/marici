#!/usr/bin/env python3
"""Exact resource selection among minimum faithful D(S3) Wilson families."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
WILSON = K / "results" / "s3-controlled-wilson-executability.json"
KICKBACK = K / "results" / "s3-coherent-wilson-phase-kickback.json"
OUT = K / "results" / "s3-faithful-family-resource-selection.json"


def mobius(values: list[int], qubits: int) -> dict[int, int]:
    result = {}
    for mask in range(1, 1 << qubits):
        coefficient = 0
        subset = mask
        while True:
            coefficient += (-1) ** (mask.bit_count() - subset.bit_count()) * values[subset]
            if subset == 0:
                break
            subset = (subset - 1) & mask
        if coefficient % 8:
            result[mask] = coefficient % 8
    reconstructed = [sum(c for mask, c in result.items() if value & mask == mask) % 8
                     for value in range(1 << qubits)]
    assert reconstructed == values
    return result


def term_cost(mask: int, coefficient: int) -> tuple[int, int]:
    degree = mask.bit_count()
    assert coefficient in {2, 4, 6}
    if degree == 1:
        return 0, 0
    if coefficient in {2, 6}:
        ladder = degree - 2
        return 14 * ladder + 3, ladder
    if degree == 2:
        return 0, 0
    ladder = degree - 3
    return 14 * ladder + 7, ladder


def compile_power(eigenvalues: list[int], power: int) -> dict:
    exact = [(2 * power * (value % 4)) % 8 for value in eigenvalues]
    controlled_values = [0] * 8 + exact
    coefficients = mobius(controlled_values, 4)
    terms = []
    total_t = 0
    total_work = 0
    peak = 0
    for mask, coefficient in sorted(coefficients.items()):
        t_count, work = term_cost(mask, coefficient)
        total_t += t_count
        total_work += work
        peak = max(peak, work)
        terms.append({"mask": mask, "coefficient_mod8": coefficient,
                      "T_count_upper_bound": t_count, "clean_work_blocks": work})
    return {"power": power, "T_count_upper_bound": total_t,
            "total_work_block_episodes": total_work,
            "peak_work_blocks": peak, "terms": terms}


def main() -> None:
    wilson = json.loads(WILSON.read_text(encoding="utf-8"))
    kickback = json.loads(KICKBACK.read_text(encoding="utf-8"))
    ports = {}
    for label, record in wilson["logical_normalizer_test"].items():
        powers = [compile_power(record["wilson_eigenvalues"], power) for power in (1, 2)]
        ports[label] = {
            "controlled_powers": powers,
            "mod4_phase_estimation_T_upper_bound": sum(item["T_count_upper_bound"] for item in powers),
            "total_work_block_episodes": sum(item["total_work_block_episodes"] for item in powers),
            "peak_work_blocks": max(item["peak_work_blocks"] for item in powers),
        }

    families = {}
    for family in sorted(kickback["exact_modular_phase_estimation"]["family_moduli"]):
        labels = list(family)
        work_data_supports = []
        for label in labels:
            for power in ports[label]["controlled_powers"]:
                for term in power["terms"]:
                    if term["clean_work_blocks"]:
                        # Bit 3 is that port's pointer control. Across ports
                        # those controls differ, so establish overlap using
                        # only the three shared sector-label data blocks.
                        work_data_supports.append({
                            bit for bit in range(3) if term["mask"] & (1 << bit)
                        })
        assert all(left & right for index, left in enumerate(work_data_supports)
                   for right in work_data_supports[index + 1:])
        total_t = sum(ports[label]["mod4_phase_estimation_T_upper_bound"] for label in labels)
        total_work = sum(ports[label]["total_work_block_episodes"] for label in labels)
        peak = max(ports[label]["peak_work_blocks"] for label in labels)
        families[family] = {
            "labels": labels,
            "T_count_upper_bound_for_controlled_powers_1_and_2": total_t,
            "total_work_block_episodes": total_work,
            "minimum_workspace": peak,
            "serial_hygiene_events": total_work - peak,
            "all_work_gadget_pairs_intersect_on_shared_sector_data": True,
            "workspace_hygiene_frontier": [
                {"verified_work_blocks": provisioned,
                 "minimum_hygiene_events": total_work - provisioned}
                for provisioned in range(peak, total_work + 1)
            ],
        }
    pareto = []
    for family, record in families.items():
        dominated = any(
            other != family
            and families[other]["T_count_upper_bound_for_controlled_powers_1_and_2"] <= record["T_count_upper_bound_for_controlled_powers_1_and_2"]
            and families[other]["total_work_block_episodes"] <= record["total_work_block_episodes"]
            and (families[other]["T_count_upper_bound_for_controlled_powers_1_and_2"] < record["T_count_upper_bound_for_controlled_powers_1_and_2"]
                 or families[other]["total_work_block_episodes"] < record["total_work_block_episodes"])
            for other in families
        )
        if not dominated:
            pareto.append(family)
    result = {
        "schema": "marici.kitaev.s3-faithful-family-resource-selection.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (WILSON, KICKBACK)
        },
        "cost_scope": "both controlled powers U and U^2 required by exact modulus-four phase estimation; pointer Fourier/readout and physical factory costs excluded",
        "ports": ports,
        "families": families,
        "pareto_optimal_families_by_T_upper_bound_and_work_episodes": pareto,
        "verdict": "Minimum faithful Wilson families are not resource-equivalent after compiling both controlled powers required for mod-four phase estimation. The reported Pareto set is exact for the declared phase-native upper-bound compiler, not a global circuit optimum or physical schedule.",
    }
    assert pareto == ["CDFG"]
    assert families["CDFG"]["T_count_upper_bound_for_controlled_powers_1_and_2"] == 361
    assert families["CDFG"]["total_work_block_episodes"] == 16
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
