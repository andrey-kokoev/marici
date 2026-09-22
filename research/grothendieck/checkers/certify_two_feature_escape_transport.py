"""Exact labelled two-feature algebra and Arb shared-template certificate."""
from pathlib import Path
import json
import sympy as S
from flint import arb,ctx

# Ordered tensor expansion, including the quadratic error term.
a,b,da,db=S.symbols('a b da db')
assert S.expand((a+da)*(b+db)-a*b-a*db-b*da-da*db)==0
C,L,k=S.symbols('C L k')
ma1,ma2,mb1,mb2=S.symbols('ma1 ma2 mb1 mb2')
slot=lambda mu:S.sqrt(2)*(C+(mu-L)*k)
observed=(slot(ma2)-slot(ma1))*(slot(mb2)-slot(mb1))
assert S.expand(observed-2*k*k*(ma2-ma1)*(mb2-mb1))==0
crossed=-slot(ma1)*slot(mb2)
assert S.expand(crossed).coeff(C,2)==-2
mc1,mc2=S.symbols('mc1 mc2')
third=observed*(slot(mc2)-slot(mc1))
assert S.expand(third-2*S.sqrt(2)*k**3*(ma2-ma1)*(mb2-mb1)*(mc2-mc1))==0
# Unequal calibration ratios restore a common-even error term.
r1,r2=S.symbols('r1 r2')
calibrated=r2*(C+(ma2-L)*k)-r1*(C+(ma1-L)*k)
assert S.expand(calibrated-(r2-r1)*C-k*(r2*(ma2-L)-r1*(ma1-L)))==0
assert S.Rational(1,5)+S.Rational(1,5)+S.Rational(1,25)<S.Rational(1,2)

ctx.prec=192
y=arb(3);R=arb(8);N=800;delta=R/N
denominator=100000000
numerators=[];correlation=arb(0);noise_squared=arb(0)
for j in range(N):
    x=j*delta
    cell_integral=((-y*x).exp()-(-y*(x+delta)).exp())/y
    average=cell_integral/delta
    # Proposal only; all bounds are verified afterward by Arb.
    numerator=round(float(average)*denominator)
    assert numerator>=0
    c=arb(numerator)/denominator
    numerators.append(numerator)
    correlation+=c*cell_integral
    err=arb(abs(c-average).upper())
    noise_squared+=delta*err**2
noise=noise_squared.sqrt()
ratio=(2*y*correlation)**2
assert correlation>0
assert ratio>arb('0.9998')
assert ratio<1
three_feature_ratio=(2*y*correlation)**3
assert three_feature_ratio>arb('0.9997') and three_feature_ratio<1
assert noise<arb('1e-8')
# The shared e^{-3x} template meets the prior and cell-noise requirements
# of the existing gamma=1 finite-field certificate.
M=((1+y*y)/(2*(y-1))).sqrt()
assert noise<arb('0.001')*M

root=Path(__file__).resolve().parents[3]
artifact=root/'research/grothendieck/results/cubic-shared-profile-template.json'
artifact.write_text(json.dumps({
    'schema':'marici.grothendieck.cubic-shared-profile-template.v1',
    'profile':'exp(-3*x)','source_window':[0,8],'mesh_step':'1/100','cells':N,
    'coefficient_denominator':denominator,'coefficient_numerators':numerators,
    'outside_window':'zero',
    'use':'The SAME residual template in every normalized window. The even five-label template is also shared; its contribution cancels under the four-sector observer.',
    'calibration_scope':'Exact source X_F normalizers are assumed. No late-window amplitude or absolute measurement-noise certificate is supplied.'},indent=2)+'\n',encoding='utf-8')
result={'schema':'marici.grothendieck.two-feature-escape-transport.v1','passed':True,
        'arithmetic':'SymPy exact identities and Arb 192-bit real balls',
        'checks':{'tensor_cross_error_retained':True,'shared_even_template_cancels':True,
                  'unequal_calibration_breaks_cancellation':True,
                  'crossed_source_common_error_survives':True,
                  'three_feature_witness_corollary':True,
                  'one_fifth_gap_errors_leave_half_margin':True},
        'rigorous_balls':{'residual_template_correlation':str(correlation),
                          'cubic_signal_ratio':str(ratio),'three_feature_signal_ratio':str(three_feature_ratio),
                          'coefficient_L2_noise':str(noise),
                          'template_weighted_D1_norm':str(M)},
        'certified_claims':{'coherent_cubic_signal_ratio_between_0_9998_and_1':True,
                            'coherent_three_feature_ratio_between_0_9997_and_1':True},
        'template_artifact':str(artifact.relative_to(root)).replace('\\','/'),
        'scope':'Certifies the shared-template factor multiplying the existing exact positive cubic witness. No theta-window normalizers, moment gaps, or absolute noisy four-sector measurement are numerically calibrated here.'}
out=root/'research/grothendieck/results/two-feature-escape-transport.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
