"""High-precision audit of modular odd-jet cancellation across theta labels."""
import json
from decimal import Decimal as D, localcontext
from pathlib import Path


PI = D("3.141592653589793238462643383279502884197169399375105820974944592307816406286")


def next_polynomial(coefficients, p):
    """Apply P -> (p-2x)P+2x P' for d/dr of exp(pr-x)P(x)."""
    result = [D(0)] * (len(coefficients) + 1)
    for degree, coefficient in enumerate(coefficients):
        result[degree] += p * coefficient
        result[degree + 1] -= 2 * coefficient
        if degree:
            result[degree] += 2 * degree * coefficient
    return result


def evaluate(coefficients, x):
    value = D(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def exponential_jet(c, p, order):
    polynomial = [D(1)]
    for _ in range(order):
        polynomial = next_polynomial(polynomial, p)
    return (-c).exp() * evaluate(polynomial, c)


def labelled_phi_jet(label, order):
    c = PI * label * label
    return 4 * c * c * exponential_jet(c, D(9) / 2, order) - 6 * c * exponential_jet(c, D(5) / 2, order)


with localcontext() as context:
    context.prec = 70
    orders = [1, 3, 5, 7, 9]
    max_label = 20
    rows = []
    for order in orders:
        labelled = [labelled_phi_jet(label, order) for label in range(1, max_label + 1)]
        total = sum(labelled, D(0))
        rows.append({
            "order": order,
            "label_1_jet": str(labelled[0]),
            "label_2_jet": str(labelled[1]),
            "partial_sum_labels_1_to_20": str(total),
            "absolute_label_sum": str(sum((abs(value) for value in labelled), D(0))),
            "relative_cancellation": str(abs(total) / sum((abs(value) for value in labelled), D(0))),
        })
    phi_zero = sum((labelled_phi_jet(label, 0) for label in range(1, max_label + 1)), D(0))
    phi_second = sum((labelled_phi_jet(label, 2) for label in range(1, max_label + 1)), D(0))
    potential_second_at_zero = -phi_second / phi_zero

result = {
    "decimal_precision": 70,
    "max_label": 20,
    "odd_jet_rows": rows,
    "phi_at_zero_labels_1_to_20": str(phi_zero),
    "phi_second_at_zero_labels_1_to_20": str(phi_second),
    "potential_V_second_at_zero": str(potential_second_at_zero),
    "potential_V_second_at_zero_positive": potential_second_at_zero > 0,
    "derivative_recurrence": "P_next=(p-2x)P+2x*P_prime",
    "individual_label_jets_nonzero": True,
    "modular_zero_identity_assumed": False,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-labelled-boundary-jet-cancellation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(
            f"order={row['order']} label1={row['label_1_jet']} "
            f"label2={row['label_2_jet']} total={row['partial_sum_labels_1_to_20']} "
            f"relative={row['relative_cancellation']}"
        )
