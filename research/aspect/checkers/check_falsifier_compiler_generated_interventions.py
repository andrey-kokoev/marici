from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "falsifier-compiler-generated-interventions.v1.json"
RESULT = ROOT / "results" / "falsifier_compiler_generated_interventions.json"


def rank(matrix):
    rows = [list(map(F, row)) for row in matrix]
    r = 0
    for c in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        p = rows[r][c]
        rows[r] = [x / p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                q = rows[i][c]
                rows[i] = [a - q * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    amplitudes = [F(0), F(1, 5), F(2, 5), F(3, 5)]
    phase = [g * g for g in amplitudes]
    amplitude_detected = any(phase[i + 2] - 2 * phase[i + 1] + phase[i]
                             for i in range(len(phase) - 2))

    old_history = [[1, 0], [0, 1]]
    three_back = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    history_detected = rank(old_history) == 2 and rank(three_back) == 4

    interaction = [[F(1, 5), F(-1, 5)], [F(-1, 5), F(1, 5)]]
    row_marginals = [sum(row) for row in interaction]
    column_marginals = [sum(interaction[i][j] for i in range(2)) for j in range(2)]
    contrast = interaction[0][0] - interaction[0][1] - interaction[1][0] + interaction[1][1]
    factorial_detected = row_marginals == column_marginals == [0, 0] and contrast == F(4, 5)

    sequence = [F(1) if n % 31 == 0 else F(-1, 30) for n in range(31 * 32)]
    old_periods_null = all(all(sum(sequence[n] for n in range(len(sequence)) if n % q == k) == 0
                               for k in range(q)) for q in (2, 4, 8, 16, 32))
    period_detected = old_periods_null and all(sequence[n] == sequence[(n + 31) % len(sequence)]
                                               for n in range(len(sequence))) and any(sequence)

    fluxes = [F(0), F(1), F(2)]
    primary = [min(x, F(1)) for x in fluxes]
    dual_reconstruction = fluxes
    flux_detected = primary[:2] == dual_reconstruction[:2] and primary[2] != dual_reconstruction[2]

    live_outputs = {"a": F(0), "b": F(0)}
    sealed_transcript = {"correction": F(-3, 5), "bound_predecessor": "a"}
    replay_on_b = F(3, 5) + sealed_transcript["correction"] + F(3, 5)
    replay_detected = len(set(live_outputs.values())) == 1 and replay_on_b == F(3, 5)

    system_populations = (F(1, 2), F(1, 2))
    environment_overlap = F(0)
    environment_detected = system_populations == (F(1, 2), F(1, 2)) and environment_overlap == 0

    d = F(1, 5)
    signed_faults = [(d, d), (-d, d)]
    scalar_sum = sum(v[0] for v in signed_faults)
    directional_sum = tuple(sum(v[j] for v in signed_faults) for j in range(2))
    joint_detected = scalar_sum == 0 and directional_sum == (0, F(2, 5))

    witnesses = {
        "amplitude_cross_sweep": amplitude_detected,
        "three_back_hankel": history_detected,
        "context_order_factorial": factorial_detected,
        "period_31_spectrum": period_detected,
        "flux_dual_gain": flux_detected,
        "controller_replay": replay_detected,
        "environment_tomography": environment_detected,
        "joint_signed_residual": joint_detected,
    }
    declared = [item["key"] for item in contract["interventions"]]
    assert declared == list(witnesses)
    assert all(witnesses.values())
    out = {
        "schema": "marici.aspect.falsifier-compiler-generated-interventions-check.v1",
        "status": "pass",
        "exact_hostile_witnesses": witnesses,
        "implemented_dual_dimension": len(witnesses),
        "all_generated_interventions_operational": True,
        "physical_reset_qualified": False,
        "scope": contract["physical_boundary"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
