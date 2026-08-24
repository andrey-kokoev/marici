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


def lowest_compressed_eigenvalue(support_points, padding_factor, analyze=False):
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
    values, vectors = eigsh(
        operator,
        k=3,
        which="SA",
        tol=1e-11,
        maxiter=10000,
        return_eigenvectors=True,
    )
    order = np.argsort(values)
    values = values[order]
    vectors = vectors[:, order]
    result = {
        "support_points": support_points,
        "padding_factor": padding_factor,
        "dx": dx,
        "frequency_step": 2 * np.pi / (total_points * dx),
        "three_lowest_eigenvalues": [float(value) for value in values],
    }
    if analyze:
        vector = vectors[:, 0]
        vector /= np.linalg.norm(vector)
        if np.dot(vector, vector[::-1]) < 0:
            vector = -vector
        full = np.zeros(total_points, dtype=np.complex128)
        full[start:stop] = vector
        spectrum = np.fft.fft(full, norm="ortho")
        spectral_mass = np.abs(spectrum) ** 2
        negative = symbol < 0
        negative_contribution = float(np.sum(symbol[negative] * spectral_mass[negative]))
        positive_contribution = float(np.sum(symbol[~negative] * spectral_mass[~negative]))
        x = (np.arange(support_points) + 0.5) * dx - LOG_TWO / 2

        def correlation(candidate):
            candidate = np.asarray(candidate, dtype=float)
            candidate /= np.linalg.norm(candidate)
            return float(abs(np.dot(vector, candidate)))

        cosine = np.cos(np.pi * x / LOG_TWO)
        cosine /= np.linalg.norm(cosine)
        acted_cosine = matvec(cosine)
        cosine_rayleigh = float(np.dot(cosine, acted_cosine))
        dirichlet_convergence = []
        for dimension in [1, 2, 4, 8, 16, 32]:
            basis = np.column_stack(
                [
                    np.cos((2 * index + 1) * np.pi * x / LOG_TWO)
                    for index in range(dimension)
                ]
            )
            basis, _ = np.linalg.qr(basis)
            compressed = basis.T @ np.column_stack(
                [matvec(basis[:, index]) for index in range(dimension)]
            )
            sub_values = np.linalg.eigvalsh(
                (compressed + compressed.T) / 2
            )
            dirichlet_convergence.append(
                {
                    "dimension": dimension,
                    "lowest_eigenvalue": float(sub_values[0]),
                }
            )

        result["lowest_mode"] = {
            "even_residual_norm": float(np.linalg.norm(vector - vector[::-1])),
            "odd_residual_norm": float(np.linalg.norm(vector + vector[::-1])),
            "endpoint_to_peak_ratio": float(
                max(abs(vector[0]), abs(vector[-1])) / np.max(np.abs(vector))
            ),
            "zero_crossings": int(np.count_nonzero(vector[:-1] * vector[1:] < 0)),
            "negative_band_mass_fraction": float(np.sum(spectral_mass[negative])),
            "negative_band_energy": negative_contribution,
            "positive_band_energy": positive_contribution,
            "energy_sum": negative_contribution + positive_contribution,
            "correlation_constant": correlation(np.ones_like(x)),
            "correlation_cos_pi": correlation(np.cos(np.pi * x / LOG_TWO)),
            "correlation_cos_2pi": correlation(np.cos(2 * np.pi * x / LOG_TWO)),
            "correlation_quartic_bump": correlation(
                (1 - (2 * x / LOG_TWO) ** 2) ** 4
            ),
            "cos_pi_rayleigh": cosine_rayleigh,
            "cos_pi_eigen_residual_norm": float(
                np.linalg.norm(acted_cosine - cosine_rayleigh * cosine)
            ),
            "even_dirichlet_subspace_convergence": dirichlet_convergence,
        }
    return result


runs = [
    lowest_compressed_eigenvalue(
        support_points, padding_factor, bool(analyze)
    )
    for support_points, padding_factor, *analyze in [
        (128, 32, True),
        (256, 16),
        (256, 32),
        (256, 64),
        (256, 128, True),
        (512, 32),
        (512, 64, True),
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
