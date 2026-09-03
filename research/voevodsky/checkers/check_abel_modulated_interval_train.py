from __future__ import annotations
import json
import sympy as sp

def main():
    z=sp.symbols('z')
    a=sp.symbols('a0:6')
    partial=[sum(z**k for k in range(j+1)) for j in range(6)]
    direct=sum(a[j]*z**j for j in range(6))
    abel=a[5]*partial[5]+sum((a[j]-a[j+1])*partial[j] for j in range(5))
    assert sp.expand(direct-abel)==0
    # For |z|=1, z!=1, every geometric partial sum is <=2/|1-z|.
    result={"schema":"marici.voevodsky.abel-modulated-interval-train-check.v1",
            "status":"abel_factorization_verified","term_count":6,
            "bound":"abs(sum a_j z^j)<=min(N,2/abs(1-z))*(abs(a_last)+TV(a))",
            "quadratic_component_bound_used":False,
            "source_endpoint_variation_bounded":False,
            "transition_integral_certified":False,
            "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
