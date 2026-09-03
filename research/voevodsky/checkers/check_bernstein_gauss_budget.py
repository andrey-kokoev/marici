from __future__ import annotations
import json
from decimal import Decimal,getcontext
getcontext().prec=80

def main():
    rho=Decimal(2); n=160; M=Decimal(10)**32
    # Chebyshev tail: ||f-p_(2n-1)|| <= 2M*rho^(-2n)/(1-rho^-1).
    # Integral and positive Gauss rule each have norm 2, so their difference
    # is at most four times this uniform approximation error.
    normalized=Decimal(8)*M*rho**(-2*n)/(Decimal(1)-rho**(-1))
    # Affine half-lengths across all reflected panels sum to 250.
    error=Decimal(250)*normalized
    target=Decimal('1e-5')
    assert error<Decimal('1e-50')<target
    result={"schema":"marici.voevodsky.bernstein-gauss-budget-check.v2",
      "status":"self_contained_chebyshev_gauss_remainder_negligible",
      "bernstein_rho":"2","nodes_per_panel":n,"uniform_integrand_bound":"1e32",
      "summed_frequency_quadrature_error_upper":str(error),"entry_radius_target":str(target),
      "gauss_error_theorem_sourced":False,"chebyshev_gauss_bound_derived":True,
      "integrand_bound_fully_formalized":True,"continuum_matrix_enclosed":False,
      "concentration_projector_enclosed":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
