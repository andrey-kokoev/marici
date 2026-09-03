"""Fast outward interval prime sums with profile-specific support cutoffs."""
import json,math,pathlib
import mpmath as mp
mp.iv.dps=60
I=mp.iv.mpf;a=2*mp.iv.log(2)
BASE=[I(1),I(-5),I(33)/4,I(-5),I(1)];BM=[2,1,0,-1,-2]
CROSS=[I(1)/2,-I(5)/2,I(37)/8,I(-5),I(37)/8,-I(5)/2,I(1)/2];CM=[3,2,1,0,-1,-2,-3]
def lag_coeff(k):
 v={m:c for m,c in zip(BM,BASE)};ms=list(range(2+k,-3-k,-1));return [I('0.5')*(v.get(m-k,I(0))+v.get(m+k,I(0))) for m in ms],ms
L2,L2M=lag_coeff(2);L3,L3M=lag_coeff(3);L4,L4M=lag_coeff(4);L5,L5M=lag_coeff(5);L6,L6M=lag_coeff(6)
def k7(x):
 if x.b<=-4 or x.a>=4:return mp.iv.mpf(0)
 out=mp.iv.mpf(0)
 for j in range(9):
  y=x+4-j
  if y.b<=0: term=mp.iv.mpf(0)
  elif y.a>=0: term=y**7
  else: term=mp.iv.mpf([0,y.b])**7
  out+=(-1)**j*math.comb(8,j)*term/math.factorial(7)
 return out
def profile(x,cs,ms):return sum((c*k7(x+m*a) for c,m in zip(cs,ms) if not (c.a==0 and c.b==0)),mp.iv.mpf(0))
def primes(limit):
 sieve=bytearray(b'\x01')*(limit+1);sieve[:2]=b'\x00\x00'
 for p in range(2,math.isqrt(limit)+1):
  if sieve[p]:sieve[p*p:limit+1:p]=b'\x00'*(((limit-p*p)//p)+1)
 return (p for p in range(2,limit+1) if sieve[p])
def prime_range(cs,ms,limit,lo=2,hi=None):
 out=mp.iv.mpf(0);hi=limit if hi is None else hi
 for p in primes(limit):
  if p<lo or p>hi:continue
  q=p
  while q<=limit:
   out-=2*mp.iv.log(p)/mp.iv.sqrt(q)*profile(mp.iv.log(q),cs,ms);q*=p
 return out
def prime(cs,ms,limit):return prime_range(cs,ms,limit)
def prime_lag_range(k,limit,lo=2,hi=None):
 """For k>=5 and x=log(q)>=log(2), the +ka translate is outside BASE support."""
 assert k>=5
 out=mp.iv.mpf(0);hi=limit if hi is None else hi
 for p in primes(limit):
  if p<lo or p>hi:continue
  q=p
  while q<=limit:
   out-=mp.iv.log(p)/mp.iv.sqrt(q)*profile(mp.iv.log(q)-k*a,BASE,BM);q*=p
 return out
def prime_lag5_range(limit,lo=2,hi=None):return prime_lag_range(5,limit,lo,hi)
def bnd(x):return [mp.nstr(x.a,50),mp.nstr(x.b,50)]
def main():
 rows=[]
 for name,cs,ms,cutoff in [('baseline',BASE,BM,874),('cross',CROSS,CM,3495),('lag2',L2,L2M,13978),('lag3',L3,L3M,55909),('lag4',L4,L4M,223635)]:rows.append({'profile':name,'cutoff':cutoff,'prime':bnd(prime(cs,ms,cutoff))})
 rows.append({'profile':'lag5','cutoff':894542,'prime':bnd(prime_lag5_range(894542))})
 r={'schema':'marici.grothendieck.interval-c-one-prime-iv.v1','arithmetic':'mpmath.iv 60 digits','rows':rows,'passed':True}
 out=pathlib.Path(__file__).parents[1]/'results/interval-c-one-prime-iv.json';out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
if __name__=='__main__':main()
