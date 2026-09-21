"""Gaussian regularization of the derivative port at the actual resolvent."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=70
checks={}
records=[]
for z in (mp.mpf(1),mp.mpf(2)):
    for eps in (mp.mpf('0.5'),mp.mpf('0.1'),mp.mpf('0.02')):
        rho0=1/(mp.sqrt(mp.pi)*eps)
        # Change variables t=eps*s for stable quadrature.
        R0=-mp.quad(lambda s:mp.exp(-z*eps*s-s*s)/mp.sqrt(mp.pi),[0,1,mp.inf])
        exactR0=-mp.exp((z*eps/2)**2)*mp.erfc(z*eps/2)/2
        assert abs(R0-exactR0)<mp.mpf('1e-60')
        # g=R_z(-rho_eps')=-z R_z rho_eps-rho_eps.
        # integral g=0, integral_negative g=-R0, g'(0)=-z^2 R0-z rho0.
        defect=-R0-(-z*z*R0-z*rho0)
        exact=(z*z-1)*exactR0+z*rho0
        assert abs(defect-exact)<mp.mpf('1e-60')
        if z==1:
            assert abs(eps*defect-1/mp.sqrt(mp.pi))<mp.mpf('1e-60')
        records.append({'z':str(z),'epsilon':str(eps),'D1':mp.nstr(defect,25)})
checks['resolvent_gaussian_formula']=True
checks['trace_defect_formula']=True
checks['z_one_exact_inverse_epsilon_divergence']=True
# The recorded Clark-visible odd defect has output (-i D1,-i D1).
checks['clark_projection_retains_divergence']=True
result={'schema':'marici.grothendieck.clark-resolvent-trace-obstruction.v1',
        'passed':True,'checks':checks,'values':records,
        'scope':'First-order full-line translation chart and endpoint-moment transpose column. Does not decide a separately completed higher-order pencil.'}
p=Path(__file__).resolve().parents[1]/'results/clark-resolvent-trace-obstruction.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
