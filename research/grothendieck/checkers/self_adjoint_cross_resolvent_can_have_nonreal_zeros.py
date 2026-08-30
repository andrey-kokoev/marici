import json
import sympy as sp


def main():
    z = sp.symbols("z")
    carrier = sp.diag(-1, 0, 1)
    source = sp.Matrix([1, -1, 1])
    observer = sp.Matrix([1, 1, 1])
    resolvent = (carrier - z * sp.eye(3)).inv()
    cross = sp.factor((observer.T * resolvent * source)[0])
    diagonal = sp.factor((source.T * resolvent * source)[0])
    cross_num = sp.together(cross).as_numer_denom()[0]
    diagonal_num = sp.together(diagonal).as_numer_denom()[0]
    checks = {
        "carrier_is_self_adjoint": carrier == carrier.conjugate().T,
        "source_and_observer_are_distinct_real_ports": source != observer,
        "cross_resolvent_has_nonreal_zeros": set(sp.solve(cross_num, z)) == {-sp.I, sp.I},
        "diagonal_resolvent_has_only_real_zeros": all(root.is_real for root in sp.solve(diagonal_num, z)),
    }
    result = {
        "schema": "marici.grothendieck.self-adjoint-cross-resolvent-nonreal-zero.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "cross_resolvent": str(cross),
        "diagonal_resolvent": str(diagonal),
        "interpretation": (
            "A self-adjoint carrier does not confine zeros of a cross-resolvent coefficient. "
            "The missing law must identify or positively couple the source and observation ports."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
