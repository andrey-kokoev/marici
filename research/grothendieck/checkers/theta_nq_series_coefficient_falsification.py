"""Exact symbolic coefficient test for a positive-y-series proof of partials of Nq."""
import json
import sympy as s
q,y,p=s.symbols('q y p', positive=True)
A=p/q
C=s.cosh(s.sqrt(q*y))
b=6*A*(C-1)/(A-3)**2
m=A*(C-1)-s.log(1-b)
def at4(expr):return expr.subs(y,4*y)
m4=at4(m);eta=m4-4*m
u=1-s.exp(-2*m);c=1-s.exp(-eta)
D=u**2/y**2-s.exp(-4*m)*c/y**2
Nq=s.diff(D,q)*y**2
partials={"q":s.diff(Nq,q),"y":s.diff(Nq,y)}
P=[s.Rational(2*3141592653589793238,10**18),s.Rational(2*3141592653589793239,10**18)]
Q=[s.Rational(3,10),s.Rational(7,16)]
rows=[]
for name,expr in partials.items():
 ser=s.series(expr,y,0,7).removeO().expand()
 for pv in P:
  for qv in Q:
   coeff=[s.factor(ser.coeff(y,k).subs({p:pv,q:qv})) for k in range(6)]
   rows.append({"partial":name,"p":str(pv),"q":str(qv),
                "signs":[s.sign(c) for c in coeff],"coefficients":[str(c) for c in coeff]})
negative=[(r["partial"],r["p"],r["q"],i) for r in rows for i,z in enumerate(r["signs"]) if z<0]
result={"order":6,"cases":len(rows),"negative_coefficients":negative,"all_tested_coefficients_nonnegative":not negative}
print(json.dumps(result,indent=2));assert negative or result["all_tested_coefficients_nonnegative"]
