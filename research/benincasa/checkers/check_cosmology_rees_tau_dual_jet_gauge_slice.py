#!/usr/bin/env python3
"""Construct the unique tau-normalized slice of scalar dual-jet gauge."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
checks=[]
for x,y in [(F(2),F(3)),(F(-5,2),F(7,3)),(F(0),F(-4))]:
 a=-x;b=-y+x*x
 xp=x+a;yp=y+a*x+b;assert xp==0 and yp==0;checks.append({'lambda1_tau':str(x),'lambda2_tau':str(y),'a':str(a),'b':str(b)})
out={'schema':'marici.benincasa.cosmology-rees-tau-dual-jet-gauge-slice.v1','assumption':'lambda0(tau)=1','gauge_action':['lambda1 maps to lambda1+a lambda0','lambda2 maps to lambda2+a lambda1+b lambda0'],'slice_conditions':['lambda1(tau)=0','lambda2(tau)=0'],'unique_parameters':['a=-lambda1(tau)','b=-lambda2(tau)+lambda1(tau)^2'],'exact_checks':checks,'quotient_result':'every normalized scalar-gauge orbit has exactly one representative in the tau-flat slice','existence_of_closed_dual_jet_proved':False,'remaining_gate':'construct any regular closed dual 2-jet; the slice then removes scalar ambiguity but not transverse failures on relation generators','passed':True};(R/'cosmology_rees_tau_dual_jet_gauge_slice.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
