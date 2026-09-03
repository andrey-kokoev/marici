#!/usr/bin/env python3
"""Exhibit order dependence at the duplicate/triple pole locus."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# In u=q2=X, v=q1=Y-3, the five-q denominator is u*v^2*(u+v)*(u-6).
# v-first: coefficient v^-1 uses the linear term -v/u^2 of 1/(u+v),
# leaving -1/(u^3(u-6)); its u^-1 coefficient is 1/216.
v_then_u=F(1,216)
# u-first at u=0 uses constants 1/v and -1/6, leaving -1/(6v^3), with zero v residue.
u_then_v=F(0)
assert v_then_u!=u_then_v
out={'schema':'marici.benincasa.cosmology-rees-iterated-residue-order.v1','coordinates':{'u':'q2=X','v':'q1=q23=Y-3'},'local_denominator':'u v^2 (u+v) (u-6)','test_form':'du dv / [u v^2 (u+v) (u-6)]','iterated_residues':{'v_then_u':str(v_then_u),'u_then_v':str(u_then_v)},'order_independent':False,'exact_residual':str(v_then_u-u_then_v),'disposition':'the pole presentation does not select a canonical iterated residue; choosing an order changes the functional even on the unit numerator','required_source_datum':'an oriented cycle/chamber, blowup flag, or reviewed order-independent residue combination compatible with the pole presentation','tau_functional_constructed':False,'passed':True};(R/'cosmology_rees_iterated_residue_order.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
