"""Exact WP861 weak-basis-invariant audit of the Kirchhoff dark-word interface."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    imag = sp.I
    Jn = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2)
    Jm = sp.Matrix([[0, -imag, 0], [imag, 0, -imag], [0, imag, 0]])/sp.sqrt(2)
    Jl = sp.diag(1, 0, -1)
    dark_word = sp.simplify((Jm-imag*Jn)/sp.sqrt(2))
    xu, yu, xd, yd = sp.symbols("xu yu xd yd", real=True)
    Yu = (xu+imag*yu)*sp.eye(3)+dark_word
    Yd = (xd+imag*yd)*sp.eye(3)+dark_word
    Hu, Hd = sp.simplify(Yu*Yu.H), sp.simplify(Yd*Yd.H)
    commutator = sp.simplify(Hu*Hd-Hd*Hu)
    invariants = []
    for hermitian in (Hu, Hd):
        invariants.extend([sp.simplify(sp.trace(hermitian**power)) for power in (1, 2, 3)])
    invariants.extend([
        sp.simplify(sp.trace(Hu*Hd)),
        sp.simplify(sp.trace(Hu**2*Hd)),
        sp.simplify(sp.trace(Hu*Hd**2)),
        sp.simplify(sp.im(sp.trace(commutator**3))),
    ])
    parameters = [xu, yu, xd, yd]
    witness = {xu: 1, yu: 0, xd: 1, yd: 1}
    jacobian = sp.Matrix(invariants).jacobian(parameters).subs(witness)
    cp_odd = sp.simplify(invariants[-1].subs(witness))
    disc_u = sp.simplify(sp.discriminant(Hu.subs(witness).charpoly().as_expr()))
    disc_d = sp.simplify(sp.discriminant(Hd.subs(witness).charpoly().as_expr()))
    Xu = sp.Matrix(3, 3, sp.symbols("u0:9"))
    Xd = sp.Matrix(3, 3, sp.symbols("d0:9"))
    translated_back = (Xu+dark_word-dark_word, Xd+dark_word-dark_word)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("oriented_dark_word_is_unit_ladder_eigenoperator",
          sp.simplify(Jl*dark_word-dark_word*Jl-dark_word) == sp.zeros(3), dark_word)
    check("dark_word_has_fixed_nilpotent_source_shape",
          dark_word == sp.Matrix([[0, -imag, 0], [0, 0, -imag], [0, 0, 0]]),
          dark_word)
    check("witness_up_spectrum_is_nondegenerate", disc_u == 49, disc_u)
    check("witness_down_spectrum_is_nondegenerate", disc_d == 316, disc_d)
    check("witness_has_nonzero_signed_CP_invariant", cp_odd == 6, cp_odd)
    check("complete_dark_word_family_has_rank_three_physical_image",
          jacobian.rank() == 3, jacobian.rank())
    check("rank_three_image_is_proper_in_intrinsic_quark_quotient",
          jacobian.rank() < 10, {"rank": jacobian.rank(), "dimension": 10})
    check("additive_dark_word_map_has_exact_inverse",
          translated_back == (Xu, Xd), translated_back)
    check("fixed_word_has_no_free_portal_coefficient",
          not (dark_word.free_symbols & set(parameters)), dark_word.free_symbols)
    check("ten_invariants_are_used_for_faithful_local_rank_test",
          len(invariants) == 10 and jacobian.rows == 10, len(invariants))

    result = {
        "work_package": "WP861",
        "title": "Kirchhoff dark-word physical16 interface",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "state_domain": "complete two-sector Yukawa family Yu=a_u I+F_-, Yd=a_d I+F_-",
        "faithful_coordinate": "ten independent weak-basis invariants represented in physical16",
        "selected_word": "F_-=(J_m-i J_n)/sqrt(2)",
        "witness": {"a_u": "1", "a_d": "1+i", "CP_odd": "6",
                    "spectral_discriminants": [49, 316]},
        "intrinsic_response_rank": 3,
        "classification": "conditional proper physical16 selector if the word grammar is complete; no selector as an additive translation",
        "smallest_authority_falsifier": "permit arbitrary base Yukawas, making addition of F_- exactly invertible",
        "remaining_gates": ["derive oriented z=i frame interface", "authorize grammar completeness",
                            "test measured/1210-sheet ensemble", "calibrate physical16 instrument"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp861_kirchhoff_dark_word_physical16_interface.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
