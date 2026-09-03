import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_order_four_interpolated_hurwitz_minors.py')));Q,D,mu=g['Q'],g['D'],g['mu']
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 return r
def ms(p):
 e=[(-1)**k*p[2*k] for k in range((len(p)+1)//2)];o=[(-1)**k*p[2*k+1] for k in range(len(p)//2)];return add(mu(e,e),[F(0)]+mu(o,o))
records=[]
for n in range(2,9):
 for s in range(3):
  P=mu(mu(Q(s+n-1),D(n-1,s)),D(n-1,s+2));R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));C=add(ms(P),ms(R),-1);records.append({'n':n,'shift':s,'coefficients_nonnegative':all(z>=0 for z in C),'constant_positive':C[0]>0})
checks={'twenty_one':len(records)==21,'all_dominant':all(x['coefficients_nonnegative'] and x['constant_positive'] for x in records)};r={'schema':'marici.strominger.rh_quarter_D_imaginary_axis_dominance.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Bounded coefficientwise imaginary-axis dominance regenerated as one evidence backend.','records':records,'checks':checks};(base/'results'/'rh_quarter_D_imaginary_axis_dominance.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
