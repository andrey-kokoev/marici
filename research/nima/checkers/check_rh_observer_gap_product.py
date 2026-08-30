import json
from fractions import Fraction
from pathlib import Path


rows = []
product = Fraction(1, 1)
for n in (1, 2, 3, 4, 8, 16, 64):
    product = Fraction(1, 1)
    for j in range(1, n + 1):
        rho = Fraction(1, j + 1)
        assert 0 <= rho < 1
        product *= 1 - rho
    assert product == Fraction(1, n + 1)
    rows.append({
        "cutoff": n,
        "margin_numerator": product.numerator,
        "margin_denominator": product.denominator,
    })

result = {
    "local_defect": "rho_j = 1/(j+1)",
    "every_local_gap_is_strict": True,
    "finite_product_formula": "1/(N+1)",
    "completed_margin": 0,
    "samples": rows,
    "conclusion": "strict finite gaps do not survive completion without summable logarithmic defect",
}

output = Path(__file__).parents[1] / "results" / "rh-observer-gap-product.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

