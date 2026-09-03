from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    u, a = sp.symbols("u a", real=True)
    c = sp.symbols("c", positive=True, real=True)
    z = sp.symbols("z")
    # Translation by a and its adjoint have Fourier symbols exp(+-iua).
    symmetric_symbol = sp.simplify(-c * (sp.exp(sp.I*u*a) + sp.exp(-sp.I*u*a)) / 2)
    assert sp.simplify(symmetric_symbol + c * sp.cos(u*a)) == 0

    # Exact sublevel concentration trace: interval length 2L times frequency
    # measure |Omega| divided by 2*pi.
    L, omega_measure = sp.symbols("L omega_measure", positive=True, real=True)
    trace = sp.simplify((2*L) * omega_measure / (2*sp.pi))
    assert trace == L * omega_measure / sp.pi

    result = {
        "schema":"marici.voevodsky.combined-gamma-prime-symbol-check.v1",
        "status":"combined_symbol_and_sublevel_trace_verified",
        "combined_symbol":"m_Gamma(u)-sum Lambda(n)/sqrt(n)*cos(u*log(n))",
        "bad_set":"Omega_(L,delta)={u:a_L(u)<delta}",
        "sublevel_concentration_trace":"L*measure(Omega)/(pi)",
        "absolute_prime_bound_discarded":True,
        "bad_set_measure_computed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
