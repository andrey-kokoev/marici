import json
from fractions import Fraction
from pathlib import Path


def product(pair):
    return pair[0] * pair[1]


base = (Fraction(2), Fraction(1, 2))
rescalings = [
    (lam * base[0], base[1] / lam)
    for lam in (Fraction(1, 3), Fraction(2), Fraction(-1), Fraction(5, 2))
]
assert all(product(pair) == 1 for pair in rescalings)
assert len(set(rescalings)) == len(rescalings)

# Over the rationals, product one plus exact exchange leaves precisely two
# solutions among the bounded hostile search values.
candidates = [Fraction(n) for n in range(-5, 6)]
exchange_solutions = [k for k in candidates if k * k == 1]
assert exchange_solutions == [Fraction(-1), Fraction(1)]

# The positive-unit augmentation selects one of the two exchange solutions.
augmented_solutions = [k for k in exchange_solutions if k > 0]
assert augmented_solutions == [Fraction(1)]

# Independence witnesses.
product_without_exchange = (Fraction(2), Fraction(1, 2))
exchange_without_product = (Fraction(2), Fraction(2))
product_exchange_without_augmentation = (Fraction(-1), Fraction(-1))
assert product(product_without_exchange) == 1
assert product_without_exchange[0] != product_without_exchange[1]
assert exchange_without_product[0] == exchange_without_product[1]
assert product(exchange_without_product) != 1
assert product(product_exchange_without_augmentation) == 1
assert product_exchange_without_augmentation[0] == product_exchange_without_augmentation[1]
assert product_exchange_without_augmentation[0] < 0

result = {
    "schema": "marici.dual-boundary-exchange-augmentation.v1",
    "product_kernel": "anti-diagonal reciprocal rescaling",
    "after_exchange": [int(k) for k in exchange_solutions],
    "after_augmentation": [int(k) for k in augmented_solutions],
    "independence_witnesses": {
        "product_without_exchange": [str(x) for x in product_without_exchange],
        "exchange_without_product": [str(x) for x in exchange_without_product],
        "product_and_exchange_without_augmentation": [
            str(x) for x in product_exchange_without_augmentation
        ],
    },
    "verdict": "pairing, exchange, and augmentation are independent reconstruction gates",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "dual-boundary-exchange-augmentation.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
