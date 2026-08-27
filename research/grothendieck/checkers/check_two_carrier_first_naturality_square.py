"""Exact audit of the first two-carrier square and its cutoff leakage."""

from sympy import Matrix, diag, symbols


def main() -> None:
    h0, h1, h2, h3 = symbols("h0 h1 h2 h3", nonzero=True)

    # The two carriers remain distinct; S is only their labelled incidence.
    sampling = Matrix.eye(4)
    circle_preparation = diag(h0, h1, h2, h3)
    log_multiplication = diag(h0, h1, h2, h3)
    assert sampling * circle_preparation == log_multiplication * sampling
    assert circle_preparation.T * sampling.T == sampling.T * log_multiplication.T

    # A normalized four-mode Fourier model.  The scalar normalization is
    # irrelevant to the rank of the cutoff residual.
    fourier = Matrix(
        [
            [1, 1, 1, 1],
            [1, 1, -1, -1],
            [1, -1, 1, -1],
            [1, -1, -1, 1],
        ]
    )
    project = Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    include = project.T
    cutoff_identity = include * project
    leakage = project * fourier * (Matrix.eye(4) - cutoff_identity)

    assert leakage == Matrix([[0, 0, 1, 1], [0, 0, -1, -1]])
    assert leakage.rank() == 1
    assert leakage * Matrix([0, 0, 1, 0]) != Matrix.zeros(2, 1)

    print("typed_sampling_naturality=true")
    print("dagger_sampling_naturality=true")
    print("finite_fourier_cutoff_residual_rank=1")
    print("finite_poisson_beck_chevalley=false")
    print("named_anomaly=poisson_cutoff_leakage")


if __name__ == "__main__":
    main()
