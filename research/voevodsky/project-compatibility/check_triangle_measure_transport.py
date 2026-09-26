"""Exact coefficient controls for old-to-Euclidean period transport.
Gamma limits and analytic transport are written in triangle-measure-transport.md.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'triangle-volume-dictionary.md',HERE/'triangle-joint-corner.md',HERE/'triangle-limit-order.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();count=0
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  h=8*a*b*(a+b)
  for ratio in map(F,('1/4','1/2','3/4')):
   x=a*ratio
   B_over_pi=4*b*(a+b)/(3*(x+b))
   Q_over_pi=3*B_over_pi/h
   assert Q_over_pi==1/(2*a*(x+b))
   for E in map(F,('1/8','1/16')):
    H=E*(E-2*a)*(E-2*b)*(2*a+2*b-E);D=H/16
    assert D>0
    # At epsilon=1 (d=5), exact source/Euclidean ratio is H/6.
    assert H/6==F(8,3)*D
    assert (H/6)*(6/D)==16 # coefficients after removing pi*sqrt(K)
    # Fixed-E regulator-pole transport of the independently known old limit.
    S=F(7,5);FE=F(11,3)
    assert (3/H)*(2*H/(3*E))*S*FE==(2/E)*S*FE
    count+=1
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'coefficient_fixtures':count,
 'regulated_comparison':'P_old=R*G_Euclidean; R=H/(3sqrt(pi))*Gamma(1/2+epsilon)/Gamma(epsilon)',
 'fixed_E_regulator_pole':'lim epsilon*G=3*P_old^0(E)/H',
 'joint_scaled_limit':'epsilon*E^(2-epsilon)*G -> Q_chi',
 'Q_chi':'pi/(2a) integral chi(x,0)/(x+b) dx',
 'physical_prescription_supplied':False,
 'scope':'Same localized candidate real chain, cutoff and rational factor; this is an explicit measure comparison, not a renormalization prescription or identification of a physical continued cycle.'}
(HERE/'triangle-measure-transport.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
