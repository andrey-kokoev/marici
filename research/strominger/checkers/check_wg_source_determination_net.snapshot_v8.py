#!/usr/bin/env python3
"""Audit the owner-local net, not the truth of its mathematical conjectures.

--freeze creates the first immutable pin inventory; it never replaces one.
No compiler, Git, graph service or parent-net mutation is invoked.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = "research/strominger/contracts/wg-source-determination-conjecture-net.v1.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path(name):
    p = (ROOT / name).resolve()
    require(p.is_relative_to(ROOT), f"Outside repository: {name}")
    return p


def load(name):
    return json.loads(path(name).read_text(encoding="utf-8"))


def digest(name):
    return hashlib.sha256(path(name).read_bytes()).hexdigest()


def validate(net):
    nodes = net["nodes"]
    by_id = {n["id"]: n for n in nodes}
    require(len(by_id) == len(nodes), "Duplicate node ID")
    root = net["objective"]["target"]
    require(root in by_id, "Unknown root")
    require(net["objective"]["status"] == "open", "v1 objective is not completed")
    require(net["objective"]["formal_outcome"] is None, "No overall formal outcome")
    require(net["objective"]["physical_validation"] is False, "No physical validation")
    for key in (
        "admission_implies_source_determination",
        "interpreted_equivalence_implies_code_admission",
        "E_attachment_is_CW_attachment",
        "forward_lift_involution_from_vertex_involution",
        "finite_diagrams_imply_global_coherence",
        "registration_implies_physical_validation",
        "automatic_root_resolution",
    ):
        require(net["semantics"][key] is False, f"Forbidden inference: {key}")
    for a in net["attachments"]:
        require(a["imports_proof"] is False and a["mutates_parent"] is False,
                "Cross-links cannot import proof or mutate parents")
        parent = load(a["contract"])
        ids = {n["id"] for n in parent.get("nodes", parent.get("conjectures", []))}
        require(set(a["nodes"]) <= ids, "Unknown parent node")
    artifacts = net["artifacts"]
    for a in artifacts.values():
        require(set(a["supports"]) <= by_id.keys(), "Unknown evidence support node")
        for name in a["paths"] + a["checks"] + a["receipts"]:
            require(path(name).is_file(), f"Missing artifact: {name}")
    for n in nodes:
        for key in ("statement", "scope", "acceptance", "falsifier"):
            require(bool(n[key]), f"Missing {key}: {n['id']}")
        require(n["status"] in ("open", "resolved"), "Unknown status")
        require(len(n["depends_on"]) == len(set(n["depends_on"])), "Duplicate dependency")
        require(set(n["depends_on"]) <= by_id.keys(), "Unknown dependency")
        require(set(n["evidence"]) <= artifacts.keys(), "Unknown evidence")
        if n["status"] == "open":
            require(n["verdict"] == "open", "Open node has a terminal verdict")
            require(n.get("next_action") and n.get("deliverable"), "Missing next deliverable")
        else:
            require(n["verdict"] in ("declared", "constructed", "rejected"), "Unknown verdict")
            require(any(n["id"] in artifacts[a]["supports"] for a in n["evidence"]),
                    "No evidence labelled for this exact completed claim")
    require(by_id[root]["status"] == "open", "Root cannot be closed by a structural audit")
    require(by_id["bare-atomic-higher-admission"]["verdict"] == "rejected",
            "Envelope success cannot reverse literal-Code rejection")
    require(by_id["one-comparison-two-attachment-coherence"]["diagram_bound"] ==
            {"original_source_comparisons": 1, "source_attachments": 2},
            "Old diagram does not prove the larger one")

    if "two-comparison-inverse-facing-control" in by_id:
        require(by_id["two-comparison-inverse-facing-control"]["diagram_bound"] ==
                {"original_source_comparisons": 2, "source_attachments": 2,
                 "second_comparison": "inverse-facing", "arbitrary_forward_lift_involution": False},
                "Inverse-facing control is not arbitrary forward-lift composition")

    if "forward-lift-binary-composition" in by_id:
        require(by_id["forward-lift-binary-composition"]["claim_bound"] ==
                {"arbitrary_initial_Resolve_inputs": True, "arbitrary_finite_chains": True,
                 "propositional_forward_square": True, "judgmental_cancellation": False,
                 "coherent_C2_action": False, "proof_irrelevance_of_Resolve": False,
                 "Ready_identity_claimed": False},
                "Binary transport law is not judgmental cancellation or a fully coherent action")

    if "generated-reader-image-classification" in by_id:
        require(by_id["generated-reader-image-classification"]["claim_bound"] ==
                {"generated_fragment_only": True, "reader_labelled_normal_forms": 5,
                 "all_Body_claimed": False, "arbitrary_history_contractibility": False,
                 "filler_existence_requires_image_agreement": True,
                 "parameter_program_certification_complete": False},
                "Reader classification cannot erase its fragment or existence/provenance boundaries")

    if "circle-span-provenance-audit" in by_id:
        require(by_id["circle-span-provenance-audit"]["scope_bound"] ==
                {"first_circle_only": True, "native_rule_changes": False,
                 "original_seeds_extended": False, "all_WG_circle_obstruction": False,
                 "source_selects_span_policy": False, "complete_action_coherence": False},
                "Circle audit cannot upgrade admission, scope or source-selection claims")
        require(by_id["outgoing-span-topology-family"]["scope_bound"] ==
                {"policy": "Unit <- Out(v) -> Unit", "varied_input": "pointed_source_vertex",
                 "graph_edge_ablation": False, "full_action_coherence": False},
                "The contrast varies pointed input under a declared policy, not the graph or complete action")

    if "free-source-graph-realization" in by_id:
        require(by_id["free-source-graph-realization"]["scope_bound"] ==
                {"reuses_actual_predecessor": True, "bouquet_generators": 3,
                 "universal_mapping_equivalence": True, "WG_selects_free_realization": False,
                 "new_seed_face_relations": False, "physical_validation": False},
                "Free realization is a three-circle theorem relative to a declared task, not WG selection")

    if "filled-source-return-classification" in by_id:
        require(by_id["filled-source-return-classification"]["scope_bound"] ==
                {"actual_filled_package_fixed": True, "matched_source_edges": 5,
                 "matching_witnesses_included": True, "extension_space_is_based_loop_space": True,
                 "extra_ADB_filling_gives_contractible_choices": True,
                 "ADB_filling_already_supplied": False, "target_itself_is_circle": False},
                "Filled-package return classification cannot supply its missing premise or identify the target with a circle")

    if ("canonical-comparison-synthesis" in by_id and
            by_id["canonical-comparison-synthesis"]["status"] == "resolved"):
        require(by_id["canonical-comparison-synthesis"]["claim_bound"] ==
                {"generated_fragment_only": True, "extra_equivalence_or_agreement_input": False,
                 "actual_operand_terms_retained": True, "separating_vertex_on_refusal": True,
                 "complete_for_compatible_fillers": True, "inherited_parameter_origins_certified": False,
                 "all_native_WG_decided": False},
                "Comparison synthesis derives new parameters only for actual Fragment operands")

    visiting, done = set(), set()

    def visit(key):
        require(key not in visiting, "Dependency cycle")
        if key in done:
            return
        visiting.add(key)
        for dep in by_id[key]["depends_on"]:
            visit(dep)
        visiting.remove(key)
        done.add(key)

    for key in by_id:
        visit(key)
    adjacency = {key: set() for key in by_id}
    for n in nodes:
        for dep in n["depends_on"]:
            adjacency[n["id"]].add(dep)
            adjacency[dep].add(n["id"])
    for r in net["relations"]:
        require(r["from"] in by_id and r["to"] in by_id and r["kind"], "Bad relation")
        adjacency[r["from"]].add(r["to"])
        adjacency[r["to"]].add(r["from"])
    reached, todo = set(), [root]
    while todo:
        key = todo.pop()
        if key not in reached:
            reached.add(key)
            todo.extend(adjacency[key] - reached)
    require(reached == set(by_id), "Disconnected node")
    ready = [n for n in nodes if n["status"] == "open" and not n.get("blocked_by")
             and all(by_id[d]["status"] == "resolved" for d in n["depends_on"])]
    ready.sort(key=lambda n: (n["priority"], n["id"]))
    require(net["frontier"] == [n["id"] for n in ready], "Stale frontier/order")
    require(ready and net["recommended_start"] == ready[0]["id"], "Stale recommendation")
    return {"nodes": len(nodes), "verdicts": dict(Counter(n["verdict"] for n in nodes)),
            "frontier": net["frontier"], "connected": True, "dependency_DAG": True}


def receipt_inventory(net):
    inventory, names = [], set()
    for a in net["artifacts"].values():
        for name in a["receipts"]:
            receipt = load(name)
            require(receipt.get("status") == "pass", f"Nonpassing stored receipt: {name}")
            if receipt.get("dependency_manifest"):
                require(digest(receipt["dependency_manifest"]) == receipt["dependency_manifest_sha256"],
                        "Dependency manifest drift")
            hashes = receipt.get("source_hashes", {})
            require(bool(hashes), f"Receipt has no source hashes: {name}")
            for source, expected in hashes.items():
                require(path(source).is_file(), f"Receipt source unavailable: {source}")
                require(digest(source) == expected, f"Stale receipt source: {source}")
                names.add(source)
            inventory.append({"receipt": name, "recorded_status": receipt["status"],
                              "recorded_source_hashes_matched": len(hashes),
                              "proof_rerun_this_audit": False})
    return inventory, names


def pin_names(net, receipt_sources):
    names = set(receipt_sources)
    names.update((CONTRACT, net["packet"], net["current_pointer"], net["validator"]))
    names.update(a["contract"] for a in net["attachments"])
    for a in net["artifacts"].values():
        names.update(a["paths"] + a["checks"] + a["receipts"])
    return sorted(names)


def corruption_controls(net):
    def node(d, key):
        return next(n for n in d["nodes"] if n["id"] == key)

    def disconnect_topology(d):
        target = "topological-realization-bridge"
        for n in d["nodes"]:
            n["depends_on"] = [] if n["id"] == target else [x for x in n["depends_on"] if x != target]
        d["relations"] = [r for r in d["relations"] if target not in (r["from"], r["to"])]

    cases = {
        "duplicate_id": lambda d: d["nodes"].append(copy.deepcopy(d["nodes"][0])),
        "unknown_dependency": lambda d: d["nodes"][0]["depends_on"].append("absent"),
        "cycle": lambda d: d["nodes"][0]["depends_on"].append(d["objective"]["target"]),
        "stale_frontier": lambda d: d["frontier"].append("declared-local-contract"),
        "stale_recommendation": lambda d: d.update(recommended_start="physical-adequacy"),
        "parent_proof_import": lambda d: d["attachments"][0].update(imports_proof=True),
        "unknown_parent_node": lambda d: d["attachments"][0]["nodes"].append("absent"),
        "premature_root": lambda d: node(d, d["objective"]["target"]).update(
            status="resolved", verdict="constructed"),
        "unsupported_new_theorem": lambda d: node(d, "source-comparison-composition").update(
            status="resolved", verdict="constructed"),
        "atomic_rejection_erasure": lambda d: node(d, "bare-atomic-higher-admission").update(
            verdict="constructed"),
        "diagram_scope_inflation": lambda d: node(d, "one-comparison-two-attachment-coherence")[
            "diagram_bound"].update(original_source_comparisons=2),
        "admission_as_generation": lambda d: d["semantics"].update(
            admission_implies_source_determination=True),
        "attachment_as_CW": lambda d: d["semantics"].update(E_attachment_is_CW_attachment=True),
        "physical_upgrade": lambda d: d["objective"].update(physical_validation=True),
        "disconnected_branch": disconnect_topology,
    }
    if any(n["id"] == "two-comparison-inverse-facing-control" for n in net["nodes"]):
        cases["inverse_control_as_forward_lift_involution"] = lambda d: node(
            d, "two-comparison-inverse-facing-control")["diagram_bound"].update(
                arbitrary_forward_lift_involution=True)
    if any(n["id"] == "forward-lift-binary-composition" for n in net["nodes"]):
        cases["binary_law_as_coherent_action"] = lambda d: node(
            d, "forward-lift-binary-composition")["claim_bound"].update(coherent_C2_action=True)
    if any(n["id"] == "generated-reader-image-classification" for n in net["nodes"]):
        cases["fragment_theorem_as_all_Body"] = lambda d: node(
            d, "generated-reader-image-classification")["claim_bound"].update(all_Body_claimed=True)
        cases["uniqueness_as_unconditional_existence"] = lambda d: node(
            d, "generated-reader-image-classification")["claim_bound"].update(
                filler_existence_requires_image_agreement=False)
    if any(n["id"] == "circle-span-provenance-audit" for n in net["nodes"]):
        cases["carrier_obstruction_as_all_WG_impossibility"] = lambda d: node(
            d, "circle-span-provenance-audit")["scope_bound"].update(all_WG_circle_obstruction=True)
        cases["native_circle_admission_as_source_selection"] = lambda d: node(
            d, "circle-span-provenance-audit")["scope_bound"].update(source_selects_span_policy=True)
    if any(n["id"] == "free-source-graph-realization" for n in net["nodes"]):
        cases["free_realization_as_WG_selection"] = lambda d: node(
            d, "free-source-graph-realization")["scope_bound"].update(WG_selects_free_realization=True)
        cases["three_circle_graph_as_single_circle"] = lambda d: node(
            d, "free-source-graph-realization")["scope_bound"].update(bouquet_generators=1)
    if any(n["id"] == "filled-source-return-classification" for n in net["nodes"]):
        cases["extra_ADB_filling_as_source_fact"] = lambda d: node(
            d, "filled-source-return-classification")["scope_bound"].update(ADB_filling_already_supplied=True)
        cases["loop_valued_extensions_as_circle_target"] = lambda d: node(
            d, "filled-source-return-classification")["scope_bound"].update(target_itself_is_circle=True)
    if any(n["id"] == "canonical-comparison-synthesis" and n["status"] == "resolved" for n in net["nodes"]):
        cases["supplied_comparison_as_synthesis"] = lambda d: node(
            d, "canonical-comparison-synthesis")["claim_bound"].update(extra_equivalence_or_agreement_input=True)
        cases["new_parameters_as_inherited_origin_certification"] = lambda d: node(
            d, "canonical-comparison-synthesis")["claim_bound"].update(inherited_parameter_origins_certified=True)
    outcomes = []
    for label, mutate in cases.items():
        bad = copy.deepcopy(net)
        mutate(bad)
        try:
            validate(bad)
        except ValueError as exc:
            outcomes.append({"case": label, "rejected": True, "reason": str(exc)})
        else:
            raise ValueError(f"Corruption control accepted: {label}")
    return outcomes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze", action="store_true", help="Create pins only if absent")
    args = parser.parse_args()
    net = load(CONTRACT)
    output = path(net["audit_receipt"])
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        summary = validate(net)
        pointer = load(net["current_pointer"])
        require(pointer["contract"] == CONTRACT and pointer["id"] == net["id"] and
                pointer["owner"] == net["owner"] and pointer["packet"] == net["packet"] and
                pointer["publication"] == "owner_local_only", "Bad current pointer")
        inventory, sources = receipt_inventory(net)
        controls = corruption_controls(net)
        hashes = {name: digest(name) for name in pin_names(net, sources)}
        pins = path(net["pins"])
        expected = {"schema": "marici.wg-source-determination-pins.v1", "net": net["id"],
                    "scope": net["evidence_policy"]["current_pin_scope"], "sha256": hashes}
        if args.freeze and not pins.exists():
            with pins.open("x", encoding="utf-8") as stream:
                json.dump(expected, stream, indent=2)
                stream.write("\n")
        require(pins.is_file(), "Missing pins; initialize once with --freeze")
        require(load(net["pins"]) == expected, "Pin drift: review a new snapshot, do not refresh silently")
        report = {"status": "pass", "audit_kind": "structure_and_recorded_evidence_inventory_only",
                  "net": net["id"], **summary, "pinned_files": len(hashes),
                  "parent_contracts_unchanged_from_pins": True,
                  "formal_proofs_rerun": False, "complete_transitive_formal_closure_pinned": False,
                  "physical_validation": False, "graph_service_publication": False,
                  "receipts": inventory, "corruption_controls": controls}
    except (ValueError, KeyError, OSError) as exc:
        report = {"status": "fail", "audit_kind": "structure_and_recorded_evidence_inventory_only",
                  "error": str(exc), "failure_is_mathematical_disproof": False}
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        raise SystemExit(str(exc)) from exc
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "nodes", "verdicts", "pinned_files", "frontier")}))
    print(f"Corruption controls: {len(controls)} rejected; formal proofs not rerun.")


if __name__ == "__main__":
    main()
