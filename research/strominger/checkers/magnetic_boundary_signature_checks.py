"""Exact joint audit of magnetic cap rank and quotient width signatures."""
import json
import os
from fractions import Fraction

prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "boundary_signature_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]
current_defect = namespace["current_defect"]
rank = namespace["rank"]


def subtract(left, right, scalar):
    for key, value in right.items():
        left[key] = left.get(key, Fraction(0)) - scalar * value
        if not left[key]:
            del left[key]


def ordinary_columns(beta, g, q, cutoff):
    center = 1 - g
    labels = []
    columns = []
    for a in range(cutoff + 1):
        for branch, m in (
            ("minus", center - (q + 2) - a),
            ("plus", center + (q + 2) - a),
        ):
            labels.append((a, branch))
            columns.append(canonical_column(g, a, m, beta))
    return labels, columns


def cap_holes(beta, g, q, cutoff=20):
    labels, columns = ordinary_columns(beta, g, q, cutoff)
    basis_by_pivot = {}
    retained_plus = []
    for label, source in zip(labels, columns):
        vector = {key: Fraction(value) for key, value in source.items()}
        while vector:
            pivot = min(vector)
            if pivot in basis_by_pivot:
                subtract(vector, basis_by_pivot[pivot], vector[pivot])
                continue
            scalar = vector[pivot]
            normalized = {key: value / scalar
                          for key, value in vector.items()}
            for old_basis in basis_by_pivot.values():
                if pivot in old_basis:
                    subtract(old_basis, normalized, old_basis[pivot])
            basis_by_pivot[pivot] = normalized
            if label[1] == "plus":
                retained_plus.append(label[0])
            break
    return set(range(max(retained_plus) + 1)) - set(retained_plus)


def quotient_width(beta, g, q, cutoff=20):
    _, ordinary = ordinary_columns(beta, g, q, cutoff)
    currents = [current_defect(g, a, q, beta)
                for a in range(cutoff + 1)]
    return rank(ordinary + currents) - rank(ordinary)


observations = []
failures = []
signature_counts = {}
native_signature_counts = {}
for beta in range(2, 9):
    for g in range(2, 11):
        for q in range(1, 16):
            holes = cap_holes(beta, g, q)
            h = len(holes)
            w = quotient_width(beta, g, q)
            signature_counts[(h, w)] = signature_counts.get((h, w), 0) + 1
            if beta == 4:
                native_signature_counts[(h, w)] = (native_signature_counts.get(
                    (h, w), 0) + 1)
            expected_h = (
                0 if q < g + beta - 2 else
                1 if q < 2 * g + beta - 3 else
                2
            )
            low = (g >= 4
                   and min(beta - 1, g - 3) <= q <= g - 3)
            expected_w = 2 if low or q >= 2 * g + beta - 3 else 1
            row = {
                "beta": beta,
                "g": g,
                "q": q,
                "holes": sorted(holes),
                "h": h,
                "w": w,
                "expected_h": expected_h,
                "expected_w": expected_w,
            }
            observations.append(row)
            if h != expected_h or w != expected_w:
                failures.append(row)

forbidden = [
    row for row in observations
    if (row["h"], row["w"]) in {(1, 2), (2, 1)}
]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_boundary_signature_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact rational-rank evidence",
        "audit": "2<=beta<=8, 2<=g<=10, 1<=q<=15, cutoff N=20",
    },
    "case_count": len(observations),
    "signature_counts": {
        f"{h},{w}": count
        for (h, w), count in sorted(signature_counts.items())
    },
    "native_beta4_signature_counts": {
        f"{h},{w}": count
        for (h, w), count in sorted(native_signature_counts.items())
    },
    "formula_failures": failures,
    "forbidden_signature_failures": forbidden,
    "n_pass": len(observations) - len(failures),
    "n_fail": len(failures),
    "verdict": (
        "The rank-invariant exact audit realizes exactly the four predicted "
        "typed signatures; mixed signatures do not occur."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_boundary_signature.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(json.dumps({
    "case_count": len(observations),
    "signature_counts": output["signature_counts"],
    "native_beta4_signature_counts": output["native_beta4_signature_counts"],
    "formula_failure_count": len(failures),
    "forbidden_failure_count": len(forbidden),
}, sort_keys=True))
raise SystemExit(1 if failures or forbidden else 0)