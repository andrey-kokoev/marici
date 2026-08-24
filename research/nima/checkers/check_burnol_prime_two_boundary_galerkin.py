"""FFT Galerkin scout for Burnol's c=sqrt(2) support boundary.

The form is the compression of the Fourier multiplier alpha(tau) to an
interval of logarithmic length log(2).  Results are numerical reconnaissance,
not an interval or continuum certificate.
"""

import json

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.special import digamma


LOG_TWO = np.log(2.0)


def alpha(omega):
    return (
        8 * np.sqrt(2.0) * np.cos(LOG_TWO * omega) / (1 + 4 * omega**2)
        - np.log(np.pi)
        + np.real(digamma(0.25 + 0.5j * omega))
    )


def lowest_compressed_eigenvalue(support_points, padding_factor):
    dx = LOG_TWO / support_points
    total_points = support_points * padding_factor
    omega = 2 * np.pi * np.fft.fftfreq(total_points, d=dx)
    symbol = alpha(omega)
    start = (total_points - support_points) // 2
    stop = start + support_points

    def matvec(vector):
        full = np.zeros(total_points, dtype=np.complex128)
        full[start:stop] = vector
        transformed = np.fft.fft(full, norm="ortho")
        acted = np.fft.ifft(symbol * transformed, norm="ortho")
        return np.real(acted[start:stop])

    operator = LinearOperator(
        (support_points, support_points), matvec=matvec, dtype=np.float64
    )
    values = eigsh(
        operator,
        k=3,
        which="SA",
        tol=1e-11,
        maxiter=10000,
        return_eigenvectors=False,
    )
    return {
        "support_points": support_points,
        "padding_factor": padding_factor,
        "dx": dx,
        "frequency_step": 2 * np.pi / (total_points * dx),
        "three_lowest_eigenvalues": sorted(float(value) for value in values),
    }


runs = [
    lowest_compressed_eigenvalue(support_points, padding_factor)
    for support_points, padding_factor in [
        (128, 32),
        (256, 16),
        (256, 32),
        (256, 64),
        (256, 128),
        (512, 32),
        (512, 64),
    ]
]

print(
    json.dumps(
        {
            "schema": "marici.burnol-prime-two-boundary-galerkin.v1",
            "status": "pass",
            "scope": "FFT Galerkin scout; not a continuum or directed certificate",
            "support_length": LOG_TWO,
            "runs": runs,
            "stable_sign": all(
                run["three_lowest_eigenvalues"][0] > 0 for run in runs
            ),
            "interpretation": (
                "Positive converged scouts would show that the negative "
                "pointwise multiplier band is not by itself a support-" 
                "constrained counterexample. They do not prove positivity."
            ),
        },
        indent=2,
    )
)
