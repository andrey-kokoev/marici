"""Exact rational coefficient checks; analytic Mellin/Gamma limits are written in the note."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'triangle-moving-collision-limit.md',
 ROOT/'temp/arxiv-2408.16386-source/sections/cosmologicalintegrals.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory();records=[]
# C(d)=48*pi^epsilon*3^(2epsilon-3)/Gamma(epsilon).
C_slope=F(48,27)
assert C_slope==F(16,9)
for a in map(F,(1,2,3)):
 for b in map(F,(1,2,3)):
  for ratio in map(F,('1/4','1/2','3/4')):
   x=a*ratio;s=a-x;t=x+b;h=8*a*b*(a+b)
   A=b*s/(a*t);B=(a+b)/(2*s*t);lam=A/B
   Q=1+a*lam/(2*x*s)
   assert Q==a*t/(x*(a+b))
   k=B*B/(4*A);m=2*A
   assert 2*k*m==B*B
   for p in map(F,('-1/2','0','1/2')):
    for v in map(F,('1/10','1/3')):
     # y=sqrt(A)*p: test the exact completed-square identity rationally.
     assert A*(1+(1+p)**2-2*(1+p)*(1-v))==A*((p+v)**2+v*(2-v))
   residue_over_pi=1/(4*x*s*t*Q*B)
   assert residue_over_pi==1/(2*a*t)
   L_slope=C_slope*F(1,16)*(24*a)/(16*a*a)
   assert L_slope==1/(6*a)
   final_over_pi=2*a*L_slope*h*residue_over_pi
   assert final_over_pi==4*b*(a+b)/(3*(x+b))
   records.append({'a':str(a),'b':str(b),'x':str(x),
     'profile_epsilon_pole_over_pi':str(residue_over_pi),
     'L_zero_slope':str(L_slope),'boundary_density_over_pi':str(final_over_pi)})
assert before==inventory()
report={'passed':True,'fixture_count':len(records),'completed_square_checks':6*len(records),'source_sha256':before,'source_unchanged':True,
 'C_slope_at_zero':'16/9','L_slope_at_zero':'1/(6a)',
 'profile_pole':'I_x(epsilon) ~ pi/[2a(x+b)epsilon]',
 'sequential_coefficient_limit':'(4pi*b*(a+b)/3) integral chi(x,0)/(x+b) dx',
 'order':'E->0 in E^(1-epsilon)P_chi first, then real epsilon->0+',
 'verification_boundary':'Rational coefficient fixtures only; local Mellin residue and Gamma limit are written analysis. No regulator-first or simultaneous period limit certified.',
 'fixtures':records}
(HERE/'triangle-regulator-coefficient.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='fixtures'},indent=2))
