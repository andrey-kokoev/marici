"""Bounded numerical census of the codimension-two Gaussian fold-failure locus."""

import json, math, random
from pathlib import Path

root=Path(__file__).parent
j=json.loads((root.parent/'results'/'four-mode-chord-deletion-fold-morin.json').read_text())
rc=compile(j['rankdrop'].replace('^','**'),'<R>','eval')
nc=compile(j['kernel_normal_derivative'].replace('^','**'),'<N>','eval')

def ev(code,x):
    a,b,c,d=x
    return eval(code,{'__builtins__':{}},{'a':a,'b':b,'c':c,'d':d})
def detx(x):
    a,b,c,d=x; return 1-2*a*b*c*d-a*a+a*a*c*c-b*b+b*b*d*d-c*c-d*d
def positive(x):
    a,b,c,d=x
    return 1-a*a>0 and 1-a*a-b*b>0 and detx(x)>0
def solve(a,b,c,d):
    x=[a,b,c,d]
    for _ in range(60):
        f=[ev(rc,x),ev(nc,x)]
        if max(map(abs,f))<1e-13:return x
        h=1e-6
        jac=[]
        for code in (rc,nc):
            row=[]
            for q in (2,3):
                p=x.copy();m=x.copy();p[q]+=h;m[q]-=h
                row.append((ev(code,p)-ev(code,m))/(2*h))
            jac.append(row)
        z=jac[0][0]*jac[1][1]-jac[0][1]*jac[1][0]
        if abs(z)<1e-14:return None
        dc=(-f[0]*jac[1][1]+jac[0][1]*f[1])/z
        dd=(-jac[0][0]*f[1]+f[0]*jac[1][0])/z
        step=max(abs(dc),abs(dd)); scale=1 if step<.2 else .2/step
        x[2]+=scale*dc;x[3]+=scale*dd
        if max(abs(x[2]),abs(x[3]))>1.5:return None
    return None
def transverse_cd(x):
    h=1e-6;j=[]
    for code in (rc,nc):
        row=[]
        for q in (2,3):
            p=x.copy();m=x.copy();p[q]+=h;m[q]-=h;row.append((ev(code,p)-ev(code,m))/(2*h))
        j.append(row)
    return abs(j[0][0]*j[1][1]-j[0][1]*j[1][0])

rng=random.Random(2076)
roots=[]
for _ in range(6000):
    a=rng.uniform(-.75,.75);b=rng.uniform(-.6,.6)
    if 1-a*a-b*b<=0:continue
    x=solve(a,b,rng.uniform(-.8,.8),rng.uniform(-.8,.8))
    if x is None or not positive(x):continue
    if max(abs(ev(rc,x)),abs(ev(nc,x)))>1e-6:continue
    if min(map(abs,x))<1e-5 or transverse_cd(x)<1e-7:continue
    key=tuple(x)
    if all(sum((u-v)**2 for u,v in zip(key,y))>1e-8 for y in roots):roots.append(key)
    if len(roots)>=12:break

packet={'schema':'marici.four-mode-chord-deletion-exceptional-census.v1','attempts':6000,'interior_noncoordinate_roots':roots,'count':len(roots),'status':'numerical discovery only'}
out=root/'results'/'four-mode-chord-deletion-exceptional-census.json';out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
