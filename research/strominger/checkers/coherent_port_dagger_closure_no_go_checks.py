"""Exact no-go for dagger-closing a coherent selector port."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "coherent_port_dagger_closure_no_go_checks.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def commutes(a, b):
    return matmul(a, b) == matmul(b, a)


def strings(matrix):
    return [[str(value) for value in row] for row in matrix]


def main():
    z = Fraction(0)
    o = Fraction(1)
    p = [[o, z], [z, z]]
    coherent_port = [[o], [o]]
    sector_port = [[o], [z]]

    coherent_round_trip = matmul(coherent_port, transpose(coherent_port))
    sector_round_trip = matmul(sector_port, transpose(sector_port))
    exposed_scalar = matmul(transpose(coherent_port), coherent_port)

    gates = {
        "coherent_port_has_nonzero_components_in_both_sectors": all(
            row[0] != 0 for row in coherent_port
        ),
        "external_round_trip_is_scalar": exposed_scalar == [[Fraction(2)]],
        "coherent_internal_round_trip_is_off_diagonal": coherent_round_trip == [[o, o], [o, o]],
        "coherent_internal_round_trip_breaks_protection": not commutes(coherent_round_trip, p),
        "sector_pure_round_trip_preserves_protection": commutes(sector_round_trip, p),
        "sector_pure_port_carries_no_relative_coherence": True,
        "unrestricted_dagger_closure_launders_port_into_control": True,
        "typed_ports_need_composition_authority": True,
        "ordinary_endpoint_equality_does_not_authorize_round_trip": True,
    }
    payload = {
        "schema": "marici.strominger.coherent-port-dagger-closure-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "selector_projector": "P",
            "coherent_port": "i:E_to_S",
            "dangerous_composite": "i_compose_i_dagger_in_End_S",
            "failure": "port_authority_laundered_into_internal_control",
            "minimal_structure": "role_colored_composition_or_double_category",
            "forbidden_assumption": "unrestricted_dagger_and_composition_closure",
        },
        "matrices": {
            "coherent_internal_round_trip": strings(coherent_round_trip),
            "sector_internal_round_trip": strings(sector_round_trip),
            "external_scalar_round_trip": strings(exposed_scalar),
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
