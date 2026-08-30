from fractions import Fraction


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def matvec(matrix, vector):
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def check_transport(a, b, c, x):
    matrix = ((a, 0), (b, c))
    endpoint = (0, 1)
    state = (x, 1)
    transported_endpoint = matvec(matrix, endpoint)
    transported_state = matvec(matrix, state)
    assert det(transported_state, transported_endpoint) == a * c * x
    assert (det(state, endpoint) == 0) == (
        det(transported_state, transported_endpoint) == 0
    )


if __name__ == "__main__":
    units = [Fraction(-3), Fraction(-1, 2), Fraction(1, 3), Fraction(5)]
    values = [Fraction(-7), Fraction(0), Fraction(2, 5)]
    checked = 0
    for a in units:
        for b in values:
            for c in units:
                for x in values:
                    check_transport(a, b, c, x)
                    checked += 1
    print(f"invertible endpoint-preserving transports checked: {checked}")
    print("zero incidence preserved: yes")
    print("result: equivalence cannot remove a divisor point")
