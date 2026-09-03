#!/usr/bin/env python3
"""Verify the final inequality in a WindowBridgeCertificate/v1 file.

This verifier checks the certificate schema, convention lock, interval ordering,
provenance fields, and the strict bridge inequality

    sum(error_component.upper)
        < localized_margin.lambda.lower * vector.norm_lower.lower.

It does not generate analytic or interval bounds.  The bound generator and its
interval backend remain part of the trusted proof chain.

Usage:
    python verify_window_bridge.py --self-test
    python verify_window_bridge.py --write-template certificate.json
    python verify_window_bridge.py certificate.json
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Any, Mapping

SCHEMA = "WindowBridgeCertificate/v1"
REQUIRED_ERRORS = (
    "endpoint",
    "gamma_compact",
    "gamma_tail",
    "prime_overlap",
    "prime_tail",
    "quadrature",
    "rounding",
)


class CertificateError(ValueError):
    pass


def dec(value: Any, path: str) -> Decimal:
    if isinstance(value, bool):
        raise CertificateError(f"{path}: boolean is not a decimal")
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise CertificateError(f"{path}: invalid decimal {value!r}") from exc


def obj(parent: Mapping[str, Any], key: str, path: str) -> Mapping[str, Any]:
    value = parent.get(key)
    if not isinstance(value, Mapping):
        raise CertificateError(f"{path}.{key}: required object")
    return value


def text(parent: Mapping[str, Any], key: str, path: str) -> str:
    value = parent.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CertificateError(f"{path}.{key}: required nonempty string")
    return value.strip()


def interval(parent: Mapping[str, Any], key: str, path: str,
             *, nonnegative: bool = False, positive_lower: bool = False) -> tuple[Decimal, Decimal]:
    block = obj(parent, key, path)
    lo = dec(block.get("lower"), f"{path}.{key}.lower")
    hi = dec(block.get("upper"), f"{path}.{key}.upper")
    if hi < lo:
        raise CertificateError(f"{path}.{key}: upper < lower")
    if nonnegative and lo < 0:
        raise CertificateError(f"{path}.{key}: lower must be nonnegative")
    if positive_lower and lo <= 0:
        raise CertificateError(f"{path}.{key}: lower must be strictly positive")
    return lo, hi


def validate(cert: Mapping[str, Any]) -> dict[str, str | bool]:
    if cert.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    convention = obj(cert, "convention", "root")
    if text(convention, "weil_functional", "convention") != "Suzuki-2026-additive":
        raise CertificateError("convention.weil_functional mismatch")
    if text(convention, "fourier_transform", "convention") != "integral f(x) exp(i z x) dx":
        raise CertificateError("convention.fourier_transform mismatch")
    if convention.get("q_equals_2_theta") is not True:
        raise CertificateError("convention.q_equals_2_theta must be true")
    if text(convention, "difference", "convention") != "Q(v_t_xi)-Q(P_L v_t_xi)":
        raise CertificateError("convention.difference mismatch")

    window = obj(cert, "window", "root")
    L = dec(window.get("L"), "window.L")
    t_lo = dec(window.get("t_lo"), "window.t_lo")
    t_hi = dec(window.get("t_hi"), "window.t_hi")
    xi_abs_max = dec(window.get("xi_abs_max"), "window.xi_abs_max")
    if L <= 0 or t_lo <= 0 or t_hi < t_lo or xi_abs_max < 0:
        raise CertificateError("invalid window: require L>0, 0<t_lo<=t_hi, xi_abs_max>=0")

    margin = obj(cert, "localized_margin", "root")
    lam_lo, _ = interval(margin, "lambda", "localized_margin", positive_lower=True)
    text(margin, "theorem_source", "localized_margin")
    hashes = margin.get("certificate_hashes")
    if not isinstance(hashes, list) or not hashes or not all(isinstance(x, str) and x.strip() for x in hashes):
        raise CertificateError("localized_margin.certificate_hashes: required nonempty string list")
    text(margin, "replay_command", "localized_margin")

    vector = obj(cert, "vector", "root")
    if text(vector, "definition", "vector") != "(2*pi*t)^(-1/2)*exp(-x^2/(2*t))*exp(i*xi*x)":
        raise CertificateError("vector.definition mismatch")
    text(vector, "cutoff", "vector")
    norm_lo, _ = interval(vector, "norm_lower", "vector", positive_lower=True)

    errors = obj(cert, "error_components", "root")
    error_hi: dict[str, Decimal] = {}
    for name in REQUIRED_ERRORS:
        _, hi = interval(errors, name, "error_components", nonnegative=True)
        block = obj(errors, name, "error_components")
        text(block, "method", f"error_components.{name}")
        error_hi[name] = hi

    extra = set(errors) - set(REQUIRED_ERRORS)
    if extra:
        raise CertificateError(f"error_components: unrecognized keys {sorted(extra)}")

    provenance = obj(cert, "provenance", "root")
    for key in (
        "prime_data_sha256",
        "generator_code_sha256",
        "interval_backend",
        "interval_backend_version",
        "source_version_hashes",
    ):
        text(provenance, key, "provenance")
    precision_bits = provenance.get("precision_bits")
    if not isinstance(precision_bits, int) or isinstance(precision_bits, bool) or precision_bits < 64:
        raise CertificateError("provenance.precision_bits must be an integer >= 64")

    with localcontext() as ctx:
        ctx.prec = 100
        total_error = sum(error_hi.values(), Decimal(0))
        threshold = lam_lo * norm_lo
        slack = threshold - total_error

    accepted = total_error < threshold
    return {
        "accepted": accepted,
        "total_error_upper": format(total_error, "E"),
        "threshold_lower": format(threshold, "E"),
        "strict_slack": format(slack, "E"),
        "L": str(L),
        "t_interval": f"[{t_lo},{t_hi}]",
        "xi_interval": f"[-{xi_abs_max},{xi_abs_max}]",
    }


def template() -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "convention": {
            "weil_functional": "Suzuki-2026-additive",
            "fourier_transform": "integral f(x) exp(i z x) dx",
            "q_equals_2_theta": True,
            "difference": "Q(v_t_xi)-Q(P_L v_t_xi)",
        },
        "window": {
            "L": "0.8",
            "t_lo": "0.01",
            "t_hi": "0.02",
            "xi_abs_max": "100",
        },
        "localized_margin": {
            "lambda": {"lower": "8.9e-18", "upper": "9.1e-18"},
            "theorem_source": "arXiv:2608.24827v2, Theorem 1.2 and Corollary 6.3",
            "certificate_hashes": ["REPLACE_WITH_VERIFIED_SHA256"],
            "replay_command": "REPLACE_WITH_REPLAY_COMMAND",
        },
        "vector": {
            "definition": "(2*pi*t)^(-1/2)*exp(-x^2/(2*t))*exp(i*xi*x)",
            "cutoff": "P_L v = 1_{[-L,L]} v",
            "norm_lower": {
                "lower": "REPLACE_WITH_CERTIFIED_LOWER_BOUND",
                "upper": "REPLACE_WITH_CERTIFIED_UPPER_BOUND",
            },
        },
        "error_components": {
            name: {
                "lower": "0",
                "upper": "REPLACE_WITH_CERTIFIED_UPPER_BOUND",
                "method": "REPLACE_WITH_BOUND_METHOD_AND_SOURCE_CONSTANTS",
            }
            for name in REQUIRED_ERRORS
        },
        "provenance": {
            "prime_data_sha256": "REPLACE_WITH_SHA256",
            "generator_code_sha256": "REPLACE_WITH_SHA256",
            "interval_backend": "Arb",
            "interval_backend_version": "REPLACE_WITH_VERSION",
            "precision_bits": 256,
            "source_version_hashes": "REPLACE_WITH_THEOREM_AND_SOURCE_HASHES",
        },
    }


def synthetic(accept: bool) -> dict[str, Any]:
    cert = template()
    cert["localized_margin"]["certificate_hashes"] = ["a" * 64]
    cert["localized_margin"]["replay_command"] = "python verify_margin.py"
    cert["vector"]["norm_lower"] = {"lower": "2", "upper": "2.1"}
    for name in REQUIRED_ERRORS:
        cert["error_components"][name] = {
            "lower": "0",
            "upper": "1e-20",
            "method": "synthetic self-test",
        }
    if not accept:
        cert["error_components"]["prime_tail"]["upper"] = "2e-17"
    cert["provenance"].update({
        "prime_data_sha256": "b" * 64,
        "generator_code_sha256": "c" * 64,
        "interval_backend_version": "self-test",
        "source_version_hashes": "d" * 64,
    })
    return cert


def self_test() -> None:
    good = validate(synthetic(True))
    if good["accepted"] is not True:
        raise AssertionError("positive self-test did not pass")
    bad = validate(synthetic(False))
    if bad["accepted"] is not False:
        raise AssertionError("negative self-test did not fail")

    malformed = synthetic(True)
    malformed["convention"]["q_equals_2_theta"] = False
    try:
        validate(malformed)
    except CertificateError:
        pass
    else:
        raise AssertionError("convention-lock self-test did not reject malformed input")

    print("SELF-TEST PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--write-template", type=Path)
    args = parser.parse_args()

    if args.self_test:
        self_test()

    if args.write_template:
        args.write_template.write_text(json.dumps(template(), indent=2) + "\n", encoding="utf-8")
        print(f"WROTE {args.write_template}")

    if args.certificate:
        try:
            raw = args.certificate.read_bytes()
            cert = json.loads(raw.decode("utf-8"))
            if not isinstance(cert, Mapping):
                raise CertificateError("root must be a JSON object")
            result = validate(cert)
            result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
            print(json.dumps(result, indent=2))
            return 0 if result["accepted"] else 2
        except (OSError, UnicodeError, json.JSONDecodeError, CertificateError) as exc:
            print(f"INVALID CERTIFICATE: {exc}", file=sys.stderr)
            return 1

    if not (args.self_test or args.write_template):
        parser.error("supply a certificate or use --self-test/--write-template")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
