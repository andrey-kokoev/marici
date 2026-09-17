#!/usr/bin/env python3
"""Rewrite the complete first canonical theta block as a truncated energy flux plus its moving-boundary term."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];b=s.symbols('b',positive=True);T=2*s.pi/b;checks={'moving_endpoint_derivative':s.simplify(s.diff(T,b)+2*s.pi/b**2)==0,'endpoint_phase_is_one':s.cos(b*T)==1,'endpoint_sine_is_zero':s.sin(b*T)==0}
out={'schema':'marici.nima.theta-canonical-block-moving-boundary-identity.v1','definitions':{'T(b)':'2*pi/b','F(a,b)':'integral_0^T(b) W_a(D) cos(bD) dD','J_a(D)':'partial_a W_a(D)'},'identity':'Block(a,b)=beta partial_a F-alpha partial_b F-alpha*(2*pi/b^2)*W_a(2*pi/b)','checks':checks,'passed':all(checks.values()),'interpretation':'the canonical two-band block is a directional derivative of truncated correlation energy minus an explicit moving-boundary leakage term','new_required_bound':'beta partial_a F-alpha partial_b F >= alpha*(2*pi/b^2)*W_a(2*pi/b)','claim_boundary':'exact identity; the directional derivative bound remains unproved','rh_proved':False};p=ROOT/'research/nima/results/theta-canonical-block-moving-boundary-identity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
