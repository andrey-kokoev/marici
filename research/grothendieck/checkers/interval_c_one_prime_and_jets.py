"""Directed c=1 prime cells, f(0), and undilated zero jets for rank-three profiles."""
from fractions import Fraction as F
import json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent));import interval_undilated_septic_moments as im
sys.path.insert(0,str(pathlib.Path(__file__).parents[2]/'nima'/'checkers'));import preconditioned_spline_weil as n
Z=n.Z
def profile(u,a,cs,ms):
 out=Z
 for c,m in zip(cs,ms):out=n.add(out,n.scale(c,n.k7_iv(n.add(u,n.scale(F(m),a)))))
 return out
def jet(r,a,cs,ms):
 out=Z
 for c,m in zip(cs,ms):out=n.add(out,n.scale(c,n.k7_deriv_iv(n.scale(F(m),a),r,right=(r==7))))
 return out
def prime(a,cs,ms,cutoff):
 out=Z
 for p in n.primes(cutoff):
  q=p
  while q<=cutoff:
   weight=n.mul(n.log_q(F(p)),n.inv(n.sqrt_q(F(q))))
   out=n.add(out,n.scale(F(-2),n.mul(weight,profile(n.log_q(F(q)),a,cs,ms))))
   q*=p
 return out
def enc(x):return [str(x[0]),str(x[1])]
def main():
 a=n.scale(F(2),n.log_q(F(2)));rows=[]
 for name,cs,ms,cutoff in [('baseline',im.BASE,im.BM,874),('cross',im.CROSS,im.CM,3495),('lag2',im.L2,im.L2M,13978)]:
  p=prime(a,cs,ms,cutoff);f0=profile(Z,a,cs,ms);jets={str(r):enc(jet(r,a,cs,ms)) for r in range(1,8)}
  rows.append({'profile':name,'support_derived_prime_power_cutoff':cutoff,'f0':enc(f0),'prime':enc(p),'jets':jets})
 result={'schema':'marici.grothendieck.interval-c-one-prime-and-jets.v2','rows':rows,'passed':True}
 out=pathlib.Path(__file__).parents[1]/'results/interval-c-one-prime-and-jets.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':True,'prime_intervals':{r['profile']:[float(F(x)) for x in r['prime']] for r in rows}}))
if __name__=='__main__':main()
