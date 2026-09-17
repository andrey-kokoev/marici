#!/usr/bin/env python3
"""Exact two-observer obstruction to cancelling the terminal atomic rotor by bulk volume."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
t=s.symbols('t', real=True);gamma=s.Integer(1);f=s.exp(-t**2);g=(t**2-1)*s.exp(-t**2)
def bulk(h):return s.integrate(h**2,(t,-s.oo,s.oo))
def atom(h):return s.simplify(h.subs(t,gamma)**2+h.subs(t,-gamma)**2)
Bf,Bg=map(s.simplify,(bulk(f),bulk(g)));Af,Ag=map(s.simplify,(atom(f),atom(g)));# Normalize both to equal bulk mass one.
ratio_f=s.simplify(Af/Bf);ratio_g=s.simplify(Ag/Bg);checks={'bulk_norms_positive':bool(Bf>0 and Bg>0),'first_atomic_response_positive':bool(Af>0),'second_atomic_response_zero':Ag==0,'atomic_to_bulk_ratios_differ':s.simplify(ratio_f-ratio_g)!=0,'no_universal_bulk_scalar_cancellation':s.simplify(ratio_f-ratio_g)!=0};out={'schema':'marici.voevodsky.bulk-volume-cannot-cancel-terminal-atomic-rotor.v1','crossing_gamma':'1','observers':{'f':'exp(-t^2)','g':'(t^2-1) exp(-t^2)'},'bulk_integrals':{'f':str(Bf),'g':str(Bg)},'atomic_responses':{'f':str(Af),'g':str(Ag)},'atomic_to_bulk_ratios':{'f':str(ratio_f),'g':str(ratio_g)},'checks':checks,'passed':all(checks.values()),'conclusion':'No observer-independent multiple of the Plancherel bulk functional can cancel the terminal point-evaluation rotor for all observers.','remaining_routes':['crossing-specific finite-rank geometric/index row','source-forced common renormalized density on both opposite edges'],'rh_proved':False};p=Path(__file__).parents[1]/'results'/'bulk_volume_cannot_cancel_terminal_atomic_rotor.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
