"""Arb calibration of the two private-sector cubic observer.

Uses Voevodsky's exact private-row enumeration; does not re-prove source descent.
Recomputes scaled theta enclosures and the shared residual template.
"""
from pathlib import Path
from math import floor
import runpy
import json
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(Path(__file__).with_name('certify_robust_cubic_template_measurement.py')))
assert b['result']['passed']
ctx.prec=192
y=b['y'];gamma=b['gamma'];L=b['L']
A1,A2,B1,B2=b['windows']
D=b['window'](20,3,'private_cross_window')
h2=1/(2*(y+gamma))
S0=(A2['mu']-A1['mu'])*(B2['mu']-B1['mu'])/(2*y*y)
Sx=-(A1['mu']-L)*(B2['mu']-L)/(2*y*y)
E0=2*h2*A1['X']*B1['X']*(A1['mu']-L)*(B1['mu']-L)
Ex=2*h2*A1['X']*D['X']*(A1['mu']-L)*(D['mu']-L)
assert S0>0 and Sx<0 and E0>0 and Ex>0

def rational_calibration(value):
    sign=1 if value>0 else -1
    positive=abs(value)
    exponent=floor(float(positive.log()/arb(10).log()))
    numerator=round(float(positive/(arb(10)**exponent))*1000000)
    fixed=sign*arb(numerator)/1000000*(arb(10)**exponent)
    assert abs(fixed/value-1)<arb('0.02')
    return fixed,{'sign':sign,'mantissa_numerator':numerator,
                  'mantissa_denominator':1000000,'decimal_exponent':exponent}

k0,cal0=rational_calibration(S0/E0)
kx,calx=rational_calibration(Sx/Ex)
assert abs(kx)>abs(k0)
operator_bound=abs(kx) # dual norm of the two-sector l1 sum
# The same shared cell template, tested now by the UNIT weak-residual test.
profile=b['base'];delta=arb(1)/100;test_rate=y+2*gamma
corr=arb(0)
for j,numerator in enumerate(profile['numerators']):
    c=arb(numerator)/profile['denominator']
    corr+=c*((-test_rate*j*delta).exp()-(-test_rate*(j+1)*delta).exp())/test_rate
rho=(2*(y+gamma)*corr)**2
assert rho>arb('0.9997') and rho<1
# Calibration error of the original source functional on its two visible bases.
delta0=abs(k0*E0-S0);deltax=abs(kx*Ex-Sx)
assert delta0<arb('0.002') and deltax<arb('0.002')
delta0_template=abs(k0*E0*rho-S0)
deltax_template=abs(kx*Ex*rho-Sx)
assert delta0_template<arb('0.002') and deltax_template<arb('0.002')
noise_exponent=floor(float((arb('0.001')/operator_bound).log()/arb(10).log()))
noise=arb(10)**noise_exponent
noise_error=operator_bound*noise
assert noise_error<arb('0.001')
margin=k0*E0*rho-noise_error
assert margin>arb('0.05')
original_functional_margin=margin-delta0_template
assert original_functional_margin>arb('0.05')
assert k0*E0-noise_error-delta0>arb('0.05')

result={'schema':'marici.grothendieck.private-sector-cubic-noise.v1','passed':True,
        'arithmetic':'Arb 192-bit scaled theta integration and exact rational calibration',
        'parameters':{'background_A':2,'spectral_y':3,'receiver_gamma':1,
                      'prime_cutoff_for_field_comparison':100000,
                      'residual_test':'sqrt(8)*exp(-5*u) on the weak residual coordinate',
                      'row0':['2->4','12->60','420->4620 forgotten'],
                      'row_cross':['2->4','20->60','420->4620 forgotten']},
        'rational_observer_coefficients_per_w_seam_squared':{'row0':cal0,'row_cross':calx},
        'private_window':{key:(str(value) if isinstance(value,arb) else value) for key,value in D.items()},
        'rigorous_balls':{name:str(value) for name,value in {
            'original_positive_source_value_per_w_squared':S0,
            'original_crossed_source_value_per_w_squared':Sx,
            'private_row0_residual_response':E0,'private_cross_residual_response':Ex,
            'rational_row0_coefficient':k0,'rational_cross_coefficient':kx,
            'observer_norm_per_w_squared':operator_bound,
            'shared_template_signal_factor':rho,
            'positive_basis_calibration_error_per_w_squared':delta0,
            'crossed_basis_calibration_error_per_w_squared':deltax,
            'positive_basis_template_and_calibration_error':delta0_template,
            'crossed_basis_template_and_calibration_error':deltax_template,
            'independent_noise_error_per_w_squared':noise_error,
            'remaining_witness_margin_per_w_squared':margin,
            'margin_after_original_functional_calibration_discrepancy':original_functional_margin}.items()},
        'certified_claims':{'remaining_margin_exceeds_0_05_w_seam_squared':True,
                            'visible_basis_calibration_errors_below_0_002':True,
                            'total_independent_full_output_noise_suffices':f'10^({noise_exponent})',
                            'same_margin_for_actual_finite_prime_or_shared_template_residuals':True},
        'source_identity_input':'research/voevodsky/alternative-balanced-sectors-reduce-cubic-response-amplification-to-sharp-gaussian-order.md',
        'scope':'Original fixed cubic witness with two admitted private sectors. Rational observer differs from the exact whole-corner functional by the explicitly bounded two basis errors; the other 268 basis values remain zero. No translated-family uniform tolerance or noisy derived class is asserted.'}
out=ROOT/'research/grothendieck/results/private-sector-cubic-noise.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
