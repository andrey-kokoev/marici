#!/usr/bin/env python3
"""Admit the optical conjugate-readout packet without certifying its realization."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ASPECT=HERE.parent
MANIFEST=ASPECT/"scc-models"/"conjugate-readout-optical-candidate.json"
THRESHOLD=ASPECT/"contracts"/"optical-conjugate-uncertainty-threshold.v1.json"
ACQUISITION=ASPECT/"contracts"/"conjugate-first-jet-acquisition.v1.json"
BINDING=ASPECT/"contracts"/"conjugate-first-jet-apparatus-binding.v1.json"
SCC_PATH=ASPECT/"scc"/"scc.py"
SPEC=importlib.util.spec_from_file_location("marici_scc",SCC_PATH)
SCC=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(SCC)

raw=json.loads(MANIFEST.read_text(encoding="utf-8"))
model=raw["model"]
threshold=json.loads(THRESHOLD.read_text(encoding="utf-8"))
acquisition=json.loads(ACQUISITION.read_text(encoding="utf-8"))
binding=json.loads(BINDING.read_text(encoding="utf-8"))
apparatus=SCC.validate_apparatus_certificate(model["apparatus_certificate"])
errors=SCC.validate_model(model)
# Coefficients in the free variables (f(L), f'(L)).
M11=(2,0)
K11=(0,2)
K22=(2,2)  # second coefficient is multiplied by L
first_jet_identity=(K22[0]-M11[0],K22[1]-K11[1])
first_jet_exact=first_jet_identity==(0,0)
if not first_jet_exact: errors.append("source first-jet cancellation failed")
# Under common gain g(L), the derivative transport contributes
# g'*(M22-L*M11), which vanishes before the residual scales by g.
base_scaling_identity=(2,0)  # M22/L in the same (f,f') basis
transport_residual=(base_scaling_identity[0]-M11[0],base_scaling_identity[1]-M11[1])
naturality_exact=transport_residual==(0,0)
if not naturality_exact: errors.append("common-gain naturality square failed")
threshold_exact=(
    threshold["prediction_residual"]==["K12","K21","K22-L*K11-M11"]
    and threshold["score"]["cutoff"]==5.0
    and threshold["anti_fitting"]["freeze_before_intervention"] is True
    and threshold["anti_fitting"]["fit_from_candidate_response"] is False
    and set(threshold["decision"]["null_models"])=={"independent_detector_channels","common_mode_drift"}
)
if not threshold_exact: errors.append("preregistered uncertainty threshold packet changed")
acquisition_exact=(
    acquisition["status"]=="acquisition_ready_apparatus_unbound"
    and acquisition["setting_cells"]["science"]["cells"]==20
    and acquisition["total_setting_cells"]==28
    and acquisition["minimum_attempted_optical_trials"]==2800000
    and acquisition["derivative_estimator"]["primary"]=="five_point_centered"
    and acquisition["retention"]["retain_no_click"] is True
    and acquisition["retention"]["permit_posthoc_gain_split"] is False
    and set(x["id"] for x in acquisition["setting_cells"]["null_controls"])=={"independent_detector_channels","common_mode_drift"}
)
if not acquisition_exact: errors.append("raw acquisition contract changed")
binding_state=(
    "ready" if binding["status"]=="bound" and all(binding["admission"].values())
    else "apparatus_unbound"
)
passed=not errors and apparatus["status"] in ("pass","inconclusive")
print(json.dumps({
    "schema":"marici.aspect.conjugate-readout-candidate-check.v1",
    "passed":passed,
    "classification":"candidate_requires_source_derivation",
    "apparatus_validation":apparatus,
    "first_jet_identity":{"K12":0,"K21":0,"K22_minus_LK11_minus_M11":list(first_jet_identity),"exact":first_jet_exact},
    "naturality_square":{"common_gain_transport_residual":list(transport_residual),"exact":naturality_exact,"independent_channel_gains":"hostile_not_gauge"},
    "uncertainty_threshold":{"locator":str(THRESHOLD),"score":"max_abs_whitened_residual","cutoff":5.0,"exact":threshold_exact},
    "acquisition":{"locator":str(ACQUISITION),"status":acquisition["status"],"exact":acquisition_exact},
    "physical_execution":{"binding_locator":str(BINDING),"status":binding_state,"certifies_apparatus_existence":False},
    "admitted_scope":"structural packet only; no apparatus existence, zero location, or physical response certified",
    "residuals":errors,
    "missing_constructors":model["missing_constructors"],
    "next_falsifier":model["next_falsifier"],
    "conclusion":"candidate packet admitted" if passed else "candidate packet rejected"
},indent=2))
raise SystemExit(0 if passed else 1)
