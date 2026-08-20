"""Integral lattice of the quadratic Kummer eigenline over Z[sqrt(2)]."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-quadratic-kummer-integral-lattice.json"

# Write a=m+n*r, r^2=2.  For alpha=(2+r)/2,
# a*alpha=(m+n)+(m/2+n)r.  This is integral iff m is even, i.e. iff
# a belongs to (r).  Multiplication by r on basis (1,r) is [[0,2],[1,0]].
def product_alpha(m, n):
    return (m + n, (m, 2 * n))  # second coordinate is (m+2n)/2

for m in range(-8, 9):
    for n in range(-8, 9):
        constant, (num, twice_n) = product_alpha(m, n)
        integral = (num + twice_n) % 2 == 0
        assert integral == (m % 2 == 0)
        # (r)*(a0+b0*r)=2*b0+a0*r has even constant coefficient.
        in_sqrt2_ideal = m % 2 == 0
        assert integral == in_sqrt2_ideal

mult_sqrt2 = [[0, 2], [1, 0]]
det = mult_sqrt2[0][0] * mult_sqrt2[1][1] - mult_sqrt2[0][1] * mult_sqrt2[1][0]
assert det == -2
smith = [1, 2]

packet = {
    "schema": "marici.benincasa.rank12_quadratic_kummer_integral_lattice.v1",
    "quadratic_field": "Q(sqrt(2))",
    "integer_ring": "Z[sqrt(2)]",
    "chosen_root": "s=-3+2*sqrt(2)",
    "source_generator": "k=(-(2+sqrt(2))/2,1,0,0)",
    "integrality_ideal": "(sqrt(2))",
    "primitive_integral_generator": "kappa=sqrt(2)*k=(-(1+sqrt(2)),sqrt(2),0,0)",
    "multiplication_by_sqrt2_matrix": mult_sqrt2,
    "smith_invariants_over_Z": smith,
    "lattice_quotient": "O_K*k / O_K*kappa = O_K/(sqrt(2)) = F_2",
    "monodromy_on_both_lattices": -1,
    "physical_activation_selected": False,
    "interpretation": "The source-normalized Kummer eigenline is an index-two enlargement of its primitive integral intersection lattice. This is intrinsic coefficient-lattice data, while the frozen regulator cone still selects no physical crossing class.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
