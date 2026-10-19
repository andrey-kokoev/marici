"""Validate local low-energy research inventory and strict no-promotion boundaries."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
NET = ROOT / "research/scattering/low-energy/contracts/low-energy-scattering-work-net.v1.json"
PINS = ROOT / "research/scattering/low-energy/contracts/low-energy-scattering-source-pins.v1.json"


def validate(net, pins):
    if net["registration"] != "local_research_net_not_registered_physical_target":
        raise ValueError("physical registration claim")
    if net["objective"]["outcome"] is not None or net["objective"]["target"] != "reviewed_low-energy_scattering_comparison":
        raise ValueError("root promoted")
    if net["source_pins"] != PINS.relative_to(ROOT).as_posix():
        raise ValueError("pins disconnected")
    if net["related_high_energy_assessment"] not in pins["source_sha256"]:
        raise ValueError("high-energy boundary missing")
    if net["regime"]["common_numeric_energy_interval"] is not None or net["regime"]["physical_species_or_energy_unit_selected"] is not False or net["regime"]["models_are_not_assumed_equivalent"] is not True:
        raise ValueError("different energy/channel types conflated")
    if any(net["boundary"].values()):
        raise ValueError("physical/formal promotion")
    expected = {
        "branch-scope-and-source-inventory": ("constructed", "scoped_inventory"),
        "neutron-two-rim-stationary-branch": ("source_report_located", "conditional_model"),
        "native-three-port-stationary-branch": ("source_report_located", "conditional_model"),
        "pentachoron-point-contact-branch": ("source_report_located", "conditional_model"),
        "low-energy-threshold-and-packet-audit": ("open", "open"),
        "cross-model-channel-typing": ("open", "open"),
        "low-energy-native-contact-selection": ("deferred_missing_native_principle", "open"),
        "low-energy-physical-preparation-and-readout": ("deferred_missing_physical_binding", "open"),
        "reviewed_low-energy_scattering_comparison": ("open", "open")
    }
    nodes = net["conjectures"]
    if [n["id"] for n in nodes] != list(expected):
        raise ValueError("missing or reordered obligation")
    seen = set()
    for node in nodes:
        name = node["id"]
        if (node["status"], node["verdict"]) != expected[name] or node["outcome"] is not None:
            raise ValueError("disposition promoted: " + name)
        if len(set(node["depends_on"])) != len(node["depends_on"]) or not set(node["depends_on"]) <= seen:
            raise ValueError("bad prerequisite order: " + name)
        if any(p not in pins["source_sha256"] and p != "research/scattering/low-energy/CONJECTURE-NET.md" for p in node.get("evidence", [])):
            raise ValueError("unpinned evidence: " + name)
        if name.endswith("stationary-branch") or name == "pentachoron-point-contact-branch":
            if node.get("source_result_imported_as_formal_proof") is not False:
                raise ValueError("historical source report promoted")
        seen.add(name)
    if net["frontier"] != ["low-energy-threshold-and-packet-audit", "cross-model-channel-typing"]:
        raise ValueError("frontier changed")
    root = nodes[-1]
    if set(root["depends_on"]) != {"low-energy-threshold-and-packet-audit", "cross-model-channel-typing", "low-energy-native-contact-selection", "low-energy-physical-preparation-and-readout"}:
        raise ValueError("root gate bypass")
    return True


def main():
    net, pins = json.loads(NET.read_text()), json.loads(PINS.read_text())
    checks = []
    validate(net, pins)
    checks.append("dependency_and_disposition_schema")
    for p, sha in pins["source_sha256"].items():
        f = ROOT / p
        if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != sha:
            raise ValueError("stale or missing source: " + p)
        checks.append("pinned:" + p)
    for name in ("physical_scattering_explained", "registered_physical_target", "models_identified", "high_energy_net_outcomes_imported"):
        hostile = copy.deepcopy(net)
        hostile["boundary"][name] = True
        try:
            validate(hostile, pins)
        except ValueError:
            checks.append("refused_promotion:" + name)
        else:
            raise AssertionError("promotion accepted: " + name)
    for name, mutation in (
        ("root", lambda c: c["objective"].update(outcome="++")),
        ("missing_native_gate", lambda c: c["conjectures"][-1]["depends_on"].remove("low-energy-native-contact-selection")),
        ("false_common_energy", lambda c: c["regime"].update(common_numeric_energy_interval=[0,4])),
        ("report_as_proof", lambda c: c["conjectures"][1].update(source_result_imported_as_formal_proof=True)),
    ):
        hostile = copy.deepcopy(net)
        mutation(hostile)
        try:
            validate(hostile, pins)
        except ValueError:
            checks.append("refused_promotion:" + name)
        else:
            raise AssertionError("promotion accepted: " + name)
    print(json.dumps({"status": "pass", "check_count": len(checks), "nodes": len(net["conjectures"]),
                      "pinned_sources": len(pins["source_sha256"]), "frontier": net["frontier"]}))


if __name__ == "__main__":
    main()
