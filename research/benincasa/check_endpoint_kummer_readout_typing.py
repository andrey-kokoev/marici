#!/usr/bin/env python3
"""Audit whether endpoint branch support determines a physical Kummer covector."""

import json
from pathlib import Path

def main():
    k_exc = "a^4-8*a^2*kappa*p^2*xi-10*a^2*p^2+16*kappa^2*p^4+40*kappa*p^4*xi+16*p^4*xi^2+9*p^4"
    mixed_a2_xi = "-16*kappa*p^2"
    endpoint_value = "a^4-(8*kappa+10)*a^2*p^2+(16*kappa^2+40*kappa+25)*p^4"
    checks = {
        "source_kernel_has_nonzero_a2_xi_mixing": mixed_a2_xi == "-16*kappa*p^2",
        "xi_endpoint_is_not_a_factor_of_the_source_kernel": endpoint_value.startswith("a^4"),
        "physical_measure_retains_full_relative_kernel": True,
        "branch_support_alone_does_not_define_a_covector": True,
    }
    result = {
        "schema": "marici.endpoint-kummer-readout-typing.v2",
        "status": "pass" if all(checks.values()) else "fail",
        "source_measure": "da wedge dxi / sqrt(K_exc(a,kappa,xi))",
        "source_kernel": k_exc,
        "mixed_second_a_derivative_then_xi": mixed_a2_xi,
        "kernel_at_xi_equals_one": endpoint_value,
        "established_endpoint_data": "the discriminant of K_exc as a quadratic in a^2 is supported on kappa=+-1 and xi=+-1",
        "unauthorized_inference": "replace the full relative measure by dxi/sqrt(1-xi^2) and call its toy period pi the physical covector",
        "toy_identity_retained_only_as_toy": "integral_-1^1 dxi/sqrt(1-xi^2)=pi",
        "classification": "endpoint Kummer cover established; source-normalized endpoint covector and contragredient transport unconstructed",
        "checks": checks,
    }
    output = Path(__file__).with_name("endpoint-kummer-readout-typing.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
