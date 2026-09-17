#!/usr/bin/env python3
"""Collapse the adjacent-band weighted correlation to one canonical two-band sine moment."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];D,E,L,b=s.symbols('D E L b',positive=True,real=True);W=s.Function('W');# Under bL=pi, sin(b(E-L))=-sin(bE).
phase=s.simplify(s.sin(b*(E-L)).subs(L,s.pi/b)+s.sin(b*E));checks={'half_period_phase_reversal':phase==0,'pointwise_weighted_sign_not_available':True}
out={'schema':'marici.nima.theta-weighted-band-correlation-collapse.v1','assumption':'L=pi/b','identity':'integral_0^L sin(bD)[D W_a(D)-(D+L)W_a(D+L)] dD = integral_0^(2L) D W_a(D) sin(bD) dD','paired_form':'integral_0^L sin(bD)[D W_a(D)-(D+L)W_a(D+L)] dD','checks':checks,'passed':all(checks.values()),'interpretation':'the hostile entrance lobe is not estimated separately; it is paired with the next half-period in one source sine moment','sufficient_condition':'D W_a(D) >= (D+L) W_a(D+L) for almost every D in (0,L)','sufficient_condition_status':'not globally available because D W_a(D) rises from zero near D=0','remaining_exact_gate':'positivity of the canonical two-band sine moment after inclusion of the already positive J-current','claim_boundary':'algebraic band sewing only; no sign is claimed','rh_proved':False};p=ROOT/'research/nima/results/theta-weighted-band-correlation-collapse.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
