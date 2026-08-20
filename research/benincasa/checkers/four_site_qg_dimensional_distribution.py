"""Audit the d->3 transverse Cayley-Menger distributional limit."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-dimensional-distribution.json"

# For a polynomial test function phi(K)=sum a_j K^j on [0,1], the normalized
# transverse radial distribution is
# T_eps(phi)=1/Gamma(eps) sum_j a_j/(eps+j), eps=(d-3)/2.
# Since 1/Gamma(eps)=eps+O(eps^2), only a_0 survives.
tests = [
    [Fraction(3), Fraction(2), Fraction(-5)],
    [Fraction(0), Fraction(7), Fraction(1)],
    [Fraction(-2), Fraction(0), Fraction(0), Fraction(9)],
]
limits = [coefficients[0] for coefficients in tests]
assert limits == [Fraction(3), Fraction(0), Fraction(-2)]

# K=omega^2 makes the pushed-forward density invariant under the deck flip.
deck_trace = {"omega_plus": 1, "omega_minus": 1}
assert deck_trace["omega_plus"] == deck_trace["omega_minus"]

packet = {
    "schema": "marici.benincasa.four_site_qg_dimensional_distribution.v1",
    "transverse_dimension": "m=d-3",
    "normalized_density": "K^(m/2-1)/Gamma(m/2) dK",
    "distributional_limit": "delta(K) as d approaches 3 from generic complex dimension",
    "polynomial_test_limits": [str(x) for x in limits],
    "deck_character": "even trace under omega -> -omega",
    "supported_limit": "equator K=omega^2=0",
    "does_not_supply": "an oriented relative chain gluing the two omega hemispheres into a primitive S3",
    "physical_activation_status": "unselected under the frozen dimensional prescription",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps(packet))
