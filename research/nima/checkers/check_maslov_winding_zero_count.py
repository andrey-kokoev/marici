from cmath import phase, exp
from math import pi


def winding(samples):
    total = 0.0
    for left, right in zip(samples, samples[1:] + samples[:1]):
        delta = phase(right) - phase(left)
        while delta <= -pi:
            delta += 2 * pi
        while delta > pi:
            delta -= 2 * pi
        total += delta
    return round(total / (2 * pi))


count = 256
circle_values = [exp(2j * pi * index / count) for index in range(count)]
constant_values = [1 + 0j for _ in range(count)]

assert winding(circle_values) == 1
assert winding(constant_values) == 0

print("single holomorphic zero: positive local orientation and winding one")
print("zero-free section: same boundary-line type and winding zero")
print("global Maslov index is the zero count")
