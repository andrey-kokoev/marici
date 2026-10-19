"""Conditional fixed-sample protocol checks; all controls are synthetic, not data."""
import copy
import json
from fractions import Fraction as F
from pathlib import Path
from check_physics_interface_geometry_admission import ROOT, load, sha, require, sqrt_box, exp_minus

CONTRACT='research/nima/contracts/physics-phase-measurement-protocol.v1.json'


def radius(c):
    u=c['uncertainty'];n=c['sample_size_per_setting']
    d=F(u['coordinate_radius']);v=F(u['variance_bound_per_real_coordinate'])
    a=F(u['validation_alpha']);b=F(u['complex_bias_bound'])
    require(type(n) is int and n>0 and d>0 and v>0 and b>=0,'invalid uncertainty domain')
    require(F(4)*v/(n*d*d)<=a,'insufficient fixed sample size')
    require(0<a and 0<F(u['calibration_alpha']) and
            a+F(u['calibration_alpha'])<=F(u['familywise_alpha'])<1,'coverage budget')
    return sqrt_box(F(2))[1]*d+b


def ratio_interval(z1,z2,r):
    require(r>=0,'negative radius')
    def magnitude(z):return sqrt_box(z[0]*z[0]+z[1]*z[1])
    lo1,hi1=magnitude(z1);lo2,hi2=magnitude(z2)
    lower1=max(F(0),lo1-r)
    if lower1==0:return None
    return max(F(0),lo2-r)/(2*(hi1+r)),(hi2+r)/(2*lower1)


def excluded(interval,prediction,epsilon):
    if interval is None:return False
    return interval[1]<prediction[0]-epsilon or interval[0]>prediction[1]+epsilon


def main():
    c=load(CONTRACT);test=load(c['prediction_contract']);r=radius(c)
    require(c['status']=='candidate_pending_instrument_review','scope promotion')
    require(all(c[k] is None for k in ('physical_authorization','calibration_bundle','validation_data')),'fixtures promoted to evidence')
    require(c['target']==test['target'],'target mismatch')
    require(F(c['calibration_requirements']['additive_bias'])==F(c['uncertainty']['complex_bias_bound']), 'bias contract mismatch')
    b=test['design_calibration_boxes'];l1,h1=map(F,b['lambda1']);l2,h2=map(F,b['lambda2']);rl,rh=map(F,b['relative_readout_gain'])
    ref=(rl*sqrt_box(l2/h1)[0]/2,rh*sqrt_box(h2/l1)[1]/2)
    alt=(ref[0]*exp_minus(2*(h2-l1))[0],ref[1]*exp_minus(2*(l2-h1))[1])
    gain=F(c['calibration_requirements']['minimum_common_gain_times_port_transfer'])
    require(gain>0,'signal floor')
    ref_signal=gain*sqrt_box(l1)[0]
    alt_signal=ref_signal*exp_minus(2*h1)[0]
    # On the simultaneous coverage event sample magnitudes differ from truth by <=R.
    # Their confidence endpoints can therefore differ by <=2R, not merely R.
    require(alt_signal>2*r,'worst-case denominator')
    passive_ci_lower=(2*ref_signal*ref[0]-2*r)/(2*(ref_signal+2*r))
    rival_ci_upper=(2*alt_signal*alt[1]+2*r)/(2*(alt_signal-2*r))
    eps=F(test['epsilon']);separator=F(test['structural_separator'])
    require(rival_ci_upper<separator<passive_ci_lower,'coverage-event separator')
    require(rival_ci_upper<ref[0]-eps and passive_ci_lower>alt[1]+eps,'coverage-event rival exclusion')
    controls=[]
    for label,change in (
        ('underpowered',lambda x:x.update(sample_size_per_setting=100)),
        ('noise-inflation',lambda x:x['uncertainty'].update(variance_bound_per_real_coordinate='2')),
        ('alpha-overspend',lambda x:x['uncertainty'].update(calibration_alpha='1/100')),
    ):
        bad=copy.deepcopy(c);change(bad)
        try:radius(bad)
        except ValueError:controls.append(label)
        else:raise AssertionError('accepted '+label)
    require(ratio_interval((F(0),F(0)),(F(1),F(0)),r) is None,'zero denominator')
    controls.append('zero-denominator-abstains')
    passive=ratio_interval((F(3,10),F(0)),(F(3,5),F(0)),r)
    require(not excluded(passive,ref,eps) and excluded(passive,alt,eps),'passive synthetic control')
    # A rational pair lying inside the phase-rival enclosure; not acquired observations.
    rival=ratio_interval((F(9,50),F(0)),(F(81,1000),F(0)),r)
    require(excluded(rival,ref,eps) and not excluded(rival,alt,eps),'rival synthetic control')
    neither=ratio_interval((F(1),F(0)),(F(3),F(0)),r)
    require(excluded(neither,ref,eps) and excluded(neither,alt,eps),'neither model control')
    controls+=['passive-compatible','rival-compatible','neither-model']
    paths=[CONTRACT,c['prediction_contract'],'research/nima/checkers/check_physics_interface_geometry_admission.py',str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    out={'schema':c['schema'],'status':'pass','disposition':c['status'],
         'sample_size_per_setting':c['sample_size_per_setting'],'total_shots':2*c['sample_size_per_setting'],
         'conditional_familywise_coverage':str(1-F(c['uncertainty']['familywise_alpha'])),
         'complex_radius_upper':str(r),
         'coverage_event_passive_ratio_lower':str(passive_ci_lower),
         'coverage_event_rival_ratio_upper':str(rival_ci_upper),
         'display_bounds':{'radius_upper':float(r),'passive_lower':float(passive_ci_lower),'rival_upper':float(rival_ci_upper)},
         'controls':controls,'acquired_data':False,'physical_authorization':False,
         'source_sha256':{p:sha(p) for p in paths}}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
