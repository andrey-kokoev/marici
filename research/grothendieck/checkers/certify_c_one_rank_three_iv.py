"""Outward interval assembly of the coherent c=1 rank-three Gram matrix."""
from fractions import Fraction as F
import json,pathlib,sys
import mpmath as mp
mp.iv.dps=60
sys.path.insert(0,str(pathlib.Path(__file__).parent));import interval_undilated_septic_moments as im;import interval_c_one_prime_and_jets as cj
sys.path.insert(0,str(pathlib.Path(__file__).parents[2]/'nima'/'checkers'));import preconditioned_spline_weil as n
N=8;delta=F(1,4);TV=F(5184);root=pathlib.Path(__file__).parents[1]/'results'
def q(x):
 x=F(x);return mp.iv.mpf(x.numerator)/mp.iv.mpf(x.denominator)
def iv(pair):return mp.iv.mpf([q(pair[0]).a,q(pair[1]).b])
def bounds(x):return [mp.nstr(x.a,50),mp.nstr(x.b,50)]
def tail_data():
 stop=N+16;dp=sum(F(1,k+1)-F(1)/(F(k)+delta) for k in range(N,stop));x=F(stop)
 L=n.log_q((x+1)/(x+delta));g=F(1)/(x+delta)-F(1)/(x+1);gp=-(x+delta)**-2+(x+1)**-2;g3=-F(6)*(x+delta)**-4+F(6)*(x+1)**-4
 sup=n.add(L,(g/2-gp/12,g/2-gp/12));slo=(sup[0]+g3/F(720),sup[1]+g3/F(720))
 return iv((dp-sup[1],dp-slo[0])),[iv(n.sp_bounds(N,r+1,alpha=delta)) for r in range(1,8)],q(TV*n.sp_bounds(N,8,alpha=delta)[1])
def main():
 md=json.loads((root/'interval-undilated-septic-moments.json').read_text());pd=json.loads((root/'interval-c-one-prime-iv.json').read_text())
 moments={(('lag1' if r['profile']=='cross' else r['profile']),r['n']):iv(r['interval']) for r in md['rows']}
 primes={(('lag1' if r['profile']=='cross' else r['profile'])):mp.iv.mpf([mp.iv.mpf(r['prime'][0]).a,mp.iv.mpf(r['prime'][1]).b]) for r in pd['rows']}
 profiles={'baseline':(im.BASE,im.BM),'lag1':(im.CROSS,im.CM),'lag2':(im.L2,im.L2M),'lag3':(im.L3,im.L3M),'lag4':(im.L4,im.L4M),'lag5':(im.L5,im.L5M),'lag6':(im.L6,im.L6M)};a=n.scale(F(2),n.log_q(F(2)))
 D,zeta,e=tail_data();gamma=iv(n.gamma_interval());pi=iv(n.pi_interval());logpi=mp.iv.log(pi);cells={}
 for name in ['baseline','lag1','lag2','lag3','lag4','lag5','lag6']:
  cs,ms=profiles[name];f0=iv(cj.profile(n.Z,a,cs,ms));jets={r:iv(cj.jet(r,a,cs,ms)) for r in range(1,8)};finite=mp.iv.mpf(0)
  for k in range(N):finite+=f0/(k+1)-moments[(name,k)]
  tail=f0*D
  for r in range(1,8):tail-=jets[r]*zeta[r-1]
  tail+=mp.iv.mpf([-e.b,e.b])
  arch=-(gamma+logpi)*f0+finite+tail;cells[name]=arch+primes[name]
 d,c1,c2,c3,c4,c5,c6=cells['baseline'],cells['lag1'],cells['lag2'],cells['lag3'],cells['lag4'],cells['lag5'],cells['lag6'];minor2=d*d-c1*c1;det3=d*d*d-2*d*c1*c1-d*c2*c2+2*c1*c1*c2
 A=[[cells['baseline' if i==j else 'lag'+str(abs(i-j))] for j in range(7)] for i in range(7)]
 L=[[mp.iv.mpf(0) for j in range(7)] for i in range(7)];D=[]
 for j in range(7):
  pivot=A[j][j]-sum((L[j][k]*L[j][k]*D[k] for k in range(j)),mp.iv.mpf(0));D.append(pivot);L[j][j]=mp.iv.mpf(1)
  for i in range(j+1,7):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),mp.iv.mpf(0)))/pivot
 passed=d.a>0 and minor2.a>0 and det3.a>0 and all(x.a>0 for x in D)
 result={'schema':'marici.grothendieck.c-one-rank-seven-iv-certificate-n8.v1','cells':{k:bounds(v) for k,v in cells.items()},'minor2':bounds(minor2),'det3':bounds(det3),'ldl_pivots_rank7':[bounds(x) for x in D],'passed':passed,'arithmetic':'mpmath.iv 60 decimal digits over directed rational source intervals'}
 (root/'c-one-rank-seven-iv-certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
