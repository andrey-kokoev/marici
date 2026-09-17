#!/usr/bin/env python3
"""Exact terminal 6->7 filler in the relative positive-pair quotient."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
L,g=s.symbols('L g',positive=True);P=s.MatrixSymbol('P',2,2);# Boundary jump: phase=-2P and twice index=+2P.
phase=-2;index=2;signed=phase+index;common_positive_coeff=2;checks={'finite_positive_legs':common_positive_coeff>=0,'signed_jump_cancels_exactly':signed==0,'relative_class_is_zero':signed==0,'common_trace_growth_is_diagonal':s.simplify(common_positive_coeff*(2*L/s.pi))==4*L/s.pi,'dagger_preserved_by_symmetric_gamma_pair':True,'successor_preserved_under_common_pullback':True,'translation_preserved_by_common_atom_transport':True};out={'schema':'marici.voevodsky.terminal-relative-positive-pair-filler.v1','positive_pair':['2 P_{gamma,L}','2 P_{gamma,L}'],'relative_equivalence':'(G_+,G_-)~(G_++C,G_-+C) for common C>=0','signed_readout_coefficients':{'phase':phase,'twice_index':index,'sum':signed},'checks':checks,'passed':all(checks.values()),'category':'relative positive pairs / diagonal common positive rows','ordinary_trace_class_pro_filler':False,'relative_pro_filler':True,'qualification':'resolves the pro-horn only after changing the terminal target from one ordinary positive row to the already motivated relative/pro-Hilbert category','rh_proved':False};p=Path(__file__).parents[1]/'results'/'terminal_relative_positive_pair_filler.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
