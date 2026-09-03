#!/usr/bin/env python3
"""Falsify a common-zero quotient/residue model for all five q divisors."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
_,q=g['exact_fiber'](3,6,-3);q2,q31=q[1],q[4]
def sub(a,b):
 o=dict(a)
 for k,v in b.items():o[k]=o.get(k,F(0))-v
 return {k:v for k,v in o.items() if v}
diff=sub(q31,q2);assert diff=={(0,0):F(-6)}
out={'schema':'marici.benincasa.cosmology-rees-common-zero-residue-falsifier.v1','source_point':[3,6,-3],'q2':{str(k):str(v) for k,v in q2.items()},'q31':{str(k):str(v) for k,v in q31.items()},'bezout_certificate':'q31-q2=-6, an invertible constant over Q and F_p for p not 2 or 3','ideal_generated_by_all_q':'unit ideal','common_zero_locus':'empty','disposition':'a Grothendieck residue or trace on the ordinary quotient by all five q_i is impossible; that quotient is zero','required_replacement':'retain the distinct pole-level localization/local-cohomology module and construct a cycle or Čech-residue functional compatible with its transition maps','tau_dual_constructed':False,'passed':True};(R/'cosmology_rees_common_zero_residue_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
