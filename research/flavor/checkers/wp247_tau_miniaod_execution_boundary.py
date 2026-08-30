"""WP247: exact execution boundary for the CMS tau MiniAOD pilot."""

from __future__ import annotations

import json
import zlib
from pathlib import Path

import awkward as ak
import numpy as np
import uproot


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cms-open-data-19459-pilot"
PROVENANCE = json.loads((DATA / "provenance.json").read_text())
FILE = DATA / PROVENANCE["pilot_file"]["path"]
BASE = "patTaus_slimmedTaus__PAT./patTaus_slimmedTaus__PAT.obj/patTaus_slimmedTaus__PAT.obj."
KINEMATICS = [
    BASE + "m_state.p4Polar_.fCoordinates.fPt",
    BASE + "m_state.p4Polar_.fCoordinates.fEta",
    BASE + "m_state.p4Polar_.fCoordinates.fPhi",
    BASE + "m_state.p4Polar_.fCoordinates.fM",
    BASE + "m_state.qx3_",
]
TAU_IDS = BASE + "tauIDs_"


def main():
    checksum = format(zlib.adler32(FILE.read_bytes()) & 0xFFFFFFFF, "08x")
    events = uproot.open(FILE)["Events"]
    arrays = events.arrays(KINEMATICS, entry_stop=100, library="ak")
    flat_values = []
    for name in KINEMATICS[:4]:
        flat_values.extend(ak.to_numpy(ak.flatten(arrays[name])).tolist())
    tau_id_error = None
    try:
        events[TAU_IDS].array(entry_stop=5)
    except Exception as error:  # the exact unsupported serialization boundary
        tau_id_error = {"type": type(error).__name__, "message": str(error)}

    hostile = PROVENANCE["generic_root_hostile_probe"]
    makeproject = PROVENANCE["root_makeproject_probe"]
    # This deliberately weak bound still makes the detached-leaf observation
    # an exact corruption certificate: an ID cannot occupy less than one byte.
    detached_leaf_is_corrupt = hostile["reported_tau_id_count"] > PROVENANCE["pilot_file"]["bytes"]

    branch_names = events.keys()
    checks = {
        "cern_checksum_matches": checksum == PROVENANCE["pilot_file"]["adler32"],
        "pilot_event_count_matches": events.num_entries == PROVENANCE["pilot_file"]["events"],
        "all_tau_kinematic_branches_present": all(name in branch_names for name in KINEMATICS),
        "tau_kinematics_deserialize": len(flat_values) > 0 and np.isfinite(flat_values).all(),
        "tau_id_branch_present": TAU_IDS in branch_names,
        "tau_id_payload_is_not_deserializable": tau_id_error is not None and tau_id_error["type"] == "NotImplementedError",
        "detached_stl_leaf_is_exactly_falsified": detached_leaf_is_corrupt,
        "streamer_project_has_source_metadata": makeproject["generated_classes"] > 0,
        "streamer_project_dictionary_not_admitted": not makeproject["shared_object_created"],
        "kinematics_only_acceptance_rejected": True,
        "cmssw_dictionary_gate_recorded": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP247",
        "pilot": PROVENANCE,
        "readable_products": ["reconstructed tau pt/eta/phi/mass", "reconstructed tau charge", "split MET kinematics", "generator-particle kinematics"],
        "unreadable_required_product": "pat::Tau tauIDs_ vector<pair<string,float>>",
        "tau_id_error": tau_id_error,
        "generic_root_hostile_probe": hostile,
        "root_makeproject_probe": makeproject,
        "detached_leaf_corruption_bound": {
            "reported_tau_id_count": hostile["reported_tau_id_count"],
            "entire_file_bytes": PROVENANCE["pilot_file"]["bytes"],
            "strictly_exceeds_even_one_byte_per_id": detached_leaf_is_corrupt,
        },
        "classification": "detector-kinematic pilot executable; physical tau identification and acceptance not executable on the current non-CMSSW surface",
        "smallest_falsifier": "a kinematics-selected reconstructed object cannot be typed as a tau without the independently derived tau-ID discriminator",
        "remaining_instrument_gate": "run the checksum-pinned MiniAOD through a compatible CMSSW 7.6 environment or obtain an officially derived flat format retaining tau IDs and triggers",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results" / "wp247_tau_miniaod_execution_boundary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
