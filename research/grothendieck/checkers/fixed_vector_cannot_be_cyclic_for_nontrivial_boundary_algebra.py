import json
import sympy as sp


def main():
    # A nontrivial representation with a common fixed vector.
    omega = sp.Matrix([1, 0, 0])
    generators = [sp.eye(3), sp.diag(1, -1, 1), sp.diag(1, 1, -1)]
    orbit = sp.Matrix.hstack(*(a * omega for a in generators))
    shift = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    transverse_orbit = sp.Matrix.hstack(omega, shift * omega, shift**2 * omega)
    checks = {
        "all_boundary_generators_fix_vacuum": all(a * omega == omega for a in generators),
        "boundary_representation_is_nontrivial": any(a != sp.eye(3) for a in generators),
        "cyclic_orbit_has_rank_one": orbit.rank() == 1,
        "fixed_vacuum_is_not_cyclic": orbit.rank() < 3,
        "noncommuting_transverse_shift_generates_full_module": transverse_orbit.rank() == 3,
        "transverse_shift_does_not_commute_with_stabilizer": shift * generators[1] != generators[1] * shift,
    }
    result = {
        "schema": "marici.grothendieck.fixed-vector-noncyclic-boundary-algebra.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "orbit_rank": orbit.rank(),
        "ambient_dimension": 3,
        "interpretation": (
            "A vector fixed by a nontrivial boundary algebra has a one-dimensional algebra orbit "
            "and cannot be cyclic for that representation. A noncommuting transverse Weyl action can generate the full module."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
