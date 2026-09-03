#!/usr/bin/env python3
"""Derive the q-divisor pole balance required of split-flag transport."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# A: q1=q2 at (E,E): remaining q3*q23*q31=3E*E*(E-6).
# B: q23=q2 at (E,0): remaining q1*q3*q31=(-E)*2E*(E-6).
A_lead=F(-1,18);B_lead=F(1,12) # coefficients of E^-2, excluding common H/Jacobian behavior
ratio=-A_lead/B_lead;assert ratio==F(2,3) and A_lead+ratio*B_lead==0
out={'schema':'marici.benincasa.cosmology-rees-split-flag-pole-balance.v1','flag_A':{'locus':'q1=q2 at (E,E)','remaining_q_product':'3 E^2 (E-6)','q_only_E_minus_2_coefficient':str(A_lead)},'flag_B':{'locus':'q23=q2 at (E,0)','remaining_q_product':'-2 E^2 (E-6)','q_only_E_minus_2_coefficient':str(B_lead)},'necessary_leading_balance':'weight_B/weight_A=2/3 if the transported K-half and Jacobian factors have the same leading value','constant_equal_weight_transport':False,'full_second_jet_transport_constructed':False,'exact_residual':'the q-divisors alone force singular E^-2 terms and a non-equal leading balance; H(E) on the two moving loci must be computed before this necessary ratio can be promoted to the actual transport','next_acceptance_test':'factor K(E) and choose H(E), evaluate H on both moving loci through sufficient E order, then solve cancellation and finite jet coefficients','passed':True};(R/'cosmology_rees_split_flag_pole_balance.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
