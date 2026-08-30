"""Conservative Strominger extension of Nima's data-descent kernel v2.

The base validator is used unchanged.  This module adds the two constructors
that the functional-completion packet needs and that v2 does not currently
type: topology-bearing completion and finite linear observation fibers.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from data_descent_kernel import TypeErrorRecord, compile_packet as compile_v2


def _error(errors: list[TypeErrorRecord], code: str, subject: str, detail: str) -> None:
    errors.append(TypeErrorRecord(code, subject, detail))


def validate_extension(packet: dict[str, Any]) -> list[TypeErrorRecord]:
    errors: list[TypeErrorRecord] = []
    contexts = {x["id"]: x for x in packet.get("contexts", [])}
    objects = {x["id"]: x for x in packet.get("local_objects", [])}
    derived = {x["id"]: x for x in packet.get("derived_objects", [])}

    completions = {x["id"]: x for x in packet.get("topological_completions", [])}
    for cid, completion in completions.items():
        if completion.get("source") not in objects or completion.get("target") not in objects:
            _error(errors, "unknown_completion_object", cid, "completion endpoints must be declared")
        if completion.get("topology") != "weak_star_sigma_M_C0":
            _error(errors, "missing_weak_star_topology", cid, str(completion.get("topology")))
        if completion.get("constructor_kind") != "topological_completion":
            _error(errors, "completion_as_flat_base_change", cid, str(completion.get("constructor_kind")))
        if not completion.get("dense_image_evidence"):
            _error(errors, "missing_completion_density", cid, "dense image requires evidence")
        if not completion.get("source_authority"):
            _error(errors, "missing_completion_authority", cid, "completion needs source authority")
        if not completion.get("comparison_evidence"):
            _error(errors, "missing_completion_comparison", cid, "source/target comparison is required")

    loci = {x["id"]: x for x in packet.get("geometric_loci", [])}
    physical = {x["id"]: x for x in packet.get("physical_kernel_classes", [])}
    for kid, kernel in physical.items():
        dobj = derived.get(kernel.get("derived_object"))
        if dobj is None or dobj.get("kind") != "Kernel":
            _error(errors, "completed_kernel_not_ordinary_kernel", kid, str(kernel.get("derived_object")))
        if kernel.get("homological_degree") != 0 or kernel.get("tor_grade") is not None:
            _error(errors, "completed_kernel_mistyped_as_derived_grade", kid, "expected degree-zero Kernel and no Tor grade")
        if kernel.get("completion") not in completions:
            _error(errors, "unknown_kernel_completion", kid, str(kernel.get("completion")))
        if kernel.get("rank") != 21 or kernel.get("harmonic_support") != [2, 3, 4]:
            _error(errors, "wrong_completed_kernel", kid, "expected rank 21 on l=2,3,4")
        if kernel.get("origin") != "global_spectral_zero":
            _error(errors, "characteristic_kernel_conflation", kid, str(kernel.get("origin")))
    for identification in packet.get("identifications", []):
        if identification.get("left") in loci and identification.get("right") in physical:
            _error(errors, "characteristic_kernel_identification", identification["id"], "geometric locus is not the physical kernel")
        if identification.get("right") in loci and identification.get("left") in physical:
            _error(errors, "characteristic_kernel_identification", identification["id"], "geometric locus is not the physical kernel")

    for state in packet.get("localized_global_states", []):
        if state.get("characteristic_locus") not in loci:
            _error(errors, "unknown_characteristic_locus", state["id"], str(state.get("characteristic_locus")))
        if state.get("space") != "compact_support_or_planar_L2" or state.get("rank") != 0:
            _error(errors, "unauthorized_characteristic_state", state["id"], "localized global characteristic state must have rank zero")
        if not state.get("no_go_evidence"):
            _error(errors, "missing_characteristic_no_go", state["id"], "Paley-Wiener/L2 evidence required")

    for fiber in packet.get("observation_fibers", []):
        fid = fiber["id"]
        if fiber.get("kind") != "finite_linear_observation_fiber":
            _error(errors, "unknown_observation_fiber", fid, str(fiber.get("kind")))
        if fiber.get("source_kernel") not in physical:
            _error(errors, "unknown_observation_source", fid, str(fiber.get("source_kernel")))
        ports = fiber.get("ports", [])
        coordinates = [x.get("coordinate") for x in ports]
        if len(ports) != 21 or sorted(coordinates) != list(range(21)):
            _error(errors, "observation_rank_defect", fid, f"coordinates={coordinates}")
        if fiber.get("joint_rank") != len(set(coordinates)) or fiber.get("joint_rank") != 21:
            _error(errors, "nonfaithful_observation_fiber", fid, str(fiber.get("joint_rank")))
        if fiber.get("execution") != "finite_exact_harmonic_coefficient_projection":
            _error(errors, "nonexecutable_observation_fiber", fid, str(fiber.get("execution")))
        if not fiber.get("source_derived_port_authority"):
            _error(errors, "support_does_not_authorize_ports", fid, "independent readout authority is required")
        if fiber.get("authority_basis") == "geometric_support_only":
            _error(errors, "support_does_not_authorize_ports", fid, "support is not executable capability")

    for corr in packet.get("typed_coincidences", []):
        if corr.get("same_rank") and corr.get("comparison_map") is None:
            if corr.get("disposition") != "typed_numerical_coincidence_only":
                _error(errors, "unauthorized_rank_coincidence_identification", corr["id"], "no source-derived comparison map")
        if corr.get("identified", False) and not corr.get("comparison_map"):
            _error(errors, "unauthorized_rank_coincidence_identification", corr["id"], "rank equality is not an isomorphism")

    return errors


def compile_packet(packet: dict[str, Any]) -> dict[str, Any]:
    base = compile_v2(packet)
    errors = [TypeErrorRecord(**x) for x in base["errors"]]
    errors.extend(validate_extension(packet))
    return {
        **base,
        "valid": not errors,
        "error_count": len(errors),
        "errors": [asdict(error) for error in errors],
        "topological_completion_count": len(packet.get("topological_completions", [])),
        "observation_fiber_count": len(packet.get("observation_fibers", [])),
        "extension": "strominger.functional-completion.v1",
    }
