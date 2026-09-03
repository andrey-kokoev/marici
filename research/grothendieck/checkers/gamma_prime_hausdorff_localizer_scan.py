"""Uncertified scan of the gamma-plus-prime Hausdorff localizer."""
from __future__ import annotations

import json
import math
from pathlib import Path
import mpmath as mp


def von_mangoldt_table(limit: int) -> list[float]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    values = [0.0] * (limit + 1)
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        logp = math.log(p)
        power = p
        while power <= limit:
            values[power] = logp
            if power > limit // p:
                break
            power *= p
    return values


def gamma_kernel(t: mp.mpf) -> mp.mpf:
    integrand = lambda r: (mp.exp(-r) - mp.exp(-r / 4 - r * r / (16 * t))) / (-mp.expm1(-r))
    return (-mp.euler - mp.log(mp.pi) + mp.quad(integrand, [0, 1, mp.inf])) / (4 * mp.sqrt(mp.pi * t))


def prime_kernel(t: mp.mpf, mangoldt: list[float]) -> mp.mpf:
    total = mp.fsum(
        mp.mpf(weight) / mp.sqrt(n) * mp.exp(-(mp.log(n) ** 2) / (4 * t))
        for n, weight in enumerate(mangoldt)
        if n >= 2 and weight
    )
    return -total / (2 * mp.sqrt(mp.pi * t))


def remainder(t: mp.mpf, mangoldt: list[float]) -> mp.mpf:
    return gamma_kernel(t) + prime_kernel(t, mangoldt)


