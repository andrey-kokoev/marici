"""Cosmological parameters from Gram ratios (Nov 2024)."""
import json
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[1]

r, l, s, c = 11, 12, 4, 10

# Simple Gram ratios for cosmological densities
Omega_b  = Fraction(c - s, r**2)         # 6/121
Omega_DM = Fraction(c - s, l + r)        # 6/23
Omega_de = Fraction(r, l + s)            # 11/16
total    = Omega_b + Omega_DM + Omega_de

obs = {'Omega_b': 0.0486, 'Omega_DM': 0.264, 'Omega_de': 0.687}

result = {
    'schema': 'marici.nima.cosmological_gram_ratios.v1',
    'formulas': {
        'Omega_b':  f'({c}-{s})/{r}² = 6/121 = {float(Omega_b):.6f}',
        'Omega_DM': f'({c}-{s})/({l}+{r}) = 6/23 = {float(Omega_DM):.6f}',
        'Omega_de': f'{r}/({l}+{s}) = 11/16 = {float(Omega_de):.6f}',
    },
    'precision': {
        'Omega_b_err_pct':  abs(float(Omega_b)-obs['Omega_b'])/obs['Omega_b']*100,
        'Omega_DM_err_pct': abs(float(Omega_DM)-obs['Omega_DM'])/obs['Omega_DM']*100,
        'Omega_de_err_pct': abs(float(Omega_de)-obs['Omega_de'])/obs['Omega_de']*100,
    },
    'sum_check': {
        'total': float(total),
        'deficit_from_1': float(Fraction(1)-total),
        'deficit_fraction': f'{Fraction(1)-total}',
        'possible_Omega_k': float(Fraction(1)-total),
        'Omega_k_observed': '~ -0.001 +/- 0.002',
    },
    'note': 'The deficit 1 - sum = 91/44528 = (r*l - s*c - 1) / (r² * (l+r) * (l+s)) could be curvature.',
}

out = ROOT / 'results/cosmological-gram-ratios.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))