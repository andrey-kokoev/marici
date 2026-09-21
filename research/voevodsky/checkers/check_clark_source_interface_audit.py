"""Exact packet/domain algebra; optionally replay upstream checks in a sandbox.

No positivity or completed operator-equivalence claim is tested here.
"""
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile

import sympy as sp


def exact_checks():
    C = sp.Matrix([[0, 0, -1, 1], [0, 0, -1, 1],
                   [-1, -1, 0, 0], [1, 1, 0, 0]]) / 2
    degree = (0, 0, 1, 1)
    # F[j,a,k] represents <f_j,G_a(z_k)>. Distinct symbols retain all
    # source/channel/spectral indices; c,d are independent packet weights.
    F = {(j, a, k): sp.Symbol(f"F_{j}_{a}_{k}")
         for j in range(2) for a in range(4) for k in range(2)}
    c = sp.symbols("c0:2")
    d = sp.symbols("d0:2")
    reservoir = sum(
        sp.conjugate(c[i]) * d[k] * C[a, b]
        * (F[degree[a], b, k] + sp.conjugate(F[degree[b], a, i]))
        for i in range(2) for k in range(2)
        for a in range(4) for b in range(4)
    )
    r_c = sum(c[k] * (F[0, 3, k] - F[0, 2, k]) for k in range(2))
    r_d = sum(d[k] * (F[0, 3, k] - F[0, 2, k]) for k in range(2))
    retained = sp.conjugate(sum(c)) * r_d + sp.conjugate(r_c) * sum(d)
    assert sp.expand(reservoir - retained) == 0
    # Dropping the coefficient-sum channels is not an identity.
    assert sp.expand(reservoir - (r_d + sp.conjugate(r_c))) != 0

    # Signed output kernel factorization, with ALL conjugations retained.
    Xz, Xw, Dz, Dw, z, wb = sp.symbols("Xz Xw Dz Dw z wb")
    numerator = (Xw - sp.I * Dw) * (Xz + sp.I * Dz) \
        - (Xw + sp.I * Dw) * (Xz - sp.I * Dz)
    divided = numerator / (-sp.I * (z - wb))
    pick_form = 2 * Xw * Xz * (-Dz / Xz + Dw / Xw) / (z - wb)
    assert sp.cancel(divided - pick_form) == 0

    # Matrix obstruction only: the upstream packet supplies its embedding
    # into the actual arithmetic history algebra.
    U = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
    a, b, c02, e, f, g = sp.symbols("a b c02 e f g", real=True)
    G = sp.Matrix([[a, b, c02], [b, e, f], [c02, f, g]])
    equations = list(U.T * G * U - G)
    solutions = sp.linsolve(equations, (a, b, c02, e, f, g))
    assert solutions == sp.FiniteSet((a, -e / 2, -e, e, 0, 0))
    invariant = sp.Matrix([[a, -e / 2, -e], [-e / 2, e, 0], [-e, 0, 0]])
    assert sp.expand(invariant.det()) == -e**3

    return {
        "polarized_packet_reservoir_with_coefficient_sums": True,
        "dropping_coefficient_sums_is_not_an_identity": True,
        "clark_to_pick_kernel_sign_and_factor": True,
        "terminal_jordan_real_symmetric_invariant_family": True,
        "terminal_invariant_determinant": "-e^3",
    }


def replay(filename):
    source = Path(__file__).resolve().parents[2] / "grothendieck" / "checkers" / filename
    text = source.read_text(encoding="utf-8")
    # Preserve the checker code; redirect only __file__-relative artifacts.
    # This avoids overwriting another research stream's evidence files.
    with tempfile.TemporaryDirectory(prefix="clark-audit-") as temporary:
        root = Path(temporary)
        (root / "checkers").mkdir()
        (root / "results").mkdir()
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            exec(compile(text, str(source), "exec"), {
                "__name__": "__main__",
                "__file__": str(root / "checkers" / filename),
            })
        artifacts = list((root / "results").glob("*.json"))
        assert len(artifacts) == 1
        result = json.loads(artifacts[0].read_text(encoding="utf-8"))
        assert result["passed"] is True
        return {
            "source": str(source.relative_to(Path(__file__).resolve().parents[3])).replace("\\", "/"),
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "artifact_redirected_only": True,
            "result": result,
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-existing", action="store_true")
    args = parser.parse_args()
    result = {
        "schema": "marici.voevodsky.clark-source-interface-audit.v1",
        "passed": True,
        "exact_checks": exact_checks(),
        "upstream_replays": [],
        "scope": "Packet algebra and optional prior regressions only. Analytic domain bounds and the Pick/RH implication are mathematical arguments in the accompanying note, not numerical certifications.",
    }
    if args.replay_existing:
        result["upstream_replays"] = [replay(name) for name in (
            "check_clark_polarized_forcing_sewing.py",
            "check_clark_arithmetic_green_crosswalk.py",
        )]
    destination = Path(__file__).resolve().parents[1] / "results" / "clark-source-interface-audit.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
