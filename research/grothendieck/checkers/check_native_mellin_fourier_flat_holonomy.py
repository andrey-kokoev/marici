"""Exact Gaussian-integer check of native Mellin--Fourier flat holonomy."""


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def main():
    # q=1, t=pi/2, so M=diag(i,-i).  Complex integer arithmetic is exact.
    i = 1j
    m = ((i, 0), (0, -i))
    m_inverse = ((-i, 0), (0, i))
    f = ((0, 1), (1, 0))
    identity = ((1, 0), (0, 1))

    reflected = matmul(matmul(f, m), f)
    loop = matmul(matmul(matmul(f, m), f), m)

    checks = [
        ("reflection_is_involution", matmul(f, f) == identity),
        ("mellin_inverse_exact", matmul(m, m_inverse) == identity),
        ("reflection_reverses_mellin", reflected == m_inverse),
        ("dihedral_loop_holonomy_identity", loop == identity),
        ("closure_independent_of_amplitude", matmul(loop, ((3, 0), (0, 5))) == ((3, 0), (0, 5))),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

