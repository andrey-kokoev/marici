"""Compare canonical reserve rates for atomic and continuous control measures."""

import math
import mpmath as mp


mp.mp.dps = 70
MAX_ORDER = 8
ATOM_COUNT = 80


def riemann_atoms():
    positions = []
    for index in range(1, ATOM_COUNT + 1):
        gamma = mp.im(mp.zetazero(index))
        positions.append(1 / (1 + 4 * gamma**2))
    weights = [4 * x for x in positions]
    return positions, weights


def normalize(weights):
    total = mp.fsum(weights)
    return [weight / total for weight in weights]


def atomic_moments(positions, weights):
    weights = normalize(weights)
    return [
        mp.fsum(weight * x**degree for x, weight in zip(positions, weights))
        for degree in range(2 * MAX_ORDER + 2)
    ]


def uniform_moments():
    return [1 / mp.mpf(degree + 1) for degree in range(2 * MAX_ORDER + 2)]


def cantor_moments(depth=14):
    positions = [mp.mpf(0)]
    for level in range(depth):
        scale = mp.mpf(3) ** (-(level + 1))
        positions = positions + [x + 2 * scale for x in positions]
    weights = [mp.mpf(1) for _ in positions]
    return atomic_moments(positions, weights)


def generalized_minimum(form, reference):
    chol = mp.cholesky(reference)
    inverse = chol**-1
    reduced = inverse * form * inverse.T
    values, vectors = mp.eigsy(reduced)
    # Convert the minimizing generalized vector back to monomial coefficients.
    coefficient = inverse.T * vectors[:, 0]
    return values[0], coefficient


def reserve_sequence(moments):
    rows = []
    for order in range(MAX_ORDER + 1):
        size = order + 1
        forms = []
        references = []
        for kind in range(3):
            form = mp.matrix(size, size)
            reference = mp.matrix(size, size)
            for i in range(size):
                for j in range(size):
                    degree = i + j
                    if kind == 0:
                        form[i, j] = moments[degree]
                        reference[i, j] = 1 / mp.mpf(degree + 1)
                    elif kind == 1:
                        form[i, j] = moments[degree + 1]
                        reference[i, j] = 1 / mp.mpf(degree + 2)
                    else:
                        form[i, j] = moments[degree] - moments[degree + 1]
                        reference[i, j] = 1 / (
                            mp.mpf(degree + 1) * mp.mpf(degree + 2)
                        )
            forms.append(form)
            references.append(reference)
        candidates = [
            generalized_minimum(form, reference)
            for form, reference in zip(forms, references)
        ]
        controlling = min(range(3), key=lambda index: candidates[index][0])
        value, coefficient = candidates[controlling]
        roots = []
        if order:
            # mpmath expects descending coefficients.
            try:
                roots = sorted(
                    [root for root in mp.polyroots(list(reversed(coefficient)), maxsteps=500)
                     if abs(mp.im(root)) < mp.mpf("1e-30")],
                    reverse=True,
                )
            except Exception:
                roots = []
        rows.append((value, controlling, roots))
    return rows


actual_positions, actual_weights = riemann_atoms()
x1 = actual_positions[0]
measures = {
    "riemann_locations_source_weights": atomic_moments(actual_positions, actual_weights),
    "riemann_locations_equal_weights": atomic_moments(
        actual_positions, [mp.mpf(1) for _ in actual_positions]
    ),
    "riemann_locations_tilted_weights": atomic_moments(
        actual_positions,
        [weight * mp.e ** (mp.mpf("0.7") * mp.sin(index))
         for index, weight in enumerate(actual_weights, 1)],
    ),
    "polynomial_accumulation_j_minus_2": atomic_moments(
        [x1 / mp.mpf(index) ** 2 for index in range(1, ATOM_COUNT + 1)],
        [mp.mpf(1) for _ in range(ATOM_COUNT)],
    ),
    "geometric_accumulation_half": atomic_moments(
        [x1 * mp.mpf("0.5") ** (index - 1) for index in range(1, ATOM_COUNT + 1)],
        [mp.mpf(1) for _ in range(ATOM_COUNT)],
    ),
    "uniform_continuous": uniform_moments(),
    "cantor_singular_control": cantor_moments(),
}

kind_names = ("ordinary", "x", "one_minus_x")
print(f"atom_count={ATOM_COUNT} max_order={MAX_ORDER}")
for name, moments in measures.items():
    print(name)
    rows = reserve_sequence(moments)
    for order, (value, kind, roots) in enumerate(rows):
        root_text = ",".join(mp.nstr(mp.re(root), 8) for root in roots[:4])
        print(
            f"  n={order} eps={mp.nstr(value, 14)} "
            f"minus_log_over_n={mp.nstr(-mp.log(value)/order, 10) if order else 'na'} "
            f"minus_log_over_n2={mp.nstr(-mp.log(value)/(order*order), 10) if order else 'na'} "
            f"kind={kind_names[kind]} roots={root_text}"
        )

print("riemann_vandermonde_stability")
normalized_actual_weights = normalize(actual_weights)
actual_rows = reserve_sequence(measures["riemann_locations_source_weights"])
for order in range(1, MAX_ORDER + 1):
    leading = mp.matrix(order, order)
    reference = mp.matrix(order, order)
    for i in range(order):
        for j in range(order):
            degree = i + j
            leading[i, j] = mp.fsum(
                normalized_actual_weights[index]
                * actual_positions[index]
                * actual_positions[index] ** degree
                for index in range(order)
            )
            reference[i, j] = 1 / mp.mpf(degree + 2)
    sigma_squared, _ = generalized_minimum(leading, reference)
    epsilon = actual_rows[order][0]
    eta = mp.sqrt(epsilon / sigma_squared)
    print(
        f"  n={order} sigma={mp.nstr(mp.sqrt(sigma_squared), 14)} "
        f"eta={mp.nstr(eta, 14)} annihilator_dominance={eta < 1}"
    )
