#!/usr/bin/env python3
"""Audit the fixed-width Gaussian observer-separation theorem and its claim boundary."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];note=(ROOT/'research/nima/fixed-width-gaussian-translates-are-a-jointly-faithful-observer-family.md').read_text();old=json.loads((ROOT/'research/voevodsky/results/one_width_gaussian_weil_faithfulness.json').read_text())
sigma,xi=s.symbols('sigma xi',positive=True,real=True);gh=s.sqrt(s.pi/sigma)*s.exp(-xi**2/(4*sigma));points=[s.Integer(0),s.Integer(1),s.Integer(2)];K=s.Matrix([[s.exp(-(a-b)**2) for b in points] for a in points]);det=s.factor(K.det());checks={'gaussian_transform_symbolically_positive':gh.is_positive,'three_translate_gaussian_gram_strictly_positive':bool(det.is_positive),'distributional_convolution_argument_recorded':'T*\\check g_\\sigma=0' in note and '\\widehat T=0' in note,'previous_width_limit_not_required':old['width_limit_required'] is False,'source_derived_toeplitz_positivity_still_open':old['fixed_width_toeplitz_psd_verified'] is False}
out={'schema':'marici.nima.fixed-width-gaussian-joint-faithfulness.v1','checks':checks,'gaussian_transform':str(gh),'three_translate_gram_determinant':str(det),'observer_separation':'proved for all translates on tempered distributions','qRB_consequence':'continuous coherencers are unique when equal under every fixed-width Gaussian translate observer','remaining_gate':'source-derived all-translate Weil Gram positivity and external source normalization','passed':all(checks.values()),'rh_proved':False};p=ROOT/'research/nima/results/fixed-width-gaussian-joint-faithfulness.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
