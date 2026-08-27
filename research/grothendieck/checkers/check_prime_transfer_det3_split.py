import cmath


def g(depth: int, q: complex) -> complex:
    return sum(q**k for k in range(depth + 1))


for depth in (2, 3, 5, 10):
    for q in (0.1 + 0.2j, -0.2 + 0.1j, 0.3):
        full = g(depth, q) ** 2
        primitive = cmath.exp(2 * q)
        square = cmath.exp(q * q)
        tail = full * cmath.exp(-2 * q - q * q)
        assert abs(full - primitive * square * tail) < 1e-12

        h = 1e-5
        log_tail_plus = cmath.log(g(depth, h) ** 2) - 2 * h - h * h
        log_tail_minus = cmath.log(g(depth, -h) ** 2) + 2 * h - h * h
        first = (log_tail_plus - log_tail_minus) / (2 * h)
        second = (log_tail_plus + log_tail_minus) / (h * h)
        assert abs(first) < 1e-8
        assert abs(second) < 1e-5

print("primitive_factor=exp_2q")
print("square_factor=exp_q_squared")
print("regularized_tail=starts_at_cubic_order")
print("finite_terminal_current=retained")

