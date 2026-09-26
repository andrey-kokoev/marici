"""CMB acoustic scale from Gram cosmological parameters — matches Planck 2018 to <1.5%."""
import json, math, numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

r, l, s, c = 11, 12, 4, 10

Ob = (c-s)/r**2        # 6/121
Odm = (c-s)/(l+r)      # 6/23
Ode = r/(l+s)          # 11/16
Ok = 1 - Ob - Odm - Ode  # 91/44528
Om = Ob + Odm

H0 = 67.4
h = H0/100
om_b_h2 = Ob * h**2
om_m_h2 = Om * h**2

z_star = 1090  # Planck 2018

# Sound horizon approximation (Hu 2001, Planck 2018 calibration)
r_s = 147.05 * (om_m_h2/0.143)**(-0.25) * (om_b_h2/0.0224)**(-0.13)

# Comoving distance to last scattering
E = lambda z: math.sqrt(Om*(1+z)**3 + Ode + Ok*(1+z)**2)
zs = np.linspace(0, z_star, 20000)
integral = sum(1/E(z) for z in zs) * (z_star/20000)
c_km = 299792.458
DM = c_km * integral / H0

l_A = math.pi * DM / r_s

print("=== CMB FROM GRAM PARAMETERS ===")
print(f"Omega_b h^2 = {om_b_h2:.4f}  (Planck: 0.0224, err {abs(om_b_h2/0.0224-1)*100:.2f}%)")
print(f"Omega_m h^2 = {om_m_h2:.4f}  (Planck: 0.143, err {abs(om_m_h2/0.143-1)*100:.2f}%)")
print(f"r_s = {r_s:.1f} Mpc  (Planck: 147.1, err {abs(r_s/147.1-1)*100:.2f}%)")
print(f"l_A = {l_A:.1f}  (Planck: 301.8, err {abs(l_A/301.8-1)*100:.2f}%)")
print(f"Omega_k = {Ok:.6f}  (CMB-S4 will test)")

result = {
    'schema': 'marici.nima.cmb_from_gram.v2',
    'gram_parameters': {
        'Omega_b': float(Ob), 'Omega_DM': float(Odm), 'Omega_de': float(Ode), 'Omega_k': float(Ok),
    },
    'cmb_outputs': {
        'omega_b_h2': round(om_b_h2, 4), 'omega_m_h2': round(om_m_h2, 4),
        'r_s_Mpc': round(r_s, 1), 'l_A': round(l_A, 1),
    },
    'precision_vs_Planck2018': {
        'omega_b_h2_error_pct': round(abs(om_b_h2/0.0224-1)*100, 2),
        'omega_m_h2_error_pct': round(abs(om_m_h2/0.143-1)*100, 2),
        'r_s_error_pct': round(abs(r_s/147.1-1)*100, 2),
        'l_A_error_pct': round(abs(l_A/301.8-1)*100, 2),
    },
}

out = ROOT / 'results/cmb-from-gram.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))