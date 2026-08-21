#!/usr/bin/env python3
"""Exact finite controls for selection-compatible multiplication maps."""

import json
import math
from pathlib import Path


N_MAX = 60
cyclic_checks = 0
cyclic_rows = []
for modulus in range(2, 31):
    compatible = []
    for n in range(1, N_MAX + 1):
        preserves_delta = all((n * x) % modulus != 0 for x in range(1, modulus))
        expected = math.gcd(n, modulus) == 1
        assert preserves_delta == expected
        if preserves_delta:
            compatible.append(n)
        cyclic_checks += modulus - 1
    cyclic_rows.append({
        "group": f"C{modulus}",
        "exponent": modulus,
        "compatible_n_through_60": compatible,
    })

# Product-group controls: exponent is lcm of cyclic factors.
product_groups = [(2, 2, 2, 2, 2), (2, 4), (3, 6), (4, 6), (5, 10, 20)]
product_checks = 0
product_rows = []
for factors in product_groups:
    exponent = math.lcm(*factors)
    compatible = []
    elements = []
    def build(prefix, index):
        if index == len(factors):
            elements.append(tuple(prefix))
            return
        for value in range(factors[index]):
            build(prefix + [value], index + 1)
    build([], 0)
    zero = tuple(0 for _ in factors)
    for n in range(1, N_MAX + 1):
        kernel_trivial = all(
            element == zero or tuple((n * x) % m for x, m in zip(element, factors)) != zero
            for element in elements
        )
        expected = math.gcd(n, exponent) == 1
        assert kernel_trivial == expected
        if kernel_trivial:
            compatible.append(n)
        product_checks += len(elements) - 1
    product_rows.append({
        "group": " x ".join(f"C{m}" for m in factors),
        "exponent": exponent,
        "compatible_n_through_60": compatible,
    })

# The compatible indices form a multiplicative monoid, but usually not an
# additive submonoid.  For exponent 2, odd+odd is the immediate obstruction.
monoid_checks = 0
for exponent in range(2, 31):
    units = [n for n in range(1, N_MAX + 1) if math.gcd(n, exponent) == 1]
    for a in units:
        for b in units:
            assert math.gcd(a * b, exponent) == 1
            monoid_checks += 1

result = {
    "schema": "marici.nima.prime_to_exponent_readout_operations.v1",
    "criterion": "[n]^* delta_0 = delta_0 iff gcd(n, exponent(G)) = 1",
    "n_max": N_MAX,
    "cyclic_groups": cyclic_rows,
    "product_groups": product_rows,
    "cyclic_kernel_checks": cyclic_checks,
    "product_kernel_checks": product_checks,
    "multiplicative_monoid_checks": monoid_checks,
    "closed_under_addition": False,
    "cosmology_C2_power5_survivors": "positive odd integers",
    "passed": True,
}
out = Path(__file__).with_name("results") / "prime-to-exponent-readout-operations.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "schema": result["schema"],
    "cyclic_kernel_checks": cyclic_checks,
    "product_kernel_checks": product_checks,
    "multiplicative_monoid_checks": monoid_checks,
    "criterion": result["criterion"],
    "passed": True,
}, indent=2))

