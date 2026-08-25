from fractions import Fraction


ORDER = 8


def mul(a, b):
    out = [Fraction(0) for _ in range(ORDER + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= ORDER:
                out[i + j] += ai * bj
    return out


def log_series(z):
    # z[0] must be one; log(z)=sum_{m>=1}(-1)^(m+1)(z-1)^m/m.
    u = z[:]
    u[0] -= 1
    power = [Fraction(1)] + [Fraction(0)] * ORDER
    out = [Fraction(0)] * (ORDER + 1)
    for m in range(1, ORDER + 1):
        power = mul(power, u)
        sign = 1 if m % 2 else -1
        for k in range(ORDER + 1):
            out[k] += sign * power[k] / m
    return out


honest = [Fraction(1)] * (ORDER + 1)  # 1/(1-x)
honest_log = log_series(honest)
assert honest_log[0] == 0
assert honest_log[1:] == [Fraction(1, k) for k in range(1, ORDER + 1)]

hostile = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (ORDER - 1)
assert hostile[1] < 0  # not a positive graded trace


def shift(label, n):
    return label * n


def defect(n):
    return {Fraction(1): 1, Fraction(n): -1}


def add_vectors(*vectors):
    out = {}
    for vector in vectors:
        for label, coefficient in vector.items():
            out[label] = out.get(label, 0) + coefficient
    return {label: c for label, c in out.items() if c}


def shifted(vector, n):
    return {shift(label, n): coefficient for label, coefficient in vector.items()}


d6_left = add_vectors(defect(2), shifted(defect(3), 2))
d6_right = add_vectors(defect(3), shifted(defect(2), 3))
assert d6_left == d6_right == defect(6)
assert sum(d6_left.values()) == 0  # endpoint augmentation vanishes

print(
    {
        "status": "passed",
        "ordinary_log_coefficients": [str(x) for x in honest_log[1:]],
        "negative_primitive_rejected": True,
        "mixed_path_relation": "d6=d2+S2(d3)=d3+S3(d2)",
        "endpoint_augmentation": 0,
        "disposition": "local_sign_fixed_completion_orientation_unfixed",
    }
)
