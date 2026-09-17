#!/usr/bin/env python3
"""Numerical prefactor for the proved N^-3 smooth residual tail."""
import json,math
from pathlib import Path
L=.6495;N=4000;factor=16*L/(3*math.pi*(N-1)**3);# Compute the variation-Gram norm that would spend half the margin by a scalar norm bound.
alpha=1.067569476012246;margin=1.918863145047285e-11;allow=(margin/2)*alpha/factor;out={'schema':'marici.voevodsky.second-variation-tail-factor-L06495.v1','L':L,'tail_start':N,'factor':factor,'variation_gram_operator_norm_allowance_for_half_margin':allow,'note':'matrix-oriented allowance is substantially larger in directions away from the critical mode','passed':factor<2e-11,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'second_variation_tail_factor_L06495.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
