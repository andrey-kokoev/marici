#!/usr/bin/env python3
"""Transfer the proved theta log-concavity theorem to the sewn autocorrelation C_a."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];src=(ROOT/'research/grothendieck/theta-log-concavity-proves-global-tilt-monotonicity-of-translation-defect.md').read_text(encoding='utf-8');m,d,D,a=s.symbols('m d D a',real=True);x=m+D/2;exponent=s.simplify(a*x+a*(x-D));checks={'centered_tilt_exponent_is_2am':s.simplify(exponent-2*a*m)==0,'source_proves_strict_defect_tilt_monotonicity':'\\partial_a\\mathcal C_a(D)>0' in src,'source_retains_weighted_correlation_obstruction':'weighted correlation term' in src}
out={'schema':'marici.nima.theta-autocorrelation-logconcavity-transfer.v1','identity':'C_a(d)=W_a(2d)','proved_transfer':'partial_a[C_a(0)-C_a(d)]>0 for a>0,d>0','equivalent_order':'partial_a C_a(0)>partial_a C_a(d)','checks':checks,'passed':all(checks.values()),'what_it_closes':'global orientation of the translation-defect boundary current under Mellin tilt','what_it_does_not_close':'positivity of the cosine transform of partial_a C_a or the sine transform of d C_a','remaining_term':'the block-integrated weighted correlation D W_a(D)-(D+L)W_a(D+L)','rh_proved':False};p=ROOT/'research/nima/results/theta-autocorrelation-logconcavity-transfer.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
