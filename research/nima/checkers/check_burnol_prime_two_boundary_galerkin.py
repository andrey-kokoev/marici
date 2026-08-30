"""FFT Galerkin scout for Burnol's c=sqrt(2) support boundary.

The form is the compression of the Fourier multiplier alpha(tau) to an
interval of logarithmic length log(2).  Results are numerical reconnaissance,
not an interval or continuum certificate.
"""

import json

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh, minres
from scipy.special import digamma


LOG_TWO = np.log(2.0)


def alpha(omega):
    return boundary_symbol(omega) + archimedean_symbol(omega)


def boundary_symbol(omega):
    return 8 * np.sqrt(2.0) * np.cos(LOG_TWO * omega) / (1 + 4 * omega**2)


def archimedean_symbol(omega):
    return -np.log(np.pi) + np.real(digamma(0.25 + 0.5j * omega))


def truncated_gamma_symbol(omega, levels):
    result = np.full_like(omega, -np.log(np.pi) + float(digamma(0.25)))
    for index in range(levels):
        rate = 2 * index + 0.5
        result += 2 * omega**2 / (rate * (rate**2 + omega**2))
    return result


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
        boundary_energy = float(np.sum(boundary_symbol(omega) * spectral_mass))
        archimedean_energy = float(
            np.sum(archimedean_symbol(omega) * spectral_mass)
        )
        negative = symbol < 0
        negative_contribution = float(np.sum(symbol[negative] * spectral_mass[negative]))
        positive_contribution = float(np.sum(symbol[~negative] * spectral_mass[~negative]))
        x = (np.arange(support_points) + 0.5) * dx - LOG_TWO / 2

        def arch_matvec(source):
            source_full = np.zeros(total_points, dtype=np.complex128)
            source_full[start:stop] = source
            return np.fft.ifft(
                archimedean_symbol(omega)
                * np.fft.fft(source_full, norm="ortho"),
                norm="ortho",
            )[start:stop].real

        arch_operator = LinearOperator(
            (support_points, support_points),
            matvec=arch_matvec,
            dtype=np.float64,
        )
        arch_values, arch_vectors = eigsh(
            arch_operator,
            k=6,
            which="SA",
            tol=1e-11,
            maxiter=10000,
        )
        arch_order = np.argsort(arch_values)
        arch_values = arch_values[arch_order]
        arch_vectors = arch_vectors[:, arch_order]
        arch_modes = [
            {
                "eigenvalue": float(arch_values[index]),
                "parity": (
                    "even"
                    if np.dot(arch_vectors[:, index], arch_vectors[::-1, index]) > 0
                    else "odd"
                ),
            }
            for index in range(6)
        ]
        truncated_tower = []
        for levels in [
            1, 2, 4, 8, 16, 32, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            52, 56, 58, 60, 62, 64, 128
        ]:
            truncated_symbol = boundary_symbol(omega) + truncated_gamma_symbol(
                omega, levels
            )

            def truncated_matvec(source):
                source_full = np.zeros(total_points, dtype=np.complex128)
                source_full[start:stop] = source
                return np.fft.ifft(
                    truncated_symbol
                    * np.fft.fft(source_full, norm="ortho"),
                    norm="ortho",
                )[start:stop].real

            truncated_operator = LinearOperator(
                (support_points, support_points),
                matvec=truncated_matvec,
                dtype=np.float64,
            )
            truncated_value = eigsh(
                truncated_operator,
                k=1,
                which="SA",
                tol=1e-10,
                maxiter=10000,
                return_eigenvectors=False,
            )[0]
            truncated_tower.append(
                {"levels": levels, "lowest_eigenvalue": float(truncated_value)}
            )

        def correlation(candidate):
            candidate = np.asarray(candidate, dtype=float)
            candidate /= np.linalg.norm(candidate)
            return float(abs(np.dot(vector, candidate)))

        cosine = np.cos(np.pi * x / LOG_TWO)
        cosine /= np.linalg.norm(cosine)
        acted_cosine = matvec(cosine)
        cosine_rayleigh = float(np.dot(cosine, acted_cosine))
        transformed_boundary = np.fft.ifft(
            boundary_symbol(omega) * spectrum, norm="ortho"
        )[start:stop].real
        cosh_half = np.cosh(x / 2)
        sinh_half = np.sinh(x / 2)
        rank_two_boundary = 2 * dx * (
            cosh_half * np.dot(cosh_half, vector)
            - sinh_half * np.dot(sinh_half, vector)
        )
        solved_cosh, info_cosh = minres(
            arch_operator, cosh_half, rtol=1e-11, maxiter=10000
        )
        solved_sinh, info_sinh = minres(
            arch_operator, sinh_half, rtol=1e-11, maxiter=10000
        )
        even_secular_at_zero = 1 + 2 * dx * np.dot(cosh_half, solved_cosh)
        odd_contraction_at_zero = 2 * dx * np.dot(sinh_half, solved_sinh)
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
        first_modes = []
        for mode_index in range(3):
            mode = vectors[:, mode_index]
            mode_full = np.zeros(total_points, dtype=np.complex128)
            mode_full[start:stop] = mode
            mode_spectrum = np.fft.fft(mode_full, norm="ortho")
            reflected_overlap = float(np.dot(mode, mode[::-1]))
            first_modes.append(
                {
                    "eigenvalue": float(values[mode_index]),
                    "parity": "even" if reflected_overlap > 0 else "odd",
                    "parity_overlap": reflected_overlap,
                    "archimedean_energy": float(
                        np.sum(
                            archimedean_symbol(omega)
                            * np.abs(mode_spectrum) ** 2
                        )
                    ),
                    "rank_two_boundary_energy": float(
                        np.sum(
                            boundary_symbol(omega)
                            * np.abs(mode_spectrum) ** 2
                        )
                    ),
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
            "archimedean_energy": archimedean_energy,
            "rank_two_boundary_energy": boundary_energy,
            "rank_two_kernel_residual_norm": float(
                np.linalg.norm(transformed_boundary - rank_two_boundary)
            ),
            "even_rank_one_secular_at_zero": float(even_secular_at_zero),
            "odd_rank_one_contraction_at_zero": float(odd_contraction_at_zero),
            "rank_one_solve_info": [int(info_cosh), int(info_sinh)],
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
            "first_three_mode_sectors": first_modes,
            "archimedean_six_lowest_modes": arch_modes,
            "truncated_gamma_tower": truncated_tower,
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
        (1024, 64, True),
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
