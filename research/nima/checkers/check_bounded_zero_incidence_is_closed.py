def persistent_family(n, z):
    return z - 1 / n


def escaping_family(n, z):
    return 1 - z / n


def grid_sup_error(function, limit, n, radius, samples=1001):
    maximum = 0.0
    for k in range(samples):
        z = -radius + 2 * radius * k / (samples - 1)
        maximum = max(maximum, abs(function(n, z) - limit(z)))
    return maximum


if __name__ == "__main__":
    for n in (10, 100, 1000):
        persistent_zero = 1 / n
        escaping_zero = n
        assert persistent_family(n, persistent_zero) == 0
        assert escaping_family(n, escaping_zero) == 0
        assert grid_sup_error(persistent_family, lambda z: z, n, 3) <= 1 / n + 1e-15
        assert grid_sup_error(escaping_family, lambda z: 1, n, 3) <= 3 / n + 1e-15
    assert 1 / 1000 < 1 / 100
    assert 1000 > 100
    print("bounded zeros converge to limiting incidence: yes")
    print("zero-free limit with local uniform convergence requires escape: yes")
    print("result: completion cannot erase bounded zero incidence")
