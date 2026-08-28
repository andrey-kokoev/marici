"""Exact WP858 audit of the coherent return-port dark-ray selector."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    z = sp.symbols("z", nonzero=True)
    root2 = sp.sqrt(2)
    common_row = sp.Matrix([[1, z]])/root2
    dark = sp.Matrix([-z, 1])/root2
    link = sp.Matrix([[0, z], [1/z, 0]])
    shifted_row = sp.Matrix([[1, -z]])/root2
    shifted_dark = sp.Matrix([z, 1])/root2
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("common_return_port_has_rank_one", common_row.rank() == 1, common_row.rank())
    check("dark_ray_is_exact_common_port_kernel", common_row*dark == sp.zeros(1, 1),
          common_row*dark)
    check("dark_ray_has_equal_component_magnitudes_for_unit_phase",
          dark.subs(z, 1) == sp.Matrix([-1, 1])/root2, dark.subs(z, 1))
    check("boundary_link_has_fixed_unit_spectrum", link.charpoly().as_expr() == z**0*(sp.Symbol("lambda")**2-1),
          link.charpoly().as_expr())
    check("dark_ray_is_negative_boundary_link_eigenray", link*dark == -dark,
          link*dark)
    phase_gauge = sp.diag(1, sp.I)
    link_i = sp.simplify(phase_gauge*link.subs(z, 1)*phase_gauge.conjugate().T)
    dark_i = sp.Matrix([sp.I, 1])/root2
    check("port_rephasing_transports_link_and_dark_ray_covariantly",
          link_i == link.subs(z, -sp.I)
          and phase_gauge*dark.subs(z, 1) == sp.I*dark_i,
          {"link": link_i, "dark": phase_gauge*dark.subs(z, 1)})
    check("phase_shifted_common_port_selects_orthogonal_rival",
          shifted_row*shifted_dark == sp.zeros(1, 1)
          and sp.simplify((sp.Matrix([[-1/z, 1]])*shifted_dark)[0]/root2) == 0,
          shifted_dark)
    check("Hamiltonian_sign_reversal_exchanges_spectral_ordering",
          (-link)*dark == dark, (-link)*dark)
    p_minus, p_plus = sp.Rational(4, 5), sp.Rational(1, 5)
    thermal_purity = p_minus**2+p_plus**2
    thermal_coherence = (p_minus-p_plus)/2
    check("finite_temperature_hostile_is_mixed", thermal_purity == sp.Rational(17, 25),
          thermal_purity)
    check("finite_temperature_hostile_reduces_port_coherence",
          thermal_coherence == sp.Rational(3, 10)
          and thermal_coherence < sp.Rational(1, 2), thermal_coherence)

    result = {
        "work_package": "WP858",
        "title": "Coherent return-port dark-ray selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "two boundary amplitudes plus one retained coherent return-port phase",
        "selected_ray": "d_z=(-z,1)/sqrt(2)",
        "selector_mechanism": "kernel of normalized common-port row and negative eigenray of boundary link",
        "groupoid_change": "independent port phases -> stabilizer of retained return-port phase",
        "smallest_rivals": ["phase-shifted common junction M_-z", "Hamiltonian sign reversal -K_z",
                            "finite-temperature Gibbs completion"],
        "classification": "conditional relational parity/magnitude selector with a reusable phase reference",
        "remaining_gates": ["derive common junction and spectral ordering microscopically",
                            "identify relaxation with flavor RG", "isometric threshold transport",
                            "calibrated referenced physical16 instrument"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp858_coherent_return_port_dark_ray_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
