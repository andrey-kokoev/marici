"""Dense critical-curvature margins for choosing compact proof zones."""

import json
import math
import random

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature, state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


zones=[(0.1,0.3),(0.3,0.5),(0.5,0.7),(0.7,0.85),(0.85,0.95),(0.95,0.99)]
records={str(zone):(math.inf,None) for zone in zones}
for pi in range(100,991):
    p=pi/1000
    for ci in range(101):
        c=ci/100
        q=c*p
        lo,hi=0.0,1.0
        while boundary_derivative(p,q,hi)>0: hi*=2
        for _ in range(60):
            mid=(lo+hi)/2
            if boundary_derivative(p,q,mid)>0: lo=mid
            else: hi=mid
        holding=(lo+hi)/2
        t,r=state(p,q,holding)
        margin=-directional_curvature(t,r,p,q)
        for zone in zones:
            if zone[0]<=p<=zone[1]:
                key=str(zone)
                if margin<records[key][0]:
                    records[key]=(margin,(p,c,holding,t,r,margin/(1-p),margin/(1-p)**2))

print(json.dumps(records,indent=2))

rng=random.Random(20260823)
smallest=(math.inf,None)
failures=0
for _ in range(200_000):
    selector=rng.random()
    if selector<1/3:
        p=0.1+0.1*rng.random()**3
    elif selector<2/3:
        p=0.99-0.89*rng.random()**3
    else:
        p=0.1+0.89*rng.random()
    c=rng.random();q=c*p
    lo,hi=0.0,1.0
    while boundary_derivative(p,q,hi)>0: hi*=2
    for _ in range(55):
        mid=(lo+hi)/2
        if boundary_derivative(p,q,mid)>0: lo=mid
        else: hi=mid
    holding=(lo+hi)/2;t,r=state(p,q,holding)
    normalized=-directional_curvature(t,r,p,q)/(1-p)**2
    reserve=normalized-0.14
    if reserve<smallest[0]:smallest=(reserve,(p,c,holding,t,r))
    if reserve<-1e-12:failures+=1
print(json.dumps({"hostile_trials":200_000,"reserve_failures":failures,"smallest_reserve":smallest},indent=2))
