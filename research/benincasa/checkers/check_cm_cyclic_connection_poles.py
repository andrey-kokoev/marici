#!/usr/bin/env python3
"""Test the predeclared soft-plus-triangle model for the cyclic quotient line."""

import ast
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
PRIMES = (32003, 65521)
POINTS = (
    (5, 7, 11),
    (7, 11, 13),
    (11, 13, 17),
    (5, 13, 19),
    (7, 17, 23),
)


def centered(value, prime):
    value %= prime
    return value if value <= prime // 2 else value - prime


def run_case(point, prime):
    environment = os.environ.copy()
    environment.update(
        NORMAL_TOWER="1",
        CM_CYCLIC_SECOND="horizontal",
        KINEMATIC_POINT="A",
        CM_P_SQUARES=",".join(map(str, point)),
        PRIME=str(prime),
    )
    completed = subprocess.run(
        ["cargo", "run", "--quiet", "--bin", "cm_normal_tower_rank"],
        cwd=CRATE,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    )
    kernel = ast.literal_eval(
        re.search(r"NORMAL_TOWER_KERNEL=(.*)", completed.stdout).group(1)
    )
    relations = []
    for column in range(10, 14):
        matches = [row for row in kernel if row[column] != 0]
        if len(matches) != 1:
            raise RuntimeError(f"column {column} lacks a unique echelon relation")
        relation = matches[0]
        inverse = pow(relation[column], -1, prime)
        relations.append([(value * inverse) % prime for value in relation])
    coordinates = [(-relation[3]) % prime for relation in relations]
    if coordinates[0] == 0:
        raise RuntimeError("cyclic trace has zero quotient coordinate")
    omega = [value * pow(coordinates[0], -1, prime) % prime for value in coordinates[1:]]
    return omega


def lambda_polynomial(point, prime):
    s1, s2, s3 = point
    value = s1*s1 + s2*s2 + s3*s3 - 2*(s1*s2 + s1*s3 + s2*s3)
    derivatives = (2*(s1-s2-s3), 2*(s2-s1-s3), 2*(s3-s1-s2))
    return value % prime, tuple(value % prime for value in derivatives)


def coefficient_rows(point, prime):
    lam, derivatives = lambda_polynomial(point, prime)
    if lam == 0 or any(value % prime == 0 for value in point):
        raise RuntimeError("sample lies on a predeclared divisor")
    return [
        (pow(point[index] % prime, -1, prime), derivatives[index] * pow(lam, -1, prime) % prime)
        for index in range(3)
    ]


def solve_two(rows, values, prime):
    for first in range(len(rows)):
        for second in range(first + 1, len(rows)):
            a, b = rows[first]
            c, d = rows[second]
            determinant = (a*d-b*c) % prime
            if determinant:
                x = (values[first]*d-b*values[second]) * pow(determinant, -1, prime) % prime
                y = (a*values[second]-values[first]*c) * pow(determinant, -1, prime) % prime
                return x, y
    raise RuntimeError("ansatz matrix has rank below two")


def small_rational(residues, primes, denominator_limit=128, numerator_limit=512):
    for denominator in range(1, denominator_limit + 1):
        candidates = [centered(residue * denominator, prime) for residue, prime in zip(residues, primes)]
        if len(set(candidates)) == 1 and abs(candidates[0]) <= numerator_limit:
            return [candidates[0], denominator]
    return None


def main():
    runs = []
    fits = []
    for prime in PRIMES:
        rows = []
        values = []
        prime_runs = []
        for point in POINTS:
            omega = run_case(point, prime)
            local_rows = coefficient_rows(point, prime)
            rows.extend(local_rows)
            values.extend(omega)
            prime_runs.append({"squared_momenta": list(point), "omega": omega})
        fit = solve_two(rows, values, prime)
        fits.append(fit)
        residuals = [
            (value - row[0]*fit[0] - row[1]*fit[1]) % prime
            for row, value in zip(rows, values)
        ]
        runs.append({
            "prime": prime,
            "fit_mod_prime": list(fit),
            "samples": prime_runs,
            "nonzero_residual_count": sum(value != 0 for value in residuals),
        })
    model_fits = all(run["nonzero_residual_count"] == 0 for run in runs)
    soft = small_rational([fit[0] for fit in fits], PRIMES) if model_fits else None
    triangle = small_rational([fit[1] for fit in fits], PRIMES) if model_fits else None
    checks = {
        "all_samples_off_predeclared_divisors": True,
        "soft_plus_triangle_ansatz_is_falsified_at_both_primes": (
            not model_fits
            and all(run["nonzero_residual_count"] == 13 for run in runs)
        ),
        "failed_model_is_not_assigned_residues": soft is None and triangle is None,
    }
    packet = {
        "schema": "marici.cm_cyclic_connection_poles.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "predeclared_model": (
            "omega_i=c_soft*dlog(P_i^2)+c_triangle*dlog(Lambda_P), "
            "Lambda_P=s1^2+s2^2+s3^2-2s1s2-2s1s3-2s2s3"
        ),
        "runs": runs,
        "reconstructed_coefficients_if_model_had_passed": {
            "c_soft": soft,
            "c_triangle": triangle,
        },
        "checks": checks,
    }
    output = ROOT / "results" / "cm-cyclic-connection-poles.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "coefficients": packet["reconstructed_coefficients_if_model_had_passed"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
