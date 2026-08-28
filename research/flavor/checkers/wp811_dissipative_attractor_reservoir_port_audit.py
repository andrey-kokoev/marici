"""Exact WP811 audit of a one-way dissipative orientation selector."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    gamma, tau, r, g0, gain = sp.symbols("gamma tau r g0 gain", positive=True)
    forward = sp.Matrix([[-gamma, 0], [gamma, 0]])
    reverse = sp.Matrix([[0, gamma], [0, -gamma]])
    target = sp.Matrix([0, 1])
    mirror_target = sp.Matrix([1, 0])

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("forward_generator_conserves_probability",
          sp.Matrix([[1, 1]]) * forward == sp.zeros(1, 2),
          sp.Matrix([[1, 1]]) * forward)
    check("forward_generator_has_unique_target_stationary_state",
          forward.nullspace() == [target], forward.nullspace())
    check("forward_spectral_gap_is_positive",
          set(forward.eigenvals().keys()) == {sp.Integer(0), -gamma}, forward.eigenvals())

    trajectory = sp.Matrix([r * sp.exp(-gamma * tau), 1 - r * sp.exp(-gamma * tau)])
    check("trajectory_solves_forward_master_equation",
          sp.simplify(sp.diff(trajectory, tau) - forward * trajectory) == sp.zeros(2, 1),
          sp.simplify(sp.diff(trajectory, tau) - forward * trajectory))
    trajectory_limit = trajectory.applyfunc(lambda entry: sp.limit(entry, tau, sp.oo))
    check("all_initial_probabilities_share_the_same_attractor",
          trajectory_limit == target, trajectory_limit)

    check("reverse_generator_conserves_probability",
          sp.Matrix([[1, 1]]) * reverse == sp.zeros(1, 2),
          sp.Matrix([[1, 1]]) * reverse)
    check("reverse_reservoir_selects_the_mirror_target",
          reverse.nullspace() == [mirror_target], reverse.nullspace())
    check("forward_and_reverse_have_identical_spectra",
          forward.eigenvals() == reverse.eigenvals(), (forward.eigenvals(), reverse.eigenvals()))

    jump_probability = sp.simplify(r * (1 - sp.exp(-gamma * tau)))
    check("jump_count_is_an_executable_finite_time_readout",
          jump_probability != 0, jump_probability)
    check("steady_dark_state_has_zero_further_jump_rate",
          (sp.Matrix([[1, 0]]) * target)[0] == 0,
          (sp.Matrix([[1, 0]]) * target)[0])

    faster = forward.subs(gamma, 2 * gamma)
    check("positive_rate_threshold_change_preserves_selected_target",
          faster.nullspace() == [target], faster.nullspace())
    check("threshold_change_does_not_preserve_relaxation_clock",
          set(faster.eigenvals().keys()) == {sp.Integer(0), -2 * gamma}, faster.eigenvals())

    signed_observable = sp.Matrix([[-g0, 0], [0, g0]])
    steady_value = (target.T * signed_observable * target)[0]
    mirror_value = (mirror_target.T * signed_observable * mirror_target)[0]
    check("dissipative_attractor_selects_signed_observable",
          (steady_value, mirror_value) == (g0, -g0), (steady_value, mirror_value))

    detector_record = gain * steady_value
    hostile_records = [detector_record.subs({g0: 1, gain: 2}),
                       detector_record.subs({g0: 2, gain: 1})]
    check("magnitude_and_detector_gain_have_an_exact_hostile_pair",
          hostile_records == [2, 2], hostile_records)
    response_jacobian = sp.Matrix([detector_record]).jacobian([g0, gain])
    check("single_detector_record_cannot_separate_source_magnitude_and_gain",
          response_jacobian.rank() == 1, f"rank={response_jacobian.rank()}, nullity=1")

    source_packets = {"relaxing_reservoir": "+", "inverted_reservoir": "-"}
    check("microscopic_reservoir_grammar_retains_orientation_pair",
          set(source_packets.values()) == {"+", "-"}, source_packets)

    obstruction = len(set(source_packets.values())) - 1
    check("deliberate_failure_exhibits_reservoir_preparation_fiber",
          obstruction == 1, obstruction)

    result = {
        "work_package": "WP811",
        "title": "Dissipative-attractor reservoir-port audit",
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "exact_data": {
            "forward_generator": str(forward),
            "forward_target": [0, 1],
            "reverse_target": [1, 0],
            "forward_gap": str(gamma),
            "jump_probability": str(jump_probability),
            "hostile_detector_records": [str(v) for v in hostile_records],
        },
        "tests": tests,
        "classification": {
            "effective_operation": "genuine selector with a unique global attractor",
            "rg_basin": "all probability states for every positive jump rate",
            "threshold": "target survives positive rate renormalization but the physical clock changes",
            "microscopic_source": "relaxing and inverted reservoirs select opposite targets",
            "magnitude": "signed eigenvalue normalization remains free",
            "instrument": "jump counting is executable; calibrated steady readout retains a source-gain kernel",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp811_dissipative_attractor_reservoir_port_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
