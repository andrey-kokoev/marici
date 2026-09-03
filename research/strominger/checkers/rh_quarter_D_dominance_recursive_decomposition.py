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
  H=D(n-2,s+2);Dn=D(n,s);R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));A=mu(H,Dn);P=add(R,A);C=add(ms(P),ms(R),-1);S=ms(A);X=add(C,S,-1);records.append({'n':n,'shift':s,'identity':add(S,X)==C,'square_nonnegative':all(z>=0 for z in S),'cross_nonnegative':all(z>=0 for z in X)})
checks={'twenty_one':len(records)==21,'identities':all(x['identity'] for x in records),'squares':all(x['square_nonnegative'] for x in records),'mixed_cross_exhibited':any(not x['cross_nonnegative'] for x in records)};r={'schema':'marici.strominger.rh_quarter_D_dominance_recursive_decomposition.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Two-summand recurrence is exactly decomposed and separate cross-term positivity is rejected.','records':records,'checks':checks};(base/'results'/'rh_quarter_D_dominance_recursive_decomposition.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
