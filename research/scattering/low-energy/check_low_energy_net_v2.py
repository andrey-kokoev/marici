"""Pin and disposition check for distinct low-energy branches and photon gate."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = "research/scattering/low-energy/contracts/low-energy-scattering-work-net.v2.json"
PINFILE = "research/scattering/low-energy/contracts/low-energy-scattering-source-pins.v2.json"
NOTE = "research/scattering/low-energy/CONJECTURE-NET.md"
SHAPE = "research/voevodsky/braid-composition-effective-shape-interaction-operators.md"
AUDIT = "research/voevodsky/shape-interaction-finite-operator-audit.md"


def validate(net, pins):
    if net["schema"] != "marici.scattering.low-energy-work-net.v2" or net["supersedes"] != CONTRACT.replace('.v2.', '.v1.'):
        raise ValueError("version mismatch")
    if net["registration"] != "local_research_net_not_registered_physical_target" or net["objective"]["outcome"] is not None:
        raise ValueError("physical registration or root promotion")
    if net["source_pins"] != PINFILE or net["related_high_energy_assessment"] not in pins["source_sha256"]:
        raise ValueError("evidence pins disconnected")
    regime = net["regime"]
    if regime["common_numeric_energy_interval"] is not None or regime["physical_species_or_energy_unit_selected"] is not False or regime["models_are_not_assumed_equivalent"] is not True:
        raise ValueError("branches conflated")
    if any(net["boundary"].values()):
        raise ValueError("physical/photon/formal promotion")
    expected = {
        "branch-scope-and-source-inventory": ("constructed", "scoped_inventory"),
        "neutron-two-rim-stationary-branch": ("source_report_located", "conditional_model"),
        "native-three-port-stationary-branch": ("source_report_located", "conditional_model"),
        "pentachoron-point-contact-branch": ("source_report_located", "conditional_model"),
        "shape-merge-split-two-three-output-candidate": ("source_report_located", "conditional_operator_model"),
        "low-energy-threshold-and-packet-audit": ("open", "open"),
        "cross-model-channel-typing": ("open", "open"),
        "electron-positron-two-three-photon-channel-realization": ("open", "open"),
        "low-energy-native-contact-selection": ("deferred_missing_native_principle", "open"),
        "low-energy-physical-preparation-and-readout": ("deferred_missing_physical_binding", "open"),
        "reviewed_low-energy_scattering_comparison": ("open", "open"),
    }
    nodes = net["conjectures"]
    if [n["id"] for n in nodes] != list(expected):
        raise ValueError("missing/reordered node")
    seen = set()
    for n in nodes:
        key = n["id"]
        if (n["status"], n["verdict"]) != expected[key] or n["outcome"] is not None:
            raise ValueError("disposition promoted: " + key)
        if len(n["depends_on"]) != len(set(n["depends_on"])) or not set(n["depends_on"]) <= seen:
            raise ValueError("invalid DAG: " + key)
        if not set(n.get("evidence", [])) <= (set(pins["source_sha256"]) | {NOTE}):
            raise ValueError("unpinned source: " + key)
        if key in {"neutron-two-rim-stationary-branch", "native-three-port-stationary-branch", "pentachoron-point-contact-branch", "shape-merge-split-two-three-output-candidate"} and n.get("source_result_imported_as_formal_proof") is not False:
            raise ValueError("historical report promoted: " + key)
        seen.add(key)
    by = {n["id"]: n for n in nodes}
    shape = by["shape-merge-split-two-three-output-candidate"]
    if {SHAPE, AUDIT} - set(shape["evidence"]) or any(shape[k] is not False for k in ("physical_two_photon_channel_constructed", "physical_three_photon_channel_constructed", "ratio_372_derived_without_fitting")):
        raise ValueError("abstract channels relabeled photons or fitted ratio promoted")
    photon = by["electron-positron-two-three-photon-channel-realization"]
    if shape["id"] not in photon["depends_on"] or photon["status"] != "open":
        raise ValueError("photon gate bypass")
    if shape["id"] not in by["cross-model-channel-typing"]["depends_on"]:
        raise ValueError("candidate omitted from comparison")
    if set(by["reviewed_low-energy_scattering_comparison"]["depends_on"]) != {
        "low-energy-threshold-and-packet-audit", "cross-model-channel-typing", photon["id"],
        "low-energy-native-contact-selection", "low-energy-physical-preparation-and-readout"}:
        raise ValueError("root gate bypass")
    if net["frontier"] != ["low-energy-threshold-and-packet-audit", "cross-model-channel-typing", photon["id"]]:
        raise ValueError("frontier changed")
    return True


def main():
    net = json.loads((ROOT / CONTRACT).read_text(encoding="utf-8"))
    pins = json.loads((ROOT / PINFILE).read_text(encoding="utf-8"))
    validate(net, pins)
    checks = ["net_disposition"]
    for name, sha in pins["source_sha256"].items():
        path = ROOT / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != sha:
            raise ValueError("stale source pin: " + name)
        checks.append("pinned:" + name)
    for key in ("physical_scattering_explained", "two_photon_channel_physically_identified", "three_photon_channel_physically_identified", "ratio_372_predicted", "registered_physical_target"):
        bad = copy.deepcopy(net)
        bad["boundary"][key] = True
        try:
            validate(bad, pins)
        except ValueError:
            checks.append("refused:" + key)
        else:
            raise AssertionError("promoted: " + key)
    for key, modify in (
        ("fit_ratio", lambda c: c["conjectures"][4].update(ratio_372_derived_without_fitting=True)),
        ("rename_two_photons", lambda c: c["conjectures"][4].update(physical_two_photon_channel_constructed=True)),
        ("delete_photon_gate", lambda c: c["conjectures"][-1]["depends_on"].remove("electron-positron-two-three-photon-channel-realization")),
        ("root", lambda c: c["objective"].update(outcome="++")),
    ):
        bad = copy.deepcopy(net)
        modify(bad)
        try:
            validate(bad, pins)
        except ValueError:
            checks.append("refused:" + key)
        else:
            raise AssertionError("promoted: " + key)
    print(json.dumps({"status": "pass", "checks": len(checks), "nodes": len(net["conjectures"]), "pinned_sources": len(pins["source_sha256"]), "frontier": net["frontier"]}))


if __name__ == "__main__":
    main()
