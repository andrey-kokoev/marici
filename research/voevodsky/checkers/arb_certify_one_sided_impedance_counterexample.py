"""Arb certificate that Re(-F'/F)<0 at s=0.01+20i."""
import json,sys
from pathlib import Path
vendored=Path(__file__).parents[2]/'benincasa'/'.tmp_flint';sys.path.insert(0,str(vendored))
from flint import acb,arb,ctx
ctx.dps=70;pi=arb.pi();N=6;U=arb(3)
def psi(v):
 return sum(((4*pi*pi*arb(n**4)*(9*v).exp()-6*pi*arb(n*n)*(5*v).exp())*(-pi*arb(n*n)*(4*v).exp()).exp() for n in range(1,N+1)),acb(0))
def moment_tail(U0,rate,k):
 if k==0:return 1/rate
 if k==1:return U0/rate+1/(rate*rate)
def tail(k):
 E=(4*U).exp();z=arb(0)
 for n in range(1,N+1):
  nn=arb(n*n);rate=4*pi*nn*E-arb('9.5');coeff=4*pi*pi*nn*nn*(arb('9.5')*U-pi*nn*E).exp();z+=coeff*moment_tail(U,rate,k)
 def term(n):
  nn=arb(n*n);rate=4*pi*nn-arb('9.5');return 4*pi*pi*nn*nn*(-pi*nn).exp()*moment_tail(arb(0),rate,k)
 M=45;z+=sum((term(n) for n in range(N+1,M+1)),arb(0));first=term(M+1);q=(arb(M+2)/arb(M+1))**4*(-pi*arb(2*(M+1)+1)).exp();return z+first/(1-q)
def disk_error(x,e): return x+acb(e*arb(0,1),e*arb(0,1))
s=acb(arb('0.01'),arb(20))
def integ(k):
 def fun(v,_analytic): return (v**k)*psi(v)*(-2*s*v).exp()
 x=acb.integral(fun,arb(0),U,abs_tol=arb('1e-55'),eval_limit=100000)
 return disk_error(x,tail(k))
I0=integ(0);I1=integ(1)
# F=2 I0 and integral u Phi exp(-su)du=4 I1.
m=2*I1/I0
out={'s':str(s),'m':str(m),'real_m':str(m.real),'real_m_strictly_negative':m.real<0,'tail_I0':str(tail(0)),'tail_I1':str(tail(1)),'interval_certified':m.real<0,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'arb-certified-one-sided-impedance-counterexample.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
