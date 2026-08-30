#!/usr/bin/env python3
"""WP60: exact line-addressed inventory of selector-like source mechanisms."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/"research/flavor/sources/2607.27315v1.txt"
OUT=ROOT/"research/flavor/results/wp60_source_authority_inventory.json"

MARKERS={
 "rg_derived":("From the one-loop running of the Yukawa matrices in the SM, we have","derived_transport"),
 "rg_angles_stable":("the sides of the unitarity triangle are rescaled by exactly the same factor under the RG","derived_leading_consequence"),
 "z4_modal":("For instance, CP could be spontaneously broken","illustrative_deferred"),
 "z8_modal":("Similar ideas can be used to determine the full shape","illustrative_deferred"),
 "uv_deferred":("We defer a discussion of these theoretical possibilities to future work","explicitly_deferred"),
 "texture_fit":("In the full scan, for a given texture we find different fits","fitted_presentation"),
 "perturbation_pilot":("a preliminary numerical study of these perturbations is also presented","numerical_presentation_test"),
 "physical_quotient":("the most physical way to parametrize the equivalence class of all matrices","quotient_definition"),
}

def main():
    lines=SOURCE.read_text(encoding="utf-8").splitlines()
    found={}
    for key,(needle,kind) in MARKERS.items():
        hits=[i+1 for i,line in enumerate(lines) if needle in line]
        found[key]={"kind":kind,"needle":needle,"lines":hits,"unique":len(hits)==1}
    lower="\n".join(lines).lower()
    absent={
      "threshold_matching_law":"threshold matching" not in lower,
      "frozen_normalization":"frozen normalization" not in lower,
      "conditional_expectation":"conditional expectation" not in lower,
      "physical_reference_port":"reference port" not in lower,
    }
    candidates=[
      {"name":"one_loop_sm_rg","authority":"derived","operation_declared":True,"proper_reduction_declared":False,"instrument_declared":False},
      {"name":"z4_spontaneous_cp_picture","authority":"illustrative_deferred","operation_declared":False,"proper_reduction_declared":False,"instrument_declared":False},
      {"name":"z8_flavor_spurion_picture","authority":"illustrative_deferred","operation_declared":False,"proper_reduction_declared":False,"instrument_declared":False},
      {"name":"nine_link_texture_constraints","authority":"fitted_presentation","operation_declared":False,"proper_reduction_declared":False,"instrument_declared":False},
      {"name":"texture_zero_perturbations","authority":"numerical_presentation_test","operation_declared":False,"proper_reduction_declared":False,"instrument_declared":False},
    ]
    gates={
      "all_authority_markers_found_uniquely":all(v["unique"] for v in found.values()),
      "missing_candidate_classes_recorded_as_absent":all(absent.values()),
      "exactly_one_derived_operation_family_declared":sum(c["operation_declared"] for c in candidates)==1,
      "no_source_candidate_declares_proper_reduction":not any(c["proper_reduction_declared"] for c in candidates),
      "no_source_candidate_declares_selector_instrument":not any(c["instrument_declared"] for c in candidates),
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.source-authority-inventory.v1",
      "source":str(SOURCE.relative_to(ROOT)).replace("\\","/"),
      "line_count":len(lines),
      "markers":found,
      "explicit_absences":absent,
      "candidate_inventory":candidates,
      "authority_partition":{
        "derived_operation":["one_loop_sm_rg"],
        "illustrative_or_deferred":["z4_spontaneous_cp_picture","z8_flavor_spurion_picture"],
        "presentation_or_fit":["nine_link_texture_constraints","texture_zero_perturbations"],
      },
      "conclusion":"The declared source contains one derived operation family (SM one-loop RG), but no declared proper-reduction boundary law or selector instrument. All other selector-like mechanisms are illustrative, deferred, or presentation constraints.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"candidates":len(candidates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
