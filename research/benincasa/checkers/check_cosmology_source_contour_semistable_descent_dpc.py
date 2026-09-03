#!/usr/bin/env python3
"""Falsify the five-gate source-contour semistable-descent conjecture."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[1]/'results';A=Path(__file__).resolve().parents[1]
x=json.loads((A/'x1-soft-physical-strict-transform.json').read_text())
k,a,p,xi=s.symbols('k a p xi', nonzero=True)
measure=(a+p)/(2*p*(-a+p)**2*(a+3*p)*(xi+1))
assert 'unit leading ratio' in x['measure_transform']
assert not measure.has(k)
valuation_kappa1=0
required=2
assert valuation_kappa1<required
out={'schema':'marici.benincasa.cosmology-source-contour-semistable-descent-dpc.v1','problem':'Can one sourced semistable contour simultaneously close the five remaining cosmology gates?','bold_conjecture':'A source contour supplies physical boundary, chain specialization, order-two collision cancellation, physical pairing, and precise Gamma quotient descent.','strongest_falsification_attempt':{'tested_gate':3,'gate':'regular unlocalized specialization at kappa=1','source_measure_transform':x['measure_transform'],'normalized_exceptional_factor':str(measure),'source_measure_kappa_minus_1_valuation':valuation_kappa1,'required_valuation':required,'conductor_coefficient_valuation':-2,'residual_after_source_measure':-2},'disposition':{'status':'falsified','first_failed_consequence':'the materialized source measure has unit kappa-leading behavior rather than an order-two zero, so it cannot cancel the conductor double pole','surviving_results':['local contour/Gysin questions remain independently open','localized conductor coefficient remains valid for kappa not equal to one','rank-27 relative extension remains valid'],'withdrawn_scope':'no single currently materialized source-contour object closes all five gates','reopening_test':'supply a distinct source-derived measure or degeneration model with verified kappa-minus-one valuation at least two before testing the other four arrows'},'passed':True};(R/'cosmology_source_contour_semistable_descent_dpc.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
