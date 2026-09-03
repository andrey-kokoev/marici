#!/usr/bin/env python3
"""Solve the exact singular cancellation between the two split flag values."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# Chosen branches: w_A=E(E^2-36), w_B=E^2(E+6).
# Flag value factors excluding the common numerator/Jacobian convention:
# F_A=1/[3E^3(E-6)(E^2-36)], F_B=-1/[2E^4(E-6)(E+6)].
# Therefore F_A/F_B=-2E/[3(E-6)].
for E in [1,2,3,4,5]:
 FA=F(1,3*E**3*(E-6)*(E*E-36));FB=F(-1,2*E**4*(E-6)*(E+6));assert FA/FB==F(-2*E,3*(E-6))
out={'schema':'marici.benincasa.cosmology-rees-valuation-matched-transport.v1','branches':{'w_A':'E(E^2-36)','w_B':'E^2(E+6)'},'flag_factors':{'F_A':'1/[3E^3(E-6)(E^2-36)]','F_B':'-1/[2E^4(E-6)(E+6)]'},'exact_cancelling_weight_ratio':'weight_B/weight_A=2E/[3(E-6)]','leading_ratio':'-E/9+O(E^2)','cancelling_combination_value':'0 identically','regular_nonzero_transport':'add a correction delta_B(E) to weight_B; since F_B has order E^-4, coefficients of delta_B at E^4,E^5,E^6 independently set the finite, first-jet, and second-jet values','normalization_effect':'tau normalization fixes only the E^4 correction coefficient','second_jet_unique':False,'exact_residual':'regularity plus tau normalization leaves the first and second jet coefficients free; assembled adjoint closure or a source transport law is still required','passed':True};(R/'cosmology_rees_valuation_matched_transport.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
