#!/usr/bin/env python3
"""Show why fitting ambient-degree dependence on three adjacent edges is nonpromoting."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
# Any three rational coefficient observations have one quadratic interpolant.
xs=(12,14,16);ys=(Fraction(1),Fraction(-3,2),Fraction(7,5))
def lagrange(x):
 return sum((ys[i]*Fraction((x-xs[(i+1)%3])*(x-xs[(i+2)%3]),(xs[i]-xs[(i+1)%3])*(xs[i]-xs[(i+2)%3])) for i in range(3)),Fraction())
def alt(x):return lagrange(x)+Fraction((x-12)*(x-14)*(x-16),8)
assert all(lagrange(x)==alt(x)==y for x,y in zip(xs,ys));assert lagrange(18)!=alt(18)
out={'schema':'marici.benincasa.cosmology-finite-order-coefficient-recurrence-gate.v1','observed_edge_degrees':list(xs),'fact':'every three rational coefficient values admit a unique quadratic interpolant','indistinguishable_alternative':'add any rational multiple of (A-12)(A-14)(A-16)','agreement_on_observed_edges':True,'different_A18_prediction_in_demonstration':True,'source_derived_order_bound_available':False,'decision':'Coefficient interpolation across three adjacent edges cannot establish a source-level recurrence without an independently proved order and descriptor-support law.','required_promotion_data':['source-derived recurrence order','ambient-independent descriptor-support rule','base cases covering the proved order','exact recurrence verification'],'passed':True};(R/'cosmology_finite_order_coefficient_recurrence_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
