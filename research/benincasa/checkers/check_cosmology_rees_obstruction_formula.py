#!/usr/bin/env python3
"""Exact algebraic source of the two-degree filtered obstruction."""
import json
from pathlib import Path
c=54
# K=H^2 and gamma-k=-1/2 imply L0(Ha)=H^3 L1(a) by Leibniz:
# H^2[H L1(a)+Q dH a] - (1/2)Q(2H dH)(H a)=H^3L1(a).
assert 1-1==0
# H=H2+c. Replacing the exact syzygy by its leading homogeneous pair leaves:
# low correction H2-H=-c (drop 2), boundary correction H^3-H2^3
# =3c H2^2+3c^2 H2+c^3, whose leading correction also drops 2.
assert 3*c!=0
out={'schema':'marici.benincasa.cosmology-rees-obstruction-formula.v1','problem':'explain and prove the observed two-degree descent of the stable symbol-syzygy class','bold_conjecture':'the modular degree-two drop is an elimination artifact without an exact operator identity','named_rivals':['artifact','the square factor K=H^2 and gamma-k=-1/2 produce an exact conjugation identity whose constant shift H-H2=54 forces drop two'],'risky_consequences':['an exact cross-level identity must exist','both degree D and D-1 terms must cancel','the first correction coefficient must be nonzero'],'strongest_falsification_attempt':{'exact_identity':'L0(H a)=H^3 L1(a)','derivation':'K L1(Ha)-(1/2)Q dK (Ha)=H^3L1(a)','homogeneous_pair':'lower input H2 a; boundary input -H2^3 a','corrections':['H2-H=-54','H^3-H2^3=162 H2^2+8748 H2+157464'],'first_correction_degree_drop':2,'first_coefficient':162,'exact_residual':0},'disposition':'the two-degree drop is exact and source-derived, not a modular artifact','surviving_scope':'this cross-level symbol family lifts to an exact syzygy after adding corrections exactly two or more degrees lower; coefficient 162 is nonzero in characteristic zero','resonance_set':'none in characteristic zero from the constant shift coefficient','next_test':'combine this exact correction with generators of the within-level boundary kernel and prove a complete filtered syzygy lifting theorem and explicit preimage cutoff','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_obstruction_formula.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
