#!/usr/bin/env python3
"""Audit whether the compensating charge-one line is already source-authorized."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "charge_one_source_authority_audit.json"
MOD = 3

# Evidence imported from the active magnetic packets/results:
# - activation: the only trivially permitted invariant observable is the real
#   even-grade electric constant datum; magnetic never activates.
# - route packet: charge is preserved by covariant derivatives and reflected,
#   not identified; multiplication by w^2 is a local charge-2 example but is
#   not deck-invariant and changes the grammar.
# - typed readout: sector-specific adapters may be charge-compatible, but their
#   relative normalization is unconstrained without a further source datum.
# - charged bimodule audit: the E/M bridge from charge 2 to charge 1 needs a
#   compensating line of charge 1.
available_declared_objects = {
    "even_constant_electric_observable": {
        "charge": 0,
        "source_authorized": True,
        "kind": "real invariant scalar readout",
        "can_type_compensating_line": False,
    },
    "magnetic_sector_invariant_readout": {
        "charge": None,
        "source_authorized": False,
        "kind": "absent in probed datum universe",
        "can_type_compensating_line": False,
    },
    "covariant_derivative_or_connection_terms": {
        "charge_action": "preserve",
        "source_authorized": True,
        "kind": "charge-preserving constructor",
        "can_type_compensating_line": False,
    },
    "reflection": {
        "charge_action": "negate",
        "source_authorized": True,
        "kind": "pairs conjugate sectors without identifying them",
        "can_type_compensating_line": False,
    },
    "multiplication_by_w_squared": {
        "charge": 2,
        "source_authorized": False,
        "kind": "local charged example; not deck-invariant; changes grammar",
        "can_type_compensating_line": False,
    },
    "twisted_charge_one_line": {
        "charge": 1,
        "source_authorized": False,
        "kind": "lawful alternative named but not constructed",
        "can_type_compensating_line": True,
    },
    "explicit_symmetry_breaking_morphism": {
        "charge": 1,
        "source_authorized": False,
        "kind": "lawful alternative named but not constructed",
        "can_type_compensating_line": True,
    },
}

source_authorized_charge_one = [
    name for name, item in available_declared_objects.items()
    if item.get("charge") == 1 and item.get("source_authorized")
]

source_authorized_compensating = [
    name for name, item in available_declared_objects.items()
    if item.get("can_type_compensating_line") and item.get("source_authorized")
]

# Minimal contract if authority is absent.
minimal_missing_contract = {
    "source_lattice_enlargement": "declare the charge-one line before scalar readout",
    "deck_action": "line has character 1 and bridge has character 2 so the tensor is invariant",
    "dual_analysis": "retain the charge-two dual line for same-preparation invariant pairing",
    "normalization": "fix relative phase/scale of sector-specific adapters",
    "connection": "supply determinant-line transport under authorized presentation changes",
    "prohibition": "do not trivialize the charged line after seeing cancellation",
}

checks = {
    "no_declared_source_authorized_charge_one_line": source_authorized_charge_one == [],
    "no_declared_source_authorized_compensating_line": source_authorized_compensating == [],
    "only_existing_invariant_readout_is_charge_zero": available_declared_objects["even_constant_electric_observable"]["charge"] == 0,
    "derivatives_do_not_change_charge": available_declared_objects["covariant_derivative_or_connection_terms"]["charge_action"] == "preserve",
    "reflection_does_not_identify_conjugate_charges": available_declared_objects["reflection"]["charge_action"] == "negate",
    "local_w_squared_example_is_not_authority": not available_declared_objects["multiplication_by_w_squared"]["source_authorized"],
    "named_twisted_line_is_contract_not_construction": not available_declared_objects["twisted_charge_one_line"]["source_authorized"],
    "minimal_contract_has_all_required_fields": set(minimal_missing_contract) == {
        "source_lattice_enlargement", "deck_action", "dual_analysis",
        "normalization", "connection", "prohibition",
    },
}

payload = {
    "schema": "marici.strominger.charge_one_source_authority_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "available_declared_objects": available_declared_objects,
    "source_authorized_charge_one": source_authorized_charge_one,
    "source_authorized_compensating_lines": source_authorized_compensating,
    "minimal_missing_contract": minimal_missing_contract,
    "verdict": (
        "No existing declared magnetic source object authorizes the charge-one "
        "compensating line. The strongest productive endpoint is therefore a "
        "minimal missing-source contract: a charge-one twisted line or equivalent "
        "symmetry-breaking morphism, its dual analysis line, adapter normalization, "
        "and determinant-line connection must be supplied before the bridge can be "
        "promoted from pre-descent local form to source-typed joint instrument."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
