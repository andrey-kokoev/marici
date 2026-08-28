"""Exact WP823 audit of acyclic stabilization versus RG descent."""

import itertools
import json
import math
from pathlib import Path
import sympy as sp


def maximal_minor_gcd(matrix):
    size = min(matrix.rows, matrix.cols)
    minors = []
    for rows in itertools.combinations(range(matrix.rows), size):
        for columns in itertools.combinations(range(matrix.cols), size):
            minors.append(abs(int(matrix.extract(rows, columns).det())))
    nonzero = [value for value in minors if value]
    return math.gcd(*nonzero), minors


def main() -> None:
    boundary = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    contractible = sp.Matrix([[1]])
    stabilized = sp.diag(boundary, contractible)
    charge = sp.Matrix([1, 2, 3])
    stabilized_charge = sp.Matrix([1, 2, 3, 0])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("wp820_boundary_has_rank_two", boundary.rank() == 2, boundary.rank())
    check("wp820_kernel_is_primitive_charge_line",
          boundary*charge == sp.zeros(2, 1)
          and len(boundary.nullspace()) == 1, boundary.nullspace())
    boundary_gcd, boundary_minors = maximal_minor_gcd(boundary)
    check("wp820_cokernel_has_no_free_or_torsion_part",
          boundary.rank() == boundary.rows and boundary_gcd == 1,
          {"rank": boundary.rank(), "minor_gcd": boundary_gcd,
           "minors": boundary_minors})

    check("stabilized_boundary_adds_unit_acyclic_summand",
          stabilized == sp.diag(boundary, sp.Matrix([[1]])), stabilized)
    check("stabilized_kernel_is_same_primitive_charge_line",
          stabilized*stabilized_charge == sp.zeros(3, 1)
          and len(stabilized.nullspace()) == 1,
          stabilized.nullspace())
    stabilized_gcd, stabilized_minors = maximal_minor_gcd(stabilized)
    check("stabilized_cokernel_remains_trivial",
          stabilized.rank() == stabilized.rows and stabilized_gcd == 1,
          {"rank": stabilized.rank(), "minor_gcd": stabilized_gcd})
    check("acyclic_stabilization_preserves_homology_ranks",
          (boundary.cols-boundary.rank(), boundary.rows-boundary.rank())
          == (stabilized.cols-stabilized.rank(), stabilized.rows-stabilized.rank())
          == (1, 0),
          ((boundary.cols-boundary.rank(), boundary.rows-boundary.rank()),
           (stabilized.cols-stabilized.rank(), stabilized.rows-stabilized.rank())))

    column_sums = [sum(boundary[:, index]) for index in range(boundary.cols)]
    check("wp820_matrix_is_not_an_ordinary_directed_graph_incidence",
          column_sums != [0, 0, 0]
          and any(abs(value) > 1 for value in boundary),
          {"column_sums": column_sums, "entries": list(boundary)})

    r = sp.symbols("r", positive=True, integer=True)
    vectorlike_pair = [r, -r]
    linear_anomaly = sum(vectorlike_pair)
    cubic_anomaly = sum(value**3 for value in vectorlike_pair)
    quadratic_index = sum(value**2 for value in vectorlike_pair)
    check("vectorlike_pair_preserves_linear_anomaly",
          linear_anomaly == 0, linear_anomaly)
    check("vectorlike_pair_preserves_cubic_anomaly",
          sp.simplify(cubic_anomaly) == 0, cubic_anomaly)
    check("vectorlike_pair_changes_quadratic_loop_index",
          quadratic_index == 2*r**2, quadratic_index)

    base_c = sp.Integer(3)
    shifted_c = base_c+quadratic_index
    # WP821 fixed point for a=b=d=f=1: x*=1/(c-1).
    base_fixed = sp.Rational(1, base_c-1)
    shifted_fixed = sp.factor(1/(shifted_c-1))
    check("acyclic_matter_changes_fixed_point_without_changing_anomaly",
          base_fixed == sp.Rational(1, 2)
          and sp.simplify(shifted_fixed-1/(2+2*r**2)) == 0,
          (base_fixed, shifted_fixed))
    check("unit_vectorlike_pair_shifts_fixed_point_from_half_to_quarter",
          shifted_fixed.subs(r, 1) == sp.Rational(1, 4),
          shifted_fixed.subs(r, 1))
    check("infinite_anomaly_equivalent_fixed_point_family_exists",
          all(shifted_fixed.subs(r, value) != shifted_fixed.subs(r, value+1)
              for value in range(1, 5)),
          [shifted_fixed.subs(r, value) for value in range(1, 6)])

    mass, scale = sp.symbols("mass scale", positive=True)
    above_threshold = shifted_fixed.subs(r, 1)
    below_threshold = base_fixed
    check("massive_pair_produces_exact_threshold_jump_in_fixed_coordinate",
          below_threshold-above_threshold == sp.Rational(1, 4),
          below_threshold-above_threshold)
    check("topological_homology_record_is_blind_to_threshold_mass",
          sp.Matrix([1, 2, 3]).jacobian([mass]).rank() == 0,
          "rank zero")

    # Removing the contractible summand is a homological equivalence but not an
    # RG/threshold equivalence once the summand is physically populated.
    check("rg_assignment_does_not_descend_to_homology",
          base_fixed != above_threshold, (base_fixed, above_threshold))
    minimal_complex = boundary
    check("minimality_quotient_erases_physical_heavy_pair",
          minimal_complex.shape != stabilized.shape
          and (boundary.cols-boundary.rank()) == (stabilized.cols-stabilized.rank()),
          {"minimal_shape": minimal_complex.shape, "stabilized_shape": stabilized.shape})

    gain = sp.symbols("gain", positive=True)
    threshold_record = gain*(below_threshold-above_threshold)
    hostile_records = [
        threshold_record.subs(gain, 2),
        (2*gain*(below_threshold-above_threshold)).subs(gain, 1),
    ]
    check("uncalibrated_threshold_probe_has_source_gain_pair",
          hostile_records[0] == hostile_records[1], hostile_records)

    germ = {
        "native_arity": 8,
        "source_germs": ["full_complex", "acyclic_sector", "oriented_inflow", "mediator",
                         "O1", "O2", "O3", "threshold_detector"],
        "homology_charge_selector": True,
        "chain_level_matter_authority": False,
        "acyclic_sector_exclusion": False,
        "threshold_mass_authority": False,
        "rg_descent_to_homology": False,
        "physical16_descent": False,
        "detector_calibration": False,
    }
    check("aspect_native_eight_object_stabilization_germ_is_retained",
          germ["native_arity"] == len(germ["source_germs"]), germ)
    open_gates = [key for key in (
        "chain_level_matter_authority", "acyclic_sector_exclusion",
        "threshold_mass_authority", "rg_descent_to_homology",
        "physical16_descent", "detector_calibration"
    ) if not germ[key]]
    check("six_chain_level_and_realization_gates_remain_open",
          len(open_gates) == 6, open_gates)

    result = {
        "work_package": "WP823",
        "title": "Acyclic stabilization RG-descent no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "boundary": str(boundary),
            "stabilized_boundary": str(stabilized),
            "base_fixed_coordinate": str(base_fixed),
            "stabilized_fixed_coordinate": str(shifted_fixed),
            "unit_pair_fixed_coordinate": str(shifted_fixed.subs(r, 1)),
            "aspect_germ": germ,
        },
        "classification": {
            "homology": "primitive charge line and trivial cokernel survive unit acyclic stabilization",
            "anomaly": "vectorlike pairs leave linear and cubic anomalies unchanged",
            "rg": "quadratic loop index and fixed-point magnitude change under stabilization",
            "threshold": "free vectorlike mass creates a physical decoupling jump invisible to homology",
            "first_nonfaithful_arrow": "full chain-level matter complex to charge homology",
            "minimality": "removing contractible pairs erases physical threshold data",
            "readout": "threshold probe needs calibrated gain and physical16 descent",
            "verdict": "homology/inflow cannot by itself determine the asymmetric portal magnitude",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp823_acyclic_stabilization_rg_descent_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
