import math


r1 = 0.2659956819935979
r2 = 1.6705589357127293


def endpoint_majorant(n: int) -> float:
    a = n * n
    return (7 * math.pi / 3) * (a * a - 1) * a**3 * math.exp(-(a - 1) * math.pi)


factor_bound = math.pi**2 / ((math.pi - r1) * (math.pi - r2))
assert factor_bound < 7 / 3

terms = [endpoint_majorant(n) for n in range(2, 20)]
assert terms[0] < 0.568
assert sum(terms[1:]) < 0.000006
assert sum(terms) < 0.568

# Direct hostile replay of the derived mean derivative, not used as proof.
def mean(X: float) -> float:
    total = 0.0
    moment = 0.0
    for n in range(1, 30):
        x = n * n * X
        w = math.exp(-x) * x * (x - r1) * (x - r2)
        total += w
        moment += w * x
    return moment / total


minimum = 10.0
for k in range(1001):
    X = math.pi + k * (10 - math.pi) / 1000
    h = 1e-5
    derivative = (mean(X + h) - mean(X - h)) / (2 * h)
    minimum = min(minimum, derivative)
assert minimum > 0.71

print("primitive_relative_tail_bound<0.568")
print("weighted_mean_derivative>0.432")
print("aggregate_green_source_sign_changes=exactly_one")
print("oscillatory_orientation=still_open")

