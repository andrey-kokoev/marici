import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
marici = root.parents[1]
records = [
    json.loads((marici / "research" / "benincasa" / "results" / name).read_text(encoding="utf-8"))
    for name in (
        "rank26-conductor-gamma-bockstein.json",
        "rank26-conductor-gamma-bockstein-p32003.json",
    )
]

# Choose the intrinsic splitting R = K + V, where K is the root-invisible
# relation line and V represents the visible one-dimensional quotient R/K.
# A candidate scalar-valued constructor is the row [a,b].
a = sp.symbols("a")
b, source_unit = sp.symbols("b source_unit", nonzero=True)
candidate = sp.Matrix([[a, b]])
invisible = sp.Matrix([1, 0])
visible = sp.Matrix([0, 1])

vanishing_equation = sp.Eq((candidate * invisible)[0], 0)
vanishing_solution = sp.solve(vanishing_equation, a)
projective_family = candidate.subs(a, 0)
normalized_solution = sp.solve(
    [sp.Eq((candidate * invisible)[0], 0), sp.Eq((candidate * visible)[0], source_unit)],
    [a, b],
    dict=True,
)

checks = {
    "both_source_records_pass": all(record["passed"] for record in records),
    "both_relation_spaces_have_dimension_two": all(record["relation_space_dimension"] == 2 for record in records),
    "both_bockstein_images_have_rank_one": all(record["bockstein_image_rank"] == 1 for record in records),
    "both_select_one_visible_and_one_invisible_relation": all(
        record["checks"]["root_visible_relation_has_nonzero_bockstein"]
        and record["checks"]["root_invisible_relation_has_zero_bockstein"]
        for record in records
    ),
    "annihilating_the_invisible_line_forces_a_zero": vanishing_solution == [0],
    "one_nonzero_scalar_remains": projective_family == sp.Matrix([[0, b]]),
    "source_unit_fixes_the_scalar_uniquely": normalized_solution == [{a: 0, b: source_unit}],
}

result = {
    "schema": "marici.aspect.gamma-bockstein-projective-uniqueness.v1",
    "status": "pass" if all(checks.values()) else "failure",
    "checks": checks,
    "forced_form": "beta(k,v)=lambda*v with lambda nonzero",
    "projective_verdict": "the constructor is forced up to one target-line scalar",
    "normalization_gate": "a source-declared normal coordinate and target generator must fix lambda before absolute uniqueness is claimed",
    "next_falsifier": "rescale the normal coordinate while preserving the relation kernel and image line; any claimed absolute explanation that does not record this transformation fails",
}

out = root / "results" / "gamma_bockstein_projective_uniqueness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
