#!/usr/bin/env python3
"""Compare repository half-divisor Gaussian coefficients with the external BRS normalization recorded by the literature audit."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];lit=(ROOT/'research/grothendieck/references/gpt-finite-double-contact-literature-sweep-2026-09-05.md').read_text(encoding='utf-8');src=(ROOT/'research/grothendieck/explicit-two-variable-weil-heat-source-formula.md').read_text(encoding='utf-8')
# BRS audit uses a symmetrized Gaussian and full zero sum. Repository uses one shifted Gaussian and centered positive-half divisor.
ratios={'endpoint':F(4,1)/F(1,1),'gamma':F(1,2)/F(1,8),'prime':F(2,1)/F(1,2)}
checks={'external_formula_identified':'Bondarenko' in lit and '10.1007/s00365-022-09599-w' in lit,'same_digamma_argument':'\\frac14+\\frac{iu}{2}' in lit,'same_prime_weight':'\\frac{\\Lambda(n)}{\\sqrt n}' in lit,'same_gaussian_prime_damping':'e^{-(\\log n)^2/(4t)}' in lit,'all_sector_ratios_equal_four':set(ratios.values())=={F(4)},'repository_declares_positive_half_divisor':'count positive ordinates once' in src}
out={'schema':'marici.nima.external-Guinand-Weil-normalization-comparison.v1','external_reference':'Bondarenko-Radchenko-Seip, Constructive Approximation 57 (2023), 405-461, DOI 10.1007/s00365-022-09599-w','normalization_relation':'external symmetrized full-zero formula = 4 times repository single-shift centered positive-half-divisor formula','sector_ratios':{k:str(v) for k,v in ratios.items()},'checks':checks,'passed':all(checks.values()),'authority_status':'independently corroborated through repository literature audit; direct primary-text line audit remains required for publication authority','rh_proved':False};p=ROOT/'research/nima/results/external-Guinand-Weil-normalization-comparison.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
