"""Exact finite controls for spatial dualization; not an analytic Fourier proof."""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib

def pair(a,b):
    return sum(x*y for x,y in zip(a,b))

# A nonorthonormal basis matters: momentum Gram H, dual Gram H^-1.
h = (F(4),F(9),F(25))
hi = tuple(1/x for x in h)
p = (F(2),F(-1),F(3))
x = (F(1,3),F(2),F(-1))
y = (F(2),F(-3),F(1,2))
norm = lambda a: sum(hi[i]*a[i]**2 for i in range(3))
# Momentum coordinate change p'=A p, dual change x'=A^-T x.
a = (F(2),F(3),F(5))
pp = tuple(a[i]*p[i] for i in range(3))
xp = tuple(x[i]/a[i] for i in range(3))
hp = tuple(h[i]/a[i]**2 for i in range(3))
c = F(7)
checks = {
    'dual_pairing_invariant': pair(pp,xp)==pair(p,x),
    'dual_metric_invariant': sum(xp[i]**2/hp[i] for i in range(3))==norm(x),
    'same_variance_pairing_rejected': pair(pp,tuple(a[i]*x[i] for i in range(3)))!=pair(p,x),
    'momentum_gram_not_dual_gram': sum(h[i]*x[i]**2 for i in range(3))!=norm(x),
    'character_exponent_additive': pair(p,tuple(x[i]+y[i] for i in range(3)))==pair(p,x)+pair(p,y),
    'phase_scale_relabeling': pair(p,tuple(c*t for t in x))/c==pair(p,x),
    'physical_length_changes_with_scale': norm(tuple(c*t for t in x))==c*c*norm(x) and norm(x)!=0,
    'reciprocal_unit_rescaling_preserves_phase': pair(tuple(c*t for t in p),tuple(t/c for t in x))==pair(p,x),
}
root = Path(__file__).resolve().parents[2]
paths = [Path(__file__), root/'research/nima/fourier-transform-as-character-linearization-of-segal-translation-object.md', root/'research/nima/marici-machian-gravity-direction.md']
packet = dict(passed=all(checks.values()),checks=checks,
    scope='Finite rational coordinate and scale identities, not Fourier inversion or physical selection.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('spatial-dual-bridge.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
