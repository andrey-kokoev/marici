from fractions import Fraction as F


def gates(a, b, c):
    discriminant = b * b - 4 * a * (c - 2 * a)
    return {
        "hyperbolic": discriminant >= 0,
        "midpoint_above_left_wall": b <= 4 * a,
        "alternating_endpoint": c + 2 * a >= 2 * b,
    }


def interval_by_vertex_and_endpoints(a, b, c):
    discriminant = b * b - 4 * a * (c - 2 * a)
    if discriminant < 0:
        return False
    # Direct square-root-free tests for
    # (-b-sqrt(discriminant))/(2a) >= -2 and
    # (-b+sqrt(discriminant))/(2a) <= 2.
    left_margin = 4 * a - b
    right_margin = 4 * a + b
    lower_root_admitted = left_margin >= 0 and left_margin * left_margin >= discriminant
    upper_root_admitted = right_margin >= 0 and right_margin * right_margin >= discriminant
    return lower_root_admitted and upper_root_admitted


def main() -> None:
    checks = {}

    good = (F(1), F(2), F(2))
    checks["good_packet_passes_all"] = all(gates(*good).values())

    independent = {
        "hyperbolicity_only_failure": ((F(1), F(1), F(3)), "hyperbolic"),
        "midpoint_only_failure": ((F(1), F(5), F(8)), "midpoint_above_left_wall"),
        "endpoint_only_failure": ((F(1), F(4), F(0)), "alternating_endpoint"),
    }
    for name, (packet, failed_gate) in independent.items():
        result = gates(*packet)
        checks[name] = not result[failed_gate] and all(value for key, value in result.items() if key != failed_gate)

    hostile = (F(1), F(4), F(0))
    hostile_gates = gates(*hostile)
    checks["hostile_discriminant_is_24"] = hostile[1] ** 2 - 4 * hostile[0] * (hostile[2] - 2 * hostile[0]) == 24
    checks["hostile_midpoint_on_left_wall"] = hostile[1] == 4 * hostile[0]
    checks["hostile_q_minus_two_is_minus_six"] = hostile[2] + 2 * hostile[0] - 2 * hostile[1] == -6
    checks["hostile_fails_only_endpoint"] = [key for key, value in hostile_gates.items() if not value] == ["alternating_endpoint"]

    # Exhaust the first nonnegative coefficient census. The theorem's Boolean
    # characterization and the vertex/endpoint characterization must agree.
    census = 0
    for a in range(1, 9):
        for b in range(0, 13):
            for c in range(0, 13):
                theorem = all(gates(F(a), F(b), F(c)).values())
                geometric = interval_by_vertex_and_endpoints(F(a), F(b), F(c))
                checks[f"census_{census}"] = theorem == geometric
                census += 1
    checks["census_size"] = census == 1352

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed; coefficient_packets={census}")


if __name__ == "__main__":
    main()
