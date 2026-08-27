import json
from pathlib import Path


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


p_n = (1, 0, 0)
p_q = (0, 1, 0)
p_x = tuple(-a - b for a, b in zip(p_n, p_q))
assert tuple(a + b + c for a, b, c in zip(p_n, p_q, p_x)) == (0, 0, 0)
native_pseudoscalar = dot(p_n, cross(p_q, p_x))
assert native_pseudoscalar == 0

orientation_reference = (0, 0, 1)
signed_port = dot(orientation_reference, cross(p_n, p_q))
assert signed_port == 1
assert dot(tuple(-x for x in orientation_reference), cross(p_n, p_q)) == -signed_port


def tetrahedral_boundary(face_signs):
    if len(face_signs) != 4:
        return None
    value = 1
    for sign in face_signs:
        value *= sign
    return value


two_negative = tetrahedral_boundary((-1, -1, 1, 1))
one_negative = tetrahedral_boundary((-1, 1, 1, 1))
missing_face = tetrahedral_boundary((-1, -1, 1))
assert two_negative == 1
assert one_negative == -1
assert missing_face is None

result = {
    "schema": "marici.orientation-port-cocycle.v1",
    "native_three_momentum_pseudoscalar": native_pseudoscalar,
    "source_oriented_port_fixture": signed_port,
    "orientation_reversal_flips_port": True,
    "two_negative_faces_boundary": two_negative,
    "one_negative_face_boundary": one_negative,
    "missing_face_boundary": missing_face,
    "local_separation_implies_global_coherence": False,
    "claim_boundary": "local orientation breaking and global cocycle coherence are separate gates",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "orientation-port-cocycle.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
