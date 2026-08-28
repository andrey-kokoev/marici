"""Exact WP974 binary trace-word CP degree-gate checker."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def rotations(word):
    return {word[i:] + word[:i] for i in range(len(word))}

def reversal_equivalent(word):
    return word[::-1] in rotations(word)

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def trace(a):
    return sum(a[i][i] for i in range(3))

def evaluate(word, x, y):
    value = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for letter in word:
        value = mul(value, x if letter == "X" else y)
    return trace(value)

words_by_degree = {
    degree: tuple("".join(bits) for bits in itertools.product("XY", repeat=degree))
    for degree in range(1, 7)
}
asymmetric_by_degree = {
    degree: tuple(word for word in words if not reversal_equivalent(word))
    for degree, words in words_by_degree.items()
}

X = [[1, 0, 0], [0, 2, 0], [0, 0, 4]]
Y = [[0, 1, -1j], [1, 0, 1], [1j, 1, 0]]
Y_conjugate = [[entry.conjugate() for entry in row] for row in Y]
probe_word = "XXYXYY"
probe = evaluate(probe_word, X, Y)
probe_conjugate = evaluate(probe_word, X, Y_conjugate)

lower_words_agree = all(
    evaluate(word, X, Y) == evaluate(word, X, Y_conjugate)
    for degree in range(1, 6)
    for word in words_by_degree[degree]
)

checks = {
    "all_words_through_degree_five_are_reversal_equivalent": all(not asymmetric_by_degree[d] for d in range(1, 6)),
    "degree_six_has_reversal_asymmetric_words": bool(asymmetric_by_degree[6]),
    "chosen_probe_is_degree_six": len(probe_word) == 6,
    "chosen_probe_is_reversal_asymmetric": not reversal_equivalent(probe_word),
    "cp_conjugates_agree_on_all_words_through_degree_five": lower_words_agree,
    "degree_six_probe_is_not_real": probe.imag != 0,
    "degree_six_probe_changes_by_complex_conjugation": probe_conjugate == probe.conjugate() and probe_conjugate != probe,
}
if not all(checks.values()):
    raise SystemExit({"checks": checks, "probe": probe, "probe_conjugate": probe_conjugate})

result = {
    "schema": "marici.flavor.trace-word-cp-degree-gate.v1",
    "work_package": "WP974",
    "status": "PASS",
    "checks": checks,
    "domain": "two Hermitian coefficient fields with scalar trace-word source invariants",
    "quotient": "simultaneous source conjugation, then full weak-basis physical16",
    "first_reversal_asymmetric_degree": 6,
    "degree_six_asymmetric_word_count": len(asymmetric_by_degree[6]),
    "probe_word": probe_word,
    "probe_value": str(probe),
    "cp_conjugate_probe_value": str(probe_conjugate),
    "classification": "renormalizable trace potentials are CP-orientation blind",
    "remaining_gate": "independently derived degree-six orientation source or explicitly new relational groupoid",
}
out = ROOT / "results" / "wp974_trace_word_cp_degree_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