def scan_case(t: mp.mpf, h: mp.mpf, rank: int, mangoldt: list[float]) -> dict:
    gamma_values = [gamma_kernel(t + n * h) for n in range(2 * rank)]
    prime_values = [prime_kernel(t + n * h, mangoldt) for n in range(2 * rank)]
    values = [g + p for g, p in zip(gamma_values, prime_values)]
    matrix = mp.matrix(rank)
    normalized = mp.matrix(rank)
    for i in range(rank):
        for j in range(rank):
            n = i + j
            matrix[i, j] = values[n] - values[n + 1]
            normalized[i, j] = (
                mp.exp(-(t + n * h) / 4) * values[n]
                - mp.exp(-(t + (n + 1) * h) / 4) * values[n + 1]
            )
    eigenvalues = sorted(mp.eigsy(matrix, eigvals_only=True))
    normalized_eigenvalues = sorted(mp.eigsy(normalized, eigvals_only=True))
    endpoint_c = (mp.exp(h / 4) - 1) * mp.exp(t / 4)
    v = mp.matrix([mp.exp(i * h / 4) for i in range(rank)])
    projected = matrix - endpoint_c * (v * v.T)
    full_eigenvalues = sorted(mp.eigsy(projected, eigvals_only=True))
    result = {
        "t": str(t), "h": str(h), "rank": rank,
        "gamma_prime_min_eigenvalue": mp.nstr(eigenvalues[0], 20),
        "completed_min_eigenvalue": mp.nstr(full_eigenvalues[0], 20),
        "normalized_gamma_prime_min_eigenvalue": mp.nstr(normalized_eigenvalues[0], 20),
    }
    if rank == 2:
        gamma_differences = [gamma_values[n] - gamma_values[n + 1] for n in range(3)]
        prime_differences = [prime_values[n] - prime_values[n + 1] for n in range(3)]
        gamma_d2 = gamma_differences[0] * gamma_differences[2] - gamma_differences[1] ** 2
        prime_d2 = prime_differences[0] * prime_differences[2] - prime_differences[1] ** 2
        total_differences = [gamma_differences[k] + prime_differences[k] for k in range(3)]
        continuum_values = [
            -mp.exp((t + n * h) / 4)
            * (1 + mp.erf(mp.sqrt(t + n * h) / 2))
            / 2
            for n in range(4)
        ]
        continuum_differences = [continuum_values[n] - continuum_values[n + 1] for n in range(3)]
        archimedean_differences = [
            gamma_differences[k] + continuum_differences[k] for k in range(3)
        ]
        fluctuation_differences = [
            prime_differences[k] - continuum_differences[k] for k in range(3)
        ]
        archimedean_d2 = (
            archimedean_differences[0] * archimedean_differences[2]
            - archimedean_differences[1] ** 2
        )
        fluctuation_d2 = (
            fluctuation_differences[0] * fluctuation_differences[2]
            - fluctuation_differences[1] ** 2
        )
        total_d2 = mp.det(matrix)
        gamma_mu = gamma_differences[1] / gamma_differences[0]
        prime_mu = prime_differences[1] / prime_differences[0]
        gamma_delta = gamma_d2 / gamma_differences[0] ** 2
        prime_delta = prime_d2 / prime_differences[0] ** 2
        curvature_term = (gamma_differences[0] + prime_differences[0]) * (
            gamma_differences[0] * gamma_delta + prime_differences[0] * prime_delta
        )
        slope_term = gamma_differences[0] * prime_differences[0] * (gamma_mu - prime_mu) ** 2
        total_mu = total_differences[1] / total_differences[0]
        rational_center = mp.mpf(round(float(total_mu), 3))
        gamma_centered = (
            gamma_differences[2]
            - 2 * rational_center * gamma_differences[1]
            + rational_center**2 * gamma_differences[0]
        )
        prime_centered = (
            prime_differences[2]
            - 2 * rational_center * prime_differences[1]
            + rational_center**2 * prime_differences[0]
        )
        total_centered = gamma_centered + prime_centered
        centered_linear = total_differences[1] - rational_center * total_differences[0]
        linear_error_coefficient = 2 * (
            abs(total_differences[2]) + abs(total_differences[0]) + 2 * abs(total_differences[1])
        )
        half_margin = total_d2 / 2
        uniform_sample_tolerance = (
            -linear_error_coefficient
            + mp.sqrt(linear_error_coefficient**2 + 32 * half_margin)
        ) / 16
        result.update({
            "total_a0": mp.nstr(total_differences[0], 20),
            "total_a1": mp.nstr(total_differences[1], 20),
            "total_a2": mp.nstr(total_differences[2], 20),
            "uniform_source_sample_tolerance_for_half_margin": mp.nstr(uniform_sample_tolerance, 20),
            "archimedean_plus_continuum_a0": mp.nstr(archimedean_differences[0], 20),
            "prime_fluctuation_a0": mp.nstr(fluctuation_differences[0], 20),
            "archimedean_plus_continuum_D2": mp.nstr(archimedean_d2, 20),
            "prime_fluctuation_D2": mp.nstr(fluctuation_d2, 20),
            "archimedean_fluctuation_cross_D2": mp.nstr(
                total_d2 - archimedean_d2 - fluctuation_d2, 20
            ),
            "gamma_a0": mp.nstr(gamma_differences[0], 20),
            "prime_a0": mp.nstr(prime_differences[0], 20),
            "gamma_D2": mp.nstr(gamma_d2, 20),
            "prime_D2": mp.nstr(prime_d2, 20),
            "gamma_mu": mp.nstr(gamma_mu, 20),
            "prime_mu": mp.nstr(prime_mu, 20),
            "slope_gap_squared": mp.nstr((gamma_mu - prime_mu) ** 2, 20),
            "rational_center": mp.nstr(rational_center, 8),
            "gamma_centered_quadratic": mp.nstr(gamma_centered, 20),
            "prime_centered_quadratic": mp.nstr(prime_centered, 20),
            "total_centered_quadratic": mp.nstr(total_centered, 20),
            "centered_linear": mp.nstr(centered_linear, 20),
            "common_center_identity_residual": mp.nstr(
                total_d2 - total_differences[0] * total_centered + centered_linear**2, 5
            ),
            "curvature_term": mp.nstr(curvature_term, 20),
            "slope_compensation_term": mp.nstr(slope_term, 20),
            "gamma_prime_cross_D2": mp.nstr(total_d2 - gamma_d2 - prime_d2, 20),
            "gamma_prime_D2": mp.nstr(total_d2, 20),
            "slope_identity_residual": mp.nstr(total_d2 - curvature_term - slope_term, 5),
        })
    return result


def main() -> None:
    mp.mp.dps = 100
    limit = 200_000
    mangoldt = von_mangoldt_table(limit)
    cases = [
        scan_case(mp.mpf(t), mp.mpf(h), rank, mangoldt)
        for t, h in [("0.001", "0.001"), ("0.01", "0.005"), ("0.05", "0.01")]
        for rank in (2, 3, 4)
    ]
    cases.extend(
        scan_case(mp.mpf(t), mp.mpf("0.01"), 2, mangoldt)
        for t in ("0.20", "0.24", "0.25", "0.30")
    )
    result = {"prime_limit": limit, "certified": False, "cases": cases}
    output = Path(__file__).parents[1] / "results" / "gamma-prime-hausdorff-localizer-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
