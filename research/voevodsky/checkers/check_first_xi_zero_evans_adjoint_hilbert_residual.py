"""High-precision scout for the unchanged Evans adjoint residual.

Requires mpmath. This is a numerical falsifier, not an interval proof.
"""
import mpmath as mp

mp.mp.dps = 40


def completed_xi(t):
    s = mp.mpf("0.5") + 1j * t
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.pi ** (-s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s, method="euler-mac")
    )


def even_hilbert_integral(t, cutoff):
    density = lambda x: abs(completed_xi(x)) ** 2

    def integrand(x):
        # At x=t the numerator has a quadratic zero, so this is removable.
        if abs(x - t) < mp.mpf("1e-25"):
            return mp.mpf("0")
        return density(x) * (2 * t) / (x * x - t * t)

    return mp.quad(integrand, [0, t - 1, t, t + 1, cutoff])


def main():
    t = mp.im(mp.zetazero(1))
    values = {cutoff: even_hilbert_integral(t, cutoff) for cutoff in (20, 30, 40, 50)}
    print("first ordinate:", mp.nstr(t, 35))
    print("root residual:", mp.nstr(abs(completed_xi(t)), 12))
    for cutoff, value in values.items():
        print(f"cutoff {cutoff}: {mp.nstr(value, 30)}")
    assert max(abs(values[50] - values[c]) for c in (30, 40)) < mp.mpf("1e-9")
    assert values[50] < mp.mpf("-0.15")


if __name__ == "__main__":
    main()
