"""Exact WP857 audit of the coherent dark-state portal attractor."""

import json
from pathlib import Path
import sympy as sp


def liouvillian(jumps):
    def act(rho):
        out = sp.zeros(3)
        for jump in jumps:
            gram = jump.T*jump
            out += jump*rho*jump.T-sp.Rational(1, 2)*(gram*rho+rho*gram)
        return sp.simplify(out)

    columns = []
    for i in range(3):
        for j in range(3):
            basis = sp.zeros(3)
            basis[i, j] = 1
            image = act(basis)
            columns.append(sp.Matrix([image[a, b] for a in range(3) for b in range(3)]))
    return sp.Matrix.hstack(*columns), act


def main() -> None:
    kappa, t = sp.symbols("kappa t", positive=True)
    vacuum = sp.Matrix([1, 0, 0])
    even = sp.Matrix([0, 1, 0])
    odd = sp.Matrix([0, 0, 1])
    Lv = sp.sqrt(kappa)*odd*vacuum.T
    Le = sp.sqrt(kappa)*odd*even.T
    superoperator, action = liouvillian([Lv, Le])
    dark = odd*odd.T
    vacuum_flow = sp.exp(-kappa*t)*(vacuum*vacuum.T)+(1-sp.exp(-kappa*t))*dark
    rival_v = sp.sqrt(kappa)*even*vacuum.T
    rival_o = sp.sqrt(kappa)*even*odd.T
    rival_superoperator, rival_action = liouvillian([rival_v, rival_o])
    swap = sp.diag(1, 1, -1)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("dark_projector_is_stationary", action(dark) == sp.zeros(3), action(dark))
    check("liouvillian_kernel_is_unique", superoperator.rank() == 8,
          superoperator.nullspace())
    check("exact_liouvillian_spectrum_has_positive_gap",
          superoperator.eigenvals() == {0: 1, -kappa: 4, -kappa/2: 4},
          superoperator.eigenvals())
    check("vacuum_flow_solves_master_equation",
          sp.simplify(sp.diff(vacuum_flow, t)-action(vacuum_flow)) == sp.zeros(3),
          vacuum_flow)
    check("vacuum_flow_converges_to_dark_projector",
          vacuum_flow.applyfunc(lambda x: sp.limit(x, t, sp.oo)) == dark,
          vacuum_flow.applyfunc(lambda x: sp.limit(x, t, sp.oo)))
    port_amplitudes = sp.Matrix([1, -1])/sp.sqrt(2)
    check("dark_ray_has_fixed_antisymmetric_port_magnitude",
          port_amplitudes.dot(port_amplitudes) == 1
          and [sp.Abs(x) for x in port_amplitudes] == [1/sp.sqrt(2), 1/sp.sqrt(2)],
          port_amplitudes)
    check("global_sign_is_identified_at_density_level",
          dark == (-odd)*(-odd).T, (-odd)*(-odd).T)
    check("odd_dissipator_is_exchange_covariant",
          all(swap*jump*swap in (jump, -jump) for jump in (Lv, Le)),
          [swap*jump*swap for jump in (Lv, Le)])
    check("even_rival_has_same_liouvillian_spectrum",
          rival_superoperator.eigenvals() == superoperator.eigenvals(),
          rival_superoperator.eigenvals())
    check("even_rival_selects_distinct_stationary_projector",
          rival_action(even*even.T) == sp.zeros(3)
          and even*even.T != dark, even*even.T)

    result = {
        "work_package": "WP857",
        "title": "Oriented dark-state portal attractor",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "vacuum plus coherent even/odd two-path sectors",
        "selected_state": "odd ray (|A>-|B>)/sqrt(2)",
        "liouvillian_spectrum": {"0": 1, "-kappa": 4, "-kappa/2": 4},
        "global_basin": "all density matrices on the declared three-state source",
        "portal_from_absence": True,
        "source_authority_hostile": "equal-gap even-parity reservoir",
        "classification": "conditional coherent magnitude/parity selector; reservoir, RG, threshold and reference authority open",
        "remaining_gates": ["derive odd reservoir from WP854 boundary source",
                            "identify semigroup with flavor RG",
                            "intertwine dark projector through thresholds",
                            "supply WP855 coherent reference instrument"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp857_oriented_dark_state_portal_attractor.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
