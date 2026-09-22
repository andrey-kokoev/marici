"""Audit the saved fixed-point calibration, without inventing a parameter sweep.

Exact rational arithmetic on enclosing printed Arb balls. This does not rerun
or replace their owning analytical certification.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3]
source=ROOT/'research/voevodsky/results/certified-private-sector-cubic-observer.json'
data=json.loads(source.read_text(encoding='utf-8'))
p=data['parameters']
assert (p['background_A'],p['spectral_point'],p['receiver_gamma'])==(2,'3i',2)
def ball(text):
    match=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',text)
    assert match,text
    mid,rad=map(Q,match.groups());assert rad>=0
    return mid-rad,mid+rad
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def ratio(x,y):
    assert x[0]>0 and y[0]>0
    return x[0]/y[1],x[1]/y[0]
mu1=ball(data['windows']['A1']['mu'])
mu2=ball(data['windows']['A2']['mu'])
L=ball(data['rigorous_balls']['L_at_7_over_2'])
a=sub(mu1,L);b=sub(mu2,L);gap=sub(mu2,mu1)
rho=ratio(a,b)
assert a[0]>0 and b[0]>0 and gap[0]>0
assert Q(45,100)<rho[0]<rho[1]<Q(48,100)
# The earlier algebraic settings (1,3) and (2,3) are not physical settings
# certified by this fixed-point enclosure, even up to a common positive gain.
assert Q(1,3)<rho[0] and Q(2,3)>rho[1]
# The chosen lower-filtration lift uses c=(b-a)/b=1-rho.
lift=(1-rho[1],1-rho[0])
assert 0<lift[0]<lift[1]<1
result={'passed':True,'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'fixed_parameters':{k:p[k] for k in ('background_A','spectral_point','receiver_gamma')},
 'exact_rational_enclosures':{name:list(map(str,value)) for name,value in
   [('early_residual_factor',a),('late_residual_factor',b),('old_gap',gap),
    ('early_over_late',rho),('chosen_lift_normalization',lift)]},
 'coarse_ratio_enclosure':['45/100','48/100'],
 'earlier_algebraic_counterexample_ratios_outside_actual_enclosure':True,
 'scope':'Encloses one fixed actual ratio from previously certified printed balls. Interval endpoints are not certified realizable physical settings. No physical variation or full-kernel constancy over hypothetical parameter values is inferred.'}
(ROOT/'research/voevodsky/results/fixed-calibration-sector-ratio.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
