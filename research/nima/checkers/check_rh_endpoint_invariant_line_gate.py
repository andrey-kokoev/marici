from fractions import Fraction as F
import json
from pathlib import Path


A = ((F(0), F(0)), (F(1), F(0)))
ell = (F(0), F(1))


def state(z):
    return (F(1), z)


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def rowmat(row, matrix):
    return tuple(sum(row[i] * matrix[i][j] for i in range(2)) for j in range(2))


def readout(vector):
    return sum(ell[i] * vector[i] for i in range(2))


for z in (F(-1), F(0), F(2)):
    derivative = (F(0), F(1))
    assert matvec(A, state(z)) == derivative

ell_A = rowmat(ell, A)
assert ell_A == (F(1), F(0))
assert ell_A != ell
assert readout(state(F(0))) == 0
assert sum(ell_A[i] * state(F(0))[i] for i in range(2)) == 1

result = {
    "schema": "marici.rh-endpoint-invariant-line-gate.v1",
    "regular_state_connection": "v'=Av with A=[[0,0],[1,0]]",
    "parallel_state": "v(z)=(1,z)",
    "endpoint_covector": "ell=(0,1)",
    "scalar_readout": "f(z)=z",
    "offending_zero": "z=0",
    "state_nonzero_at_readout_zero": True,
    "dual_orbit": ["ell=(0,1)", "ell A=(1,0)"],
    "dual_invariant_line": False,
    "finite_residual_at_zero": "ell A v(0)=1",
    "required_gate": "ell'+ell A=a ell with regular a",
}

out = Path(__file__).parents[1] / "results" / "rh-endpoint-invariant-line-gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
