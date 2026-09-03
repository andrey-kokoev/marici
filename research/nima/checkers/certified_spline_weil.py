"""Certified one-packet Weil Gram interval for the centered cubic B-spline."""
from fractions import Fraction as F
import sys
sys.set_int_max_str_digits(0)
from math import comb,factorial
from rational_interval import add,sub,mul,scale,inv,log_q,exp_q,pi_interval,gamma_interval
import json, pathlib

def k7(x:F)->F:
 return sum(F((-1)**j*comb(8,j),5040)*max(F(0),x+4-j)**7 for j in range(9))
K0=k7(F(0))
def k7_iv(x):
 assert 0<=x[0]<=x[1]
 return (F(0),F(0)) if x[0]>=4 else (k7(min(F(4),x[1])),k7(x[0]))

def primes(n):
 out=[]
 for p in range(2,n+1):
  if all(p%d for d in range(2,int(p**.5)+1)):out.append(p)
 return out

def prime_term(fourier_2pi=False):
 total=(F(0),F(0));pi=pi_interval()
 for p in primes(53):
  q=p
  while q<=53:
   lq=log_q(F(q));arg=lq if not fourier_2pi else mul(lq,inv(scale(F(2),pi)))
   kval=k7_iv(arg);weight=mul(log_q(F(p)),inv(__import__('rational_interval').sqrt_q(F(q))))
   total=add(total,scale(F(-2),mul(weight,kval)));q*=p
 return total

def exp_moment(c:F,a:int,b:int,r:int):
 def endpoint(x):
  poly=sum((c*x)**j/F(factorial(j)) for j in range(r+1))
  return scale(F(factorial(r),1)*F(1,c**(r+1)),mul(exp_q(-c*x),(poly,poly)))
 return sub(endpoint(a),endpoint(b))
def integral_k(c:F):
 out=(F(0),F(0))
 for j in range(9):
  a=max(0,2*(j-4));b=8
  if a>=b:continue
  # (x/2+4-j)^7
  d=F(4-j)
  for r in range(8):
   coeff=F((-1)**j*comb(8,j)*comb(7,r),5040)*d**(7-r)*F(1,2)**r
   out=add(out,scale(coeff,exp_moment(c,a,b,r)))
 return out

def arch(N=1):
 s=(F(0),F(0))
 for n in range(N):s=add(s,sub((K0/F(n+1),K0/F(n+1)),integral_k(F(n)+F(1,4))))
 # Repeated integration by parts through degree seven.
 def d0(r):
  top=4 if r==7 else 3
  return sum(F((-1)**j*comb(8,j),factorial(7-r))*(4-j)**(7-r) for j in range(top+1))/2**r
 a=F(N)+F(1,4);tail=(F(0),F(0))
 li=log_q(F(N+1,1)/a);g=F(3,4)/(a*(N+1))
 tail=add(tail,scale(-K0,(li[0],li[1]+g)))
 for r in range(1,8):
  power=r+1;zlo=F(1,r)*a**(-r);zhi=zlo+a**(-power)
  tail=add(tail,scale(-d0(r),(zlo,zhi)))
 # f^(7) has jumps 35,-21,7,-1,0 divided by 2^7: remaining variation 93/128.
 rem=F(93,128)*(a**(-8)+F(1,7)*a**(-7))
 tail=add(tail,(-rem,rem))
 piv=pi_interval();lp=(log_q(piv[0])[0],log_q(piv[1])[1])
 const=scale(-K0,add(gamma_interval(),lp))
 return add(const,add(s,tail))
def pole():
 e=exp_q(F(1,4));sh=scale(F(1,2),sub(e,inv(e)));v=scale(F(4),sh)
 return scale(F(2),mul(mul(mul(v,v),mul(v,v)),mul(mul(v,v),mul(v,v))))
def main():
 A=arch();P=prime_term();Po=pole();q=add(add(Po,A),P)
 wrong_sign=add(add(Po,A),scale(F(-1),P));wrong_fourier=add(add(Po,A),prime_term(True))
 import hashlib
 def digest(x):return hashlib.sha256((str(x.numerator)+"/"+str(x.denominator)).encode()).hexdigest()
 data={"schema":"marici.certified_spline_weil.v1","basis":"centered_cardinal_cubic_B_spline","correlation":"centered_cardinal_degree_7","gram_fraction_sha256":[digest(q[0]),digest(q[1])],"gram_float":[float(q[0]),float(q[1])],"components_float":{"pole":[float(x) for x in Po],"arch":[float(x) for x in A],"prime":[float(x) for x in P]},"deliberate_failures":{"prime_sign_flip":[float(x) for x in wrong_sign],"fourier_2pi_rescale":[float(x) for x in wrong_fourier]},"certification":"Fraction arithmetic plus rational_interval.py remainder bounds; arch tail uses two integrations by parts and a global truncated-power bound on |(k(x/2))''|.","nonverification":"A positive one-by-one finite Gram interval does not prove Weil positivity or RH."}
 path=pathlib.Path('research/nima/results/certified_spline_weil.json');path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({"gram_float":data["gram_float"],"components_float":data["components_float"],"failures":data["deliberate_failures"]}))
if __name__=='__main__':main()
