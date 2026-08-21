"""Propagate the certified quarter-point moments to Loewner contact curvature."""
import json
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).parents[1]
SOURCE = ROOT / "results" / "quarter-point-order-two-interval.json"
OUTPUT = ROOT / "results" / "quarter-point-loewner-diagonal-curvature.json"


def mul(x, y):
    products = [a * b for a in x for b in y]
    return min(products), max(products)


with localcontext() as context:
    context.prec = 90
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    moments = [tuple(map(Decimal, box)) for box in payload["moments_A0_through_A5"]]
    a0, a1, a2 = moments[:3]
    a0a2 = mul(a0, a2)
    a1sq = mul(a1, a1)
    hankel = (a0a2[0] - a1sq[1], a0a2[1] - a1sq[0])
    curvature = (Decimal(16) * hankel[0], Decimal(16) * hankel[1])

result = {
    "expansion": "D(c,c+delta)=16*(A0*A2-A1^2)*delta^2+O(delta^3), c=1/4",
    "first_hankel_determinant_interval": [str(x) for x in hankel],
    "loewner_diagonal_curvature_interval": [str(x) for x in curvature],
    "strictly_positive": curvature[0] > 0,
    "interval_certified": True,
    "zero_locations_used": False,
    "rh_proved": False,
}

assert result["strictly_positive"]

if __name__ == "__main__":
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
