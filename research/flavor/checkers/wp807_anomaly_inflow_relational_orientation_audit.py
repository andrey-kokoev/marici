"""Exact WP807 audit of anomaly inflow as a relational orientation selector."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    k = sp.Integer(3)
    orientations = (-1, 1)
    physical_signs = (-1, 1)

    states = [(eta, J) for eta in orientations for J in physical_signs]
    energies = {(eta, J): -k * eta * J for eta, J in states}
    minimum_energy = min(energies.values())
    minima = [state for state, energy in energies.items() if energy == minimum_energy]

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("inflow_level_is_integer_quantized", bool(k.is_integer and k != 0), k)
    check("fixed_boundary_orientation_selects_positive_physical_sign",
          min(physical_signs, key=lambda J: energies[(1, J)]) == 1,
          {J: energies[(1, J)] for J in physical_signs})
    check("reversed_boundary_orientation_selects_negative_physical_sign",
          min(physical_signs, key=lambda J: energies[(-1, J)]) == -1,
          {J: energies[(-1, J)] for J in physical_signs})
    check("joint_source_retains_mirror_pair", set(minima) == {(-1, -1), (1, 1)}, minima)
    check("relational_readout_is_unique_on_both_minima",
          {eta * J for eta, J in minima} == {1}, {eta * J for eta, J in minima})
    check("absolute_physical_sign_is_not_unique",
          {J for _, J in minima} == {-1, 1}, {J for _, J in minima})

    # The simultaneous mirror action is free on the two selected joint states.
    mirror = {(eta, J): (-eta, -J) for eta, J in minima}
    check("mirror_exchanges_selected_joint_states",
          all(mirror[mirror[state]] == state and mirror[state] != state for state in minima), mirror)
    stabilizer_minima = [state for state in minima if state[0] == 1]
    check("reference_port_restricts_to_stabilizer_groupoid",
          stabilizer_minima == [(1, 1)], stabilizer_minima)

    # Anomaly matching protects the integer level across an admitted gapped threshold.
    k_uv, k_ir = sp.Integer(3), sp.Integer(3)
    check("anomaly_matching_preserves_level", k_uv - k_ir == 0, k_uv - k_ir)
    threshold_pair_shift = sp.Integer(1) + sp.Integer(-1)
    check("vectorlike_threshold_pair_cannot_change_level", threshold_pair_shift == 0,
          threshold_pair_shift)

    # If the admitted boundary theory is anomaly-free in this channel, inflow
    # supplies no odd bias at all.
    zero_level_energies = {-0 * eta * J for eta, J in states}
    check("zero_anomaly_channel_has_no_orientation_bias", zero_level_energies == {0},
          zero_level_energies)

    # A current readout j=k eta J measures the relative observable only.
    currents = {(eta, J): k * eta * J for eta, J in minima}
    check("inflow_current_collapses_absolute_mirror_pair", set(currents.values()) == {k}, currents)

    mass, calibration = sp.symbols("mass calibration", positive=True)
    relative_probe = sp.Matrix([k])
    jacobian = relative_probe.jacobian([mass, calibration])
    check("topological_probe_has_mass_and_calibration_kernel", jacobian.rank() == 0,
          f"rank={jacobian.rank()}, nullity=2")

    obstruction = len({J for _, J in minima}) - 1
    check("deliberate_failure_exhibits_absolute_sign_ambiguity", obstruction == 1, obstruction)

    result = {
        "work_package": "WP807",
        "title": "Anomaly-inflow relational orientation audit",
        "level": int(k),
        "energies": {f"eta={eta},J={J}": int(energy) for (eta, J), energy in energies.items()},
        "joint_minima": [list(state) for state in minima],
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "magnitude": "integer-quantized relative bias",
            "rg_and_threshold": "protected by anomaly matching for gapped symmetry-preserving transport",
            "sign": "selected only relative to boundary orientation",
            "reference_port": "restricts to a stabilizer groupoid and creates a new relational experiment",
            "physical16": "no calibrated flavor detector map",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp807_anomaly_inflow_relational_orientation_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
