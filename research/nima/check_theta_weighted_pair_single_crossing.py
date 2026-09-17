#!/usr/bin/env python3
"""Derive the single-crossing law for paired weighted theta correlations."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];D,L=s.symbols('D L',positive=True);ell=s.Function('ell');# h=(D+L)W(D+L)/(D W(D)), W=exp ell.
logh=s.log(D+L)-s.log(D)+ell(D+L)-ell(D);der=s.diff(logh,D);expected=1/(D+L)-1/D+s.diff(ell(D+L),D)-s.diff(ell(D),D);checks={'log_ratio_derivative':s.simplify(der-expected)==0,'rational_part_strictly_negative':s.simplify(1/(D+L)-1/D)==-L/(D*(D+L))}
out={'schema':'marici.nima.theta-weighted-pair-single-crossing.v1','ratio':'h_L(D)=(D+L)W_a(D+L)/(D W_a(D))','derivative':'d log h/dD = 1/(D+L)-1/D + (log W_a)prime(D+L)-(log W_a)prime(D)','input_theorem':'W_a is positive and log-concave as the correlation of the log-concave completed theta density (Prekopa closure)','conclusion':'h_L is strictly decreasing; D W_a(D)-(D+L)W_a(D+L) has at most one zero on (0,L), changing from negative to positive if it crosses','checks':checks,'passed':all(checks.values()),'remaining_gate':'compare the mass of the initial negative lobe and terminal positive lobe with the proved positive J-current','claim_boundary':'single-crossing control does not determine the integrated sign','rh_proved':False};p=ROOT/'research/nima/results/theta-weighted-pair-single-crossing.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
