"""Exact finite-E collision coefficients and complete six-term bracket fixtures.
Written analytic proof: triangle-limit-order.md.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'triangle-moving-collision-limit.md',HERE/'triangle-regulator-coefficient.md',
 ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex',
 ROOT/'temp/arxiv-2408.16386-source/sections/cosmologicalintegrals.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory();records=[]
for a in map(F,(1,3)):
 b=a
 for u in map(F,('1/8','1/16','1/32','1/64')):
  ell=2*a*(1-u*u)/(1+u*u);E=a+b-ell
  g=(a*a+b*b-ell*ell)/2;d=a-g/a
  v=4*a*u*(1-u*u)/(1+u*u)**2
  H=E*(E-2*a)*(E-2*b)*(2*a+2*b-E)
  assert H==4*a*a*v*v and ell*ell==d*d+v*v
  # Rational points on the chord, with rational distance to the origin.
  origin_distance=2*a*u/(1+u*u)
  for n in (2,3,4):
   p=1/(n*u);longitudinal=origin_distance*(p-1/p)/2
   r=origin_distance*(p+1/p)/2
   s=ell/2-longitudinal;t=ell/2+longitudinal
   x=a-d*s/ell;root_w=v*s/ell;w=root_w**2
   assert 0<x<a and s>0 and t>0
   assert r*r==x*x+w and s*s==(a-x)**2+w and s+t==ell
   K=ell/(2*s*t)
   k=K*d*d/(4*w*ell*ell)
   m=K*2*w
   assert m==K*(2*d*d*w+2*v*v*w)/(ell*ell)
   assert m==v*root_w/t # exact q3 derivative in V=1-z
   Tprime=1-v/root_w
   k_direct=-1/(8*s**3)+v/(8*t*root_w**3)-Tprime**2/(8*t**3)
   assert k==k_direct and 1/(2*s)+Tprime/(2*t)==0
   assert 2*k*m==(d/(2*s*t))**2
   assert m!=K*2*d*d*w/(ell*ell) # dropping the finite-E term is wrong
   q1=r+a+s;q2=r+b+t;q12=a+b+s+t
   q23=E+r+s-a;q31=E+r+t-b
   assert min(q1,q2,q12,q23,q31,E+r,E+s,E+t)>0
   bracket=(1/q23+1/q31)/(E+r)+(1/q31+1/q12)/(E+t)+(1/q12+1/q23)/(E+s)
   FE=bracket/(q1*q2)
   energy_weighted_regulator_first_over_pi=2*H*s*t*FE/(3*d)
   target_over_pi=4*b*(a+b)/(3*(x+b))
   records.append({'a':str(a),'E':str(E),'x':str(x),
     'pole_coefficient_over_pi':str(2*s*t/d),
     'E_P0_density_over_pi':str(energy_weighted_regulator_first_over_pi),
     'limiting_density_over_pi':str(target_over_pi),
     'relative_difference':str((energy_weighted_regulator_first_over_pi-target_over_pi)/target_over_pi)})
# General compact-interval limit coefficient algebra, independently of the chord fixtures.
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  x=a/3;s=a-x;t=x+b;h=8*a*b*(a+b)
  E_FE_limit=(a+b)/(4*a*s*t*t)
  assert F(2,3)*h*s*t/(a+b)*E_FE_limit==4*b*(a+b)/(3*t)
assert before==inventory()
report={'passed':True,'finite_energy_fixture_count':len(records),'general_limit_coefficient_fixtures':9,
 'source_sha256':before,'source_unchanged':True,
 'finite_E_pole_coefficient':'2pi*s_c*t_c/d',
 'finite_E_regulator_first_period':'(2pi H/(3E)) integral chi(x,w_star)*s_c*t_c*F_E/d dx',
 'regulator_then_energy':'(4pi*b*(a+b)/3) integral chi(x,0)/(x+b) dx',
 'energy_then_regulator':0,'same_observable':'E*P_chi(E,epsilon)',
 'verification_boundary':'Exact coefficient and six-term fixtures; real sequential-limit proof is written analysis. No global physical period or joint-limit theorem certified.',
 'fixtures':records}
(HERE/'triangle-limit-order.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='fixtures'},indent=2))
