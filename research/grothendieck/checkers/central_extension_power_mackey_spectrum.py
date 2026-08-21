"""Exact nonsplit central-extension fiber spectra."""

from math import gcd
import json
from pathlib import Path


def qmul(x, y):
    sx, ax=x; sy, ay=y
    if ax==0: return (sx*sy,ay)
    if ay==0: return (sx*sy,ax)
    if ax==ay: return (-sx*sy,0)
    table={(1,2):(1,3),(2,3):(1,1),(3,1):(1,2),
           (2,1):(-1,3),(3,2):(-1,1),(1,3):(-1,2)}
    s,a=table[(ax,ay)]; return (sx*sy*s,a)


def power(x,n,mul,identity):
    out=identity
    for _ in range(n): out=mul(out,x)
    return out


def run(name,group,quotient,q,mul,identity,kernel_exponent):
    survivors=[]; checks=0
    for n in range(1,19):
        global_ok=True
        for h in quotient["elements"]:
            source=[x for x in group if q(x)==h]
            target_h=power(h,n,quotient["mul"],quotient["identity"])
            target=[x for x in group if q(x)==target_h]
            images=[power(x,n,mul,identity) for x in source]
            global_ok &= sorted(images)==sorted(target)
            checks += len(source)*len(group)
        predicted=gcd(n,kernel_exponent)==1
        assert global_ok==predicted,(name,n,global_ok,predicted)
        if global_ok: survivors.append(n)
    return {"extension":name,"kernel_exponent":kernel_exponent,
            "survivors_1_to_18":survivors,"checks":checks}


def main():
    c4=list(range(4)); c2=list(range(2))
    c2q={"elements":c2,"mul":lambda a,b:(a+b)%2,"identity":0}
    a=run("C4_to_C2",c4,c2q,lambda x:x%2,
          lambda x,y:(x+y)%4,0,2)

    q8=[(s,axis) for axis in range(4) for s in (-1,1)]
    v4=list(range(4)); v4q={"elements":v4,"mul":lambda x,y:x^y,"identity":0}
    qquot=lambda x:0 if x[1]==0 else x[1]
    b=run("Q8_to_V4",q8,v4q,qquot,qmul,(1,0),2)

    h27=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
    hmul=lambda u,v:((u[0]+v[0])%3,(u[1]+v[1])%3,
                     (u[2]+v[2]+u[0]*v[1])%3)
    c3sq=[(x,y) for x in range(3) for y in range(3)]
    c3q={"elements":c3sq,"mul":lambda u,v:((u[0]+v[0])%3,(u[1]+v[1])%3),"identity":(0,0)}
    c=run("Heisenberg27_to_C3xC3",h27,c3q,lambda u:(u[0],u[1]),
          hmul,(0,0,0),3)

    families=[a,b,c]
    result={"theorem":"central extension compatibility iff gcd(n,exp(K))=1",
            "families":families,"index_cases":54,
            "coefficient_value_checks":sum(x["checks"] for x in families),
            "status":"pass"}
    out=Path(__file__).parents[1]/"results"/"central-extension-power-mackey-spectrum.json"
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
