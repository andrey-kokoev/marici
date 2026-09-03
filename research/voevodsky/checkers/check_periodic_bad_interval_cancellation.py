from __future__ import annotations
import json
import sympy as sp

def main():
    z=sp.symbols('z', complex=True)
    for N in range(1,9):
        direct=sum(z**j for j in range(N))
        closed=(1-z**N)/(1-z)
        assert sp.simplify(direct-closed)==0
    # Exact Fourier orthogonality for a periodic train: the squared geometric
    # sum has mean N, not N^2, over one dual period.
    theta=sp.symbols('theta', real=True)
    N=7
    S=sum(sp.exp(sp.I*j*theta) for j in range(N))
    mean=sp.integrate(sp.expand_complex(S*sp.conjugate(S)),(theta,0,2*sp.pi))/(2*sp.pi)
    assert sp.simplify(mean-N)==0
    result={"schema":"marici.voevodsky.periodic-bad-interval-cancellation-check.v1",
            "status":"dirichlet_kernel_cancellation_verified","interval_count":N,
            "pointwise_peak_squared":N*N,"period_mean_squared":N,
            "quadratic_component_envelope_sharp":False,
            "variable_width_error_bounded":False,"transition_trace_certified":False,
            "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
