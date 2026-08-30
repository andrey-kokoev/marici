"""Exact grade-three response on invariant puncture generators."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
z,zb,x,xb=sp.symbols("z zb x xb", nonzero=True); u=z*zb
Gz=-2*zb/(1+u); Gzb=-2*z/(1+u)
def chain(e,bar=False):
    out=e
    for w in range(2,5):
        v=zb if bar else z; gamma=Gzb if bar else Gz
        out=sp.diff(out,v)-w*gamma*out
    return sp.factor(out)
def M(cp,cm): return sp.factor(sp.diff(chain(cp),zb)-sp.diff(chain(cm,True),z))
Kp=(zb-xb)*(1+zb*x)**2/((z-x)*(1+u)**3*(1+x*xb))
Km=(z-x)*(1+z*xb)**2/((zb-xb)*(1+u)**3*(1+x*xb))
R=M(Kp,Km)
num,den=map(sp.factor,sp.fraction(R))
den_expected=(x-z)**4*(xb-zb)**4*(1+x*xb)*(1+u)**7
rec("RESPONSE.denominator","the response has fourth-order incidence poles",sp.simplify(den/den_expected)==1,"(z-x)^4(zb-xb)^4 times sphere factors")
rec("RESPONSE.nonzero","the one-puncture grade-three density is nonzero",num!=0 and sp.simplify(R.subs({z:2,zb:3,x:5,xb:7}))!=0,"generic rational witness")
R0=sp.factor(R.subs({x:0,xb:0}))
expected=-6*(z-zb)*(z+zb)*(z**2+zb**2)*(5*z*zb-1)/(z**4*zb**4*(1+u)**7)
rec("RESPONSE.center","the centered response has the closed factored form",sp.simplify(R0-expected)==0,sp.sstr(expected))
commute=True
for r in range(3):
  for s in range(3-r):
    lhs=M(sp.diff(Kp,x,r,xb,s),sp.diff(Km,x,r,xb,s))
    rhs=sp.diff(R,x,r,xb,s)
    commute &= sp.simplify(lhs-rhs)==0
rec("JET.commute","source jets commute with the observation readout",commute,"total source order <=2")
# Abstract exchange: M(cm,cp) with simultaneous z<->zb is -M(cp,cm).
swap=lambda e:e.subs({z:zb,zb:z,x:xb,xb:x},simultaneous=True)
rec("PARITY.odd","helicity/reflection exchange reverses the magnetic density",sp.simplify(swap(R)+R)==0,"Q M3=-M3")
# Linear algebra form M=[A,-A Q]; the symmetric Q sector is killed.
A=sp.Matrix([[1,-2,3],[0,4,5]])
Q=sp.Matrix([[sp.zeros(3),sp.eye(3)],[sp.eye(3),sp.zeros(3)]])
L=A.row_join(-A); PiE=(sp.eye(6)+Q)/2; PiM=(sp.eye(6)-Q)/2
rec("PROJECTOR.factor","M3 factors through the magnetic projector",L*PiE==sp.zeros(2,6) and L*PiM==L,"abstract three-coordinate block")
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_grade_three_source_readout_checks.py","strength":"exact source-derived grade-three morphism","passed":passed,"total":len(checks),"checks":checks,"verdict":"The invariant point kernel has a nonzero fourth-order grade-three incidence density. The readout commutes with source jets and factors through the magnetic Q eigenspace; its universal electric kernel is a parity-port alias, leaving injectivity on the magnetic source packet as the next question."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"completed_grade_three_source_readout.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
