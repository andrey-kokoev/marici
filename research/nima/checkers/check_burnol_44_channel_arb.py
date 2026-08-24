"""Arb sign certificate for the 44-channel Burnol boundary system.

Run with Sage, for example:

    sage -python check_burnol_44_channel_arb.py

Unlike the double-precision scout, every scalar is a RealBall and the step
exponential carries an explicit operator-norm Taylor remainder.  Modified
Gram--Schmidt is implemented directly because Sage does not provide QR over
RealBallField.
"""

from sage.all import RDF, RealBallField, identity_matrix, matrix, zero_matrix


LEVELS = 44
STEPS = 32
PRECISION = 256
TAYLOR_ORDER = 24
R = RealBallField(PRECISION)
LENGTH = R(2).log()
RATES = [R(2 * n) + R(1) / 2 for n in range(LEVELS)]
H_ZERO = -R.pi().log() - R.euler_constant() - R.pi() / 2 - 3 * LENGTH
D_COEFFICIENT = H_ZERO + sum(2 / rate for rate in RATES)


def infinity_norm_bound(a):
    """Return a rigorous scalar upper bound for the matrix infinity norm."""
    return max(sum(entry.abs().upper() for entry in a.row(i)) for i in range(a.nrows()))


def add_entrywise_error(a, error):
    result = matrix(a)
    for i in range(result.nrows()):
        for j in range(result.ncols()):
            result[i, j] = result[i, j].add_error(error)
    return result


def ball_matrix_exp(a, order=TAYLOR_ORDER):
    """Scaling-and-squaring exponential with a rigorous Taylor tail."""
    norm = infinity_norm_bound(a)
    scaling = 0
    while norm / (2**scaling) > R(1).upper() / 8:
        scaling += 1
    scaled = a / (2**scaling)
    r = R(infinity_norm_bound(scaled))
    term = identity_matrix(R, a.nrows())
    total = matrix(term)
    for k in range(1, order + 1):
        term = term * scaled / k
        total += term
    # exp(r) r^(N+1)/(N+1)! bounds the full matrix-norm Taylor tail.
    factorial = R(1)
    for k in range(2, order + 2):
        factorial *= k
    tail = r.exp() * r ** (order + 1) / factorial
    total = add_entrywise_error(total, tail.upper())
    for _ in range(scaling):
        total = total * total
    return total, scaling, tail


def modified_gram_schmidt(a):
    """Thin interval QR sufficient to enclose the propagated column plane."""
    columns = []
    for j in range(a.ncols()):
        vector = a.column(j)
        for basis in columns:
            vector -= basis.dot_product(vector) * basis
        squared_norm = vector.dot_product(vector)
        if squared_norm.lower() <= 0:
            raise ArithmeticError("interval Gram--Schmidt lost rank")
        columns.append(vector / squared_norm.sqrt())
    return matrix(R, a.nrows(), a.ncols(), lambda i, j: columns[j][i])


def midpoint_qr_precondition(a):
    """Right-precondition a ball basis using only its midpoint QR factor.

    The RDF computation is not used as evidence.  Its inverse triangular
    factor is embedded as a point ball matrix and multiplied into the full
    enclosure, so the resulting column space is rigorously identical.
    """
    midpoint = matrix(RDF, a.nrows(), a.ncols(), lambda i, j: RDF(a[i, j].center()))
    _, full_factor = midpoint.QR()
    factor = full_factor[: a.ncols(), :]
    diagonal_signs = [1 if factor[j, j] >= 0 else -1 for j in range(a.ncols())]
    sign = matrix.diagonal(RDF, diagonal_signs)
    factor = sign * factor
    change = factor.inverse()
    return a * matrix(R, change)


def flow_matrix(eigenvalue=R(0)):
    denominator = D_COEFFICIENT - eigenvalue
    functional = matrix(R, 1, LEVELS, [-1] + [1] * (LEVELS - 1))
    coefficients = matrix(R, LEVELS, 1, [1] + [-2 * rate for rate in RATES[1:]])
    coupling = matrix.diagonal(R, [rate**2 for rate in RATES])
    coupling += coefficients * functional / denominator
    zero = zero_matrix(R, LEVELS)
    one = identity_matrix(R, LEVELS)
    return zero.augment(one).stack(coupling.augment(zero))


def endpoint_plane():
    slopes = [RATES[0]] + [-rate for rate in RATES[1:]]
    return identity_matrix(R, LEVELS).stack(matrix.diagonal(R, slopes))


def center_block(parity):
    flow = flow_matrix()
    step, scaling, tail = ball_matrix_exp(-(LENGTH / (2 * STEPS)) * flow)
    plane = midpoint_qr_precondition(endpoint_plane())
    for _ in range(STEPS):
        plane = midpoint_qr_precondition(step * plane)
    if parity == "even":
        block = plane[LEVELS:, :]
    elif parity == "odd":
        block = plane[:LEVELS, :]
    else:
        raise ValueError(parity)
    return block, scaling, tail


def main():
    print("schema=marici.burnol-44-channel-arb.v1")
    print(f"precision={PRECISION} steps={STEPS} order={TAYLOR_ORDER}")
    print(f"d_coefficient={D_COEFFICIENT}")
    for parity in ("even", "odd"):
        block, scaling, tail = center_block(parity)
        determinant = block.det()
        print(f"{parity}.scaling={scaling}")
        print(f"{parity}.unscaled_tail={tail}")
        print(f"{parity}.determinant={determinant}")
        print(f"{parity}.sign_certified={not determinant.contains_zero()}")


if __name__ == "__main__":
    main()
