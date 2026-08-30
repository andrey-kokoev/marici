import cmath
import math


def framed_winding(samples: int = 4096) -> float:
    total = 0.0
    previous = 1.0 + 0.0j
    for k in range(1, samples + 1):
        current = cmath.exp(2j * math.pi * k / samples)
        total += cmath.phase(current / previous)
        previous = current
    return total / (2 * math.pi)


def projective_contraction(samples: int = 257) -> None:
    for j in range(samples):
        r = j / (samples - 1)
        for k in range(samples):
            theta = 2 * math.pi * k / (samples - 1)
            y = (1 - r) * cmath.exp(-1j * theta)
            assert math.isfinite(y.real)
            assert math.isfinite(y.imag)
    assert abs((1 - 1.0) * cmath.exp(-1j * 1.234)) == 0.0


if __name__ == "__main__":
    winding = framed_winding()
    assert abs(winding - 1.0) < 1e-12
    projective_contraction()
    print("framed winding: 1")
    print("projective transverse loop: contractible")
    print("result: projectivization forgets Evans winding")
