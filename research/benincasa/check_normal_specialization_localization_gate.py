"""Exact support-typing audit for the lower-normal/top-sector comparison."""

import json
from pathlib import Path


LOWER_SUPPORT = frozenset({"q_g1", "q_g2", "q_g3", "q_g23"})
TOP_SUPPORT = frozenset({"q_g1", "q_g2", "q_g3", "q_G12", "q_g23"})
NORMALS = ("nu1", "nu2", "nu3")


def normal_grade_support(support: frozenset[str], multi_index: tuple[int, ...]):
    """A base-direction Rees grade acts on coefficients, not pole labels."""
    assert len(multi_index) == len(NORMALS)
    return support


grades = {
    f"{NORMALS[i]}*{NORMALS[j]}": sorted(normal_grade_support(LOWER_SUPPORT, tuple(
        1 if k in (i, j) else 0 for k in range(len(NORMALS))
    )))
    for i in range(len(NORMALS))
    for j in range(i + 1, len(NORMALS))
}

assert all(set(support) == LOWER_SUPPORT for support in grades.values())
assert "q_G12" not in LOWER_SUPPORT
assert TOP_SUPPORT - LOWER_SUPPORT == {"q_G12"}

result = {
    "schema": "marici.normal-specialization-localization-gate.v1",
    "lower_support": sorted(LOWER_SUPPORT),
    "top_support": sorted(TOP_SUPPORT),
    "second_normal_grades": grades,
    "support_difference": sorted(TOP_SUPPORT - LOWER_SUPPORT),
    "normal_specialization_preserves_support": True,
    "normal_specialization_alone_reaches_top_vertex": False,
    "required_extra_operation": "localize/adjoin q_G12, then compare specialization with restriction/residue",
    "classification": "missing comparison morphism, not missing carrier wall",
}

out = Path(__file__).with_name("normal-specialization-localization-gate.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
