"""Dependency-free rational enclosures for the Weil spline checker."""
from fractions import Fraction as F
from math import isqrt

Interval=tuple[F,F]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def mul(a,b):
 v=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);return min(v),max(v)
def inv(a):
 assert not (a[0]<=0<=a[1]);return (1/a[1],1/a[0]) if a[0]>0 else (1/a[1],1/a[0])
def scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def sqrt_q(x:F,digits=40)->Interval:
 assert x>=0
 s=10**digits;n=isqrt((x.numerator*s*s)//x.denominator);lo=F(n,s)
 while lo*lo>x:n-=1;lo=F(n,s)
 hi=F(n+1,s)
 while hi*hi<x:n+=1;lo=F(n,s);hi=F(n+1,s)
 return lo,hi

def atanh_series(y:F,n=80)->Interval:
 assert 0<=y<1
 s=sum((y**(2*k+1))/F(2*k+1) for k in range(n))
 tail=(y**(2*n+1))/F(2*n+1)/(1-y*y)
 return s,s+tail

def log_q(x:F,n=100)->Interval:
 assert x>0;k=0;m=x
 while m>=2:m/=2;k+=1
 while m<1:m*=2;k-=1
 lm=scale(F(2),atanh_series((m-1)/(m+1),n))
 l2=scale(F(2),atanh_series(F(1,3),n))
 return add(lm,scale(F(k),l2))

def exp_nonneg(x:F,n=160)->Interval:
 assert x>=0
 term=F(1);s=term
 for k in range(1,n+1):term*=x/F(k);s+=term
 assert F(n+2)>x
 nxt=term*x/F(n+1);tail=nxt/(1-x/F(n+2))
 return s,s+tail

def exp_q(x:F,n=160)->Interval:
 neg=x<0;x=abs(x)
 # Since e>2, exp(-x) <= 2^-floor(x); zero is a valid lower enclosure.
 if neg and x>100:return F(0),F(1,2**(x.numerator//x.denominator))
 halves=0
 while x>1:x/=2;halves+=1
 out=exp_nonneg(x,n)
 for _ in range(halves):out=mul(out,out)
 return inv(out) if neg else out

def atan_inv(q:int,n=80)->Interval:
 x=F(1,q);terms=[(-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n+1)]
 s=sum(terms[:-1]);sn=s+terms[-1]
 return min(s,sn),max(s,sn)
def pi_interval(n=80)->Interval:return sub(scale(F(16),atan_inv(5,n)),scale(F(4),atan_inv(239,n)))
def gamma_interval(n=10000)->Interval:
 H=sum(F(1,k) for k in range(1,n+1));ln=log_q(F(n),120)
 base=sub((H,H),ln);base=add(base,(-F(1,2*n),-F(1,2*n)))
 t2=F(1,12*n*n);t4=F(1,120*n**4)
 lo=base[0]+t2-t4;hi=base[1]+t2-t4+F(1,252*n**6)
 return lo,hi

def _contains(iv,x):return float(iv[0])<=x<=float(iv[1])
def self_test():
 import math
 tests={"sqrt2":(_contains(sqrt_q(F(2)),math.sqrt(2))),"log2":_contains(log_q(F(2)),math.log(2)),"exp1":_contains(exp_q(F(1)),math.e),"pi":_contains(pi_interval(),math.pi),"gamma":_contains(gamma_interval(),0.5772156649015329)}
 # Deliberate failure: a zero-width first-order log approximation must miss log(2).
 bad=F(2,3);tests["deliberate_undertruncation_detected"]=not _contains((bad,bad),math.log(2))
 assert all(tests.values()),tests
 print(tests)
if __name__=="__main__":self_test()
