"""Bilateral attachment and forced-history tests with exact Gaussian fixture.

The hostile forcing is deliberately synthetic, not completed theta or Xi.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=70
z=mp.mpc(mp.mpf(1)/3,mp.mpf(1)/5)
u=lambda x:mp.exp(-x*x)
phi=lambda x:(-2*x-z)*u(x)
E=mp.sqrt(mp.pi/2)
inner=-z*E  # <u,phi>, u real; odd derivative integrates to zero.
assert abs(mp.re(z)*E+mp.re(inner))<mp.mpf('1e-65')
checks={}
for L in (mp.log(2),mp.log(3)):
    for x in (-2,-mp.mpf(1)/3,0,1):
        defect=u(x+L)-mp.exp(z*L)*u(x)
        forcing=mp.quad(lambda t:mp.exp(z*(L-t))*phi(x+t),[0,L])
        assert abs(defect-forcing)<mp.mpf('1e-60')
    seam=mp.quad(lambda x:abs(u(x))**2,[0,L])
    plus=mp.quad(lambda x:abs(u(x))**2,[0,mp.inf])
    plus_shift=mp.quad(lambda x:abs(u(x+L))**2,[0,mp.inf])
    minus=mp.quad(lambda x:abs(u(x))**2,[-mp.inf,0])
    minus_shift=mp.quad(lambda x:abs(u(x+L))**2,[-mp.inf,0])
    assert abs(plus-plus_shift-seam)<mp.mpf('1e-60')
    assert abs(minus_shift-minus-seam)<mp.mpf('1e-60')
checks['forced_translation_cocycle']=True
checks['bilateral_seam_cancellation']=True
# Integral exp(-z*x) phi(x) is the integral of derivative(exp(-z*x)u(x)).
tau=mp.quad(lambda x:mp.exp(-z*x)*phi(x),[-mp.inf,0,mp.inf])
assert abs(tau)<mp.mpf('1e-60')
assert abs(phi(0))>0 and abs(u(mp.log(2))-mp.exp(z*mp.log(2))*u(0))>mp.mpf('.1')
checks['zero_seam_does_not_remove_forcing']=True
# <phi,u> = conjugate(<u,phi>); conservative second-row residual at w=1, alpha=0.
r=mp.conj(inner)-z
assert abs(mp.re(r)+mp.re(z)*(E+1))<mp.mpf('1e-60')
checks['conservative_port_residual_real_part']=True
result={'schema':'marici.grothendieck.bilateral-forcing-attachment.v1','passed':True,
        'checks':checks,'precision_decimal_digits':70,
        'scope':'Gaussian synthetic hostile and analytic identities. No off-seam Xi zero asserted; completed-theta port balance unproved.'}
p=Path(__file__).resolve().parents[1]/'results/bilateral-forcing-attachment.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
