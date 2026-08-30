"""Smith classification of the seven Z/7-by-Z/7 extension laws."""
import json
import math
from pathlib import Path


classes = []
for t in range(7):
    # Relation matrix [[7, -t], [0, 7]].  For a full-rank 2x2 integer
    # presentation, d1 is the gcd of entries and d1*d2 is |det|.
    d1 = math.gcd(7, t)
    d2 = 49 // d1
    classes.append(
        {
            "extension_class": t,
            "smith": [d1, d2],
            "middle_group": "Z/7 + Z/7" if t == 0 else "Z/49",
            "split": t == 0,
            "exponent": d2,
        }
    )

tests = {
    "seven_labelled_extension_classes": len(classes) == 7,
    "zero_class_is_split": classes[0]["smith"] == [7, 7] and classes[0]["split"],
    "six_nonzero_classes_are_cyclic": all(
        row["smith"] == [1, 49] and not row["split"] for row in classes[1:]
    ),
    "cardinality_does_not_distinguish": all(
        row["smith"][0] * row["smith"][1] == 49 for row in classes
    ),
    "exponent_distinguishes_split_orbit": classes[0]["exponent"] == 7
    and all(row["exponent"] == 49 for row in classes[1:]),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_seven_extension_laws_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "classes": classes,
    "verdict": "the observable seven classifies endpoint-labelled gluing laws",
}

out = Path(__file__).resolve().parents[1] / "results" / "magnetic_seven_extension_laws_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
