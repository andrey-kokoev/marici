from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = json.loads((ROOT / "research/nima/six-point-nmhv-triangulation-fixture.json").read_text(encoding="utf-8"))
RESULT = ROOT / "research/nima/results/six-point-nmhv-residue-naturality.json"


def facet_form_terms(n: int, removed: int):
    remaining = [i for i in range(n + 1) if i != removed]
    terms = {}
    for position, omitted in enumerate(remaining):
        wedge = tuple(i for i in remaining if i != omitted)
        denominator = wedge
        terms[(wedge, denominator)] = -1 if position % 2 else 1
    return terms


def residue_terms(n: int, facet: int, normal_last: bool):
    terms = {}
    for omitted in range(n + 1):
        if omitted == facet:
            continue
        differential_order = [i for i in range(n + 1) if i != omitted]
        position = differential_order.index(facet)
        crossings = (len(differential_order) - 1 - position) if normal_last else position
        sign = (-1 if omitted % 2 else 1) * (-1 if crossings % 2 else 1)
        wedge = tuple(i for i in differential_order if i != facet)
        denominator = wedge
        terms[(wedge, denominator)] = sign
    return terms


def scaled(terms, sign):
    return {key: sign * value for key, value in terms.items()}


def main():
    cells = [tuple(cell) for side in ("left", "right") for cell in FIXTURE["triangulations"][side]]
    incidence_checks = []
    hostile_failures = 0
    for cell in cells:
        for k, vertex in enumerate(cell):
            residue = residue_terms(4, k, normal_last=True)
            facet = facet_form_terms(4, k)
            expected = scaled(facet, -1 if k % 2 else 1)
            hostile = residue_terms(4, k, normal_last=False)
            passed = residue == expected
            hostile_rejected = hostile != expected
            hostile_failures += int(hostile_rejected)
            incidence_checks.append({
                "cell": "".join(map(str, cell)),
                "removed_vertex": vertex,
                "facet_position": k,
                "boundary_sign": -1 if k % 2 else 1,
                "residue_matches_oriented_facet": passed,
                "normal_first_convention_rejected": hostile_rejected
            })
    checks = {
        "all_30_residues_match_boundary_sign": all(item["residue_matches_oriented_facet"] for item in incidence_checks),
        "all_30_hostile_normal_first_conventions_rejected": hostile_failures == 30,
        "exactly_30_cell_facet_incidences": len(incidence_checks) == 30
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_residue_naturality.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "residue_convention": "Write the logarithmic normal d(alpha_k)/alpha_k last; the Poincare residue is its preceding coefficient.",
        "projective_form": "Omega_n=sum_i (-1)^i wedge_{j!=i} d(alpha_j) / product_{j!=i} alpha_j",
        "incidences": incidence_checks,
        "claim_boundary": "Universal barycentric-coordinate proof instantiated on all 30 fixture incidences. It proves canonical simplex residue naturality with the declared orientation; it does not extend the benchmark to non-simplicial cells or loops."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
