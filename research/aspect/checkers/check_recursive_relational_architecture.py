from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "recursive_relational_architecture.json"


def bilinear(matrix, x, y):
    return sum(F(matrix[i][j]) * x[i] * y[j] for i in range(2) for j in range(2))


def descends_bilinear(matrix):
    e0, e1 = (F(1), F(0)), (F(0), F(1))
    # q keeps coordinate zero, so ker(q) is spanned by e1.
    left = [bilinear(matrix, e1, y) for y in (e0, e1)]
    right = [bilinear(matrix, x, e1) for x in (e0, e1)]
    return all(v == 0 for v in left + right), left, right


def tensor_descends(nonzero_entries, arity):
    # Each local quotient retains label 0 and kills label 1.
    offenders = []
    for index, value in nonzero_entries.items():
        if value != 0 and any(label == 1 for label in index):
            offenders.append({"index": "".join(map(str, index)), "value": str(value)})
    return not offenders, offenders


def main():
    good = ((1, 0), (0, 0))
    hyperbolic = ((0, 1), (1, 0))
    good_ok, good_left, good_right = descends_bilinear(good)
    bad_ok, bad_left, bad_right = descends_bilinear(hyperbolic)
    assert good_ok
    assert not bad_ok
    assert bad_left == [F(1), F(0)]
    assert bad_right == [F(1), F(0)]

    tri_good, tri_good_offenders = tensor_descends({(0, 0, 0): F(1)}, 3)
    tri_bad, tri_bad_offenders = tensor_descends({(1, 1, 1): F(1)}, 3)
    assert tri_good and not tri_good_offenders
    assert not tri_bad and tri_bad_offenders == [{"index": "111", "value": "1"}]

    out = {
        "schema": "marici.aspect.recursive-relational-architecture.v1",
        "status": "pass",
        "unit": "marked carrier germ with type, identity token, provenance interface, and an unconsumed comparison port; no temporal realization is primitive",
        "elementary_cell": "2+1: forward/backward witness pair plus its local mate",
        "grafting_rule": "form every relation that fails descent before consuming the corresponding comparison ports in local quotients",
        "realization_rule": "an event is produced only by a separate realization map from a carrier germ to an ordered record",
        "bilinear": {
            "descending_form": {"matrix": good, "descends": good_ok},
            "hyperbolic_form": {"matrix": hyperbolic, "descends": bad_ok,
                                "left_kernel_residuals": [str(x) for x in bad_left],
                                "right_kernel_residuals": [str(x) for x in bad_right]},
        },
        "three_sector": {
            "local_coordinate_tensor_descends": tri_good,
            "pure_relational_111_tensor_descends": tri_bad,
            "offenders": tri_bad_offenders,
        },
        "selection_rule": "for an n-ary target, test every local completion kernel in every argument; each nonzero contraction forces a relational mate before that quotient",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
