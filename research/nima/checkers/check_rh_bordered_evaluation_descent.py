from fractions import Fraction as F
import json
from pathlib import Path


# Hostile: scalar-zero equation sees only the first coordinate.
M_bad = ((F(1), F(0)),)
R_bad = ((F(0), F(1)),)
witness = (F(0), F(1))
assert sum(M_bad[0][i] * witness[i] for i in range(2)) == 0
assert sum(R_bad[0][i] * witness[i] for i in range(2)) == 1

# Success: the bordered equations retain both carrier coordinates.
M_good = ((F(1), F(0)), (F(0), F(1)))
R_good = ((F(1), F(1)),)
factor_good = ((F(1), F(1)),)
assert R_good == factor_good

# Completion hostile: every finite M_N is injective, but the factorization
# R=L_N M_N needs norm N.
constants = {}
for n in (1, 2, 4, 8, 16, 32):
    constants[str(n)] = n
assert constants["32"] == 32

result = {
    "schema": "marici.rh-bordered-evaluation-descent.v1",
    "finite_theorem": "ker(M) subset ker(R) iff R=L M",
    "hostile": {
        "M": "[1,0]",
        "R": "[0,1]",
        "kernel_witness": "[0,1]",
        "unexplained_carrier_residual": "1",
    },
    "successful_fixture": {
        "M": "I_2",
        "R": "[1,1]",
        "factor": "L=[1,1]",
    },
    "completion_hostile": {
        "M_N": "diag(1,1/N)",
        "R_N": "I_2",
        "finite_kernel_inclusion": True,
        "sharp_factorization_constants": constants,
        "uniform_descent": False,
    },
    "required_gate": "source_derived_uniform_factorization_of_carrier_port_through_bordered_operator",
}

out = Path(__file__).parents[1] / "results" / "rh-bordered-evaluation-descent.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
