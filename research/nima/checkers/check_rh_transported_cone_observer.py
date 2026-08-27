import json
from pathlib import Path


U = ((1, 0), (0, -1))
x = (1, 1)
ell = (1, 1)


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def rowmat(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(2)) for j in range(2))


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


transported_state = matvec(U, x)
fixed_endpoint = dot(ell, transported_state)
transported_observer = rowmat(ell, U)  # U^{-1}=U
covariant_pairing = dot(transported_observer, transported_state)

assert transported_state == (1, -1)
assert fixed_endpoint == 0
assert transported_observer == (1, -1)
assert covariant_pairing == 2
assert dot(ell, x) == 2

result = {
    "schema": "marici.rh-transported-cone-observer.v1",
    "initial_cone_state": list(x),
    "phase_transport": "diag(1,-1)",
    "transported_state": list(transported_state),
    "fixed_evans_observer": list(ell),
    "fixed_endpoint_value": fixed_endpoint,
    "contragredient_observer": list(transported_observer),
    "covariant_pairing_value": covariant_pairing,
    "covariant_pairing_preserved": True,
    "fixed_endpoint_zero_reflection_preserved": False,
    "conclusion": "transporting_cone_and_observer_together_is_tautological",
}

out = Path(__file__).parents[1] / "results" / "rh-transported-cone-observer.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
