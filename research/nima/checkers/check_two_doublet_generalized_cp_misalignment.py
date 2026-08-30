import json
from pathlib import Path


# Angles are measured in units of pi/4. The faithful D4 doublet has rotations
# t -> t + 2r and reflections t -> 2k - t modulo 8, with k=0,1,2,3.
ANGLES = tuple(range(8))
REFLECTIONS = tuple(range(4))


def fixed_by_reflection(angle, axis):
    return (2 * axis - angle) % 8 == angle


def common_reflections(pair):
    return tuple(k for k in REFLECTIONS if all(fixed_by_reflection(t, k) for t in pair))


# Opposite quartic anisotropy signs pin one doublet to even axes and the other
# to odd (diagonal) axes. Every resulting vacuum pair lacks common reflection.
opposite_sign_pairs = tuple((a, b) for a in ANGLES if a % 2 == 0
                            for b in ANGLES if b % 2 == 1)
assert len(opposite_sign_pairs) == 16
assert all(common_reflections(pair) == () for pair in opposite_sign_pairs)

# Same signs admit aligned vacua with a surviving generalized CP.
same_sign_pairs = tuple((a, b) for a in ANGLES if a % 2 == 0
                        for b in ANGLES if b % 2 == 0)
preserving_pairs = tuple(pair for pair in same_sign_pairs if common_reflections(pair))
assert preserving_pairs

# One doublet always has a reflection stabilizer, reproducing WP596 locally.
assert all(any(fixed_by_reflection(t, k) for k in REFLECTIONS) for t in ANGLES)

# Global D4 transformations preserve the relative parity, so the two sign
# sectors are not gauge-related by the admitted common action.
def rotate_pair(pair, r):
    return tuple((t + 2 * r) % 8 for t in pair)


def reflect_pair(pair, k):
    return tuple((2 * k - t) % 8 for t in pair)


orbit = {rotate_pair((0, 1), r) for r in range(4)} | {
    reflect_pair((0, 1), k) for k in REFLECTIONS
}
assert all((b - a) % 2 == 1 for a, b in orbit)
assert (0, 0) not in orbit

result = {
    "schema": "marici.nima.two-doublet-generalized-cp-misalignment.v1",
    "opposite_sign_vacuum_count": len(opposite_sign_pairs),
    "opposite_sign_vacua_without_common_reflection": len(opposite_sign_pairs),
    "same_sign_vacuum_count": len(same_sign_pairs),
    "same_sign_vacua_with_common_reflection": len(preserving_pairs),
    "single_doublet_always_has_reflection": True,
    "opposite_and_aligned_sectors_are_common_d4_gauge_related": False,
    "verdict": "Two D4 doublets with opposite source-fixed quartic anisotropy signs remove every common generalized-CP reflection, but D4 symmetry alone does not select the relative sign."
}

out = Path(__file__).parents[1] / "results" / "two-doublet-generalized-cp-misalignment.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
