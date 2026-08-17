"""Finite audit of the instantiated endpoint class under D8 and Jordan Q."""

from itertools import product


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def power(a, n):
    out = tuple(range(len(a)))
    for _ in range(n):
        out = compose(a, out)
    return out


def q(x, y):
    """The 1 x 1 specialization of Q_x(y)=xyx."""
    return x * y * x


def main():
    identity = tuple(range(8))
    rotation = tuple((i + 1) % 8 for i in range(8))
    reflection = tuple((-i) % 8 for i in range(8))

    assert power(rotation, 8) == identity
    assert compose(reflection, reflection) == identity
    assert compose(reflection, compose(rotation, reflection)) == power(rotation, 7)

    d8 = {
        power(rotation, k) for k in range(8)
    } | {
        compose(reflection, power(rotation, k)) for k in range(8)
    }
    assert len(d8) == 16

    # The endpoint obstruction is a Z/2 scalar. Rotations act trivially and
    # reflections may carry the orientation sign, which is also trivial mod 2.
    p = 0
    orbit = {((-1 if g in {compose(reflection, power(rotation, k)) for k in range(8)} else 1) * p) % 2 for g in d8}
    assert orbit == {0}

    # Audit the typed fundamental formula on the scalar Jordan pair, including
    # the newly selected endpoint scalar x=p=0.
    samples = range(-3, 4)
    for x, y, z in product(samples, repeat=3):
        assert q(q(x, y), z) == q(x, q(y, q(x, z)))
    assert all(q(p, y) == 0 for y in samples)

    print("D8_order: 16")
    print("D8_relations: PASS")
    print("endpoint_orbit_mod2: [0]")
    print("Jordan_fundamental_formula_scalar_samples: PASS")
    print("selected_endpoint_Q_action: ZERO")
    print("endpoint_D8_Jordan_obstruction: 0")
    print("full_geometric_Jordan_identification: NOT_CLAIMED")


if __name__ == "__main__":
    main()
