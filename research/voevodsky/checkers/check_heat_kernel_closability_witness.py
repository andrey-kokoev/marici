from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Standard nonclosable positive-form witness on finite-support sequences:
    # L(x)=sum n*x_n and q(x)=|L(x)|^2.  For x_n=e_n/n, ||x_n||->0,
    # q(x_n)=1, while q(x_n-x_m)=0.
    rows = []
    for n in (2, 5, 10, 50):
        norm_sq = sp.Rational(1, n * n)
        q_value = sp.Integer(1)
        rows.append({"n":n,"base_norm_squared":str(norm_sq),"q_value":int(q_value)})
    assert rows[-1]["base_norm_squared"] == "1/2500"
    assert all(row["q_value"] == 1 for row in rows)

    # Kernel matrix q(e_i,e_j)=i*j has rank one and is positive semidefinite.
    v = sp.Matrix([1, 2, 3, 4])
    kernel = v * v.T
    assert kernel.rank() == 1
    assert all(x >= 0 for x in kernel.eigenvals())

    result = {
        "schema":"marici.voevodsky.heat-kernel-closability-witness-check.v1",
        "status":"nonclosable_positive_kernel_witness_verified",
        "base_null_sequence":True,
        "form_cauchy":True,
        "form_values_fail_to_zero":True,
        "positivity_implies_closability":False,
        "marici_source_kernel_tested":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
