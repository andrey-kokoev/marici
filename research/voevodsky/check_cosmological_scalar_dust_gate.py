"""Finite rational controls of the source's de Sitter half-integer sector.
The all-l obstruction is a written inequality; this is not a sampling proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

rows=[]
for ell in range(9):
    nu=F(2*ell+1,2)
    minimal=F(9,4)-nu**2
    conformal=F(1,4)-nu**2
    rows.append(dict(ell=ell,nu=str(nu),minimal_m2_over_H2=str(minimal),
                     conformal_m2_over_H2=str(conformal)))
checks={
    'minimal_identity':all(F(r['minimal_m2_over_H2'])==2-r['ell']*(r['ell']+1) for r in rows),
    'conformal_identity':all(F(r['conformal_m2_over_H2'])==-r['ell']*(r['ell']+1) for r in rows),
    'minimal_nonnegative_samples_exactly_l0_l1':[r['ell'] for r in rows if F(r['minimal_m2_over_H2'])>=0]==[0,1],
    'conformal_nonnegative_samples_only_l0':[r['ell'] for r in rows if F(r['conformal_m2_over_H2'])>=0]==[0],
    'heavy_mass_example_has_imaginary_order':F(9,4)-100==F(-391,4),
    'half_integer_orders_have_nonnegative_square':all(F(r['nu'])**2>=F(1,4) for r in rows),
    'minimal_positive_mass_example_below_heavy_threshold':F(rows[0]['minimal_m2_over_H2'])==2<100,
}
root=Path(__file__).resolve().parents[2]
primary=root/'temp/triangle-measure-primary-2402.06558v3-source/IR_Divs.tex'
# Optional cached external source provenance, not required for algebra tests.
packet=dict(passed=all(checks.values()),checks=checks,rows=rows,
    universal_argument='l>=0 implies l(l+1)>=0, hence minimal m^2/H^2<=2. For l>=2 it is negative.',
    scope='Free mode parameters in d=3 de Sitter, xi=0 or 1/6; not a no-go for interacting matter or all cosmological sectors.',
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    primary_sha256=hashlib.sha256(primary.read_bytes()).hexdigest() if primary.exists() else None)
Path(__file__).with_name('cosmological-scalar-dust-gate.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
